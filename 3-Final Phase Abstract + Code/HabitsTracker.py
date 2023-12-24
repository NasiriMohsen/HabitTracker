import json
import os
import datetime
from prettytable import PrettyTable
from time import sleep

def time_now():
    # Get current time
    return datetime.datetime.now() + datetime.timedelta(days=8)

class Tracker():
    def __init__(self,path = './Data.json'):
        #load the JSON file
        self.data_file_path = path
        self.load_data()
    
    def add_habit(self, title, goal, time_frame, frequency):
        """Add a new habit to the data file.
        Args:
            title (str): Title of habit.
            goal (str): Description of habit.
            time_frame (int): Time limit of habit.
            frequency (int): number defined for task completion.
        """
        if title in self.data["Habits"]:
            print("\033[1m\033[91m Habit already exists! \033[0m")
        else:
            self.data["Habits"][title] = {
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
            self.save_data()
            print("\033[1m\033[92m Habit added! \033[0m")

    def remove_habit(self,title):
        """Remove a habit from data file.
        Args:
            title (str): Title of habit to be removed.
        """
        if title in self.data["Habits"]:
            del self.data["Habits"][title]
            self.save_data()
            print("\033[1m\033[92m Habit removed! \033[0m")
        else:
            print("\033[1m\033[91m Habit not found! \033[0m")
    
    def check_off_habit(self,title):
        """Mark a task of a specific habit
        Args:
            title (str): Title of the habit to mark.
        """
        if title in self.data["Habits"]:
            # Update habit status and streak
            if self.data["Habits"][title]["Complete"]:
                print("\033[1m\033[91m Habit already completed! \033[0m")
            self.data["Habits"][title]["Counter"] += 1
            self.update_habit_status()
            sleep(0.1)
            self.data["Habits"][title]["Counter_History"].append(str(time_now())) 
            self.update_habit_status()
            
        else:
            print("\033[1m\033[91m Habit not found! \033[0m")

    def update_habit_status(self):
        """Proccess the loaded data and updates the file 
        """
        for habit in self.data["Habits"]:
            habit_data = self.data["Habits"][habit]

            if habit_data["Streak_cycle"] == [] and habit_data["Counter"] == 1 and habit_data["Start_Time"] == []:
                habit_data["Start_Time"].append(str(time_now()))
                habit_data["Timer"] = str(time_now())
                print("\033[1m\033[92m You have started a habit! \033[0m")

            if habit_data["Counter"] == habit_data["Frequency"] and habit_data["Complete"] == False:
                habit_data["Streak_cycle"].append(str(time_now()))
                habit_data["Complete"] = True
                habit_data["Previous_Timer"] = habit_data["Timer"] 
                habit_data["Timer"] = str(datetime.datetime.strptime(habit_data["Timer"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=habit_data["Time_Frame"]))
                print("\033[1m\033[92m Habit completed! \033[0m")

            if habit_data["Counter_History"] != [] and habit_data["Start_Time"] != [] and habit_data["Streak_cycle"] != []:
                Streak = (datetime.datetime.strptime(habit_data["Counter_History"][-1], "%Y-%m-%d %H:%M:%S.%f") - datetime.datetime.strptime(habit_data["Start_Time"][-1], "%Y-%m-%d %H:%M:%S.%f")).total_seconds()
                if habit_data["BestStreak"] <= Streak:
                    habit_data["BestStreak"] = Streak

            if habit_data["Timer"] != "":
                time_difference = (datetime.datetime.strptime(habit_data["Timer"], "%Y-%m-%d %H:%M:%S.%f").replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=habit_data["Time_Frame"]) - time_now()).total_seconds()
                if time_difference <= 0:
                    habit_data["Streak_cycle"] = []
                    habit_data["Start_Time"] = []
                    habit_data["Complete"] = False
                    habit_data["Counter"] = 0
                    habit_data["Timer"] = ""
                    habit_data["Previous_Timer"] = ""
                    print("\033[1m\033[91m You abandoned a habit! \033[0m")
            
            if habit_data["Previous_Timer"] != "":
                previous_time_difference = (datetime.datetime.strptime(habit_data["Previous_Timer"], "%Y-%m-%d %H:%M:%S.%f").replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=habit_data["Time_Frame"]) - time_now()).total_seconds()
                if previous_time_difference <= 0:
                    habit_data["Counter"] = 0
                    habit_data["Complete"] = False
                    habit_data["Previous_Timer"] = ""
        self.save_data()
        
    def save_data(self):
        """Save data to Json file 
        """
        # Save data to the JSON file
        with open(self.data_file_path, 'w') as file:
            json.dump(self.data, file, indent=2)

    def load_data(self):
        """Load data from Json file if not available creates it  
        """
        # Check if the JSON file exists if so laod it if not create it
        if os.path.exists(self.data_file_path):
            with open(self.data_file_path, 'r') as file:
                self.data = json.load(file)
            self.update_habit_status()
        # If the data file doesn't exist, create a default
        else:
            self.initialize_default_data()

    def initialize_default_data(self):
        """Add 5 predefined habits 
        """
        self.data = {"Habits": {}}
        self.add_habit("Sleep", "Sleep on time", 1, 1)
        self.add_habit("Workout", "Workout 1 hour", 1, 1)
        self.add_habit("Cigarettes", "No Smoking", 1, 1)
        self.add_habit("Alcohol", "No Alcohol", 7, 5)
        self.add_habit("Journal", "Journal your week", 7, 3)
        self.save_data()
