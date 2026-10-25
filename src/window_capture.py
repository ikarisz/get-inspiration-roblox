import ctypes
import ctypes.wintypes
from PIL import Image
import mss

class WindowCapture:
    """Safely captures window frames of the Roblox Player on Windows via Win32 API and mss."""
    
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.sct = mss.mss()

    def find_roblox_window(self):
        """Finds the Roblox Player window handle (HWND)."""
        hwnd = self.user32.FindWindowW(None, "Roblox")
        if not hwnd:
            # Fallback search for any window with 'Roblox' in title
            def enum_proc(h, extra):
                length = self.user32.GetWindowTextLengthW(h)
                buff = ctypes.create_unicode_buffer(length + 1)
                self.user32.GetWindowTextW(h, buff, length + 1)
                title = buff.value.lower()
                if "roblox" in title and "studio" not in title and self.user32.IsWindowVisible(h):
                    extra.append(h)
                return True
            
            hwnds = []
            CMPFUNC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.wintypes.HWND, ctypes.POINTER(ctypes.c_void_p))
            self.user32.EnumWindows(CMPFUNC(enum_proc), ctypes.byref(ctypes.py_object(hwnds)))
            if hwnds:
                hwnd = hwnds[0]
        return hwnd

    def get_window_rect(self, hwnd):
        """Returns the screen bounding box {left, top, width, height} of the window."""
        if not hwnd:
            # Fallback to primary monitor
            return self.sct.monitors[1]
        
        rect = ctypes.wintypes.RECT()
        self.user32.GetWindowRect(hwnd, ctypes.byref(rect))
        
        width = rect.right - rect.left
        height = rect.bottom - rect.top
        
        # Guard against minimized or offscreen rect
        if width <= 0 or height <= 0:
            return self.sct.monitors[1]
            
        return {
            "left": rect.left,
            "top": rect.top,
            "width": width,
            "height": height
        }

    def capture_frame(self, hwnd=None):
        """Captures a screenshot of the specified window or primary monitor."""
        box = self.get_window_rect(hwnd)
        sct_img = self.sct.grab(box)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        return img
