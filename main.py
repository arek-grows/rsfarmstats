"""
What I want to do:
- create a class with attributes for each herb, recording: herb name, shortened herb name, death rate, number of
harvests, deaths, average yield, median yield and list of harvest yields
    - not recording # of farm runs bc a run can have multiple types of herbs (this make so sense if all herbs have same
    death rate and yield rate
- class has a function that calculates the class attributes after info has been recorded

"""
import pickle
from statistics import median

database_file_name = "herbs.pkl"


class HerbTable:

    def __init__(self, name, short_name, deaths=0, nr_harvests=0, lowest_yield=None, highest_yield=None,
                 death_rate=None, average_yield=None, median_yield=None, harvest_yields=None):
        self.name = name
        self.short_name = short_name
        self.deaths = deaths
        self.nr_harvests = nr_harvests
        self.lowest_yield = lowest_yield
        self.highest_yield = highest_yield
        self.death_rate = death_rate
        self.average_yield = average_yield
        self.median_yield = median_yield
        self.harvest_yields = harvest_yields
        if self.harvest_yields is None:
            self.harvest_yields = []

    def calc_class_attrs(self, nr_harvests_current, total_yield):
        self.death_rate = self.deaths / self.nr_harvests
        if self.average_yield is not None:
            self.average_yield = (self.average_yield + total_yield) / (nr_harvests_current + 1)
        else:
            self.average_yield = total_yield / nr_harvests_current
        self.median_yield = median(self.harvest_yields)
        self.highest_yield = max(self.harvest_yields)

    def add_yields(self, yields, total_yield):
        nr_harvests_current = len(yields)
        for yy in yields:
            if yy == 0:
                self.deaths += 1
            elif self.lowest_yield is None or yy < self.lowest_yield:
                self.lowest_yield = yy
            self.harvest_yields.append(yy)
        self.nr_harvests += nr_harvests_current
        self.calc_class_attrs(nr_harvests_current, total_yield)

    def print_stats(self):
        if self.lowest_yield is None:
            print(f"No data for {self.name}")
            return
        print(f"""Stats for {self.name} harvests:
        
        # of Harvests:   {self.nr_harvests}
        Lowest Yield:    {self.lowest_yield}
        Highest Yield:   {self.highest_yield}
        
        Death Chance:    {self.death_rate * 100}%
        Median Yield:    {self.median_yield}
        Average Yield:   {self.average_yield}
        Yield per Seed:  {self.average_yield * 1.1}
""")

    def validate_data(self):
        # bug testing function
        print(f"\nValidating data for {self.name}...")
        if len(self.harvest_yields) == 0:
            print("No data to revalidate.\n")
            return
        if self.harvest_yields.count(0) != self.deaths:
            print("NOT OK: Deaths do not match.")
        else:
            print("OK: Deaths match.")
        if self.nr_harvests != len(self.harvest_yields):
            print("NOT OK: Number oh harvests do NOT match.")
        else:
            print("OK: Number of harvests match.")
        print(f"???: average_yield = {self.average_yield} | average = {sum(self.harvest_yields)/len(self.harvest_yields)}")
        print('Done validating.\n')


def calc_data_to_herb_table(herb_object, yield_list):
    """transforms cumulative data into yield per allotment harvest"""
    first_yield = yield_list[0]
    last_yield = yield_list[-1]
    real_yields = [first_yield]
    total_yield = first_yield
    for yy in yield_list[1:]:
        real_yields.append(yy - total_yield)
        total_yield = yy
    herb_object.add_yields(real_yields, last_yield)


def herb_menu(herb_object):
    while True:
        herb_input = input(
            f"{herb_object.name}:\n"
            f"[add] data from file, [type] data, show [stats] of herb, [view] harvest data, or [exit]:\n").lower()

        if herb_input == "add":
            # TODO: error handling (add), saving (add, type), line reading copout (2 new lines at end of file)
            herb_input_file_name = f"{herb_object.name} Input.txt"
            # last line has to be 2 new lines
            with open(herb_input_file_name, "r") as herb_input_file:
                appended_yields = []
                for line in herb_input_file:
                    if line != "\n":
                        appended_yields.append(int(line))
                    else:
                        calc_data_to_herb_table(herb_object, appended_yields)
                        appended_yields = []

        elif herb_input == "type":
            print("enter numbers, then [save] or [cancel]")
            done = False
            input_data = []
            while not done:
                data_input = input()
                if data_input not in ["save", "test", "cancel"]:
                    try:
                        input_data.append(int(data_input))
                    except ValueError:
                        print("Invalid input.")
                elif data_input in ["save", "test"]:
                    calc_data_to_herb_table(herb_object, input_data)
                    # TODO: save
                    if data_input == "save":
                        pass
                    done = True
                else:
                    done = True

        elif herb_input == "stats":
            herb_object.print_stats()

        elif herb_input == "view":
            print(herb_object.harvest_yields)

        elif herb_input == "exit":
            return

        else:
            print("Invalid input.")


if __name__ == '__main__':
    # unpickle here
    with open(database_file_name, "rb") as herb_objects_file:
        herb_objects = pickle.load(herb_objects_file)
    if not herb_objects:
        print("Error: Pickle file empty.")
        exit()

    short_herb_names = []
    for hh in herb_objects:
        short_herb_names.append(hh.short_name)

    loop_one = True
    while loop_one:
        print(f"Herbs: {', '.join(short_herb_names)}")
        input_one = input(
            "Enter an herb name, [all] for stats on all herbs, [backup], or [exit]:\n"
        ).lower()

        if input_one in short_herb_names:
            idx = short_herb_names.index(input_one)
            herb_menu(herb_objects[idx])

        elif input_one == "all":
            for hh in herb_objects:
                hh.print_stats()
            print()

        elif input_one == "validate":
            for hh in herb_objects:
                hh.validate_data()

        elif input_one == "backup":
            with open("herbs_backup.pkl", "wb") as herbs_backup_file:
                pickle.dump(herb_objects, herbs_backup_file)
                print("'herbs_backup.pkl' created.\n")

        elif input_one == "exit":
            exit()

        else:
            print("Invalid input.\n")
