# DONE: import the task, category, and event classes 

from task import Task
from event import Event
from category import Category

# DONE: import the datetime library

import datetime

'''
The Planner class is the central coordinating component of the system. It owns and manages 
all categories, tasks, and events. Most application behavior ultimately routes through this class.
'''

# DONE: create a Planner class

class Planner:

    # DONE: write a constructor with the attributes name, categories, tasks, and events.
    #       Each of these attributes will be passed in as arguments. They should be set
    #       to each of the attributes accordingly.
    #       If categories, tasks, or events were passed as Nonetypes, set them equal to 
    #       an empty list.

    def __init__(self, name, categories, tasks, events):
        self.name: str = name
        self.categories: list[Category]
        self.tasks: list[Task]
        self.events: list[Event]

        if categories is not None:
            self.categories = categories
        else:
            self.categories = []

        if tasks is not None:
            self.tasks = tasks
        else:
            self.tasks = []

        if events is not None:
            self.events = events
        else:
            self.events = []  

    # DONE: write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name) -> None:
        self.name = name

    def get_categories(self) -> list[Category]:
        return self.categories
    
    def set_categories(self, categories) -> None:
        self.categories = categories

    def get_tasks(self) -> list[Task]:
        return self.tasks
    
    def set_tasks(self, tasks) -> None:
        self.tasks = tasks

    def get_events(self) -> list[Event]:
        return self.events
    
    def set_events(self, events) -> None:
        self.events = events

    # DONE: write a method called to_dict. This methods should turn a Planner object into a dictionary.
    #       It should return a dictionary where each attribute and its value is a key value pair. The key 
    #       should have the exact same name as the attribute. Categories, tasks, and events are stored
    #       as lists; each item in those lists will need to be converted to a dictionary as well. Using
    #       the to_dict method from each of those classes create lists of category, task, and event dictionaries
    #       to use for the corresponding values in the dictionary.

    def to_dict(self) -> dict:
        category_list = []
        task_list = []
        event_list = []

        for category in self.categories:
            category_list.append(category.to_dict())
        for task in self.tasks:
            task_list.append(task.to_dict())
        for event in self.events:
            event_list.append(event.to_dict())

        return {"name": self.name, "categories": category_list, "tasks": task_list, "events": event_list}

    # DONE: write a static method called from_dict. This method should take in a dictionary object as an 
    #       argument. It will then create a Planner object using the key value pairs. The keys will 
    #       correspond directly with the names of the Planner attributes. 
    #       For each of the attributes in a Planner, pull the data from the planner dictionary. You will
    #       need to convert each of the categories, events, and tasks to objects as well by calling the 
    #       from_dict method of each class. Those lists of objects should be used sent as the arguments
    #       for the Planner object--not the dictionaries from the raw data.

    @staticmethod
    def from_dict(data) -> Planner:
        category_list = []
        task_list = []
        event_list = []

        for category_dict in data["categories"]:
            category_list.append(Category.from_dict(category_dict))
        for task_dict in data["tasks"]:
            task_list.append(Task.from_dict(task_dict))
        for event_dict in data["events"]:
            event_list.append(Event.from_dict(event_dict))

        return Planner(name=data["name"], categories=category_list, tasks=task_list, events=event_list)


    #########################################
    #            Task Methods               #
    #########################################

    # DONE: write a method called create_task that is passed each of the attributes for a Task object
    #       EXCEPT for the steps. It should use the data received as arguments to create a task object
    #       sending an empty list for the steps. Once the object has been created, append it to the 
    #       Planner's list of tasks.

    def create_task(self, task_name, todays_focus, description, due_date, status, weight, category_name) -> None:
        self.tasks.append(
            Task(
                task_name=task_name,
                todays_focus=todays_focus,
                description=description,
                due_date=due_date,
                status=status,
                weight=weight,
                steps=[],
                category_name=category_name
            )
        )

    # DONE: write a method called set_task_status that is passed the index of a task. Get the task from
    #       the Planner's list of tasks according to its index and find its current status. According to
    #       the list below, set the status to the correct new value.
    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''

    def set_task_status(self, i) -> None:
        switch = {"incomplete": "started", "started": "completed", "completed": "incomplete"}
        current_status = self.tasks[i].get_status()
        self.tasks[i].set_status(switch[current_status])

    # DONE: write a method called set_task_todays_focus which is passed the index of a task. Get that task 
    #       from the Planner's list of tasks according to its index. Call the set_todays_focus method from 
    #       the Task class on that object. 

    def set_task_todays_focus(self, i) -> None:
        self.tasks[i].set_todays_focus()

    # DONE: Write a method called delete_task that will take an index as an argument. It will then delete
    #       the task at that index for the Planner object

    def delete_task(self, i) -> None:
        self.tasks.pop(i)

    # DONE: Write a method called add_task_step that will take in a task index and a step title as arguments.
    #       It will then call the add_step method on the Task object at the specified index in the Planner's 
    #       task list.

    def add_task_step(self, i, title) -> None:
        self.tasks[i].add_step(title)

    # DONE: Write a method called toggle_task_step that takes in a task index and a step index as arguments.
    #       It will then call the toggle_step method on the Task object at the specified index in the Planner's
    #       task list.

    def toggle_task_step(self, task_index, step_index) -> None:
        self.tasks[task_index].toggle_step(step_index)

    # DONE: Write a method called edit_task_step that takes a task index, a step index, and a new step title 
    #       as arguments. It will then call the edit_step method on the specified Task object.

    def edit_task_step(self, task_index, step_index, new_title) -> None:
        self.tasks[task_index].edit_step(step_index, new_title)

    # DONE: Write a method called remove_task_step that will take a task index and a step index as arguments.
    #       It will then call the remove_step on the specified Task object.

    def remove_task_step(self, task_index, step_index) -> None:
        self.tasks[task_index].remove_step(step_index)

    # DONE: Write a method called edit_task that will take a task index, task name, focus bool, description, 
    #       due date, status, and weight as arguments. Call the update_task method on the specified Task.

    def edit_task(self, index, name, focus, description, due_date, status, weight) -> None:
        self.tasks[index].update_task(name, focus, description, due_date, status, weight)

    # DONE: Write a method called get_task_by_index that accepts a task index as an arugment.
    #       It should return the specified task from the Planner's task list.

    def get_task_by_index(self, index) -> Task:
        return self.tasks[index]

    # DONE: Write a method called get_overdue tasks that accepts a date object as the argument representing today.
    #       You will need a list to store the overdue tasks. For each task in the Planner's task list, determine if 
    #       the task is overdue using the is_overdue method. If it is, add it to the list of overdue tasks and return 
    #       the list when done.

    def get_overdue_tasks(self, date) -> list[Task]:
        overdue_tasks = []
        for task in self.tasks:
            if task.is_overdue(date):
                overdue_tasks.append(task)

        return overdue_tasks
    
    # DONE: Write a method called get_due_soon that accepts a date object as the argument representing today. This method
    #       will search for any tasks due within a week. To do so, find the date 7 days from now with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. You will then need to iterate through the tasks in the
    #       Planner.  If the task's due date is greater than or equal to today's and less than or equal to the end of the week,
    #       add it to the list of tasks due soon and return when done. Tasks that were not given a due date or are already
    #       completed should not be added to the list.

    def get_due_soon(self, today) -> list[Task]:
        end_date = today + datetime.timedelta(days=7)

        due_soon = []
        for task in self.tasks: 
            if datetime.date.fromisoformat(task.due_date) >= today and datetime.date.fromisoformat(task.due_date) <= end_date:
                due_soon.append(task)

        return due_soon

    # DONE: Write a method called get_tasks_in_todays_focus. For each task in the Planner's task list, add it to a list
    #       collecting tasks where the todays_focus is set to True. Return the list of tasks in today's focus.

    def get_tasks_in_todays_focus(self) -> list[Task]:
        focus = []
        for task in self.tasks:
            if task.todays_focus:
                focus.append(task)
        
        return focus


    # DONE: write a method called get_task_status_counts. It should create a dictionary with each status as a key. The
    #       count for each status should start at a 0. For each task in the Planner, increment the count for the correct
    #       status in the dictionary. Return the dictionary when done.

    def get_task_status_counts(self) -> dict:
        tally = {"incomplete": 0, "started": 0, "completed": 0}
        for task in self.tasks:
            tally[task.get_status()] += 1
        
        return tally

    # DONE: Write a method called get_incomplete_by_category. It should create a dictionary with each category as a key.
    #       There should also be a variable to count the number of not complete tasks. The count for each category should 
    #       start at 0. For each task in the Planner, increment the count for the category that task is in only if the status
    #       is not "completed". Return a dictionary that has 2 key-value pairs: one pair has the key "total" with the value 
    #       of the number of tasks that are not complete and another pair with the key "byCategory" that has the value of the
    #       dictionary.

    def get_incomplete_by_category(self) -> dict:
        by_category: dict = {}
        for category in self.categories:
            by_category[category.get_category_name()] = 0
        
        for task in self.tasks:
            if task.get_status != "completed":
                by_category[task.get_category_name()] += 1
        
        total = 0
        for arg, value in by_category.items():
            total += value
        
        return {"total": total, "byCategory": by_category}
        
    
    #########################################
    #          Category Methods             #
    #########################################

    # DONE: Write a method called get_category_by_index that is passed a category index as an argument. Return
    #       the requested Category object from the Planner's list of categories

    def get_category_by_index(self, i) -> Category:
        return self.categories[i]

    # DONE: Write a method called add_category that accepts a name and description as arugments.
    #       Create a new Category object and add it to the Planner's list of categories.

    def add_category(self, category_name, description) -> None:
        self.categories.append(Category(category_name, description))

    # DONE: Write a method called edit_category that accepts a category index, name and description
    #       as arguments. It will then call the setters for the specified Category object.

    def edit_category(self, i, category_name=None, description=None) -> None:
        if category_name is not None:
            self.categories[i].category_name = category_name
        if description is not None:
            self.categories[i].description = description


    # DONE: Write a method called remove_category_by_index that accepts a category index as an argument.
    #       It then remvoes the specified Category object from the Planner's list of categories.

    def remove_category_by_index(self, i) -> None:
        self.categories.pop(i)


    #########################################
    #            Event Methods              #
    #########################################

    # DONE: Write a method called get_event_by_index that accepts an index as an argument. It then
    #       returns the specified Event object from the Planner's list of events.

    def get_event_by_index(self, i) -> Event:
        return self.events[i]

    # DONE: Write a method called add_event that accepts an event name, description, date, start time,
    #       end time, and category name as arguments. It then creates a new Event object and adds it 
    #       to the Planner's list of events.
    
    def add_event(self, name, description, date, start_time, end_time, category_name) -> None:
        self.events.append(Event(name, description, date, start_time, end_time, category_name))

    # DONE: Write a method called remove_event_by_index that accepts an index as an argument. It then
    #       removes the specified index from the Planner's list of events.

    def remove_event_by_index(self, i) -> None:
        self.events.pop(i)

    # DONE: Write a method called set_event_category that accepts an event index and a category name. 
    #       Set the corresponding Event object's category to the specified category name.

    def set_event_category(self, i, category_name) -> None:
        self.events[i].set_category_name(category_name)

    # DONE: Write a method called get_upcoming_events that accepts a date object as the arument representing
    #       today's date. It should calculate the date exactly 7 days from today with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. You will then need to iterate through the
    #       Planner's list of events. Collect all events in a list where there is a date and the date is greater
    #       than or equal to today and less than or equal to 7 days from now. Return the list of events happening
    #       within the next week.

    def get_upcoming_events(self, today) -> list[Event]:
        end_date = today + datetime.timedelta(days=7)
        upcoming_events = []

        for event in self.events:
            if event.date >= today and event.date <= end_date:
                upcoming_events.append(event)
        
        return upcoming_events

    # DONE: write a method called get_todays_events that accepts a date object as an argument representing
    #       today's date. Iterate throught the Planner's list of events to find event's who's date matches
    #       today's date. Collect those events in a list and return them.
    
    def get_todays_events(self, today) -> list[Event]:
        todays_events = []
        for event in self.events:
            if event.date == today:
                todays_events.append(event)
        
        return todays_events