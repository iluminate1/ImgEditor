from typing import override

from PySide6.QtGui import QImage, QResizeEvent
from PySide6.QtWidgets import QMessageBox, QWidget

from ui import UnlockWidgetUI
from utils import ImageFormat, load_image, save_image, set_pixmap
from utils.exceptions import (
    ImageLoadException,
    InvalidFileException,
    InvalidImageFormat,
)
from window.matrix_dialog import ImageMatrixDialog
from window.setup_mask_dialog import SetupMaskDialog


class UnlockWidget(QWidget, UnlockWidgetUI):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.source_image: QImage
        self.unlocked: QImage
        self.setup_mask_dialog = SetupMaskDialog(self)

        self.connect_signals()

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not hasattr(self, "source_image"):
            return

        set_pixmap(self.source_image, self.source_image_label_pixmap)
        set_pixmap(self.unlocked, self.unlocked_image_label_pixmap)

    def connect_signals(self) -> None:
        _ = self.load_source_image_button.clicked.connect(self.load_source_image)
        _ = self.save_unlocked_image_button.clicked.connect(self.save_image)
        _ = self.show_unlocked_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_source_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.apply_unlocking_button.clicked.connect(self.apply_unlock)
        _ = self.setup_mask_button.clicked.connect(self.setup_mask_dialog.show)

    def load_source_image(self) -> None:
        try:
            img = load_image(self, ImageFormat.binary)
        except InvalidFileException:
            return
        except ImageLoadException as e:
            _ = QMessageBox.warning(self, e.msg, e.msg)
            return
        except InvalidImageFormat as e:
            _ = QMessageBox.warning(self, str(e.msg), "Image is not binary!!!")
            return
        else:
            self.source_image = img

        set_pixmap(img, self.source_image_label_pixmap)

    def apply_unlock(self):  # noqa: PLR0912
        """
        Perform erosion on a binary QImage using the given mask.
        Erosion shrinks the foreground (white) regions by removing pixels
        where the mask doesn't fully fit within the foreground.
        """

        mask = self.setup_mask_dialog.g_mask
        mask_rows = self.setup_mask_dialog.rows
        mask_cols = self.setup_mask_dialog.cols

        # Mask center position
        center = self.setup_mask_dialog.center_item_index

        # First step: Erosion
        eroded_image = self.source_image.copy()
        height = self.source_image.height()
        width = self.source_image.width()

        # Perform erosion
        for y in range(height):
            for x in range(width):
                if self.source_image.pixelIndex(x, y) == 1:
                    fits = True
                    for my in range(mask_rows):
                        for mx in range(mask_cols):
                            if mask[my][mx] == 1:
                                img_x = x + (mx - center)
                                img_y = y + (my - center)

                                if 0 <= img_x < width and 0 <= img_y < height:
                                    if self.source_image.pixelIndex(img_x, img_y) != 1:
                                        fits = False
                                        break
                                else:
                                    fits = False
                                    break
                        if not fits:
                            break

                    if not fits:
                        eroded_image.setPixel(x, y, 0)

        # Second step: Expansion on the eroded image
        unlocked_image = eroded_image.copy()

        for y in range(height):
            for x in range(width):
                if eroded_image.pixelIndex(x, y) == 0:
                    for my in range(mask_rows):
                        for mx in range(mask_cols):
                            if mask[my][mx] == 1:
                                img_x = x + (mx - center)
                                img_y = y + (my - center)

                                if 0 <= img_x < width and 0 <= img_y < height:  # noqa: SIM102
                                    if eroded_image.pixelIndex(img_x, img_y) == 1:
                                        unlocked_image.setPixel(x, y, 1)
                                        break
                        else:
                            continue
                        break

        self.unlocked = unlocked_image
        set_pixmap(unlocked_image, self.unlocked_image_label_pixmap)

    def show_matrix(self) -> None:
        show_matrix_dialog = ImageMatrixDialog(self)
        match self.sender():
            case self.show_source_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.source_image)
            case self.show_unlocked_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.unlocked)
            case _:
                msg = "Invalid sender"
                raise BaseException(msg)
        show_matrix_dialog.show()

    def save_image(self) -> None:
        save_image(self, self.unlocked)
