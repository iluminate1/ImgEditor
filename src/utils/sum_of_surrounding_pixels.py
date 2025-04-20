from PySide6.QtGui import QImage

from utils.pixels_helper import to_binary_format


def sum_of_surrounding_pixels(img: QImage, x: int, y: int, radius: int = 1) -> int:
    """
    Calculate the sum of pixel values around a given coordinate.

    Args:
        image: QImage
        x: X coordinate of center pixel
        y: Y coordinate of center pixel
        radius: How many pixels around to include (default 1 for 3x3 area)

    Returns:
        Sum of all pixel values in the surrounding area
    """
    total = 0
    width = img.width()
    height = img.height()

    is_image_binary = img.format() == QImage.Format.Format_Mono

    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            if max(abs(dx), abs(dy)) == radius:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx != x or ny != y):
                    if is_image_binary:
                        total += to_binary_format(img.pixelColor(nx, ny).value())
                    else:
                        total += img.pixelColor(nx, ny).value()

    return total
