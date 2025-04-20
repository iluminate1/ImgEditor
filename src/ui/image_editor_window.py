################################################################################
## Form generated from reading UI file 'MainWindowbXHqdM.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
)
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLayout,
    QMainWindow,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class ImageEditorWindowUI:
    def setupUi(self, ImageEditorWindow: QMainWindow):  # noqa: N802, N803
        if not ImageEditorWindow.objectName():
            ImageEditorWindow.setObjectName("image_editor_window")
        ImageEditorWindow.resize(1202, 655)
        ImageEditorWindow.setMinimumSize(QSize(1200, 600))

        self.centralwidget = QWidget(ImageEditorWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.image_editro_window_layout = QHBoxLayout(self.centralwidget)
        self.image_editro_window_layout.setObjectName("image_editro_window_layout")
        self.image_editro_window_layout.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.image_editro_window_layout.setContentsMargins(0, 0, 0, 0)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)

        self.tab_mono_to_grayscale = QWidget()
        self.tab_mono_to_grayscale.setObjectName("tab_mono_to_grayscale")
        self.tab_mono_to_grayscale.setMinimumSize(QSize(0, 0))
        self.tab_mono_to_grayscale_layout = QVBoxLayout(self.tab_mono_to_grayscale)
        self.tab_mono_to_grayscale_layout.setObjectName("tab_mono_to_grayscale_layout")
        self.tabWidget.addTab(self.tab_mono_to_grayscale, "")

        self.tab_grayscale_to_mono = QWidget()
        self.tab_grayscale_to_mono.setObjectName("tab_grayscale_to_mono")
        self.tab_grayscael_to_mono_layout = QHBoxLayout(self.tab_grayscale_to_mono)
        self.tab_grayscael_to_mono_layout.setObjectName("tab_grayscael_to_mono_layout")
        self.tabWidget.addTab(self.tab_grayscale_to_mono, "")

        self.tab_median_filter = QWidget()
        self.tab_median_filter.setObjectName("tab_median_filter")
        self.tab_median_filter_layout = QVBoxLayout(self.tab_median_filter)
        self.tab_median_filter_layout.setObjectName("tab_median_filter_layout")
        self.tabWidget.addTab(self.tab_median_filter, "")

        self.tab_expansion = QWidget()
        self.tab_expansion.setObjectName("tab_expansion")
        self.tab_expansion_layout = QVBoxLayout(self.tab_expansion)
        self.tab_expansion_layout.setObjectName("tab_expansion_layout")
        self.tabWidget.addTab(self.tab_expansion, "")

        self.tab_rgb_to_grayscale = QWidget()
        self.tab_rgb_to_grayscale.setObjectName("tab_rgb_to_grayscale")
        self.tab_rgb_to_grayscale_layout = QVBoxLayout(self.tab_rgb_to_grayscale)
        self.tab_rgb_to_grayscale_layout.setObjectName("tab_rgb_to_grayscale_layout")
        self.tabWidget.addTab(self.tab_rgb_to_grayscale, "")

        self.image_editro_window_layout.addWidget(self.tabWidget)

        ImageEditorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ImageEditorWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(ImageEditorWindow)

    # setupUi

    def retranslateUi(self, image_editor_window: QMainWindow):  # noqa: N802
        image_editor_window.setWindowTitle(
            QCoreApplication.translate("image_editor_window", "imgEditor", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_mono_to_grayscale),
            QCoreApplication.translate(
                "image_editor_window", "&binary -> grayscale", None
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_mono_to_grayscale),
            QCoreApplication.translate(
                "image_editor_window", "Transform binary image to grayscale", None
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_grayscale_to_mono),
            QCoreApplication.translate(
                "image_editor_window", "&grayscale -> binary", None
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_grayscale_to_mono),
            QCoreApplication.translate(
                "image_editor_window", "Transform grayscale image to binary image", None
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_median_filter),
            QCoreApplication.translate(
                "image_editor_window", "Median &filter for grayscale", None
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_median_filter),
            QCoreApplication.translate(
                "image_editor_window", "Media filtering for grayscale images", None
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_expansion),
            QCoreApplication.translate(
                "image_editor_window", "&Expansion for binary", None
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_expansion),
            QCoreApplication.translate(
                "image_editor_window", "Expansion for binary images", None
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_rgb_to_grayscale),
            QCoreApplication.translate(
                "image_editor_window", "&color -> grayscale", None
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_rgb_to_grayscale),
            QCoreApplication.translate(
                "image_editor_window",
                "Transform color image to grayscale image (MAX + MIN)",
                None,
            ),
        )


# endif // QT_CONFIG(tooltip)
# retranslateUi
