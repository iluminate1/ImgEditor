from PySide6.QtWidgets import QMainWindow

from ui import ImageEditorWindowUI
from widgets import (
    ErosionWidget,
    ExpansionWidget,
    GrayscaleToMonoWidget,
    MedianFilterWidget,
    MonoToGrayscaleWidget,
    RgbToGrayscaleWidget,
)


class ImageEditor(QMainWindow, ImageEditorWindowUI):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setup_tabs()

    def setup_tabs(self) -> None:
        self.tab_mono_to_grayscale_layout.addWidget(
            MonoToGrayscaleWidget(self.tab_mono_to_grayscale)
        )
        self.tab_grayscael_to_mono_layout.addWidget(
            GrayscaleToMonoWidget(self.tab_mono_to_grayscale)
        )
        self.tab_median_filter_layout.addWidget(
            MedianFilterWidget(self.tab_median_filter)
        )
        self.tab_expansion_layout.addWidget(
            ExpansionWidget(self.tab_expansion),
        )
        self.tab_erosion_layout.addWidget(
            ErosionWidget(self.tab_erosion),
        )
        self.tab_rgb_to_grayscale_layout.addWidget(
            RgbToGrayscaleWidget(self.tab_rgb_to_grayscale)
        )
