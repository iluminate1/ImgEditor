from collections import defaultdict

from PySide6.QtCharts import QBarSeries, QBarSet
from PySide6.QtGui import QImage, Qt
from PySide6.QtWidgets import QDialog, QWidget

from ui import ChartDialogUI
from utils.pixels_helper import to_binary_format


class ShowChartDialog(QDialog, ChartDialogUI):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.setup_ui(self)
        self.image: QImage
        self.group_size = 50

    def set_image(self, image: QImage):
        """Set the image and update histogram"""
        if image.isNull():
            return

        self.image = image
        self.__update_histogram()

    def __update_histogram(self):
        """Update the histogram chart based on current image"""
        if not self.image or self.image.isNull():
            return

        is_mono_format = self.image.format() == QImage.Format.Format_Mono

        # Calculate histogram
        histogram = defaultdict[int, int](int)
        for i in range(self.image.height()):
            for j in range(self.image.width()):
                value = self.image.pixelColor(j, i).value()
                if is_mono_format:
                    value = to_binary_format(value)

                histogram[value] += 1

        # Clear previous chart elements
        self.chart.removeAllSeries()
        for axis in self.chart.axes():
            self.chart.removeAxis(axis)

        series = QBarSeries()

        # Sort histogram values
        sorted_values = sorted(histogram.items())

        # Group values if there are too many
        if len(sorted_values) > 25:  # Threshold for grouping
            grouped = defaultdict[int, int](int)
            group_size = 10
            for i, (_value, count) in enumerate(sorted_values):
                group = i // group_size
                grouped[group] += count

            sorted_values = [
                (
                    f"{i * group_size}-{(i + 1) * group_size - 1}",
                    count,
                )
                for i, count in sorted(grouped.items())
            ]

        for value, count in sorted_values:
            bar_set = QBarSet(str(value))
            bar_set.setLabelColor(Qt.GlobalColor.black)
            bar_set.append(count)
            _ = series.append(bar_set)

        self.chart.addSeries(series)

        # Configure axes
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)

        _ = series.attachAxis(self.axis_x)
        _ = series.attachAxis(self.axis_y)

        # Set Y axis range
        max_count = max(sorted_values, key=lambda t: t[1])[1]
        self.axis_y.setRange(0, max_count * 1.1)
        self.axis_y.setTickInterval(10)
        self.axis_y.setLabelFormat("%d")
        self.axis_y.setTickCount(min(10, max_count + 1))

        self.axis_x.setLabelsVisible(False)

        # Configure series appearance
        series.setBarWidth(1)
        series.setLabelsVisible(True)
        series.setLabelsFormat("@value")
        series.setLabelsPosition(QBarSeries.LabelsPosition.LabelsOutsideEnd)

        self.chart.setMinimumSize(800, 600)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
