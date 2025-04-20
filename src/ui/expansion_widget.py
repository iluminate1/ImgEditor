################################################################################
## Form generated from reading UI file 'ExpansionWidgetgveozb.ui'
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
    QLayout,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class ExpansionWidgetUI:
    def setupUi(self, ExpansionWidget: QWidget):  # noqa: N802, N803
        if not ExpansionWidget.objectName():
            ExpansionWidget.setObjectName("ExpansionWidget")
        ExpansionWidget.resize(838, 515)
        self.verticalLayout = QVBoxLayout(ExpansionWidget)
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
        self.load_source_image_button = QPushButton(ExpansionWidget)
        self.load_source_image_button.setObjectName("load_source_image_button")

        self.horizontalLayout_4.addWidget(self.load_source_image_button)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.source_image_label_pixmap = QLabel(ExpansionWidget)
        self.source_image_label_pixmap.setObjectName("source_image_label_pixmap")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )  # noqa: N806
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

        self.label_2 = QLabel(ExpansionWidget)
        self.label_2.setObjectName("label_2")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )  # noqa: N806
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(ExpansionWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.save_expanded_image_button = QPushButton(ExpansionWidget)
        self.save_expanded_image_button.setObjectName("save_expanded_image_button")

        self.verticalLayout_5.addWidget(self.save_expanded_image_button)

        self.expanded_image_label_pixmap = QLabel(ExpansionWidget)
        self.expanded_image_label_pixmap.setObjectName("expanded_image_label_pixmap")
        sizePolicy.setHeightForWidth(
            self.expanded_image_label_pixmap.sizePolicy().hasHeightForWidth()
        )
        self.expanded_image_label_pixmap.setSizePolicy(sizePolicy)
        self.expanded_image_label_pixmap.setStyleSheet("border: 1px solid rgb(0,0,0);")
        self.expanded_image_label_pixmap.setFrameShape(QFrame.Shape.NoFrame)
        self.expanded_image_label_pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.expanded_image_label_pixmap)

        self.label_4 = QLabel(ExpansionWidget)
        self.label_4.setObjectName("label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(ExpansionWidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_source_image_matrix_button = QPushButton(ExpansionWidget)
        self.show_source_image_matrix_button.setObjectName(
            "show_source_image_matrix_button"
        )

        self.horizontalLayout_2.addWidget(self.show_source_image_matrix_button)

        self.line_3 = QFrame(ExpansionWidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.setup_mask_button = QPushButton(ExpansionWidget)
        self.setup_mask_button.setObjectName("setup_mask_button")

        self.horizontalLayout_2.addWidget(self.setup_mask_button)

        self.apply_expansion_button = QPushButton(ExpansionWidget)
        self.apply_expansion_button.setObjectName("apply_expansion_button")

        self.horizontalLayout_2.addWidget(self.apply_expansion_button)

        self.line_4 = QFrame(ExpansionWidget)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.show_expanded_image_matrix_button = QPushButton(ExpansionWidget)
        self.show_expanded_image_matrix_button.setObjectName(
            "show_expanded_image_matrix_button"
        )
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.show_expanded_image_matrix_button.sizePolicy().hasHeightForWidth()
        )
        self.show_expanded_image_matrix_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.show_expanded_image_matrix_button)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ExpansionWidget)

        QMetaObject.connectSlotsByName(ExpansionWidget)

    # setupUi

    def retranslateUi(self, ExpansionWidget: QWidget):  # noqa: N802, N803
        ExpansionWidget.setWindowTitle(
            QCoreApplication.translate("ExpansionWidget", "ExpansionWidget", None)
        )
        self.load_source_image_button.setText(
            QCoreApplication.translate("ExpansionWidget", "L&oad image", None)
        )
        self.source_image_label_pixmap.setText(
            QCoreApplication.translate("ExpansionWidget", "SOURCE IMAGE PIXMAP", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("ExpansionWidget", "Source image", None)
        )
        self.save_expanded_image_button.setText(
            QCoreApplication.translate("ExpansionWidget", "&Save image", None)
        )
        self.expanded_image_label_pixmap.setText(
            QCoreApplication.translate("ExpansionWidget", "EXPANDED IMAGE PIXMAP", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("ExpansionWidget", "Expanded image", None)
        )
        self.show_source_image_matrix_button.setText(
            QCoreApplication.translate(
                "ExpansionWidget", "Show source image matrix", None
            )
        )
        self.setup_mask_button.setText(
            QCoreApplication.translate("ExpansionWidget", "Setup mask", None)
        )
        self.apply_expansion_button.setText(
            QCoreApplication.translate("ExpansionWidget", "Apply expansion", None)
        )
        self.show_expanded_image_matrix_button.setText(
            QCoreApplication.translate(
                "ExpansionWidget", "Show expanded image matrix", None
            )
        )

    # retranslateUi
