from main import database_file_name
import pickle

with open(database_file_name, "rb") as herb_file:
    herb_objects = pickle.load(herb_file)

for hh in herb_objects:
    new_file_name = f"{hh.name} Input.txt"
    open(new_file_name, "x")
