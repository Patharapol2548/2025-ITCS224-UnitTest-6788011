import unittest

# Define the functions that we want to test
def is_child(age):
    return 0 <= age <= 9

def is_adult(age):
    return 18 <= age <= 59

def is_golden(age):
    return age >= 60

# Create the test cases
class TestAgeCategories(unittest.TestCase):
    
    def test_child_age(self):
        # Loop through valid child ages (0 to 9)
        for age in range(10): 
            with self.subTest(age=age):
                self.assertTrue(is_child(age))
                print(f"{age} is considered as a child.")

    def test_adult_age(self):
        # Loop through valid adult ages (18 to 59)
        for age in range(18, 60):
            with self.subTest(age=age):
                self.assertTrue(is_adult(age))
                print(f"{age} is considered as an adult.")

    def test_golden_age(self):
        # Loop through valid golden ages (60 to 100)
        for age in range(60, 101):
            with self.subTest(age=age):
                self.assertTrue(is_golden(age))
                print(f"{age} is considered as golden.")

if __name__ == "__main__":
    unittest.main(verbosity=2)