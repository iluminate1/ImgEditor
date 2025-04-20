import random
import time
from typing import override

from PySide6.QtGui import QImage, QResizeEvent, qRgb
from PySide6.QtWidgets import QMessageBox, QWidget

from ui import MedianFilterWidgetUI
from utils import load_image
from utils.exceptions import (
    ImageLoadException,
    InvalidFileException,
    InvalidImageFormat,
)
from utils.image_helper import ImageFormat, save_image, set_pixmap
from utils.pixels_helper import GrayscaleColor
from window.show_matrix_dialog import ShowImageMatrixDialog


class MedianFilterWidget(QWidget, MedianFilterWidgetUI):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)

        self.kernel_size_combobox.addItems(["3x3", "5x5", "7x7", "9x9"])
        self.kernel_size_dict = {0: 3, 1: 5, 2: 7, 3: 9}
        self.source_image: QImage
        self.filtered_image: QImage

        self.connect_signals()

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not hasattr(self, "source_image"):
            return

        set_pixmap(self.source_image, self.source_image_label_pixmap)
        set_pixmap(self.filtered_image, self.filtered_image_label_pixmap)

    def connect_signals(self) -> None:
        _ = self.load_source_image_button.clicked.connect(self.load_source_image)
        _ = self.save_source_image_button.clicked.connect(self.save_image)
        _ = self.save_filtered_image_button.clicked.connect(self.save_image)
        _ = self.show_source_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_filtered_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.add_noise_button.clicked.connect(self.add_noise)
        _ = self.apply_filter_button.clicked.connect(self.filter_image)

    def load_source_image(self) -> None:
        try:
            img = load_image(self, ImageFormat.grayscale)
        except InvalidFileException:
            return
        except ImageLoadException as e:
            _ = QMessageBox.warning(self, e.msg, e.msg)
            return
        except InvalidImageFormat as e:
            _ = QMessageBox.warning(self, str(e.msg), "Image is not grayscale!!!")
            return
        else:
            self.source_image = img

        set_pixmap(img, self.source_image_label_pixmap)
        self.filtered_image = QImage(img.size(), QImage.Format.Format_Grayscale8)

    def add_noise(self):
        image = self.source_image
        noise_level = self.noise_level_spinbox.value()
        height = image.height()
        width = image.width()
        total_pixel = height * width

        noise_pixels = int(total_pixel * noise_level)

        for _ in range(noise_pixels):
            x = random.randrange(0, width)
            y = random.randrange(0, height)
            image.setPixel(x, y, random.choice(list(GrayscaleColor)).value)

        set_pixmap(image, self.source_image_label_pixmap)

    def filter_image(self):
        source_image = self.source_image
        filtered_image = self.filtered_image
        kernel_size = self.kernel_size_dict.get(
            self.kernel_size_combobox.currentIndex(), 3
        )

        height = source_image.height()
        width = source_image.width()
        padding = kernel_size // 2

        start_time = time.perf_counter()
        for y in range(height):
            for x in range(width):
                # Initialize neighborhood values list
                neighborhood: list[int] = []

                # Collect all pixels in the neighborhood
                for ky in range(-padding, padding + 1):
                    for kx in range(-padding, padding + 1):
                        nx = x + kx
                        ny = y + ky

                        # Handle border pixels by reflection
                        if nx < 0:
                            nx = -nx
                        elif nx >= width:
                            nx = 2 * width - nx - 2

                        if ny < 0:
                            ny = -ny
                        elif ny >= height:
                            ny = 2 * height - ny - 2

                        # pixel = source_image.pixel(nx, ny)
                        # gray_value = pixel & 0xFF  # Extract grayscale value
                        pixel_color = source_image.pixelColor(nx, ny).value()
                        neighborhood.append(pixel_color)

                # Sort and find median
                neighborhood.sort()
                median = neighborhood[len(neighborhood) // 2]

                # Set the pixel in output image
                filtered_image.setPixel(x, y, qRgb(median, median, median))

        end_time = time.perf_counter()
        print(f"Time: {end_time - start_time}")

        set_pixmap(filtered_image, self.filtered_image_label_pixmap)

    def show_matrix(self):
        show_matrix_dialog = ShowImageMatrixDialog(self)
        match self.sender():
            case self.show_source_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.source_image)
            case self.show_filtered_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.filtered_image)
            case _:
                msg = "Invalid sender"
                raise BaseException(msg)
        show_matrix_dialog.show()

    def save_image(self):
        match self.sender():
            case self.save_source_image_button:
                save_image(self, self.source_image)
            case self.save_filtered_image_button:
                save_image(self, self.filtered_image)
            case _:
                pass
