import json
import os
import datetime
from prettytable import PrettyTable

class Tracker():
    def __init__(self):
        self.TodaysDate = datetime.datetime.now()

        if os.path.exists('./Data.json'):
            with open('./Data.json', 'r') as file:
                self.Data = json.load(file)

            for habit in self.Data["Habits"]:
                if self.TodaysDate >= (datetime.datetime.strptime(self.Data["Habits"][habit]["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=self.Data["Habits"][habit]["Time_Frame"])):
                    if self.Data["Habits"][habit]["Status"] == 0 and self.Data["Habits"][habit]["Streak"] != 0:
                        print(f'\033[1m\033[91m You have lost your {habit} { self.Data["Habits"][habit]["Streak"] } Day Streak! \033[0m')
                        self.Data["Habits"][habit]["Streak"] = 0
                    self.Data["Habits"][habit]["Status"] = 0
                    self.Data["Habits"][habit]["Time"] = str(self.TodaysDate)
                    self.Save_Data(self.Data)

        else:
            self.Data = {"Habits": {
                "Sleep": {"Goal": "Sleep on time", "Time_Frame": 1, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Workout": {"Goal": "Workout 1hour", "Time_Frame": 1, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Cigarettes": {"Goal": "No Smoking", "Time_Frame": 30, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Alcohol": {"Goal": "No Alcohal", "Time_Frame": 30, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)},
                "Journal": {"Goal": "Journal your week", "Time_Frame": 7, "Streak": 0, "Status": 0,"BestStreak": 0,"Time": str(self.TodaysDate)}
                }
            }
            self.Save_Data(self.Data)

    def Save_Data(self,Data):
        with open('./Data.json', 'w') as file:
            json.dump(Data, file, indent=2)
     
    def AddHabit(self,Title,Goal,TimeFrame,Streak,Status,BestStreak):
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
        if Title in self.Data["Habits"]:
            del self.Data["Habits"][Title]
            self.Save_Data(self.Data)
            print("\033[1m\033[92m Habit Removed! \033[0m")
        else:
            print("\033[1m\033[91m Habit Not Found! \033[0m")
        
    def TableofHabits(self):   
        self.Table = PrettyTable() 
        self.Table.clear_rows()
        self.Table.field_names = ["\033[1m\033[96m Habit's Title \033[0m", "\033[1m\033[94m Your Aim and Goal \033[0m", "\033[1m\033[95m Time Frame \033[0m", "\033[1m\033[95m Time Frame(In days) \033[0m", "\033[1m\033[91m Status \033[0m", "\033[1m\033[92m Remaining Time \033[0m", "\033[1m\033[93m Current Streak \033[0m","\033[1m\033[93m Best Streak \033[0m"]
        for habit, details in self.Data["Habits"].items():        
            if details['Status'] == 0:
                Col5 = "\033[91mIncomplete\033[0m"
            else:
                Col5 = "\033[92mComplete\033[0m"
            if details['Streak'] == 0 and details['Status'] == 0:
                Col6 = f'\033[90m {str((datetime.datetime.strptime(details["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=details["Time_Frame"])) - self.TodaysDate).split(".")[0]} \033[0m'
            elif details['Streak'] != 0 and details['Status'] == 0:
                Col6 = f'\033[1m {str((datetime.datetime.strptime(details["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=details["Time_Frame"])) - self.TodaysDate).split(".")[0]} \033[0m'
            else:
                Col6 = f'\033[92m {str((datetime.datetime.strptime(details["Time"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=details["Time_Frame"])) - self.TodaysDate).split(".")[0]} \033[0m'
            if  details['Time_Frame'] > 1:
                Col4 = f"\033[95m{details['Time_Frame']} days\033[0m"
            else: 
                Col4 = f"\033[95m{details['Time_Frame']} day\033[0m"
            self.Table.add_row([f"\033[96m{habit}\033[0m", f"\033[94m{details['Goal']}\033[0m", f"\033[95m{self.DaysToWeeks(details['Time_Frame'])}\033[0m", Col4, Col5,Col6, f"\033[93m{details['Streak']}\033[0m",f"\033[93m{details['BestStreak']}\033[0m"])
        return self.Table
    
    def ListofHabits(self):    
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
        if Title in self.Data["Habits"]:
            if self.Data["Habits"][Title]["Status"] != 1: 
                self.Data["Habits"][Title]["Status"] = 1
                self.Data["Habits"][Title]["Streak"] = self.Data["Habits"][Title]["Streak"] + 1 
                self.Data["Habits"][Title]["Time"] = str(self.TodaysDate)
                print("\033[1m\033[92m Status Updated! \033[0m")
            else: 
                print("\033[1m\033[92m Status already Updated! \033[0m")
            if self.Data["Habits"][Title]["Streak"] > self.Data["Habits"][Title]["BestStreak"]:
                self.Data["Habits"][Title]["BestStreak"] = self.Data["Habits"][Title]["Streak"]
            self.Save_Data(self.Data)
        else:
            print("\033[1m\033[91m Habit not found! \033[0m")

    def DaysToWeeks(self,Input):
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