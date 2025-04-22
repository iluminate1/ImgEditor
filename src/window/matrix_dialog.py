from functools import singledispatchmethod
from typing import TYPE_CHECKING, Literal

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QWidget

from ui import MatrixDialogUI
from utils import ImageFormat, to_binary_format

if TYPE_CHECKING:
    from collections.abc import Callable

type matrix = list[list[float]]


class ImageMatrixDialog(QDialog, MatrixDialogUI):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)

    @singledispatchmethod
    def insert_pixels_to_table(self) -> None:
        msg = "Not implemented format"
        raise NotImplementedError(msg)

    @insert_pixels_to_table.register
    def _(
        self,
        img: QImage,
        format: ImageFormat | None = None,
        color: Literal["red", "green", "blue"] | None = None,
    ):
        width = img.width()
        height = img.height()

        self.tableWidget.setRowCount(height)
        self.tableWidget.setColumnCount(width)

        for i in range(height):
            for j in range(width):
                pixel = img.pixelColor(j, i)
                p_color = pixel.value()

                match format:
                    case ImageFormat.binary:
                        item = QTableWidgetItem(str(to_binary_format(p_color)))
                    case ImageFormat.grayscale:
                        item = QTableWidgetItem(str(p_color))
                    case ImageFormat.rgb:
                        if not color:
                            msg = "Invalid color"
                            raise BaseException(msg)
                        # FIX: do it differently
                        fn: Callable[..., int] = getattr(pixel, color)
                        item = QTableWidgetItem(str(fn()))
                    case _:
                        # check for backward compatibility
                        if img.format() == QImage.Format.Format_Mono:
                            item = QTableWidgetItem(str(p_color))
                        else:
                            item = QTableWidgetItem(str(p_color))

                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

    @insert_pixels_to_table.register(list)
    def _(self, img: matrix) -> None:
        height = len(img)
        width = len(img[0])

        self.tableWidget.setRowCount(height)
        self.tableWidget.setColumnCount(width)

        for i in range(height):
            for j in range(width):
                item = QTableWidgetItem(str(img[j][i]))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
