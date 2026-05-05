'''
The Category class groups related tasks and events together. It provides organizational 
structure within the planner. 
'''

# DONE: create a Category class

class Category:

    # DONE: write a constructor with the attributes category_name and description. Each of these attributes 
    #       will be passed in as arguments. They should be set to each of the attributes accordingly.

    def __init__(self, category_name, description):
        self.category_name: str = category_name
        self.description: str = description

    # DONE: write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    def get_category_name(self) -> str:
        return self.category_name
    
    def set_category_name(self, name) -> None:
        self.category_name = name
    
    def get_description(self) -> str:
        return self.description
    
    def set_description(self, description) -> None:
        self.description = description

    # DONE: write a method called to_dict. This method should return a Category object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding 
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.

    def to_dict(self) -> dict:
        return {"category_name": self.category_name, "description": self.description}

    # DONE: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to a Category attribute. Create and return a Category 
    #       object using the data extracted from the dictionary.

    @staticmethod
    def from_dict(dict):
        return Category(category_name=dict["category_name"], description=dict["description"])