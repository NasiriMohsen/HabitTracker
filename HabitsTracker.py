import json
import os
import datetime
from prettytable import PrettyTable

class Tracker():
    def __init__(self):
        # Get the current date and time
        self.TodaysDate = datetime.datetime.now()

        # Check if the data file exists and laod it
        if os.path.exists('./Data.json'):
            with open('./Data.json', 'r') as file:
                self.Data = json.load(file)
            
            # Check habits and update their status based on time frame
            for habit in self.Data["Habits"]:
                if self.TodaysDate >= (datetime.datetime.strptime(self.Data["Habits"][habit]["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=self.Data["Habits"][habit]["Time_Frame"])):
                    if self.Data["Habits"][habit]["Status"] == 0 and self.Data["Habits"][habit]["Streak"] != 0:
                        print(f'\033[1m\033[91m You have lost your {habit} { self.Data["Habits"][habit]["Streak"] } Day Streak! \033[0m')
                        self.Data["Habits"][habit]["Streak"] = 0
                    # Update habit status and time
                    self.Data["Habits"][habit]["Status"] = 0
                    self.Data["Habits"][habit]["Time"] = str(self.TodaysDate)
                    self.Save_Data(self.Data)

        # If the data file doesn't exist, create a default
        else:
            self.Data = {"Habits": {
                "Sleep": {"Goal": "Sleep on time", "Time_Frame": 1, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Workout": {"Goal": "Workout 1hour", "Time_Frame": 2, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Cigarettes": {"Goal": "No Smoking", "Time_Frame": 21, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Alcohol": {"Goal": "No Alcohal", "Time_Frame": 31, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Journal": {"Goal": "Journal your week", "Time_Frame": 7, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)}
                }
            }
            self.Save_Data(self.Data)

    def Save_Data(self,Data):
        # Save data to the JSON file
        with open('./Data.json', 'w') as file:
            json.dump(Data, file, indent=2)
     
    def AddHabit(self,Title,Goal,TimeFrame,Streak,Status,BestStreak):
        # Add a new habit to the data
        self.Data["Habits"][Title] = {
            "Goal": Goal,
            "Time_Frame": TimeFrame,
            "Streak": Streak,
            "Status": Status,
            "BestStreak": BestStreak,
            "Time": str(self.TodaysDate)
        }
        self.Save_Data(self.Data)
        print("\033[1m\033[92m Habit Added! \033[0m")

    def RemoveHabit(self,Title):
        # Remove a habit from the data
        if Title in self.Data["Habits"]:
            del self.Data["Habits"][Title]
            self.Save_Data(self.Data)
            print("\033[1m\033[92m Habit Removed! \033[0m")
        else:
            print("\033[1m\033[91m Habit Not Found! \033[0m")
        
    def TableofHabits(self):
        # Generate a formatted table with habit information
        self.Table = PrettyTable() 
        self.Table.clear_rows()
        self.Table.field_names = ["\033[1m\033[96m Habit's Title \033[0m", "\033[1m\033[94m Your Aim and Goal \033[0m", "\033[1m\033[95m Time Frame \033[0m", "\033[1m\033[95m Time Frame in days \033[0m", "\033[1m\033[91m Status \033[0m", "\033[1m\033[92m Remaining Time \033[0m", "\033[1m\033[93m Current Streak(In days) \033[0m","\033[1m\033[93m Best Streak(In days) \033[0m"]
        for habit, details in self.Data["Habits"].items():        
            if details['Status'] == 0:
                Col5 = "\033[91m Incomplete \033[0m"
            else:
                Col5 = "\033[92m Complete \033[0m"
            if details['Streak'] == 0 and details['Status'] == 0:
                Col6 = f'\033[90m {str((datetime.datetime.strptime(details["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=details["Time_Frame"])) - self.TodaysDate).split(".")[0]} \033[0m'
            elif details['Streak'] != 0 and details['Status'] == 0:
                Col6 = f'\033[1m {str((datetime.datetime.strptime(details["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=details["Time_Frame"])) - self.TodaysDate).split(".")[0]} \033[0m'
            else:
                Col6 = f'\033[92m {str((datetime.datetime.strptime(details["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=details["Time_Frame"])) - self.TodaysDate).split(".")[0]} \033[0m'
            
            if details['Time_Frame'] > 1:
                Col4 = f"\033[95m {details['Time_Frame']} days \033[0m"
            else: 
                Col4 = f"\033[95m {details['Time_Frame']} day \033[0m"
            self.Table.add_row([f"\033[96m {habit} \033[0m", f"\033[94m {details['Goal']} \033[0m", f"\033[95m {self.DaysToWeeks(details['Time_Frame'])} \033[0m", Col4, Col5,Col6, f"\033[93m {details['Streak']}{self.strDay(details['Streak'] * details['Time_Frame'])} \033[0m",f"\033[93m {details['BestStreak']}{self.strDay(details['BestStreak'] * details['Time_Frame'])} \033[0m"])
        return self.Table
    
    def ListofHabits(self):
        # Generate a list of habit names
        self.Table = PrettyTable()
        self.Table.clear_rows()
        NamesList = []
        for habit in self.Data["Habits"]:        
            NamesList.append("\033[93m " + habit + " \033[0m")
        self.Table.field_names = NamesList
        self.Table.horizontal_char = " "
        self.Table.vertical_char = " "
        self.Table.junction_char = " "
        return self.Table
    
    def CheckHabit(self,Title):
        # Update habit status and streaks
        if Title in self.Data["Habits"]:
            # Update habit status and streak
            if self.Data["Habits"][Title]["Status"] != 1: 
                self.Data["Habits"][Title]["Status"] = 1
                self.Data["Habits"][Title]["Streak"] = self.Data["Habits"][Title]["Streak"] + 1 
                self.Data["Habits"][Title]["Time"] = str(self.TodaysDate)
                print("\033[1m\033[92m Status Updated! \033[0m")
            else: 
                print("\033[1m\033[92m Status already Updated! \033[0m")
            # Update best streak if applicable
            if self.Data["Habits"][Title]["Streak"] > self.Data["Habits"][Title]["BestStreak"]:
                self.Data["Habits"][Title]["BestStreak"] = self.Data["Habits"][Title]["Streak"]
            self.Save_Data(self.Data)
        else:
            print("\033[1m\033[91m Habit not found! \033[0m")

    def DaysToWeeks(self,Input):
        # Convert days to weeks for better readability
        Weeks = Input // 7
        Days = Input % 7
        Output = " "
        if Weeks != 0:
            Output = Output + str(Weeks) + " week"
            if Weeks > 1:
                Output = Output + "s"
        if Weeks != 0 and Days != 0:
            Output =  Output + " & "
        if Days != 0:
            Output =  Output + str(Days) + " day"
            if Days > 1:
                Output = Output + "s"
        Output = Output + " "
        return Output
    
    def strDay(self,x):
        # Convert integer value of days to a clean string
        if x > 1:
            x = " or (" + str(x) + " days)"
        elif x == 0:
            x = ""
        else:
            x = " or (" + str(x) + " day)"
        return x