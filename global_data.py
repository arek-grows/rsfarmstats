from os import getcwd

spreadsheet_name = "Herb Harvests.xlsx"
spreadsheet_path = f"{getcwd()}\\{spreadsheet_name}"
# todo: make a plot sheet?
herbsheet_names = ["Harvest Input", "Stats"]
herb_names = [
    "Torstol", "Dwarf Weed", "Lantadyme", "Cadantine", "Snapdragon", "Kwuarm", "Avantoe", "Irit", "Toadflax", "Ranarr",
    "Harralander", "Tarromin", "Marrentill", "Guam"
]
stats_name_list = ["# of Harvests", "Total Harvested", "Lowest Yield", "Highest Yield", "Death Chance",
                   "Median Yield", "Average Yield", "Yield per Seed", "harvest_yields"]