# Functions after this line are regarding visualisation(table) and the analizing functions
    def table_reset(self):
        """Reset the visual table  
        """
        table = PrettyTable()
        table.clear_rows()
        table.horizontal_char = "\033[1m═\033[0m"
        table.vertical_char = "\033[1m║\033[0m"
        table.junction_char = "\033[1m╬\033[0m"
        table.top_junction_char = "\033[1m╦\033[0m"
        table.bottom_junction_char = "\033[1m╩\033[0m"
        table.left_junction_char = "\033[1m╠\033[0m"
        table.right_junction_char = "\033[1m╣\033[0m"
        table.top_left_junction_char = "\033[1m╔\033[0m"
        table.top_right_junction_char = "\033[1m╗\033[0m"
        table.bottom_left_junction_char = "\033[1m╚\033[0m"
        table.bottom_right_junction_char = "\033[1m╝\033[0m"
        return table
    
    def habits_table(self):
        """Display a table of habits with useful information 
        """
        table = self.table_reset()
        table.field_names = [
            "\033[1m\033[93m Title of Habit \033[0m",
            "\033[1m\033[93m Periodicity \033[0m",
            "\033[1m\033[93m Task Frequency \033[0m",
            "\033[1m\033[93m Description of your goal \033[0m",
            "\033[1m\033[93m Status \033[0m",
            "\033[1m\033[93m Remaining Time \033[0m",
            "\033[1m\033[93m Current Streak \033[0m",
            "\033[1m\033[93m Best Streak \033[0m",
            "\033[1m\033[93m Started \033[0m",
            "\033[1m\033[93m Created \033[0m",
        ]

        for habit, details in self.data["Habits"].items():
            frequency_col = "\033[96m " + str(details['Frequency']) + " \033[0m"

            if details['Time_Frame'] == 1:
                periodicity_col = "\033[96m Daily \033[0m"
            else:
                periodicity_col = "\033[96m Weekly \033[0m"

            status_col = f"\033[92m {details['Counter']}/{details['Frequency']} \033[0m" if details['Counter'] >= details['Frequency'] else f"\033[91m {details['Counter']}/{details['Frequency']} \033[0m"

            if details["Timer"] != "" and details["Complete"] == False:
                time_difference = str((datetime.datetime.strptime(details["Timer"], "%Y-%m-%d %H:%M:%S.%f").replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=details["Time_Frame"]) - time_now())).split(",")[0]
                remaining_time_col = f'\033[92m {time_difference} \033[0m'
            elif details["Timer"] != "" and details["Complete"] == True:
                remaining_time_col = f'\033[92m Completed \033[0m'
            else:
                remaining_time_col = "\033[90m - \033[0m"

            if details["Counter_History"] != [] and details["Start_Time"] != [] and details["Streak_cycle"] != []:
                Streak = str(datetime.datetime.strptime(details["Counter_History"][-1], "%Y-%m-%d %H:%M:%S.%f") - datetime.datetime.strptime(details["Start_Time"][-1], "%Y-%m-%d %H:%M:%S.%f")).split(",")[0]
                if 'day' not in Streak:
                    current_streak_col = f'\033[95m 0 days \033[0m'
                else:
                    current_streak_col = f'\033[95m {Streak} \033[0m'
            else:
                current_streak_col = "\033[90m - \033[0m"
            
            if details["BestStreak"] == 0:
                best_streak_col = "\033[90m - \033[0m"
            else:
                best_streak = str(datetime.timedelta(seconds=details["BestStreak"])).split(",")[0]
                if 'day' not in best_streak:
                    best_streak_col = f'\033[95m 0 days \033[0m'
                else:
                    best_streak_col = f'\033[95m {best_streak} \033[0m'

            if details['Start_Time'] == []:
                start_time_col = f"\033[94m Not yet \033[0m"
            else:
                start_time_col = f"\033[94m {datetime.datetime.strptime(details['Start_Time'][-1], '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d')} \033[0m"

            table.add_row([
                f"\033[96m {habit} \033[0m",
                periodicity_col,
                frequency_col,
                f"\033[95m {details['Goal']} \033[0m",
                status_col,
                remaining_time_col,
                current_streak_col,
                best_streak_col,
                start_time_col,
                f"\033[94m {datetime.datetime.strptime(details['Created'], '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d')} \033[0m",
            ])
        print(table)
