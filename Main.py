from HabitsTracker import Tracker

habits = Tracker()

MainColor = "\033[92m"
ResetColor = "\033[0m"
YellowColor = "\033[93m"
print(f"{YellowColor} Progress is Progress no matter how small! {ResetColor}")
print(f"{MainColor} Hello and Welcome! {YellowColor}(^_^) ")
print(f"{MainColor} You may use the commands bellow to navigate! {ResetColor}")
while True:
    print(habits.TableofHabits())
    print()
    print(f"{MainColor} To show everything so far use: \033[1m{YellowColor}'S' {MainColor}or \033[1m{YellowColor}'s'{MainColor}! {ResetColor}")
    print(f"{MainColor} To mark your daily task use: \033[1m{YellowColor}'C' {MainColor}or \033[1m{YellowColor}'c'{MainColor}! {ResetColor}")
    print(f"{MainColor} To add a new Habit use: \033[1m{YellowColor}'A' {MainColor}or \033[1m{YellowColor}'a'{MainColor}! {ResetColor}")
    print(f"{MainColor} To remove a Habit use: \033[1m{YellowColor}'R' {MainColor}or \033[1m{YellowColor}'r'{MainColor}! {ResetColor}")
    print(f"{MainColor} To exit program use: \033[1m{YellowColor}'Q' {MainColor}or \033[1m{YellowColor}'q'{MainColor}! {ResetColor}")
    user = input(f"{MainColor} You: {ResetColor}").lower()
    
    if user == "a": 
        print()
        title = input(f"{MainColor} Choose a 'Title' for this habit: {ResetColor}")
        print()
        goal = input(f"{MainColor} Define your 'Goals and Plans' for this habit: {ResetColor}")
        print()
        print(f"{MainColor} Define a 'Time Frame' or time cycle for your self to complete this task")
        print(f"{MainColor} If not completed during this period you will break the habit and your 'Streak'")
        aflag = True
        while aflag:
            timefr = input(f"{MainColor} Please define in number of days: {ResetColor}")
            if timefr.isdigit():
                aflag = False
            else:
                print(f"{MainColor} Please enter a number! {ResetColor}")
        print()
        print(f"{MainColor} If you have already started...")
        aflag = True
        while aflag:
            streak = input(f"{MainColor} What is your current 'Streak' for succesfully completed cycles?  {ResetColor}")
            if streak.isdigit():
                aflag = False
            else:
                print(f"{MainColor} Please enter a number! {ResetColor}")
        print()
        stat = input(f"{MainColor} Have you completed your objective or 'Goal' during the current cycle? \033[1m{YellowColor}(y/n) {ResetColor}").lower()
        if stat == "yes" or stat == "y":
            stat = 1
        else:
            stat = 0
        print()
        aflag = True
        while aflag:
            best = input(f"{MainColor} How much is your 'Best Streak' record of all time for this habit? {ResetColor}")
            if best.isdigit():
                aflag = False
            else:
                print(f"{MainColor} Please enter a number! {ResetColor}")
        print()
        habits.AddHabit(title,goal,int(timefr),int(streak),stat,int(best))  
    elif user == "r":
        print(habits.ListofHabits())
        user = input(f"{MainColor} Which habit would you like to remove? {ResetColor}")
        habits.RemoveHabit(user)
    elif user == "s":
        pass
    elif user == "c":
        print(habits.ListofHabits())
        user = input(f"{MainColor} For which Habit have you completed your objective today? {ResetColor}")
        habits.CheckHabit(user)
    elif user == "q":
        print(f"{MainColor} Thank you for using Habits Tracker! {YellowColor}(^_^) ")
        print(f"{MainColor} Have a great day! {ResetColor}")
        break
    else:
        print(f"\033[91m Invalid Input! Please use the commands above! {ResetColor}")
 
