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
import pickle
from statistics import median

project_path = "C:/Users/arkad/Desktop/rsfarmstats/"
database_file_name = f"{project_path}herbs.pkl"
spreadsheet_name = "C:/Users/arkad/Desktop/rsfarmstats/Herb Harvests.xlsx"
herbs_name_dict = [
    "Torstol", "Dwarf Weed", "Lantadyme", "Cadantine", "Snapdragon", "Kwuarm", "Avantoe", "Irit", "Toadflax", "Ranarr",
    "Harralander", "Tarromin""Marrentill", "Guam"
]


class HerbTable:

    def __init__(self, name):
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

    def add_yields(self, yields):
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
            # print(f"No data for {self.name}")
            return
        print(f"""Stats for {self.name} harvests:
        
        # of Harvests:   {self.nr_harvests}
        Lowest Yield:    {self.lowest_yield}
        Highest Yield:   {self.highest_yield}
        Total Harvested: {self.total_harvested}
        
        Death Chance:    {self.death_rate * 100}%
        Median Yield:    {self.median_yield}
        Average Yield:   {self.average_yield}
        Yield per Seed:  {self.average_yield * 1.1}
""")

    def validate_data(self):
        # bug testing function
        if len(self.lowest_yield) is None:
            # print("No data to revalidate.")
            return
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


# todo: ? good i think
def calc_data_to_herb_table(herb_object, yield_list):
    """transforms cumulative data into yield per allotment harvest"""
    first_yield = yield_list[0]
    real_yields = [first_yield]
    total_yield = first_yield
    for yy in yield_list[1:]:
        real_yields.append(yy - total_yield)
        total_yield = yy
    herb_object.add_yields(real_yields)


# def herb_menu(herb_object):
#     while True:
#         herb_input = input(
#             f"\n{herb_object.name}:\n"
#             f"[add] data from file, [type] data, show [stats] of herb, [view] harvest data, or [exit]:\n").lower()
#
#         if herb_input == "add":
#             # TODO: error handling (add), saving (add, type), line reading copout (2 new lines at end of file)
#             herb_input_file_name = f"{herb_object.name} Input.txt"
#             # last line has to be 2 new lines
#             with open(herb_input_file_name, "r") as herb_input_file:
#                 appended_yields = []
#                 for line in herb_input_file:
#                     if line != "\n":
#                         appended_yields.append(int(line))
#                     else:
#                         calc_data_to_herb_table(herb_object, appended_yields)
#                         appended_yields = []
#             print("Data imported.")
#
#         elif herb_input == "type":
#             print("enter numbers, then [save] or [cancel]")
#             done = False
#             input_data = []
#             while not done:
#                 data_input = input()
#                 if data_input not in ["save", "test", "cancel"]:
#                     try:
#                         input_data.append(int(data_input))
#                     except ValueError:
#                         print("Invalid input.")
#                 elif data_input in ["save", "test"]:
#                     calc_data_to_herb_table(herb_object, input_data)
#                     # TODO: save
#                     if data_input == "save":
#                         pass
#                     done = True
#                 else:
#                     done = True
#
#         elif herb_input == "stats":
#             herb_object.print_stats()
#
#         elif herb_input == "view":
#             print(herb_object.harvest_yields)
#
#         elif herb_input == "exit":
#             return
#
#         else:
#             print("Invalid input.")


if __name__ == '__main__':
    # unpickle here
    # with open(database_file_name, "rb") as herb_objects_file:
    #     herb_objects = pickle.load(herb_objects_file)
    # if not herb_objects:
    #     print("Error: Pickle file empty.")
    #     exit()

    # short_herb_names = []
    # for hh in herb_objects:
    #     short_herb_names.append(hh.short_name)
    # before_str = ""
    # loop_one = True

    # todo: after showing stats and validating, print a list of herbs with empty data

    # todo: new functionality: show stats then, validate data or exit
    # import data from spreadsheet into objects here
    # errors for invalid spreadsheet format (todo: determine correct format)

    # show calc'd data and export into spreadsheet here

    # [validate] or [exit] here

    # while loop_one:
        # print(f"{before_str}Herbs: {', '.join(short_herb_names)}")
        # input_one = input(
        #     "Enter an herb name, [all] for stats on all herbs, [backup], or [exit]:\n"
        # ).lower()
        # before_str = "\n"

        # if input_one in short_herb_names:
        #     idx = short_herb_names.index(input_one)
        #     herb_menu(herb_objects[idx])
        #
        # elif input_one == "all":
        #     print()
        #     for hh in herb_objects:
        #         hh.print_stats()
        #
        # elif input_one == "validate":
        #     for hh in herb_objects:
        #         hh.validate_data()
        #
        # elif input_one == "backup":
        #     with open("herbs_backup.pkl", "wb") as herbs_backup_file:
        #         pickle.dump(herb_objects, herbs_backup_file)
        #         print("'herbs_backup.pkl' created.")
        #
        # elif input_one == "exit":
        #     exit()
        #
        # else:
        #     print("Invalid input.")

    pass
