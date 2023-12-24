from HabitsTracker import Tracker
import os

# Define color codes for console output
MainColor = "\033[93m"
SecondColor = "\033[97m"
ResetColor = "\033[0m"

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message
clear_screen()    
print(f"{MainColor} Hello, Welcome to the habit tracker! {SecondColor}(^_^) ")
input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
clear_screen()

# Create an instance of the Tracker class
habits = Tracker()

# User interaction loop
while True:
    # Display the habits table
    clear_screen()    
    habits.habits_table()
    print()
    print(f"{MainColor} You may use the commands bellow to navigate! {ResetColor}")
    print()
    # Display command options
    print(f"{MainColor} To see program instructions use: \033[1m{SecondColor}'H' {MainColor}or \033[1m{SecondColor}'h'{MainColor}! {ResetColor}")
    print(f"{MainColor} To show details and analize habits use: \033[1m{SecondColor}'S' {MainColor}or \033[1m{SecondColor}'s'{MainColor}! {ResetColor}")
    print(f"{MainColor} To mark a habit task use: \033[1m{SecondColor}'C' {MainColor}or \033[1m{SecondColor}'c'{MainColor}! {ResetColor}")
    print(f"{MainColor} To add a new habit use: \033[1m{SecondColor}'A' {MainColor}or \033[1m{SecondColor}'a'{MainColor}! {ResetColor}")
    print(f"{MainColor} To remove a habit use: \033[1m{SecondColor}'R' {MainColor}or \033[1m{SecondColor}'r'{MainColor}! {ResetColor}")
    print(f"{MainColor} To exit program use: \033[1m{SecondColor}'Q' {MainColor}or \033[1m{SecondColor}'q'{MainColor}! {ResetColor}")
    
    # Get user input
    user = input(f"{MainColor} You: {ResetColor}").lower()
    
    # Add a new habit
    if user == "a": 
        clear_screen()    
        print()
        title = input(f"{MainColor} Choose a 'Title' for this habit: {ResetColor}")
        print()
        goal = input(f"{MainColor} Define your 'Task' for example, goals and plans for this habit: {ResetColor}")
        print()
        print(f"{MainColor} Define the 'Time Frame' for this habit. Is it a 'Daily' \033[1m{SecondColor}'D'{MainColor}/\033[1m{SecondColor}'d'{MainColor} or 'Weekly'\033[1m{SecondColor}'W'{MainColor}/\033[1m{SecondColor}'w'{MainColor} habit")
        print(f"{MainColor} Depending on what you choose you have tiem to complete the habit's tasks{ResetColor}")
        print(f"{MainColor} If not completed during this period you will break the habit and your 'Streak'. {ResetColor}")
        aflag = True
        while aflag:
            timefr = input(f"{MainColor} Define Daily or Weekly: {ResetColor}")
            if timefr.lower() == 'd':
                timefr = 1
                aflag = False
            elif timefr.lower() == 'w':
                timefr = 7
                aflag = False
            else:
                print(f"{MainColor} Please enter a valid option! {ResetColor}")
        print()
        aflag = True
        while aflag:
            count = input(f"{MainColor} How many times do you have to perform the task you defined to mark habit as complete?  {ResetColor}")
            if count.isdigit():
                aflag = False
            else:
                print(f"{MainColor} Please enter a number! {ResetColor}")
        print()
        habits.add_habit(title,goal,int(timefr),int(count))  
    
    # Remove a habit
    elif user == "r":
        clear_screen()    
        habits.all_habits_list(True)
        user = input(f"{MainColor} Which habit would you like to remove? {ResetColor}")
        habits.remove_habit(user)
    
    # Show the table again
    elif user == "s":
        clear_screen() 
        print(f"{MainColor} You have 7 options! {ResetColor}")
        print()
        print(f"{MainColor} Option 1: Shows a table and list of all habits. {ResetColor}")
        print(f"{MainColor} Option 2: Shows a table and list of all 'Daily' habits. {ResetColor}")
        print(f"{MainColor} Option 3: Shows a table and list of all 'Weekly' habits.  {ResetColor}")
        print(f"{MainColor} Option 4: Shows the main table.  {ResetColor}")
        print(f"{MainColor} Option 5: Shows a table and title of the habit with the longest 'Streak'. {ResetColor}")
        print(f"{MainColor} Option 6: Shows a table and string of the 'Best Streak' of a specific habit.  {ResetColor}")
        print(f"{MainColor} Option 7: Go back.  {ResetColor}")
        print()
        aflag = True
        while aflag:
            option = input(f"{MainColor} Enter the number of the option you would like: {ResetColor}")
            if option.isdigit():
                aflag = False
            else:
                print(f"{MainColor} Please enter a number! {ResetColor}")
        print()
        option = int(option)
        if option == 1:
            clear_screen()
            out = habits.all_habits_list(True)
            print()
            print(f"The list: {out}{ResetColor}")
            print()
            input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
        elif option == 2:
            clear_screen()
            out = habits.all_daily_habits_list(True)
            print()
            print(f"The list: {out}{ResetColor}")
            print()
            input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
        elif option == 3:
            clear_screen()
            out = habits.all_weekly_habits_list(True)
            print()
            print(f"The list: {out}{ResetColor}")
            print()
            input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
        elif option == 4:
            clear_screen()
            habits.habits_table()
            print()
            input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
        elif option == 5:
            clear_screen()
            out = habits.longest_streak_of_all_habits(True)
            print()
            print(f"The habit with the longest streak of all is: {out}{ResetColor}")
            print()
            input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
        elif option == 6:
            clear_screen()
            habits.all_habits_list(True)
            print()
            user = input(f"{MainColor} Which habit would you like to see its best streak? {ResetColor}")
            clear_screen()
            out = habits.longest_streak_of_habit(user,True)
            print()
            print(f"The longest streak from {user} is: {out}{ResetColor}")
            print()
            input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
        elif option == 7:
            clear_screen()
            pass
        else:
            clear_screen()
            print(f"{MainColor} Option not found! Going back to main menu! {ResetColor}")
            input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")

    # Mark a daily task
    elif user == "c":
        clear_screen()    
        habits.all_habits_list(True)
        user = input(f"{MainColor} For which Habit have you completed your objective today? {ResetColor}")
        habits.check_off_habit(user)
    
    # Help Page
    elif user == "h":
        clear_screen()    
        print(f"{MainColor} Habits Tracker Help Page {ResetColor}")
        print(f"{SecondColor} --------------------------------------------------- {ResetColor}")
        print(f"{MainColor} The Habits Tracker helps you manage your habits and track your progress effectively. {ResetColor}")
        print(f"{MainColor} - Follow the prompts to add, remove, and analyze habits. {ResetColor}")
        print()
        print(f"{SecondColor} Command Options: {ResetColor}")
        print(f"{MainColor} - 'H' or 'h': Displays this help page. {ResetColor}")
        print(f"{MainColor} - 'S' or 's': Shows details regarding the habits.(Contains serveral optons within,Requests info from user) {ResetColor}")
        print(f"{MainColor} - 'C' or 'c': Marks a habit task as complete.(Requests a habit's name) {ResetColor}")
        print(f"{MainColor} - 'A' or 'a': Adds a new habit.(Requests info from user) {ResetColor}")
        print(f"{MainColor} - 'R' or 'r': Removes a habit.(Requests a habit's name) {ResetColor}")
        print(f"{MainColor} - 'Q' or 'q': Exits the program. {ResetColor}")
        print()
        print(f"{SecondColor} Habit Explanation: {ResetColor}")
        print(f"{MainColor} - Habit Example 1: Drink 7 glasses of water in a day. {ResetColor}")
        print(f"{MainColor} - Habit Example 2: Meditate 3 times a week. {ResetColor}")
        print(f"{MainColor} - User must define a 'Time Frame'.(For Example 1 it is 'Daily' and for Example 2 it is 'Weekly'.) {ResetColor}")
        print(f"{MainColor} - User must define a 'Task'.(For Example 1 it is 'Drink a glass of water' and for Example 2 it is 'Meditate'.) {ResetColor}")
        print(f"{MainColor} - User must define a task frequency. (For Example 1 it is '7' and for Example 2 it is '3'.) {ResetColor}")
        print(f"{MainColor} - User must mark tasks as completed after each occurrence. {ResetColor}")
        print(f"{MainColor} - Upon completing the defined tasks within the time frame, the habit is complete, and the timer resets. {ResetColor}")
        print(f"{MainColor} - Failing to complete tasks in the defined time frame will 'Break the habit'! {ResetColor}")

        print(f"{SecondColor} --------------------------------------------------- {ResetColor}")
        input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")

    # Exit program
    elif user == "q":
        clear_screen()    
        print(f"{MainColor} Thank you for using Habits Tracker! {SecondColor}(^_^) ")
        print(f"{MainColor} Have a great day! {ResetColor}")
        break
    
    # Handle invalid input
    else:
        clear_screen()    
        print(f"\033[91m Invalid Input! Please use the commands Provided! {ResetColor}")
        input(f"{MainColor} Press 'Enter' on your keyboard to continue. {ResetColor}")
 
