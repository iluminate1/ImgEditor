from PySide6.QtWidgets import QWidget

from ui import ExpansionWidgetUI


class ExpansionWidget(QWidget, ExpansionWidgetUI):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent=parent)
        self.setupUi(self)
