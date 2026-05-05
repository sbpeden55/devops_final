import unittest
from category import Category

class Test_Category(unittest.TestCase):

    def setUp(self):
        # This creates a sample Category that all tests will use.
        # It keeps the tests consistent and avoids repeating setup code.
        self.category = Category(
            "DoDate Testing",
            "tasks pertaining to the test suite for the DoDate semester project"
        )

    def test_init(self):
        # This checks that the Category stores its name and description correctly
        # when it is first created.
        self.assertEqual(self.category.category_name, "DoDate Testing")
        self.assertEqual(self.category.description, "tasks pertaining to the test suite for the DoDate semester project")

    def test_getters(self):
        # This checks that the getter methods return the correct values
        # that were stored in the Category.
        self.assertEqual(self.category.get_category_name(), "DoDate Testing")
        self.assertEqual(self.category.get_description(), "tasks pertaining to the test suite for the DoDate semester project")

    def test_setters(self):
        # This changes the Category values using setter methods
        # and verifies that the updates were applied correctly.
        self.category.set_category_name("DoDate Test Suite")
        self.category.set_description("tasks for DoDate project test suite")

        self.assertEqual(self.category.category_name, "DoDate Test Suite")
        self.assertEqual(self.category.description, "tasks for DoDate project test suite")

    def test_to_dict(self):
        # This checks that converting the Category to a dictionary
        # keeps the same name and description values.
        test_dict = {
            "category_name": "DoDate Testing",
            "description": "tasks pertaining to the test suite for the DoDate semester project"
        }
        self.assertEqual(self.category.to_dict(), test_dict)

    def test_from_dict(self):
        # This builds a Category from a dictionary and checks that
        # the values were set correctly in the new object.
        data = {
            "category_name": "DoDate Testing",
            "description": "tasks pertaining to the test suite for the DoDate semester project"
        }

        test_category = Category.from_dict(data)

        self.assertEqual(test_category.category_name, "DoDate Testing")
        self.assertEqual(test_category.description, "tasks pertaining to the test suite for the DoDate semester project")


if __name__ == "__main__":
    unittest.main()