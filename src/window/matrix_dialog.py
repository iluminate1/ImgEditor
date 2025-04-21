from functools import singledispatchmethod

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QWidget

from ui import MatrixDialogUI
from utils import to_binary_format

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
    def _(self, img: QImage):
        width = img.width()
        height = img.height()

        self.tableWidget.setRowCount(height)
        self.tableWidget.setColumnCount(width)

        is_mono_format = img.format() == QImage.Format.Format_Mono

        for i in range(height):
            for j in range(width):
                pixel_color = img.pixelColor(j, i).value()

                if is_mono_format:
                    item = QTableWidgetItem(str(to_binary_format(pixel_color)))
                else:
                    item = QTableWidgetItem(str(pixel_color))

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
