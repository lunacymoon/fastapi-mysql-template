import re
from datetime import date, datetime


def snake_to_camel(string):
    return ''.join(word.title() for word in string.split('_'))


def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()


def date_to_datetime(obj) -> datetime:
    return datetime.combine(obj, datetime.min.time())


def datetime_to_date(obj) -> date:
    return obj.date()


def string_to_datetime(string) -> datetime:
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S')


def string_to_date(string) -> date:
    return datetime.strptime(string, '%Y-%m-%d').date()


def date_to_string(obj) -> str:
    return obj.strftime('%Y-%m-%d')


def datetime_to_string(obj) -> str:
    return obj.strftime('%Y-%m-%d %H:%M:%S')


def excel_string_to_date(string) -> date:
    date = None
    date_formats = ['%Y-%m-%d', '%Y/%m/%d']
    for date_format in date_formats:
        try:
            date = datetime.strptime(string, date_format).date()
        except Exception as _:  # noqa: F841
            pass
        else:
            return date
    return None
