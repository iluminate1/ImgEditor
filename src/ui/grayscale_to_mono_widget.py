################################################################################
## Form generated from reading UI file 'GrayscaleToMonowCetTz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class GrayscaleToMonoWidgetUI:
    def setupUi(self, GrayscaleToMonoWidget: QWidget):  # noqa: N802, N803
        if not GrayscaleToMonoWidget.objectName():
            GrayscaleToMonoWidget.setObjectName("GrayscaleToMonoWidget")
        GrayscaleToMonoWidget.resize(1200, 600)
        GrayscaleToMonoWidget.setMinimumSize(QSize(900, 400))

        self.horizontalLayout_12 = QHBoxLayout(GrayscaleToMonoWidget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.load_source_image_button = QPushButton(GrayscaleToMonoWidget)
        self.load_source_image_button.setObjectName("load_source_image_button")

        self.verticalLayout_10.addWidget(self.load_source_image_button)

        self.line_16 = QFrame(GrayscaleToMonoWidget)
        self.line_16.setObjectName("line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_16)

        self.source_image_label_pixmap = QLabel(GrayscaleToMonoWidget)
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
        self.source_image_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.source_image_label_pixmap)

        self.label_11 = QLabel(GrayscaleToMonoWidget)
        self.label_11.setObjectName("label_11")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.line_17 = QFrame(GrayscaleToMonoWidget)
        self.line_17.setObjectName("line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_17)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.show_source_image_matrix_button = QPushButton(GrayscaleToMonoWidget)
        self.show_source_image_matrix_button.setObjectName(
            "show_source_image_matrix_button"
        )

        self.horizontalLayout_11.addWidget(self.show_source_image_matrix_button)

        self.show_source_image_histogram_button = QPushButton(GrayscaleToMonoWidget)
        self.show_source_image_histogram_button.setObjectName(
            "show_source_image_histogram_button"
        )

        self.horizontalLayout_11.addWidget(self.show_source_image_histogram_button)

        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.line_18 = QFrame(GrayscaleToMonoWidget)
        self.line_18.setObjectName("line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_18)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.save_avg_brightness_image_button = QPushButton(GrayscaleToMonoWidget)
        self.save_avg_brightness_image_button.setObjectName(
            "save_avg_brightness_image_button"
        )

        self.verticalLayout_9.addWidget(self.save_avg_brightness_image_button)

        self.line_13 = QFrame(GrayscaleToMonoWidget)
        self.line_13.setObjectName("line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_13)

        self.avg_birghtness_image_label_pixmap = QLabel(GrayscaleToMonoWidget)
        self.avg_birghtness_image_label_pixmap.setObjectName(
            "avg_birghtness_image_label_pixmap"
        )
        sizePolicy.setHeightForWidth(
            self.avg_birghtness_image_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.avg_birghtness_image_label_pixmap.setSizePolicy(sizePolicy)
        self.avg_birghtness_image_label_pixmap.setStyleSheet(
            "border: 1px solid rgb(0, 0, 0);"
        )
        self.avg_birghtness_image_label_pixmap.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.verticalLayout_9.addWidget(self.avg_birghtness_image_label_pixmap)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QLabel(GrayscaleToMonoWidget)
        self.label_10.setObjectName("label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.avg_brightness_spinbox = QSpinBox(GrayscaleToMonoWidget)
        self.avg_brightness_spinbox.setObjectName("avg_brightness_spinbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.avg_brightness_spinbox.sizePolicy().hasHeightForWidth()
        )
        self.avg_brightness_spinbox.setSizePolicy(sizePolicy2)
        self.avg_brightness_spinbox.setMaximumSize(QSize(16777215, 15))
        font = QFont()
        font.setPointSize(9)
        self.avg_brightness_spinbox.setFont(font)
        self.avg_brightness_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.avg_brightness_spinbox.setMinimum(50)
        self.avg_brightness_spinbox.setMaximum(254)
        self.avg_brightness_spinbox.setStepType(
            QAbstractSpinBox.StepType.AdaptiveDecimalStepType
        )
        self.avg_brightness_spinbox.setValue(120)

        self.horizontalLayout_10.addWidget(self.avg_brightness_spinbox)

        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.line_14 = QFrame(GrayscaleToMonoWidget)
        self.line_14.setObjectName("line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_14)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.show_avg_brightness_image_matrix_button = QPushButton(
            GrayscaleToMonoWidget
        )
        self.show_avg_brightness_image_matrix_button.setObjectName(
            "show_avg_brightness_image_matrix_button"
        )

        self.horizontalLayout_5.addWidget(self.show_avg_brightness_image_matrix_button)

        self.apply_avg_method_button = QPushButton(GrayscaleToMonoWidget)
        self.apply_avg_method_button.setObjectName("apply_avg_method_button")

        self.horizontalLayout_5.addWidget(self.apply_avg_method_button)

        self.show_avg_brightness_image_histogram_button = QPushButton(
            GrayscaleToMonoWidget
        )
        self.show_avg_brightness_image_histogram_button.setObjectName(
            "show_avg_brightness_image_histogram_button"
        )

        self.horizontalLayout_5.addWidget(
            self.show_avg_brightness_image_histogram_button
        )

        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_12.addLayout(self.verticalLayout_9)

        self.line_15 = QFrame(GrayscaleToMonoWidget)
        self.line_15.setObjectName("line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_15)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.save_s8_image_button = QPushButton(GrayscaleToMonoWidget)
        self.save_s8_image_button.setObjectName("save_s8_image_button")

        self.verticalLayout_8.addWidget(self.save_s8_image_button)

        self.line_11 = QFrame(GrayscaleToMonoWidget)
        self.line_11.setObjectName("line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_11)

        self.s8_label_pixmap = QLabel(GrayscaleToMonoWidget)
        self.s8_label_pixmap.setObjectName("s8_label_pixmap")
        sizePolicy.setHeightForWidth(
            self.s8_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.s8_label_pixmap.setSizePolicy(sizePolicy)
        self.s8_label_pixmap.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.s8_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.s8_label_pixmap)

        self.label_9 = QLabel(GrayscaleToMonoWidget)
        self.label_9.setObjectName("label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.line_12 = QFrame(GrayscaleToMonoWidget)
        self.line_12.setObjectName("line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.show_s8_image_matrix_button = QPushButton(GrayscaleToMonoWidget)
        self.show_s8_image_matrix_button.setObjectName("show_s8_image_matrix_button")

        self.horizontalLayout_9.addWidget(self.show_s8_image_matrix_button)

        self.show_s8_image_histogram_button = QPushButton(GrayscaleToMonoWidget)
        self.show_s8_image_histogram_button.setObjectName(
            "show_s8_image_histogram_button"
        )

        self.horizontalLayout_9.addWidget(self.show_s8_image_histogram_button)

        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12.addLayout(self.verticalLayout_8)

        self.retranslateUi(GrayscaleToMonoWidget)

        QMetaObject.connectSlotsByName(GrayscaleToMonoWidget)

    # setupUi

    def retranslateUi(self, GrayscaleToMonoWidget: QWidget):  # noqa: N802, N803
        GrayscaleToMonoWidget.setWindowTitle(
            QCoreApplication.translate(
                "GrayscaleToMonoWidget", "GrayscaleToMonoWidget", None
            )
        )
        self.load_source_image_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "L&oad image", None)
        )
        self.source_image_label_pixmap.setText(
            QCoreApplication.translate(
                "GrayscaleToMonoWidget", "SOURCE IMAGE PIXMAP", None
            )
        )
        self.label_11.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Source Image", None)
        )
        self.show_source_image_matrix_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Show Matrix", None)
        )
        self.show_source_image_histogram_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Show Histogram", None)
        )
        self.save_avg_brightness_image_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Save image", None)
        )
        self.avg_birghtness_image_label_pixmap.setText(
            QCoreApplication.translate(
                "GrayscaleToMonoWidget", "AVG IMAGE PIXMAP", None
            )
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "GrayscaleToMonoWidget", "Average brightness image", None
            )
        )
        self.avg_brightness_spinbox.setPrefix("")
        self.show_avg_brightness_image_matrix_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Show Matrix", None)
        )
        self.apply_avg_method_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "&Apply", None)
        )
        self.show_avg_brightness_image_histogram_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Show Histogram", None)
        )
        self.save_s8_image_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Save image", None)
        )
        self.s8_label_pixmap.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "S8 IMAGE PIXMAP", None)
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "GrayscaleToMonoWidget", "S8 brightness image", None
            )
        )
        self.show_s8_image_matrix_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Show Matrix", None)
        )
        self.show_s8_image_histogram_button.setText(
            QCoreApplication.translate("GrayscaleToMonoWidget", "Show Histogram", None)
        )

    # retranslateUi
