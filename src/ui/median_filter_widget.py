################################################################################
## Form generated from reading UI file 'MediaFilterWidgetSTUwoo.ui'
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
    QAbstractSpinBox,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class MedianFilterWidgetUI:
    def setupUi(self, MedianFilterWidget: QWidget):  # noqa: N802, N803
        if not MedianFilterWidget.objectName():
            MedianFilterWidget.setObjectName("MedianFilterWidget")

        self.verticalLayout = QVBoxLayout(MedianFilterWidget)
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
        self.load_source_image_button = QPushButton(MedianFilterWidget)
        self.load_source_image_button.setObjectName("load_source_image_button")

        self.horizontalLayout_4.addWidget(self.load_source_image_button)

        self.save_source_image_button = QPushButton(MedianFilterWidget)
        self.save_source_image_button.setObjectName("save_source_image_button")

        self.horizontalLayout_4.addWidget(self.save_source_image_button)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.source_image_label_pixmap = QLabel(MedianFilterWidget)
        self.source_image_label_pixmap.setObjectName("source_image_label_pixmap")
        sizePolicy = QSizePolicy(  # noqa: N806
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

        self.label_2 = QLabel(MedianFilterWidget)
        self.label_2.setObjectName("label_2")
        sizePolicy1 = QSizePolicy(  # noqa: N806
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(MedianFilterWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.save_filtered_image_button = QPushButton(MedianFilterWidget)
        self.save_filtered_image_button.setObjectName("save_filtered_image_button")

        self.verticalLayout_5.addWidget(self.save_filtered_image_button)

        self.filtered_image_label_pixmap = QLabel(MedianFilterWidget)
        self.filtered_image_label_pixmap.setObjectName("filtered_image_label_pixmap")
        sizePolicy.setHeightForWidth(
            self.filtered_image_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.filtered_image_label_pixmap.setSizePolicy(sizePolicy)
        self.filtered_image_label_pixmap.setStyleSheet("border: 1px solid rgb(0,0,0);")
        self.filtered_image_label_pixmap.setFrameShape(QFrame.Shape.NoFrame)
        self.filtered_image_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.filtered_image_label_pixmap)

        self.label_4 = QLabel(MedianFilterWidget)
        self.label_4.setObjectName("label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(MedianFilterWidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_source_image_matrix_button = QPushButton(MedianFilterWidget)
        self.show_source_image_matrix_button.setObjectName(
            "show_source_image_matrix_button"
        )

        self.horizontalLayout_2.addWidget(self.show_source_image_matrix_button)

        self.add_noise_button = QPushButton(MedianFilterWidget)
        self.add_noise_button.setObjectName("add_noise_button")

        self.horizontalLayout_2.addWidget(self.add_noise_button)

        self.noise_level_spinbox = QDoubleSpinBox(MedianFilterWidget)
        self.noise_level_spinbox.setObjectName("noise_level_spinbox")
        self.noise_level_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.noise_level_spinbox.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.PlusMinus
        )
        self.noise_level_spinbox.setMaximum(1.000000000000000)
        self.noise_level_spinbox.setSingleStep(0.100000000000000)
        self.noise_level_spinbox.setStepType(
            QAbstractSpinBox.StepType.AdaptiveDecimalStepType
        )
        self.noise_level_spinbox.setValue(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.noise_level_spinbox)

        self.line_3 = QFrame(MedianFilterWidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.kernel_size_combobox = QComboBox(MedianFilterWidget)
        self.kernel_size_combobox.setObjectName("kernel_size_combobox")

        self.horizontalLayout_2.addWidget(self.kernel_size_combobox)

        self.apply_filter_button = QPushButton(MedianFilterWidget)
        self.apply_filter_button.setObjectName("apply_filter_button")

        self.horizontalLayout_2.addWidget(self.apply_filter_button)

        self.show_filtered_image_matrix_button = QPushButton(MedianFilterWidget)
        self.show_filtered_image_matrix_button.setObjectName(
            "show_filtered_image_matrix_button"
        )
        sizePolicy2 = QSizePolicy(  # noqa: N806
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.show_filtered_image_matrix_button.sizePolicy().hasHeightForWidth()
        )
        self.show_filtered_image_matrix_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.show_filtered_image_matrix_button)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(MedianFilterWidget)

        self.kernel_size_combobox.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(MedianFilterWidget)

    # setupUi

    def retranslateUi(self, MedianFilterWidget: QWidget):  # noqa: N802, N803
        MedianFilterWidget.setWindowTitle(
            QCoreApplication.translate("MedianFilterWidget", "MedianFilterWidget", None)
        )
        self.load_source_image_button.setText(
            QCoreApplication.translate("MedianFilterWidget", "L&oad image", None)
        )
        self.save_source_image_button.setText(
            QCoreApplication.translate("MedianFilterWidget", "Save image", None)
        )
        self.source_image_label_pixmap.setText(
            QCoreApplication.translate(
                "MedianFilterWidget", "SOURCE IMAGE PIXMAP", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate("MedianFilterWidget", "Source image", None)
        )
        self.save_filtered_image_button.setText(
            QCoreApplication.translate("MedianFilterWidget", "&Save image", None)
        )
        self.filtered_image_label_pixmap.setText(
            QCoreApplication.translate(
                "MedianFilterWidget", "FILTERED IMAGE PIXMAP", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("MedianFilterWidget", "Filtered image", None)
        )
        self.show_source_image_matrix_button.setText(
            QCoreApplication.translate(
                "MedianFilterWidget", "Show source image matrix", None
            )
        )
        self.add_noise_button.setText(
            QCoreApplication.translate("MedianFilterWidget", "Add &noise", None)
        )
        self.noise_level_spinbox.setPrefix(
            QCoreApplication.translate("MedianFilterWidget", "level: ", None)
        )
        self.kernel_size_combobox.setCurrentText("")
        self.kernel_size_combobox.setPlaceholderText(
            QCoreApplication.translate("MedianFilterWidget", "select kernel size", None)
        )
        self.apply_filter_button.setText(
            QCoreApplication.translate("MedianFilterWidget", "F&ilter", None)
        )
        self.show_filtered_image_matrix_button.setText(
            QCoreApplication.translate(
                "MedianFilterWidget", "Show filtered matrix", None
            )
        )

    # retranslateUi
