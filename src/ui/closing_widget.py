################################################################################
## Form generated from reading UI file 'ClosuresWidgetsuAqji.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class ClosingWidgetUI:
    def setupUi(self, ClosingWidget: QWidget):  # noqa: N802, N803, PLR0915
        if not ClosingWidget.objectName():
            ClosingWidget.setObjectName("ClosingWidget")
        ClosingWidget.resize(838, 515)
        self.verticalLayout = QVBoxLayout(ClosingWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.load_source_image_button = QPushButton(ClosingWidget)
        self.load_source_image_button.setObjectName("load_source_image_button")

        self.horizontalLayout_4.addWidget(self.load_source_image_button)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.source_image_label_pixmap = QLabel(ClosingWidget)
        self.source_image_label_pixmap.setObjectName("source_image_label_pixmap")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.source_image_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.source_image_label_pixmap.setSizePolicy(sizePolicy)
        self.source_image_label_pixmap.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.source_image_label_pixmap.setFrameShape(QFrame.Shape.NoFrame)
        self.source_image_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.source_image_label_pixmap)

        self.label_2 = QLabel(ClosingWidget)
        self.label_2.setObjectName("label_2")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(ClosingWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.save_closed_image_button = QPushButton(ClosingWidget)
        self.save_closed_image_button.setObjectName("save_closed_image_button")

        self.verticalLayout_5.addWidget(self.save_closed_image_button)

        self.closed_image_label_pixmap = QLabel(ClosingWidget)
        self.closed_image_label_pixmap.setObjectName("closed_image_label_pixmap")
        sizePolicy.setHeightForWidth(
            self.closed_image_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.closed_image_label_pixmap.setSizePolicy(sizePolicy)
        self.closed_image_label_pixmap.setStyleSheet("border: 1px solid rgb(0,0,0);")
        self.closed_image_label_pixmap.setFrameShape(QFrame.Shape.NoFrame)
        self.closed_image_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.closed_image_label_pixmap)

        self.label_4 = QLabel(ClosingWidget)
        self.label_4.setObjectName("label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(ClosingWidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_source_image_matrix_button = QPushButton(ClosingWidget)
        self.show_source_image_matrix_button.setObjectName(
            "show_source_image_matrix_button"
        )

        self.horizontalLayout_2.addWidget(self.show_source_image_matrix_button)

        self.line_3 = QFrame(ClosingWidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.setup_mask_button = QPushButton(ClosingWidget)
        self.setup_mask_button.setObjectName("setup_mask_button")

        self.horizontalLayout_2.addWidget(self.setup_mask_button)

        self.apply_closing_button = QPushButton(ClosingWidget)
        self.apply_closing_button.setObjectName("apply_closing_button")

        self.horizontalLayout_2.addWidget(self.apply_closing_button)

        self.line_4 = QFrame(ClosingWidget)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.show_closed_image_matrix_button = QPushButton(ClosingWidget)
        self.show_closed_image_matrix_button.setObjectName(
            "show_closed_image_matrix_button"
        )
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.show_closed_image_matrix_button.sizePolicy().hasHeightForWidth()
        )
        self.show_closed_image_matrix_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.show_closed_image_matrix_button)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ClosingWidget)

        QMetaObject.connectSlotsByName(ClosingWidget)

    # setupUi

    def retranslateUi(self, ClosingWidget: QWidget):  # noqa: N802, N803
        ClosingWidget.setWindowTitle(
            QCoreApplication.translate("ClosingWidget", "ClosingWidget", None)
        )
        self.load_source_image_button.setText(
            QCoreApplication.translate("ClosingWidget", "L&oad image", None)
        )
        self.source_image_label_pixmap.setText(
            QCoreApplication.translate("ClosingWidget", "SOURCE IMAGE PIXMAP", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("ClosingWidget", "Source image", None)
        )
        self.save_closed_image_button.setText(
            QCoreApplication.translate("ClosingWidget", "&Save image", None)
        )
        self.closed_image_label_pixmap.setText(
            QCoreApplication.translate("ClosingWidget", "CLOSED IMAGE PIXMAP", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("ClosingWidget", "Closed image", None)
        )
        self.show_source_image_matrix_button.setText(
            QCoreApplication.translate(
                "ClosingWidget", "Show source image matrix", None
            )
        )
        self.setup_mask_button.setText(
            QCoreApplication.translate("ClosingWidget", "Setup mask", None)
        )
        self.apply_closing_button.setText(
            QCoreApplication.translate("ClosingWidget", "Apply closing", None)
        )
        self.show_closed_image_matrix_button.setText(
            QCoreApplication.translate(
                "ClosingWidget", "Show closed image matrix", None
            )
        )

    # retranslateUi
