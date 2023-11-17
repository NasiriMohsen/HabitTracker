# Habits Tracker

Habits Tracker is a simple Python script that allows users to track their habits, set goals, and monitor their progress.

- A user can define multiple habits. A habit has a task specification and a periodicity.
- A task can be completed or “checked-off”,at any point in time.
- Each task needs to be checked-off at least once during the period the user defined for the respective habit. If a user misses to complete a habit during the specified period, the user is said to break the habit Habits with 'Gray' remaining time are considered as broken habits!
- If user manages to complete the task of a habit x consecutive periods in a row without breaking the habit, the user will establish a streak of x periods. For instance, if the user wants to work out every day and does so for two full weeks, they establish a 14-day streak of working out.

## Features

- Add new habits with specific goals and periodicity.
- Remove existing habits.
- Mark daily tasks as completed to track streaks.
- View a table of habits with detailed information.

## Getting Started

### Prerequisites

- Tested on Python 3.11.4
- `prettytable` library (install with `pip install prettytable`)

### Installation

1. Clone the repository:
```bash
   git clone https://github.com/NasiriMohsen/HabitTracker.git
   cd HabitTracker
```

2. Run the script:
```bash
   python Main.py
```

## Usage

- Follow the on-screen instructions to interact with the Habits Tracker.
- Type 'A' to add a new habit.
- Type 'R' to remove a habit.
- Type 'C' to mark a daily task.
- Type 'S' to show everything.
- Type 'Q' to exit the program.
