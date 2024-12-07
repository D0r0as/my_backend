from typing import Final

class intNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "{object} с id {id} не найден"
    message: str

    def __init__(self, _id: int, _object) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(obgect=_object, id=_id)
        super().__init__(self.message)


class strNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "{object} с id {id} не найден"
    message: str

    def __init__(self, _id: str, _object) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(obgect=_object, id=_id)
        super().__init__(self.message)

class UserAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Пользователь с ником '{id_username}' уже существует"

    def __init__(self, _id_username: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id_username=_id_username)
        super().__init__(self.message)