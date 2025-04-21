from copy import deepcopy
from functools import cached_property

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QWidget

from ui import MaskDialogUI

type matrix = list[list[int]]


class SetupMaskDialog(QDialog, MaskDialogUI):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)

        self._expansion_mask: matrix = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ]
        self.__temp_mask: matrix = deepcopy(
            self._expansion_mask,
        )

        self.init_mask()
        self.connect_signals()

    @cached_property
    def center_item_index(self) -> int:
        return len(self._expansion_mask) // 2

    @cached_property
    def rows(self) -> int:
        return len(self._expansion_mask)

    @cached_property
    def cols(self) -> int:
        return len(self._expansion_mask[0])

    @property
    def expansion_mask(self) -> matrix:
        return self._expansion_mask

    def connect_signals(self) -> None:
        _ = self.cancle_button.clicked.connect(self.close)
        _ = self.mask_size_combobox.currentIndexChanged.connect(self.change_mask_size)
        _ = self.mask_size_table.cellDoubleClicked.connect(self.change_mask_value)
        _ = self.apply_button.clicked.connect(self.apply_mask)

    def change_mask_size(self):
        old_size = self.mask_size_table.rowCount()
        new_size = int(self.mask_size_combobox.currentText().split("x")[0])

        self.mask_size_table.clear()
        self.mask_size_table.setRowCount(new_size)
        self.mask_size_table.setColumnCount(new_size)

        self.mask_size_table.horizontalHeader().updateGeometries()
        self.mask_size_table.verticalHeader().updateGeometries()

        for i in range(new_size):
            for j in range(new_size):
                item = QTableWidgetItem(str(0))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                self.mask_size_table.setItem(i, j, item)

        # Calculate padding to center the old mask in the new one
        size_diff = new_size - old_size
        left_pad = size_diff // 2
        top_pad = size_diff // 2
        center_index = new_size // 2

        # Copy values from old mask to new mask, centered
        for row in range(old_size):
            for col in range(old_size):
                ny = row + top_pad
                nx = col + left_pad
                if 0 <= ny < new_size and 0 <= nx < new_size:
                    item = self.mask_size_table.item(row + top_pad, col + left_pad)
                    if not item:
                        msg = f"Cell[{row}:{col}] is None"
                        raise BaseException(msg)

                    if nx == center_index and ny == center_index:
                        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEnabled)

                    item.setData(
                        Qt.ItemDataRole.DisplayRole, str(self.__temp_mask[row][col])
                    )
        self.update_mask(self.__temp_mask)

    def init_mask(self) -> None:
        mask = self._expansion_mask
        rows = self.rows
        cols = self.cols

        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(str(mask[row][col]))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                if row == self.center_item_index and col == self.center_item_index:
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEnabled)

                self.mask_size_table.setItem(row, col, item)

    def update_mask(self, mask_to_update: matrix) -> None:
        rows = self.mask_size_table.rowCount()
        cols = self.mask_size_table.columnCount()

        mask: matrix = []
        for row in range(rows):
            row_items: list[int] = []
            for col in range(cols):
                item = self.mask_size_table.item(row, col)
                if not item:
                    msg = f"Cell[{row}:{col}] is None"
                    raise BaseException(msg)

                value = int(item.text())
                row_items.append(value)
            mask.append(row_items)

        mask_to_update.clear()
        mask_to_update.extend(mask)

    def change_mask_value(self, row: int, column: int) -> None:
        item = self.mask_size_table.item(row, column)
        if not item:
            msg = f"Cell[{row}:{column}] is None"
            raise BaseException(msg)

        str_value = int(item.text())
        value = int(not str_value)

        self.__temp_mask[row][column] = value
        item.setData(Qt.ItemDataRole.DisplayRole, str(value))

    def apply_mask(self) -> None:
        self.update_mask(self._expansion_mask)
        _ = self.close()
