################################################################################
## Form generated from reading UI file 'RgbToGrayscaleBMUlRX.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
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
    def setupUi(self, RgbToGrayscaleWidget: QWidget):  # noqa: N802, N803, PLR0915
        if not RgbToGrayscaleWidget.objectName():
            RgbToGrayscaleWidget.setObjectName("RgbToGrayscaleWidget")
        RgbToGrayscaleWidget.resize(838, 515)
        self.verticalLayout = QVBoxLayout(RgbToGrayscaleWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.load_source_image_button = QPushButton(RgbToGrayscaleWidget)
        self.load_source_image_button.setObjectName("load_source_image_button")

        self.verticalLayout_2.addWidget(self.load_source_image_button)

        self.source_image_label_pixmap = QLabel(RgbToGrayscaleWidget)
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

        self.label_2 = QLabel(RgbToGrayscaleWidget)
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

        self.line = QFrame(RgbToGrayscaleWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.save_grayscale_image_button = QPushButton(RgbToGrayscaleWidget)
        self.save_grayscale_image_button.setObjectName("save_grayscale_image_button")

        self.verticalLayout_5.addWidget(self.save_grayscale_image_button)

        self.grayscale_image_label_pixmap = QLabel(RgbToGrayscaleWidget)
        self.grayscale_image_label_pixmap.setObjectName("grayscale_image_label_pixmap")
        sizePolicy.setHeightForWidth(
            self.grayscale_image_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.grayscale_image_label_pixmap.setSizePolicy(sizePolicy)
        self.grayscale_image_label_pixmap.setStyleSheet("border: 1px solid rgb(0,0,0);")
        self.grayscale_image_label_pixmap.setFrameShape(QFrame.Shape.NoFrame)
        self.grayscale_image_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.grayscale_image_label_pixmap)

        self.label_4 = QLabel(RgbToGrayscaleWidget)
        self.label_4.setObjectName("label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_3 = QFrame(RgbToGrayscaleWidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.show_image_red_matrix_button = QPushButton(RgbToGrayscaleWidget)
        self.show_image_red_matrix_button.setObjectName("show_image_red_matrix_button")

        self.horizontalLayout_5.addWidget(self.show_image_red_matrix_button)

        self.show_image_green_matrix_button = QPushButton(RgbToGrayscaleWidget)
        self.show_image_green_matrix_button.setObjectName(
            "show_image_green_matrix_button"
        )

        self.horizontalLayout_5.addWidget(self.show_image_green_matrix_button)

        self.show_image_blue_matrix_button = QPushButton(RgbToGrayscaleWidget)
        self.show_image_blue_matrix_button.setObjectName(
            "show_image_blue_matrix_button"
        )

        self.horizontalLayout_5.addWidget(self.show_image_blue_matrix_button)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)

        self.line_2 = QFrame(RgbToGrayscaleWidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.show_grayscale_image_matrix_button = QPushButton(RgbToGrayscaleWidget)
        self.show_grayscale_image_matrix_button.setObjectName(
            "show_grayscale_image_matrix_button"
        )

        self.horizontalLayout_4.addWidget(self.show_grayscale_image_matrix_button)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(RgbToGrayscaleWidget)

        QMetaObject.connectSlotsByName(RgbToGrayscaleWidget)

    # setupUi

    def retranslateUi(self, RgbToGrayscaleWidget: QWidget):  # noqa: N802, N803
        RgbToGrayscaleWidget.setWindowTitle(
            QCoreApplication.translate(
                "RgbToGrayscaleWidget", "RgbToGrayscaleWidget", None
            )
        )
        self.load_source_image_button.setText(
            QCoreApplication.translate("RgbToGrayscaleWidget", "L&oad image", None)
        )
        self.source_image_label_pixmap.setText(
            QCoreApplication.translate(
                "RgbToGrayscaleWidget", "SOURCE IMAGE PIXMAP", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate("RgbToGrayscaleWidget", "Source image", None)
        )
        self.save_grayscale_image_button.setText(
            QCoreApplication.translate("RgbToGrayscaleWidget", "S&ave image", None)
        )
        self.grayscale_image_label_pixmap.setText(
            QCoreApplication.translate(
                "RgbToGrayscaleWidget", "GRAYSCALE IMAGE PIXMAP", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("RgbToGrayscaleWidget", "Grayscale image", None)
        )
        self.show_image_red_matrix_button.setText(
            QCoreApplication.translate("RgbToGrayscaleWidget", "show R matrix", None)
        )
        self.show_image_green_matrix_button.setText(
            QCoreApplication.translate("RgbToGrayscaleWidget", "show G matrix", None)
        )
        self.show_image_blue_matrix_button.setText(
            QCoreApplication.translate("RgbToGrayscaleWidget", "show B matrix", None)
        )
        self.show_grayscale_image_matrix_button.setText(
            QCoreApplication.translate(
                "RgbToGrayscaleWidget", "show grayscale image matrix", None
            )
        )

    # retranslateUi
