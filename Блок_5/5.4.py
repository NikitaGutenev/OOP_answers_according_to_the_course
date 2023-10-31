"""Подвиг 4"""
# здесь объявляйте классы
class StringException(Exception):
    pass


class NegativeLengthString(StringException):
    pass


class ExceedLengthString(StringException):
    pass


try:
    # здесь команда для генерации исключения
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")


