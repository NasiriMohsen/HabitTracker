import unittest
from unittest.mock import patch
from HabitsTracker import Tracker, time_now
import os 

# 13 test methods out of 14 actual methods
# the remainig 1 is 'table_reset' and it was made to write less lines of code and it is being tested in 6 other methods  

class TestTracker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data_file = './test_data.json'
        cls.tracker = Tracker(cls.test_data_file)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_data_file):
            os.remove(cls.test_data_file)

    #def setUp(self):
    #    print("Running Test... ")

    def test_load_data(self):
        # Test the load_data method
        self.tracker.load_data()

        # Check if the data was loaded successfully
        self.assertIsNotNone(self.tracker.data)

    def test_save_data(self):
        # Test the save_data method
        title = "Save_Habit"
        goal = "Save test"
        time_frame = 7
        frequency = 3
        
        self.tracker.data["Habits"][title] = {
                "Goal": goal,
                "Time_Frame": time_frame,
                "Created": str(time_now()),
                "Frequency": frequency,
                "Counter":0,
                "Timer":"",
                "Previous_Timer":"",
                "Streak_cycle": [],
                "BestStreak": 0,
                "Counter_History": [],
                "Start_Time": [],
                "Complete": False
            }
        
        self.tracker.save_data()
        
        # Check if the habit was added successfully
        self.assertIn(title, self.tracker.data["Habits"])

    def test_add_habit(self):
        # Test the add_habit method
        habit_title = "New_Habit"
        goal = "Description of the new habit"
        time_frame = 7
        frequency = 3

        self.tracker.add_habit(habit_title, goal, time_frame, frequency)

        # Check if the habit was added successfully
        self.assertIn(habit_title, self.tracker.data["Habits"])
    
    def test_check_off_habit(self):
            # Test the check_off_habit method
            habit_title = "New_Habit"
            initial_counter = self.tracker.data["Habits"][habit_title]["Counter"]

            with patch('builtins.input', return_value='yes'):
                self.tracker.check_off_habit(habit_title)

            # Check if the counter increased after checking off the habit
            self.assertEqual(self.tracker.data["Habits"][habit_title]["Counter"], initial_counter + 1)

    def test_habits_table(self):
        # Test the habits_table method
        with patch('builtins.print') as mock_print:
            self.tracker.habits_table()

            # Check if the print function was called
            mock_print.assert_called()

    def test_all_habits_list(self):
        # Test the all_habits_list method
        habits_list = self.tracker.all_habits_list(show_table=False)

        # Check if the habits list is not empty
        self.assertGreater(len(habits_list), 0)

        # Test with table
        with patch('builtins.print') as mock_print:
            self.tracker.all_habits_list(show_table=True)
        
        # Check if the print function was called
        mock_print.assert_called()

    def test_all_daily_habits_list(self):
        # Test the all_daily_habits_list method
        daily_habits_list = self.tracker.all_daily_habits_list(show_table=False)

        # Check if the daily habits list is not empty
        self.assertGreater(len(daily_habits_list), 0)

        # Test with table
        with patch('builtins.print') as mock_print:
            self.tracker.all_daily_habits_list(show_table=True)
        
        # Check if the print function was called
        mock_print.assert_called()

    def test_all_weekly_habits_list(self):
        # Test the all_weekly_habits_list method
        weekly_habits_list = self.tracker.all_weekly_habits_list(show_table=False)

        # Check if the weekly habits list is not empty
        self.assertGreater(len(weekly_habits_list), 0)

        # Test with table
        with patch('builtins.print') as mock_print:
            self.tracker.all_weekly_habits_list(show_table=True)
        
        # Check if the print function was called
        mock_print.assert_called()

    def test_longest_streak_of_all_habits(self):
        # Test the longest_streak_of_all_habits method
        with patch('builtins.print') as mock_print:
            longest_streak_habit = self.tracker.longest_streak_of_all_habits(show_table=True)

            # Check if the print function was called
            mock_print.assert_called()

        # Check if the longest streak habit is not None
        self.assertIsNotNone(longest_streak_habit)

    def test_longest_streak_of_habit(self):
        # Test the longest_streak_of_habit method
        habit_title = "New_Habit"
        with patch('builtins.print') as mock_print:
            longest_streak = self.tracker.longest_streak_of_habit(habit_title, show_table=True)

            # Check if the print function was called
            mock_print.assert_called()

        # Check if the longest streak is not None
        self.assertIsNotNone(longest_streak)
    
    def test_remove_habit(self):
        # Test the remove_habit method
        habit_title = "New_Habit"
        self.tracker.remove_habit(habit_title)

        # Check if the habit was removed successfully
        self.assertNotIn(habit_title, self.tracker.data["Habits"])

    def test_update_habit_status(self):
        # Test the update_habit_status method

        # Add a new habit for testing
        habit_title = "TestHabit"
        goal = "Test Goal"
        time_frame = 7
        frequency = 1
        self.tracker.add_habit(habit_title, goal, time_frame, frequency)

        # Mock the time_now function
        with patch('HabitsTracker.time_now') as mock_time_now:
            # Set a fixed time for testing
            fixed_time = time_now()
            mock_time_now.return_value = fixed_time

            # Perform actions to update the habit status
            self.tracker.check_off_habit(habit_title)
            self.tracker.update_habit_status()

            # Get the habit data
            habit_data = self.tracker.data["Habits"][habit_title]

            # Check if the habit status is updated correctly
            self.assertEqual(habit_data["Counter"], 1)
            self.assertEqual(habit_data["Streak_cycle"], [str(fixed_time)])
            self.assertEqual(habit_data["Complete"], True)

            # Remove the test habit
            self.tracker.remove_habit("TestHabit")

    def test_initialize_default_data(self):
        # Test that initialize_default_data sets the correct default habits
        self.tracker.initialize_default_data()

        # Check if the default habits are present in the data attribute
        self.assertTrue("Sleep" in self.tracker.data["Habits"])
        self.assertTrue("Workout" in self.tracker.data["Habits"])
        # Add more checks for other default habits

if __name__ == "__main__":
    unittest.main()
