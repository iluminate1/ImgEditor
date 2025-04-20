from enum import Enum, IntEnum

from PySide6.QtGui import qRgb


class BinaryColor(IntEnum):
    Black = 0
    White = 1


class GrayscaleColor(Enum):
    Black = qRgb(0, 0, 0)
    White = qRgb(255, 255, 255)


def inverse_pixel(pixel: int) -> int:
    return 255 - pixel


def to_binary_format(pixel: int) -> int:
    return 0 if pixel == 255 else 1
