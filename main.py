import openpyxl
import sys


def format_excel(file_name, prefix="texto"):
    changes = {
        "_TW": "_ZH_HANT",
        "_FI": "_FI_FI",
        "_MK": "_MK_MK",
        "_GL": "_GL_ES",
        "_EU": "_EU_ES"
    }

    excel = openpyxl.load_workbook(file_name)
    sheet_name = excel.sheetnames[0]
    sheet = excel[sheet_name]
    header_row = sheet[1]  # Arrays start at 1 in Excel

    changed_cells = 0

    for cell in header_row:
        if cell.value is not None:
            for change in changes:
                if (prefix.lower() + change.lower()) == cell.value.lower():
                    new_value = prefix.lower() + changes[change].lower()
                    new_value = new_value.upper()
                    print("Changed cell", cell.value, "to", new_value)
                    changed_cells = changed_cells + 1
                    cell.value = new_value

    print(changed_cells, "cells changed")

    excel.save(file_name)


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        format_excel(sys.argv[1], sys.argv[2])
    elif len(sys.argv) >= 2:
        format_excel(sys.argv[1])
    else:
        print("Use 'python3 main.py file_name.xlsx' or \n    'python3 main.py file_name.xlsx prefix'")