# The analizing functions
    def all_habits_list(self,show_table=False):
        """Return a list of all the habits available.
        Args:
            show_table (bool): if enabled displays a table.
        Returns:
            list: contains strings of habit names.
        """
        habits_list = [habit for habit in self.data["Habits"]]
        if show_table == True:
            names_list = ["\033[1m Habits: \033[0m"]
            status_list = ["\033[1m Status: \033[0m"]
            for habit,details in self.data["Habits"].items():       
                names_list.append("\033[93m " + habit + " \033[0m")
                if len(details["Streak_cycle"]) == 0:
                    status_list.append("\033[91m Not Active \033[0m")
                elif len(details["Streak_cycle"]) != 0:
                    status_list.append("\033[92m Active \033[0m")
            table = self.table_reset()
            table.field_names = names_list
            table.add_row(status_list)
            print(table)
        return habits_list
    
    def all_daily_habits_list(self,show_table=False):
        """Generate a list of all the daily habits available.
        Args:
            show_table (bool): if enabled displays a table.
        Returns:
            list: contains strings of habit names.
        """
        habits_list = [habit for habit, details in self.data["Habits"].items() if details["Time_Frame"] == 1]
        if show_table == True:
            names_list = ["\033[1m Habits: \033[0m"]
            status_list = ["\033[1m Status: \033[0m"]
            for habit,details in self.data["Habits"].items():
                if details["Time_Frame"] == 1:    
                    names_list.append("\033[93m " + habit + " \033[0m")
                    if len(details["Streak_cycle"]) == 0:
                        status_list.append("\033[91m Not Active \033[0m")
                    elif len(details["Streak_cycle"]) != 0:
                        status_list.append("\033[92m Active \033[0m")
            table = self.table_reset()
            table.field_names = names_list
            table.add_row(status_list)
            print(table)
        return habits_list

    def all_weekly_habits_list(self,show_table=False):
        """Generate a list of all the weekly habits available.
        Args:
            show_table (bool): if enabled displays a table.
        Returns:
            list: contains strings of habit names.
        """
        habits_list = [habit for habit, details in self.data["Habits"].items() if details["Time_Frame"] == 7]
        if show_table == True:
            names_list = ["\033[1m Habits: \033[0m"]
            status_list = ["\033[1m Status: \033[0m"]
            for habit,details in self.data["Habits"].items():
                if details["Time_Frame"] == 7:     
                    names_list.append("\033[93m " + habit + " \033[0m")
                    if len(details["Streak_cycle"]) == 0:
                        status_list.append("\033[91m Not Active \033[0m")
                    elif len(details["Streak_cycle"]) != 0:
                        status_list.append("\033[92m Active \033[0m")
            table = self.table_reset()
            table.field_names = names_list
            table.add_row(status_list)
            print(table)
        return habits_list

    def longest_streak_of_all_habits(self,show_table=False):
        """Return the longest run streak of all defined habits.
        Args:
            show_table (bool): if enabled displays a table.
        Returns:
            str: name of a habit.
        """
        habit_streak_list = []
        for habit,details in self.data["Habits"].items():
            if details["Counter_History"] != [] and details["Start_Time"] != [] and details["Streak_cycle"] != []:
                Streak = (datetime.datetime.strptime(details["Counter_History"][-1], "%Y-%m-%d %H:%M:%S.%f") - datetime.datetime.strptime(details["Start_Time"][-1], "%Y-%m-%d %H:%M:%S.%f")).total_seconds()
                habit_streak_list.append((habit,Streak))
        if habit_streak_list != []:
            max_streak = max(habit_streak_list, key=lambda x: x[1])
            if show_table == True:
                table = self.table_reset()
                table.field_names = ["\033[1m Longest on going habit: \033[0m",f"\033[1m\033[93m {max_streak[0]} \033[0m"]
                table.add_row(["\033[1m Current streak: \033[0m",f"\033[1m\033[93m {str(datetime.timedelta(seconds=max_streak[1]))} \033[0m"])
                print(table)
            return max_streak[0]
        else:
            print("\033[1m\033[91m No habits active! \033[0m")
            return "Unavailable"

    def longest_streak_of_habit(self, habit_title,show_table=False):
        """Return the longest run streak for a given habit.
        Args:
            show_table (bool): if enabled displays a table.
        Returns:
            str: longest streak in date and time.
        """
        if habit_title in self.data["Habits"]:
            max_streak = str(datetime.timedelta(seconds=self.data["Habits"][habit_title]["BestStreak"]))
            if show_table == True:
                table = self.table_reset()
                table.field_names = ["\033[1m Habit: \033[0m",f"\033[1m\033[93m {habit_title} \033[0m"]
                table.add_row(["\033[1m Best Streak: \033[0m",f"\033[1m\033[93m {max_streak} \033[0m"])
                print(table)    
            return max_streak
        else:
            print("\033[1m\033[91m Habit not found! \033[0m")
            return "Unavailable"

if __name__ == "__main__":
    habits = Tracker()
    habits.habits_table()