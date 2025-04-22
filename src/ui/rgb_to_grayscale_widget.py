################################################################################
## Form generated from reading UI file 'RgbToHslsNFFoP.ui'
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
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class RgbToGrayscaleWidgetUI:
    def setupUi(self, RgbToHslWidget: QWidget):  # noqa: N802, N803, PLR0915
        if not RgbToHslWidget.objectName():
            RgbToHslWidget.setObjectName("RgbToHslWidget")
        RgbToHslWidget.resize(838, 515)
        self.verticalLayout = QVBoxLayout(RgbToHslWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.load_source_image_button = QPushButton(RgbToHslWidget)
        self.load_source_image_button.setObjectName("load_source_image_button")

        self.verticalLayout_2.addWidget(self.load_source_image_button)

        self.source_image_label_pixmap = QLabel(RgbToHslWidget)
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

        self.label_2 = QLabel(RgbToHslWidget)
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

        self.line = QFrame(RgbToHslWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.save_grayscale_image_button = QPushButton(RgbToHslWidget)
        self.save_grayscale_image_button.setObjectName("save_grayscale_image_button")

        self.verticalLayout_5.addWidget(self.save_grayscale_image_button)

        self.grayscale_image_label_pixmap = QLabel(RgbToHslWidget)
        self.grayscale_image_label_pixmap.setObjectName("grayscale_image_label_pixmap")
        sizePolicy.setHeightForWidth(
            self.grayscale_image_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.grayscale_image_label_pixmap.setSizePolicy(sizePolicy)
        self.grayscale_image_label_pixmap.setStyleSheet("border: 1px solid rgb(0,0,0);")
        self.grayscale_image_label_pixmap.setFrameShape(QFrame.Shape.NoFrame)
        self.grayscale_image_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.grayscale_image_label_pixmap)

        self.label_4 = QLabel(RgbToHslWidget)
        self.label_4.setObjectName("label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RgbToHslWidget)

        QMetaObject.connectSlotsByName(RgbToHslWidget)

    # setupUi

    def retranslateUi(self, RgbToHslWidget: QWidget):  # noqa: N802, N803
        RgbToHslWidget.setWindowTitle(
            QCoreApplication.translate("RgbToHslWidget", "RgbToHslWidget", None)
        )
        self.load_source_image_button.setText(
            QCoreApplication.translate("RgbToHslWidget", "L&oad image", None)
        )
        self.source_image_label_pixmap.setText(
            QCoreApplication.translate("RgbToHslWidget", "SOURCE IMAGE PIXMAP", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("RgbToHslWidget", "Source image", None)
        )
        self.save_grayscale_image_button.setText(
            QCoreApplication.translate("RgbToHslWidget", "S&ave image", None)
        )
        self.grayscale_image_label_pixmap.setText(
            QCoreApplication.translate("RgbToHslWidget", "GRAYSCALE IMAGE PIXMAP", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("RgbToHslWidget", "Grayscale image", None)
        )

    # retranslateUi
