from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QDialog,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QVBoxLayout,
)


class MatrixDialogUI:
    def setupUi(self, dialog: QDialog):  # noqa: N802
        if not dialog.objectName():
            dialog.setObjectName("Dialog")

        dialog.resize(705, 524)

        self.dialog_layout = QVBoxLayout(dialog)
        self.dialog_layout.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QTableWidget(dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        _ = self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.verticalLayout.addWidget(self.tableWidget)

        self.closeDialog = QPushButton(dialog)
        self.closeDialog.setObjectName("closeDialog")
        _ = self.closeDialog.clicked.connect(dialog.close)
        sizePolicy = QSizePolicy(  # noqa: N806
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeDialog.sizePolicy().hasHeightForWidth())
        self.closeDialog.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.closeDialog)

        self.dialog_layout.addLayout(self.verticalLayout)

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog: QDialog):  # noqa: N802
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.closeDialog.setText(QCoreApplication.translate("Dialog", "Close", None))
