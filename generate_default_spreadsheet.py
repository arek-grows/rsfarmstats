from openpyxl import Workbook
from openpyxl.styles import PatternFill
from global_data import spreadsheet_name, spreadsheet_path, herb_names, herbsheet_names


def create_default_spreadsheet():
    herb_book = Workbook()
    s1 = herb_book.active
    s1.title = herbsheet_names[0]
    s2 = herb_book.create_sheet(herbsheet_names[1])
    s3 = herb_book.create_sheet(herbsheet_names[2])

    # input data sheet
    s1.cell(row=1, column=1).value = "Herbs:"
    s1.cell(row=2, column=1).value = "Harvests:"
    col_range = list(range(2, 3 + ((len(herb_names) - 1) * 6), 6))
    for yy, herb_name in zip(col_range, herb_names):
        this_cell = s1.cell(row=1, column=yy)
        this_cell.value = herb_name
        this_cell.fill = PatternFill("solid", fgColor="00008000")
        pass

    # stats sheet
    stats_name_list = ["# of Harvests", "Total Harvested", "Lowest Yield", "Highest Yield", "Death Chance",
                       "Median Yield", "Average Yield", "Yield per Seed"]
    for yy, stat_name in enumerate(stats_name_list, 2):
        s2.cell(row=1, column=yy).value = stat_name
    for xx, herb_name in enumerate(herb_names, 2):
        s2.cell(row=xx, column=1).value = herb_name

    # parsed data sheet
    for xx, herb_name in enumerate(herb_names, 1):
        s3.cell(row=xx, column=1).value = herb_name

    print(f"{spreadsheet_name} created.")
    herb_book.save(spreadsheet_path)
