import unittest
import os
import json
from data_manager import Data_Manager
from planner import Planner

class Test_Data_Manager(unittest.TestCase):

    def setUp(self):
        # This creates a temporary file with simple planner data.
        # The file acts like saved data that the program would normally read.
        self.test_file = "temp_planner.json"

        self.sample_data = {
            "name": "Test",
            "categories": [],
            "tasks": [],
            "events": []
        }

        with open(self.test_file, "w") as f:
            json.dump(self.sample_data, f)

        self.dm = Data_Manager(self.test_file)

    def tearDown(self):
        # This removes the temporary file after each test so it does not affect other tests.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_init(self):
        # This checks that the Data_Manager stores the file path correctly.
        self.assertEqual(self.dm.file_path, self.test_file)

    def test_open_planner(self):
        # This checks that reading from the file creates a Planner object
        # with the same data that was saved.
        planner = self.dm.open_planner()

        self.assertIsInstance(planner, Planner)
        self.assertEqual(planner.to_dict(), self.sample_data)

    def test_save_planner(self):
        # This checks that saving a Planner writes the correct data to the file.
        planner = Planner.from_dict(self.sample_data)

        self.dm.save_planner(planner)

        with open(self.test_file, "r") as f:
            data = json.load(f)

        self.assertEqual(data, self.sample_data)


if __name__ == "__main__":
    unittest.main()