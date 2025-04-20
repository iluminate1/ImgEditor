from collections import OrderedDict
from typing import override

from PySide6.QtGui import QImage, QResizeEvent, qRgb
from PySide6.QtWidgets import QMessageBox, QWidget

from ui import MonoToGrayscaleWidgetUI
from utils import sum_of_surrounding_pixels
from utils.exceptions import (
    ImageLoadException,
    InvalidFileException,
    InvalidImageFormat,
)
from utils.image_helper import ImageFormat, load_image, save_image, set_pixmap
from utils.pixels_helper import to_binary_format
from window.show_matrix_dialog import ShowImageMatrixDialog

type matrix = list[list[float]] | None


class MonoToGrayscaleWidget(QWidget, MonoToGrayscaleWidgetUI):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.source_image: QImage
        self.grayscale_image: QImage
        self.wave_matrix: matrix = None

        self.connect_signals()

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not hasattr(self, "source_image") or self.source_image.isNull():
            return

        set_pixmap(self.source_image, self.source_image_label_pixmap)
        set_pixmap(self.grayscale_image, self.grayscale_image_label_pixmap)

    def connect_signals(self) -> None:
        _ = self.load_source_image_button.clicked.connect(self.load_source_image)
        _ = self.show_source_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_grayscale_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.save_grayscale_image_button.clicked.connect(self.save_image)
        _ = self.show_wave_matrix_button.clicked.connect(self.show_matrix)

    def load_source_image(self):
        try:
            img = load_image(self, ImageFormat.binary)
        except InvalidFileException:
            return
        except ImageLoadException as e:
            _ = QMessageBox.warning(self, str(e.msg), str(e.msg))
            return
        except InvalidImageFormat as e:
            _ = QMessageBox.warning(self, str(e.msg), "Image is not binary!!!")
            return
        else:
            self.source_image = img

        self.wave_matrix = None
        self.source_image = img
        self.grayscale_image = QImage(
            img.size(),
            QImage.Format.Format_Grayscale8,
        )

        set_pixmap(self.source_image, self.source_image_label_pixmap)

        self.two_waves_mathod()
        self.blend_image()

    def two_waves_mathod(self):
        img = self.source_image
        height = img.height()
        width = img.width()

        self.wave_matrix = []
        for i in range(height):
            row: list[float] = []
            for j in range(width):
                cur_value = to_binary_format(self.source_image.pixelColor(j, i).value())
                new_value = round(
                    cur_value
                    + sum_of_surrounding_pixels(img, j, i) * 0.6
                    + sum_of_surrounding_pixels(img, j, i, 2) * 0.3,
                    2,
                )
                row.append(new_value)
            self.wave_matrix.append(row)

    def blend_image(self):
        if not self.wave_matrix:
            return

        original_values: dict[float, int] = {}
        for row in self.wave_matrix:
            for value in row:
                if value in original_values:
                    original_values[value] += 1
                else:
                    original_values[value] = 1

        amount_of_original_values = len(original_values.keys())
        step = 255 / (amount_of_original_values - 1)

        sorted_values: OrderedDict[float, int] = OrderedDict(
            sorted(
                original_values.items(),
                reverse=True,
            )
        )

        for i, key in enumerate(sorted_values):
            sorted_values[key] = round(i * step)

        for y, row in enumerate(self.wave_matrix):
            for x, color in enumerate(row):
                pixel_color = sorted_values.get(color, -1)
                self.grayscale_image.setPixel(
                    x,
                    y,
                    qRgb(pixel_color, pixel_color, pixel_color),
                )

        set_pixmap(self.grayscale_image, self.grayscale_image_label_pixmap)

    def show_matrix(self):
        show_matrix_dialog = ShowImageMatrixDialog(self)
        match self.sender():
            case self.show_source_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.source_image)
            case self.show_wave_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.wave_matrix)
            case self.show_grayscale_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.grayscale_image)
            case _:
                msg = "Invalid sender"
                raise BaseException(msg)
        show_matrix_dialog.show()

    def save_image(self):
        save_image(self, self.grayscale_image)
