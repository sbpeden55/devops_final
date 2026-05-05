# DONE: import the datetime library

import datetime

'''
The Task class represents an actionable to-do item. Tasks have descriptive information 
and a status (incomplete, in progress, completed).
'''

# DONE: create a Task class 

class Task:

    # DONE: write a constructor with the attributes task_name, todays_focus, description, 
    #       due_date, status, weight, steps, and category_name. Each of these attributes 
    #       will be passed in as arguments. They should be set to each of the attributes accordingly.

    def __init__(self, task_name, todays_focus, description, due_date, status, weight, steps, category_name):
        self.task_name = task_name
        self.todays_focus = todays_focus
        self.description = description
        self.due_date = due_date
        self.status = status
        self.weight = weight
        self.steps = steps
        self.category_name = category_name

    # DONE: Write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    def get_task_name(self) -> str:
        return self.task_name
    
    def set_task_name(self, task_name) -> None:
        self.task_name = task_name
    
    def get_todays_focus(self) -> bool:
        return self.todays_focus
    
    def set_todays_focus(self) -> None:
        self.todays_focus = not self.todays_focus

    def get_description(self) -> str:
        return self.description
    
    def set_description(self, description) -> None:
        self.description = description

    def get_due_date(self) -> str:
        return self.due_date
    
    def set_due_date(self, due_date) -> None:
        self.due_date = due_date

    def get_status(self) -> str:
        return self.status
    
    def set_status(self, status) -> None:
        self.status = status

    def get_weight(self) -> int:
        return self.weight
    
    def set_weight(self, weight) -> None:
        self.weight = weight

    def get_steps(self) -> list[dict]:
        return self.steps
    
    def set_steps(self, steps) -> None:
        self.steps = steps

    def get_category_name(self) -> str:
        return self.category_name
    
    def set_category_name(self, category_name) -> None:
        self.category_name = category_name

    # DONE: write a method called to_dict. This method should return a Task object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding 
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.

    def to_dict(self) -> dict:
        return {
            "task_name": self.task_name,
            "todays_focus": self.todays_focus,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "weight": self.weight,
            "steps": self.steps,
            "category_name": self.category_name
        }

    # DONE: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to a Task attribute. Create and return a Task 
    #       object using the data extracted from the dictionary.

    @staticmethod
    def from_dict(data) -> Task:
        return Task(
            task_name=data["task_name"],
            todays_focus=data["todays_focus"],
            description=data["description"],
            due_date=data["due_date"],
            status=data["status"],
            weight=data["weight"],
            steps=data["steps"],
            category_name=data["category_name"]
        )

    # DONE: Write a methdo called update_task that accepts all attributes as arugments. It then sets
    #       each of the Task object's attributes to the given arguments. If any of the arugments was
    #       not given a value, the should be set to None as default. The attributes should only be 
    #       updated if a value was passed.

    # I wanted to find a quicker way to do this and learned this from StackOverflow
    def update_task(self, task_name=None, todays_focus=None, description=None, due_date=None, status=None, weight=None, steps=None, category_name=None) -> None:

        # get dictionary of all current local variables and remove "self" from it (we're never resetting that)
        arguments = locals()
        arguments.pop("self")

        # get all class variables in dictionary form
        task_data = vars(self)

        # iterate through every key, value pair in the list of dictionary elements
        # if there is a new value, replace its old one in the dictionary
        for arg, value in arguments.items():
            if value is not None:
                task_data[arg] = value


    # DONE: Write a method called is_overdue that accepts a date object as an argument representing 
    #       today's date. If the task was not given a due date or if the status is completed, return false. 
    #       Otherwise, format the due date with the following equation:
    #           due date = datetime.date.fromisoformat(Task object's due date)
    #       Use the datetime call exactly as it was given to you. After formatting, make sure the today 
    #       argument is populated. If the argument is Nonetype, set it equal to datetime.date.today()
    #       Finally, return true if the due date is less than today's date or false if not.

    def is_overdue(self, today) -> bool:
        if not self.due_date or self.status == "completed":
            return False
        
        due_date = datetime.date.fromisoformat(self.due_date)
        if today is None:
            today = datetime.date.today()

        return due_date < today

    ###################################
    #       Step Managment            #
    ###################################

    # DONE: Write a method called add_step that is passed a step title as an argument.
    #       It then creates a new step and adds it to the Task's list of steps.
    #       Steps are each a dictionary with the keys "step" and "status". The "step" key
    #       should have the value of the title sent as an argument. The "status" key should
    #       be set to "incomplete" when created.

    def add_step(self, title) -> None:
        step = {"step": title, "status": "incomplete"}
        self.steps.append(step)

    # DONE: Write a method called toggle_step that accepts a step index as an argument.
    #       The specified step's status should be set according to the following key.
    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''

    def toggle_step(self, i) -> None:
        switch = {"incomplete": "started", "started": "completed", "completed": "incomplete"}
        status = self.steps[i]["status"]
        new_status = switch[status]
        self.steps[i]["status"] = new_status


    # DONE: Write a method called edit_step that accepts a step index and a new title as arugments.
    #       The specified step should be updated.

    def edit_step(self, i, title) -> None:
        self.steps[i]["step"] = title
    

    # DONE: Write a method called remove_step that accepts a step index as an argument.
    #       The specified step should be removed from the Task's list of steps.

    def remove_step(self, i) -> None:
        self.steps.pop(i)