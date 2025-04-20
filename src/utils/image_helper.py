import enum

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QFileDialog, QLabel, QWidget

from utils.exceptions import (
    ImageLoadException,
    InvalidFileException,
    InvalidImageFormat,
)


class ImageFormat(enum.Enum):
    binary = 1
    grayscale = 2


def load_image(
    parent: QWidget,
    format: ImageFormat,
) -> QImage:
    if format not in ImageFormat:
        raise InvalidImageFormat()

    open_dialog = QFileDialog(parent)
    open_dialog.setWindowTitle("Save Image")
    open_dialog.setNameFilter("BMP Image (*.bmp)")
    open_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

    file = None
    if open_dialog.exec() == QFileDialog.DialogCode.Accepted:
        file = open_dialog.selectedFiles()[0]

    if file is None:
        raise InvalidFileException()

    img = QImage()
    status = img.load(file)

    if not status:
        raise ImageLoadException()

    if format == ImageFormat.binary:
        if img.format() != QImage.Format.Format_Mono:
            raise InvalidImageFormat()
        img = img.convertToFormat(QImage.Format.Format_Mono)

    if format == ImageFormat.grayscale:
        if not img.isGrayscale():
            raise InvalidImageFormat()
        img = img.convertToFormat(QImage.Format.Format_Grayscale8)

    return img


def save_image(
    parent: QWidget,
    image: QImage,
) -> None:
    save_dialog = QFileDialog(parent)
    save_dialog.setWindowTitle("Save Image")
    save_dialog.setNameFilter("BMP Image (*.bmp)")
    save_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
    save_dialog.setDefaultSuffix("bmp")

    if save_dialog.exec() == QFileDialog.DialogCode.Accepted:
        file = save_dialog.selectedFiles()[0]
        _ = image.save(file)


def set_pixmap(
    source: QImage,
    target: QLabel,
) -> None:
    pixmap = QPixmap.fromImage(source)
    scaled_pixmap = pixmap.scaled(target.size())
    target.setPixmap(scaled_pixmap)
