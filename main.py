"""
What I want to do:
- create a class with attributes for each herb, recording: herb name, shortened herb name, death rate, number of
harvests, deaths, average yield, median yield and list of harvest yields
    - not recording # of farm runs bc a run can have multiple types of herbs (this make so sense if all herbs have same
    death rate and yield rate
- class has a function that calculates the class attributes after info has been recorded
- harvest data recorded into a spreadsheet for ease of use then imported to each object through a class method


TODO: restructure so that harvest data is in one easily edittable (excel?) file. no need for a pickle file to store the
TODO: objects. the objects should import the data from the new easily edittable file when an herb/all herbs is called upon
TODO: then show in terminal or save in spreadsheet? do both, i think
this is inefficient at a large scale but it's fine for this small project
 """

import global_data as gd
from generate_default_spreadsheet import create_default_spreadsheet
from statistics import median
from openpyxl import load_workbook


class HerbTable:

    def __init__(self, name: str):
        self.name = name
        self.harvest_yields = []

        self.deaths = 0
        self.nr_harvests = 0
        self.lowest_yield = None
        self.highest_yield = 0

        self.death_rate = None
        self.total_harvested = None
        self.average_yield = None
        self.median_yield = None

    def calc_class_attrs(self):
        self.death_rate = self.deaths / self.nr_harvests
        self.total_harvested = sum(self.harvest_yields)
        self.average_yield = self.total_harvested / len(self.harvest_yields)
        self.median_yield = median(self.harvest_yields)

    def add_yields(self, yields: list):
        for yy in yields:
            self.nr_harvests += 1
            if yy == 0:
                self.deaths += 1
            elif self.lowest_yield is None or yy < self.lowest_yield:
                self.lowest_yield = yy
            elif yy > self.highest_yield:
                self.highest_yield = yy
            self.harvest_yields.append(yy)

    def print_stats(self):
        if self.lowest_yield is None:
            return False
        print(f"""Stats for {self.name} harvests:
        
        # of Harvests:   {self.nr_harvests}
        Total Harvested: {self.total_harvested}
        Lowest Yield:    {self.lowest_yield}
        Highest Yield:   {self.highest_yield}
        
        Death Chance:    {self.death_rate * 100}%
        Median Yield:    {self.median_yield}
        Average Yield:   {self.average_yield}
        Yield per Seed:  {self.average_yield * 1.1}
""")
        return True

    def validate_data(self):
        # bug testing function
        if len(self.lowest_yield) is None:
            return False
        print(f"\nValidating data for {self.name}...")
        if self.harvest_yields.count(0) != self.deaths:
            print("NOT OK: Deaths do not match.")
        else:
            print("OK: Deaths match.")
        if self.nr_harvests != len(self.harvest_yields):
            print("NOT OK: Number of harvests do NOT match.")
        else:
            print("OK: Number of harvests match.")
        print(
            f"Check: average_yield = {self.average_yield} | average = {sum(self.harvest_yields) / len(self.harvest_yields)}")
        print('Done validating.')
        return True


# todo: ? good i think
def calc_data_to_herb_table(herb_object: HerbTable, yield_list: list):
    """transforms cumulative data into yield per allotment harvest"""
    first_yield = yield_list[0]
    real_yields = [first_yield]
    total_yield = first_yield
    for yy in yield_list[1:]:
        real_yields.append(yy - total_yield)
        total_yield = yy
    herb_object.add_yields(real_yields)


if __name__ == '__main__':
    # todo: 3: after showing stats and validating, print a list of herbs with empty data
    # todo: DONE: check if spreadsheet exists
    # todo: 2: new functionality: [add] new data from spreadsheet (then show stats), or ask to show [stats] then,
    # todo: 2: validate data or exit
    herb_book = None
    try:
        herb_book = load_workbook(gd.spreadsheet_path)
    except FileNotFoundError:
        print(f"{gd.spreadsheet_path} does not exist.")
        print(f"Create spreadsheet? [y/n]")
        if input().lower() == 'y':
            create_default_spreadsheet()
        exit()

    input_sheet = herb_book[gd.herbsheet_names[0]]
    stats_sheet = herb_book[gd.herbsheet_names[1]]
    parse_sheet = herb_book[gd.herbsheet_names[2]]
    # create default objects or load objects from spreadsheet using pickling
    herb_objects = []
    if not parse_sheet['B1'].value:
        print("cell empty.")
    else:
        print("cell note empty")
    while True:
        print("[add] new data from spreadsheet, show [stats], [exit]")
        match input().lower():

            case "add":
                pass

            case "stats":
                pass

            case "exit":
                exit()

            case _:
                "Invalid input."
    pass
