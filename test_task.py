import unittest
from task import Task
from datetime import date

class Test_Task(unittest.TestCase):

    def setUp(self):
        # This creates one example Task that all tests will use.
        # It saves time and keeps the tests consistent.
        self.date = "2026-04-10"
        self.task = Task(
            "Finish Iteration 2 Test Suite", 
            True, 
            "Write the test suite used to test the backend of the DoDate project", 
            self.date,
            "incomplete",
            4, 
            [
                {"step": "write the suites", "status": "completed"},
                {"step": "run tests", "status": "incomplete"}
            ],
            "DoDate Project"
        )

    def test_init(self):
        # This test checks that all values given when creating the Task
        # are stored correctly inside the object.
        self.assertEqual(self.task.task_name, "Finish Iteration 2 Test Suite")
        self.assertTrue(self.task.todays_focus)
        self.assertEqual(self.task.description, "Write the test suite used to test the backend of the DoDate project")
        self.assertEqual(self.task.due_date, self.date)
        self.assertEqual(self.task.status, "incomplete")
        self.assertEqual(self.task.weight, 4)
        self.assertIn({"step": "run tests", "status": "incomplete"}, self.task.steps)
        self.assertEqual(self.task.category_name, "DoDate Project")

    def test_getters(self):
        # This test checks that each getter method correctly returns
        # the value stored in the Task.
        self.assertEqual(self.task.get_task_name(), "Finish Iteration 2 Test Suite")
        self.assertTrue(self.task.get_todays_focus())
        self.assertEqual(self.task.get_description(), "Write the test suite used to test the backend of the DoDate project")
        self.assertEqual(self.task.get_due_date(), self.date)
        self.assertEqual(self.task.get_status(), "incomplete")
        self.assertEqual(self.task.get_weight(), 4)
        self.assertIn({"step": "run tests", "status": "incomplete"}, self.task.get_steps())
        self.assertEqual(self.task.get_category_name(), "DoDate Project")

    def test_setters(self):
        # This test checks that changing values using setter methods
        # actually updates the Task.
        self.task.set_todays_focus()
        self.assertFalse(self.task.todays_focus)

        self.task.set_category_name("New Category")
        self.assertEqual(self.task.category_name, "New Category")

    def test_to_dict(self):
        # This test checks that converting the Task into a dictionary
        # keeps all of its data the same.
        test_dict = {
            "task_name": "Finish Iteration 2 Test Suite", 
            "todays_focus": True, 
            "description": "Write the test suite used to test the backend of the DoDate project", 
            "due_date": self.date,
            "status": "incomplete",
            "weight": 4, 
            "steps": [
                {"step": "write the suites", "status": "completed"},
                {"step": "run tests", "status": "incomplete"}
            ],
            "category_name": "DoDate Project"
        }
        self.assertEqual(self.task.to_dict(), test_dict)

    def test_from_dict(self):
        # This test builds a Task from a dictionary and checks that
        # all the values were set correctly.
        data = {
            "task_name": "Finish Iteration 2 Test Suite", 
            "todays_focus": True, 
            "description": "Write the test suite used to test the backend of the DoDate project", 
            "due_date": self.date,
            "status": "incomplete",
            "weight": 4, 
            "steps": [
                {"step": "write the suites", "status": "completed"},
                {"step": "run tests", "status": "incomplete"}
            ],
            "category_name": "DoDate Project"
        }

        obj = Task.from_dict(data)

        self.assertEqual(obj.get_task_name(), "Finish Iteration 2 Test Suite")
        self.assertEqual(obj.get_due_date(), self.date)

    def test_update_task(self):
        # This test checks that updating multiple fields at once
        # changes only the values that were provided.
        self.task.update_task(
            task_name="New Name",
            todays_focus=False,
            description="Description",
            status="completed",
            weight=1,
            category_name="Category"
        )

        self.assertEqual(self.task.task_name, "New Name")
        self.assertFalse(self.task.todays_focus)
        self.assertEqual(self.task.description, "Description")
        self.assertEqual(self.task.due_date, self.date)  # unchanged
        self.assertEqual(self.task.status, "completed")
        self.assertEqual(self.task.weight, 1)
        self.assertEqual(self.task.category_name, "Category")

    def test_is_overdue(self):
        # This test checks whether the Task correctly identifies
        # when it is past its due date.
        result = self.task.is_overdue(date(2026, 4, 11))
        self.assertTrue(result)

        self.task.status = "completed"
        result = self.task.is_overdue(date(2026, 4, 11))
        self.assertFalse(result)

    def test_add_step(self):
        # This test checks that adding a new step actually places it
        # into the list of steps.
        self.task.add_step("new step")
        self.assertIn({"step": "new step", "status": "incomplete"}, self.task.steps)

    def test_toggle_step(self):
        # This test checks that a step moves through its status cycle
        # when toggled.
        self.task.toggle_step(1)
        self.assertEqual(self.task.steps[1]["status"], "started")

        self.task.toggle_step(1)
        self.assertEqual(self.task.steps[1]["status"], "completed")

    def test_edit_step(self):
        # This test checks that a step's text can be changed.
        self.task.edit_step(1, "updated step")
        self.assertEqual(self.task.steps[1]["step"], "updated step")

    def test_remove_step(self):
        # This test checks that removing a step actually deletes it
        # from the list.
        self.task.remove_step(1)
        self.assertEqual(len(self.task.steps), 1)


if __name__ == "__main__":
    unittest.main()