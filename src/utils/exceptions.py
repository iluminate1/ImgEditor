class InvalidFileException(BaseException):
    def __init__(self, msg: str | None = None):
        self.msg = f"Ivalid file: {msg}"
        super().__init__(self, self.msg)


class ImageLoadException(BaseException):
    def __init__(self, msg: str = "Image can't be loaded") -> None:
        self.msg = msg
        super().__init__(self, self.msg)


class InvalidImageFormat(BaseException):
    def __init__(self, msg: str = "Invalid image format") -> None:
        self.msg = msg
        super().__init__(self, self.msg)
