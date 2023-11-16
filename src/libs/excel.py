
from asyncio.log import logger
from colorama import Fore
import openpyxl
from config import IND

from database.database import session_maker
from database.models import ObjectDB


def get_excel_file(excel_work_book: openpyxl.Workbook, excel_list_name: str) -> int:

    try:

        with session_maker() as session:
            object_list = session.query(ObjectDB).all()
            session.commit()

        if object_list:

            sheet = excel_work_book.worksheets[0]
            sheet.title = excel_list_name

            object_field_list = dict(object_list[0].__table__.columns).keys()

            # insert header column
            number_column = 1
            for field in object_field_list:
                sheet.cell(row=1, column=number_column).value = field
                number_column += 1

            # insert data of objects
            number_row = 2
            for obj in object_list:

                number_column = 1
                for field in object_field_list:
                    sheet.cell(row=number_row, column=number_column).value = getattr(obj, field)
                    number_column += 1

                number_row += 1

            return number_row - 2

    except Exception as e:
        print(f'{IND} {Fore.RED}get_excel_file -> error: {e}')
        logger.error(f'get_excel_file -> error: {e}')
        return 0
