################################################################################
## Form generated from reading UI file 'SetupMaskDialogtXLjeJ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QDialog,
    QHBoxLayout,
    QHeaderView,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
)


class MaskDialogUI:
    def setupUi(self, MaskDialog: QDialog):  # noqa: N802, N803
        if not MaskDialog.objectName():
            MaskDialog.setObjectName("MaskDialog")
        MaskDialog.resize(600, 400)

        self.dialog_layout = QVBoxLayout(MaskDialog)
        self.dialog_layout.setObjectName("dialog_layout")
        self.mask_size_table = QTableWidget(MaskDialog)

        if self.mask_size_table.columnCount() < 3:  # noqa: PLR2004
            self.mask_size_table.setColumnCount(3)
        if self.mask_size_table.rowCount() < 3:  # noqa: PLR2004
            self.mask_size_table.setRowCount(3)

        self.mask_size_table.setObjectName("mask_size_table")
        self.mask_size_table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.mask_size_table.setSelectionMode(
            QAbstractItemView.SelectionMode.NoSelection
        )
        self.mask_size_table.setRowCount(3)
        self.mask_size_table.setColumnCount(3)

        # Added manually, because designer don't have this feature
        self.mask_size_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.mask_size_table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.dialog_layout.addWidget(self.mask_size_table)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.cancle_button = QPushButton(MaskDialog)
        self.cancle_button.setObjectName("cancle_button")

        self.buttons_layout.addWidget(self.cancle_button)

        self.mask_size_combobox = QComboBox(MaskDialog)
        self.mask_size_combobox.addItem("")
        self.mask_size_combobox.addItem("")
        self.mask_size_combobox.addItem("")
        self.mask_size_combobox.addItem("")
        self.mask_size_combobox.setObjectName("mask_size_combobox")

        self.buttons_layout.addWidget(self.mask_size_combobox)

        self.apply_button = QPushButton(MaskDialog)
        self.apply_button.setObjectName("apply_button")

        self.buttons_layout.addWidget(self.apply_button)

        self.dialog_layout.addLayout(self.buttons_layout)

        self.retranslateUi(MaskDialog)

        QMetaObject.connectSlotsByName(MaskDialog)

    # setupUi

    def retranslateUi(self, MaskDialog: QDialog):  # noqa: N802, N803
        MaskDialog.setWindowTitle(
            QCoreApplication.translate("MaskDialog", "Mask setup", None)
        )
        self.cancle_button.setText(
            QCoreApplication.translate("MaskDialog", "&Cancle", None)
        )
        self.mask_size_combobox.setItemText(
            0, QCoreApplication.translate("MaskDialog", "3x3", None)
        )
        self.mask_size_combobox.setItemText(
            1, QCoreApplication.translate("MaskDialog", "5x5", None)
        )
        self.mask_size_combobox.setItemText(
            2, QCoreApplication.translate("MaskDialog", "7x7", None)
        )
        self.mask_size_combobox.setItemText(
            3, QCoreApplication.translate("MaskDialog", "9x9", None)
        )

        # if QT_CONFIG(tooltip)
        self.mask_size_combobox.setToolTip(
            QCoreApplication.translate("MaskDialog", "Select mask size", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.mask_size_combobox.setPlaceholderText(
            QCoreApplication.translate("MaskDialog", "Mask size", None)
        )
        self.apply_button.setText(
            QCoreApplication.translate("MaskDialog", "&Apply", None)
        )

    # retranslateUi
