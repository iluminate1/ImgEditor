from typing import override

from PySide6.QtGui import QImage, QResizeEvent
from PySide6.QtWidgets import QMessageBox, QWidget

from ui import ExpansionWidgetUI
from utils import ImageFormat, load_image, save_image, set_pixmap
from utils.exceptions import (
    ImageLoadException,
    InvalidFileException,
    InvalidImageFormat,
)
from window.matrix_dialog import ImageMatrixDialog
from window.setup_mask_dialog import SetupMaskDialog


class ExpansionWidget(QWidget, ExpansionWidgetUI):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.source_image: QImage
        self.expanded_image: QImage
        self.setup_mask_dialog = SetupMaskDialog(self)

        self.connect_signals()

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not hasattr(self, "source_image"):
            return

        set_pixmap(self.source_image, self.source_image_label_pixmap)
        set_pixmap(self.expanded_image, self.expanded_image_label_pixmap)

    def connect_signals(self) -> None:
        _ = self.load_source_image_button.clicked.connect(self.load_source_image)
        _ = self.save_expanded_image_button.clicked.connect(self.save_image)
        _ = self.show_source_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.show_expanded_image_matrix_button.clicked.connect(self.show_matrix)
        _ = self.apply_expansion_button.clicked.connect(self.apply_expansion)
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

    def apply_expansion(self):
        """
        Perform expansion (dilation) on a binary QImage using the given mask.
        """

        mask = self.setup_mask_dialog.expansion_mask
        mask_rows = self.setup_mask_dialog.rows
        mask_cols = self.setup_mask_dialog.cols

        # Mask center position
        center = self.setup_mask_dialog.center_item_index

        image = self.source_image
        expanded_image = image.copy()

        height = image.height()
        width = image.width()

        for y in range(height):
            for x in range(width):
                # Only process background pixels (black) for expansion
                if image.pixelIndex(x, y) == 0:
                    # Check mask neighborhood
                    for my in range(mask_rows):
                        for mx in range(mask_cols):
                            if mask[my][mx] == 1:
                                img_x = x + (mx - center)
                                img_y = y + (my - center)

                                # Check bounds
                                if 0 <= img_x < width and 0 <= img_y < height:  # noqa: SIM102
                                    # If any mask position hits a foreground pixel, set this pixel to foreground
                                    if image.pixelIndex(img_x, img_y) == 1:
                                        expanded_image.setPixel(x, y, 1)
                                        break  # No need to check other mask positions
                        else:
                            continue
                        break  # Break outer loop if inner loop broke

        self.expanded_image = expanded_image
        set_pixmap(expanded_image, self.expanded_image_label_pixmap)

    def show_matrix(self) -> None:
        show_matrix_dialog = ImageMatrixDialog(self)
        match self.sender():
            case self.show_source_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.source_image)
            case self.show_expanded_image_matrix_button:
                show_matrix_dialog.insert_pixels_to_table(self.expanded_image)
            case _:
                msg = "Invalid sender"
                raise BaseException(msg)
        show_matrix_dialog.show()

    def save_image(self) -> None:
        save_image(self, self.expanded_image)
