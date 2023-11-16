from datetime import datetime


def get_dt_now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_filename(filename: str) -> str:
    dt_now = datetime.now()
    return f'{dt_now.strftime("%Y-%m-%d_%H-%M-%S")}_{filename}.xlsx'
