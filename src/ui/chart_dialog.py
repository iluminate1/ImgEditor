from PySide6.QtCharts import QBarCategoryAxis, QChart, QChartView, QValueAxis
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (
    QDialog,
    QPushButton,
    QVBoxLayout,
)


class ChartDialogUI:
    def setup_ui(self, dialog: QDialog) -> None:
        if not dialog.objectName():
            dialog.setObjectName("ChartDialog")

        dialog.setWindowTitle("Image Histogram")
        dialog.setMinimumSize(600, 400)

        layout = QVBoxLayout()

        # Chart view
        self.chart = QChart()
        self.chart.setTitle("Image Histogram")
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        layout.addWidget(self.chart_view)

        # Axes
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append("")
        self.axis_y = QValueAxis()

        self.close_button = QPushButton("Close")
        _ = self.close_button.clicked.connect(dialog.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)
