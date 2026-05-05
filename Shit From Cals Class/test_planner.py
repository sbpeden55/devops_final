import unittest
from planner import Planner
from task import Task
from category import Category
from event import Event
from datetime import date

class Test_Planner(unittest.TestCase):

    def setUp(self):
        # This creates a sample Planner with one category, one task, and one event.
        # All tests will use this same setup so they start from the same state.
        self.cat = Category("School", "School work")
        self.task = Task("HW", True, "desc", "2026-04-10", "incomplete", 3, [], "School")
        self.event = Event("Meeting", "desc", date(2026, 4, 10), "", "", "School")

        self.planner = Planner("My Planner", [self.cat], [self.task], [self.event])

    def test_init(self):
        # This checks that the Planner stores its name and lists correctly when created.
        self.assertEqual(self.planner.name, "My Planner")
        self.assertEqual(len(self.planner.categories), 1)
        self.assertEqual(len(self.planner.tasks), 1)
        self.assertEqual(len(self.planner.events), 1)

    def test_getters(self):
        # This checks that the getter methods return the correct stored data.
        self.assertEqual(self.planner.get_name(), "My Planner")
        self.assertEqual(len(self.planner.get_categories()), 1)
        self.assertEqual(len(self.planner.get_tasks()), 1)
        self.assertEqual(len(self.planner.get_events()), 1)

    def test_setters(self):
        # This checks that changing the Planner name updates it correctly.
        self.planner.set_name("New Name")
        self.assertEqual(self.planner.get_name(), "New Name")

    def test_to_dict(self):
        # This checks that converting the Planner to a dictionary keeps all data.
        d = self.planner.to_dict()
        self.assertEqual(d["name"], "My Planner")
        self.assertEqual(len(d["tasks"]), 1)

    def test_from_dict(self):
        # This builds a new Planner from a dictionary and checks that it matches.
        d = self.planner.to_dict()
        new = Planner.from_dict(d)
        self.assertEqual(new.get_name(), "My Planner")
        self.assertEqual(len(new.get_tasks()), 1)

    def test_create_task(self):
        # This checks that creating a new task adds it to the Planner.
        self.planner.create_task("New", False, "d", "2026-04-12", "incomplete", 2, "School")
        self.assertEqual(len(self.planner.get_tasks()), 2)

    def test_set_task_status(self):
        # This checks that a task’s status changes when toggled.
        self.planner.set_task_status(0)
        self.assertEqual(self.planner.get_tasks()[0].get_status(), "started")

    def test_set_todays_focus(self):
        # This checks that toggling today's focus updates the task.
        self.planner.set_task_todays_focus(0)
        self.assertFalse(self.planner.get_tasks()[0].get_todays_focus())

    def test_delete_task(self):
        # This checks that removing a task actually deletes it from the list.
        self.planner.delete_task(0)
        self.assertEqual(len(self.planner.get_tasks()), 0)

    def test_add_task_step(self):
        # This checks that adding a step to a task updates its step list.
        self.planner.add_task_step(0, "step1")
        self.assertEqual(len(self.planner.get_tasks()[0].get_steps()), 1)

    def test_toggle_task_step(self):
        # This checks that a task step moves to the next status when toggled.
        self.planner.add_task_step(0, "step1")
        self.planner.toggle_task_step(0, 0)
        self.assertEqual(self.planner.get_tasks()[0].get_steps()[0]["status"], "started")

    def test_edit_task_step(self):
        # This checks that editing a step updates its text.
        self.planner.add_task_step(0, "step1")
        self.planner.edit_task_step(0, 0, "new step")
        self.assertEqual(self.planner.get_tasks()[0].get_steps()[0]["step"], "new step")

    def test_remove_task_step(self):
        # This checks that removing a step actually deletes it.
        self.planner.add_task_step(0, "step1")
        self.planner.remove_task_step(0, 0)
        self.assertEqual(len(self.planner.get_tasks()[0].get_steps()), 0)

    def test_edit_task(self):
        # This checks that updating a task changes its stored values.
        self.planner.edit_task(0, "New", False, "desc2", "2026-04-12", "completed", 1)
        t = self.planner.get_tasks()[0]
        self.assertEqual(t.get_task_name(), "New")
        self.assertEqual(t.get_status(), "completed")

    def test_get_task_by_index(self):
        # This checks that retrieving a task by index returns the correct one.
        self.assertEqual(self.planner.get_task_by_index(0), self.task)

    def test_get_overdue_tasks(self):
        # This checks that overdue tasks are correctly identified.
        overdue = self.planner.get_overdue_tasks(date(2026, 4, 11))
        self.assertEqual(len(overdue), 1)

    def test_get_due_soon(self):
        # This checks that tasks due within the next week are returned.
        due = self.planner.get_due_soon(date(2026, 4, 5))
        self.assertEqual(len(due), 1)

    def test_get_tasks_in_todays_focus(self):
        # This checks that only tasks marked for today are returned.
        focus = self.planner.get_tasks_in_todays_focus()
        self.assertEqual(len(focus), 1)

    def test_get_task_status_counts(self):
        # This checks that the number of tasks in each status is counted correctly.
        counts = self.planner.get_task_status_counts()
        self.assertEqual(counts["incomplete"], 1)

    def test_get_incomplete_by_category(self):
        # This checks that incomplete tasks are grouped and counted by category.
        result = self.planner.get_incomplete_by_category()
        self.assertEqual(result["total"], 1)

    def test_get_category_by_index(self):
        # This checks that retrieving a category by index returns the correct one.
        self.assertEqual(self.planner.get_category_by_index(0), self.cat)

    def test_add_category(self):
        # This checks that adding a category increases the list size.
        self.planner.add_category("New", "d")
        self.assertEqual(len(self.planner.get_categories()), 2)

    def test_edit_category(self):
        # This checks that editing a category updates its values.
        self.planner.edit_category(0, "New", "d")
        self.assertEqual(self.planner.get_categories()[0].get_category_name(), "New")

    def test_remove_category_by_index(self):
        # This checks that removing a category deletes it from the list.
        self.planner.remove_category_by_index(0)
        self.assertEqual(len(self.planner.get_categories()), 0)

    def test_get_event_by_index(self):
        # This checks that retrieving an event by index returns the correct one.
        self.assertEqual(self.planner.get_event_by_index(0), self.event)

    def test_add_event(self):
        # This checks that adding an event increases the list size.
        self.planner.add_event("E", "d", date(2026, 4, 11), "", "", "School")
        self.assertEqual(len(self.planner.get_events()), 2)

    def test_remove_event_by_index(self):
        # This checks that removing an event deletes it from the list.
        self.planner.remove_event_by_index(0)
        self.assertEqual(len(self.planner.get_events()), 0)

    def test_set_event_category(self):
        # This checks that changing an event’s category updates it correctly.
        self.planner.set_event_category(0, "New")
        self.assertEqual(self.planner.get_events()[0].get_category_name(), "New")

    def test_get_upcoming_events(self):
        # This checks that events within the next week are returned.
        events = self.planner.get_upcoming_events(date(2026, 4, 5))
        self.assertEqual(len(events), 1)

    def test_get_todays_events(self):
        # This checks that events happening today are returned.
        events = self.planner.get_todays_events(date(2026, 4, 10))
        self.assertEqual(len(events), 1)


if __name__ == "__main__":
    unittest.main()