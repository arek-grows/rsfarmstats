import pickle
from main import HerbTable, database_file_name


if __name__ == "__main__":

    try:
        test = open(database_file_name, "x")
    except FileExistsError:
        print("Herbs data exists.")
        exit()

    herbs_name_dict = {
        "Torstol": "torstol",
        "Dwarf Weed": "dwarf",
        "Lantadyme": "lanta",
        "Cadantine": "cadan",
        "Snapdragon": "snap",
        "Kwuarm": "kwaurm",
        "Avantoe": "avan",
        "Irit": "irit",
        "Toadflax": "toad",
        "Ranarr": "ranarr",
        "Harralander": "harra",
        "Tarromin": "tarro",
        "Marrentill": "marren",
        "Guam": "guam"
    }

    herb_objects = []

    for kk, vv in herbs_name_dict.items():
        herb_objects.append(HerbTable(kk, vv))

    with open(database_file_name, "wb") as herbs:
        pickle.dump(herb_objects, herbs)

    print("File created.")
