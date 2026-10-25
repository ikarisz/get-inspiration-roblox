from PIL import Image

def calculate_image_diff(img1: Image.Image, img2: Image.Image, thumb_size=(64, 36)) -> float:
    """
    Calculates the normalized visual difference between two images.
    Returns a value between 0.0 (identical) and 1.0 (completely different).
    Used to detect when a new modal / popup or menu opens on screen.
    """
    if img1 is None or img2 is None:
        return 1.0
    
    t1 = img1.resize(thumb_size).convert("L")
    t2 = img2.resize(thumb_size).convert("L")
    
    p1 = list(t1.getdata())
    p2 = list(t2.getdata())
    
    diff_sum = sum(abs(a - b) for a, b in zip(p1, p2))
    max_diff = 255 * len(p1)
    return diff_sum / max_diff
