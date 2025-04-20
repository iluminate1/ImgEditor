import sys

from PySide6.QtWidgets import QApplication

from window.img_editor_window import ImageEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()

    sys.exit(app.exec())
