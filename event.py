''' 
The Event class represents a scheduled occurrence such as a meeting, appointment, 
or gathering. Unlike tasks, events are typically tied to a specific date or time 
and do not have progress states.
'''

import datetime

# DONE: create an Event class

class Event:

    # DONE: write a constructor with the attributes event_name, description, date, start_time, 
    #       end_time, and category_name. Each of these attributes  will be passed in as arguments. 
    #       They should be set to each of the attributes accordingly.

    def __init__(self, event_name, description, date, start_time, end_time, category_name):
        self.event_name = event_name
        self.description = description
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.category_name = category_name

    # DONE: write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    def get_event_name(self) -> str:
        return self.event_name
    
    def set_event_name(self, event_name) -> None:
        self.event_name = event_name

    def get_description(self) -> str:
        return self.description
    
    def set_description(self, description) -> None:
        self.description = description

    def get_date(self) -> datetime.date:
        return self.date
    
    def set_date(self, date) -> None:
        self.date = date

    def get_start_time(self) -> datetime.time:
        return self.start_time
    
    def set_start_time(self, start_time) -> None:
        self.start_time = start_time

    def get_end_time(self) -> datetime.time:
        return self.end_time
    
    def set_end_time(self, end_time) -> None:
        self.end_time = end_time

    def get_category_name(self) -> str:
        return self.category_name
    
    def set_category_name(self, category_name) -> None:
        self.category_name = category_name

    # DONE: write a method called to_dict. This method should return an Event object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding 
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.

    def to_dict(self) -> dict:
        return {
            "event_name": self.event_name,
            "description": self.description,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "category_name": self.category_name
        }

    # DONE: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to an Event attribute. Create and return an Event 
    #       object using the data extracted from the dictionary.

    @staticmethod
    def from_dict(data) -> Event:
        return Event(
            event_name=data["event_name"],
            description=data["description"],
            date=data["date"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            category_name=data["category_name"]
        )