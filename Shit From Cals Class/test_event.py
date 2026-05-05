import unittest
from event import Event
from datetime import date, time

class Test_Event(unittest.TestCase):

    def setUp(self):
        # This creates one example Event that all tests will use.
        # Instead of rebuilding the same object every time, we reuse this one.
        self.date = date(2026, 4, 16)
        self.time = time(11, 59)
        self.event = Event(
            "Iteration 4 Due",
            "Iteration 4 of the DoDate project due at 11:59pm",
            self.date,
            self.time,
            self.time,
            "DoDate Project"
        )

    def test_init(self):
        # This test checks that when an Event is created,
        # all of its data is stored correctly inside the object.
        self.assertEqual(self.event.event_name, "Iteration 4 Due")
        self.assertEqual(self.event.description, "Iteration 4 of the DoDate project due at 11:59pm")
        self.assertEqual(self.event.date, self.date)
        self.assertEqual(self.event.start_time, self.time)
        self.assertEqual(self.event.end_time, self.time)
        self.assertEqual(self.event.category_name, "DoDate Project")

    def test_getters(self):
        # This test checks that each getter method returns the correct value.
        # In other words, it makes sure we can retrieve the data we stored.
        self.assertEqual(self.event.get_event_name(), "Iteration 4 Due")
        self.assertEqual(self.event.get_description(), "Iteration 4 of the DoDate project due at 11:59pm")
        self.assertEqual(self.event.get_date(), self.date)
        self.assertEqual(self.event.get_start_time(), self.time)
        self.assertEqual(self.event.get_end_time(), self.time)
        self.assertEqual(self.event.get_category_name(), "DoDate Project")

    def test_setters(self):
        # This test changes the values of the Event using setter methods,
        # then checks that those changes actually took effect.
        new_date = date(2026, 4, 20)
        new_time = time(9, 0)

        self.event.set_event_name("New Event")
        self.event.set_description("New Description")
        self.event.set_date(new_date)
        self.event.set_start_time(new_time)
        self.event.set_end_time(new_time)
        self.event.set_category_name("New Category")

        self.assertEqual(self.event.event_name, "New Event")
        self.assertEqual(self.event.description, "New Description")
        self.assertEqual(self.event.date, new_date)
        self.assertEqual(self.event.start_time, new_time)
        self.assertEqual(self.event.end_time, new_time)
        self.assertEqual(self.event.category_name, "New Category")

    def test_to_dict(self):
        # This test checks that converting the Event into a dictionary
        # keeps all of the information the same.
        test_dict = {
            "event_name": "Iteration 4 Due",
            "description": "Iteration 4 of the DoDate project due at 11:59pm",
            "date": self.date,
            "start_time": self.time,
            "end_time": self.time,
            "category_name": "DoDate Project"
        }
        self.assertEqual(self.event.to_dict(), test_dict)

    def test_from_dict(self):
        # This test starts with a dictionary and builds an Event from it.
        # It then checks that the new Event contains the same data.
        data = {
            "event_name": "Iteration 4 Due",
            "description": "Iteration 4 of the DoDate project due at 11:59pm",
            "date": self.date,
            "start_time": self.time,
            "end_time": self.time,
            "category_name": "DoDate Project"
        }

        test_event = Event.from_dict(data)

        self.assertEqual(test_event.event_name, "Iteration 4 Due")
        self.assertEqual(test_event.description, "Iteration 4 of the DoDate project due at 11:59pm")
        self.assertEqual(test_event.date, self.date)
        self.assertEqual(test_event.start_time, self.time)
        self.assertEqual(test_event.end_time, self.time)
        self.assertEqual(test_event.category_name, "DoDate Project")


if __name__ == "__main__":
    unittest.main()