
# DONE: import the json module and the Planner class 

import json
from planner import Planner

'''
The Data_Manager class handles persistence. It is responsible for loading planner 
data from storage and saving planner data back to storage.
'''

# DONE: create a Data_Manager class

class Data_Manager:
    
    # DONE: write a constructor with the attribute file_path which is sent as an argument

    def __init__(self, file_path):
        self.file_path = file_path

    # DONE: write a method called open_planner. It will open the file specified in the file_path
    #       attribute and read the data from it. It will then use the json loads command to 
    #       convert the json object to a dictionary. The dictionary should then be used to create 
    #       a Planner object using the from_dict method and return the resulting object.

    def open_planner(self) -> Planner:
        with open(self.file_path, "r") as file:
            json_data = json.load(file)
        return Planner.from_dict(data=json_data)
    
    # DONE: Write a method called save_planner that accepts a Planner object as an argument.
    #       It should then open the file from the file_path attribute in write mode. It will
    #       then convert the Planner to a dictionary and use the json dump command to write 
    #       the dictionary to the file.

    def save_planner(self, planner) -> None:
        with open(self.file_path, "w") as file:
            json.dump(planner.to_dict(), file, indent=5)