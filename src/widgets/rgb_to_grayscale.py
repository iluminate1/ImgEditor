import threading
from functools import cache
from typing import override

from PySide6.QtGui import QImage, QResizeEvent, qRgb
from PySide6.QtWidgets import QMessageBox, QWidget

from ui import RgbToGrayscaleWidgetUI
from utils import ImageFormat, load_image, save_image, set_pixmap
from utils.exceptions import (
    ImageLoadException,
    InvalidFileException,
    InvalidImageFormat,
)
from window.matrix_dialog import ImageMatrixDialog


class RgbToGrayscaleWidget(QWidget, RgbToGrayscaleWidgetUI):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)

        self.source_image: QImage
        self.grayscale_image: QImage
        self.connect_signals()

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not hasattr(self, "source_image") or self.source_image.isNull():
            return

        set_pixmap(self.source_image, self.source_image_label_pixmap)
        set_pixmap(self.grayscale_image, self.grayscale_image_label_pixmap)

    def connect_signals(self) -> None:
        _ = self.load_source_image_button.clicked.connect(self.load_source_image)
        _ = self.save_grayscale_image_button.clicked.connect(self.save_image)
        _ = self.show_grayscale_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_image_red_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_image_green_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_image_blue_matrix_button.clicked.connect(self.show_matrix)

    def load_source_image(self):
        try:
            img = load_image(self, ImageFormat.rgb)
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

        self.source_image = img
        self.grayscale_image = QImage(
            img.size(),
            QImage.Format.Format_Grayscale8,
        )

        set_pixmap(self.source_image, self.source_image_label_pixmap)
        threading.Thread(target=self.convert_to_grayscale).start()

    @cache  # noqa: B019
    def _get_lightness(self, rgb: tuple[int, int, int]) -> int:
        cmax = max(rgb)
        cmin = min(rgb)

        return (cmax + cmin) // 2

    def convert_to_grayscale(self) -> None:
        source_image = self.source_image
        grayscale_image = self.source_image.copy()

        width = source_image.width()
        height = source_image.height()
        for y in range(height):
            for x in range(width):
                pixel_color = source_image.pixelColor(x, y)
                rgb = (
                    pixel_color.red(),
                    pixel_color.green(),
                    pixel_color.blue(),
                )
                lightness = self._get_lightness(rgb)

                grayscale_image.setPixel(
                    x,
                    y,
                    qRgb(lightness, lightness, lightness),
                )

        self.grayscale_image = grayscale_image
        set_pixmap(grayscale_image, self.grayscale_image_label_pixmap)

    def show_matrix(self):
        show_matrix_dialog = ImageMatrixDialog(self)
        match self.sender():
            case self.show_grayscale_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.grayscale_image)
            case self.show_image_red_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(
                    self.source_image, ImageFormat.rgb, "red"
                )
            case self.show_image_green_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(
                    self.source_image, ImageFormat.rgb, "green"
                )
            case self.show_image_blue_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(
                    self.source_image, ImageFormat.rgb, "blue"
                )
            case _:
                msg = "Invalid sender"
                raise BaseException(msg)
        show_matrix_dialog.show()

    def save_image(self):
        save_image(self, self.grayscale_image)
