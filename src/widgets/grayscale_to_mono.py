import threading
from typing import override

from PySide6.QtGui import QImage, QResizeEvent
from PySide6.QtWidgets import QMessageBox, QWidget

from ui import GrayscaleToMonoWidgetUI
from utils import sum_of_surrounding_pixels
from utils.exceptions import (
    ImageLoadException,
    InvalidFileException,
    InvalidImageFormat,
)
from utils.image_helper import ImageFormat, load_image, save_image, set_pixmap
from utils.pixels_helper import BinaryColor
from window.chart_dialog import ChartDialog
from window.matrix_dialog import ImageMatrixDialog


class GrayscaleToMonoWidget(QWidget, GrayscaleToMonoWidgetUI):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.source_image: QImage
        self.avg_brightness_image: QImage
        self.s8_brightness_image: QImage

        self.connect_signals()

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not hasattr(self, "source_image") or self.source_image.isNull():
            return

        set_pixmap(self.source_image, self.source_image_label_pixmap)
        set_pixmap(self.avg_brightness_image, self.avg_birghtness_image_label_pixmap)
        set_pixmap(self.s8_brightness_image, self.s8_label_pixmap)

    def connect_signals(self) -> None:
        _ = self.load_source_image_button.clicked.connect(self.load_source_image)
        _ = self.show_source_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_source_image_histogram_button.clicked.connect(self.show_histogram)
        _ = self.show_avg_brightness_image_matrix_button.clicked.connect(
            self.show_matrix
        )
        _ = self.show_avg_brightness_image_histogram_button.clicked.connect(
            self.show_histogram
        )
        _ = self.save_avg_brightness_image_button.clicked.connect(self.save_image)
        _ = self.show_s8_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_s8_image_histogram_button.clicked.connect(self.show_histogram)
        _ = self.save_s8_image_button.clicked.connect(self.save_image)

    def load_source_image(self):
        try:
            img = load_image(self, ImageFormat.grayscale)
        except InvalidFileException:
            return
        except ImageLoadException as e:
            _ = QMessageBox.warning(self, str(e.msg), str(e.msg))
            return
        except InvalidImageFormat as e:
            _ = QMessageBox.warning(self, str(e.msg), "Image is not grayscale!!!")
            return
        else:
            self.source_image = img

        set_pixmap(self.source_image, self.source_image_label_pixmap)

        self.avg_brightness_image = QImage(
            self.source_image.size(),
            QImage.Format.Format_Mono,
        )
        self.avg_brightness_image.fill(BinaryColor.White)
        set_pixmap(self.avg_brightness_image, self.avg_birghtness_image_label_pixmap)

        self.s8_brightness_image = QImage(
            self.source_image.size(),
            QImage.Format.Format_Mono,
        )
        self.s8_brightness_image.fill(BinaryColor.White)
        set_pixmap(self.s8_brightness_image, self.s8_label_pixmap)

        _ = self.apply_avg_method_button.clicked.connect(
            self.avg_brightness_brinarization
        )

        threading.Thread(target=self.avg_brightness_brinarization).start()
        threading.Thread(target=self.s8_binarization).start()

    def avg_brightness_brinarization(self):
        avg_brightness = self.avg_brightness_spinbox.value()
        image = self.avg_brightness_image

        height = image.height()
        width = image.width()

        for i in range(height):
            for j in range(width):
                source_pixel_brightness = self.source_image.pixelColor(j, i).value()

                # is_pixel_black = source_pixel_brightness < avg_brightness
                # if is_pixel_black:
                #     image.setPixel(j, i, BinaryColor.Black)
                # else:
                #     image.setPixel(j, i, BinaryColor.White)

                image.setPixel(
                    j,
                    i,
                    source_pixel_brightness > avg_brightness,
                )

        set_pixmap(image, self.avg_birghtness_image_label_pixmap)

    def s8_binarization(self):
        image = self.s8_brightness_image

        height = image.height()
        width = image.width()

        for i in range(height):
            for j in range(width):
                source_pixel_brightness = self.source_image.pixelColor(j, i).value()
                avg_brightness = round(
                    sum_of_surrounding_pixels(
                        self.source_image,
                        j,
                        i,
                    )
                    / 8
                    + 0.0001
                )

                # is_pixel_black = source_pixel_brightness < avg_brightness
                # if is_pixel_black:
                #     image.setPixel(j, i, BinaryColor.Black)
                # else:
                #     image.setPixel(j, i, BinaryColor.White)

                image.setPixel(
                    j,
                    i,
                    not source_pixel_brightness < avg_brightness,
                )

        set_pixmap(image, self.s8_label_pixmap)

    def save_image(self):
        match self.sender():
            case self.save_avg_brightness_image_button:
                save_image(self, self.avg_brightness_image)
            case self.save_s8_image_button:
                save_image(self, self.s8_brightness_image)
            case _:
                _ = QMessageBox.warning(self, "Save failed", "Something went wrong!")

    def show_matrix(self):
        show_matrix_dialog = ImageMatrixDialog(self)
        match self.sender():
            case self.show_source_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.source_image)
            case self.show_avg_brightness_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.avg_brightness_image)
            case self.show_s8_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.s8_brightness_image)
            case _:
                msg = "Invalid sender"
                raise BaseException(msg)
        show_matrix_dialog.show()

    def show_histogram(self):
        show_chart_dialog = ChartDialog(self)
        match self.sender():
            case self.show_source_image_histogram_button:
                show_chart_dialog.set_image(self.source_image)
            case self.show_avg_brightness_image_histogram_button:
                show_chart_dialog.set_image(self.avg_brightness_image)
            case self.show_s8_image_histogram_button:
                show_chart_dialog.set_image(self.s8_brightness_image)
            case _:
                msg = "Invalid sender"
                raise BaseException(msg)
        show_chart_dialog.show()
