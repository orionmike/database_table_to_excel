from pathlib import Path

import openpyxl
from colorama import Fore

from config import ABS_PATH, IND, RESULT_DIR
from libs.excel import get_excel_file
from libs.utils import get_filename


def main() -> None:

    excel_list_name = 'object_list'

    excel_file = get_filename(excel_list_name)

    wb = openpyxl.Workbook()
    count_object = get_excel_file(wb, excel_list_name)

    if count_object > 0:
        print(f'{IND} count_object: {Fore.YELLOW}{count_object}')

        result_path_file = Path(f'{ABS_PATH}/{RESULT_DIR}/{excel_file}')

        if result_path_file.parent.exists():
            wb.save(result_path_file)
        else:
            print(f'{IND} {Fore.RED}excel file not saved')
            print(f'{IND} {Fore.RED}result folder not exist: [{result_path_file.parent}]')

        print(f'{IND} file saved: {result_path_file.parent}/{Fore.GREEN}{result_path_file.name}')
    else:
        print(f'{IND} {Fore.RED}objects not found for export')


if __name__ == "__main__":
    main()
