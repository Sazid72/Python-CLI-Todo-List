# Python-CLI-Todo-List
A simple command-line Todo List application written in Python.

## Features

* Add tasks
* View tasks
* Remove tasks
* Save tasks to a file
* Load tasks automatically when the program starts

Tasks are stored in `tasks.txt` and persist between sessions.

---

## Requirements

* Python 3.x

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/todo-cli.git
cd todo-cli
```

Run the program:

```bash
python todo.py
```

---

## Usage

When the program starts, a menu will appear:

```text
Options:
1. Add task
2. View task
3. Remove task
4. Exit
```

Choose an option by entering its corresponding number.

### Adding Tasks

Select:

```text
1
```

You can add multiple tasks continuously.

Example:

```text
Add a task: Study Python
Add a task: Go to the gym
Add a task: Read a book
```

### Important

The Add Task mode runs in a continuous loop by design.

To return to the main menu:

* Linux/macOS: Press Ctrl + D
* Windows: Press Ctrl + Z, then Enter

This will exit Add Task mode and return to the menu.

### Viewing Tasks

Select:

```text
2
```

Example output:

```text
Your listed tasks are:
1. Study Python
2. Go to the gym
3. Read a book
```

### Removing Tasks

Select:

```text
3
```

Then type the exact task name:

```text
Task to remove: Study Python
```

The task will be removed and the changes will be saved automatically.

---

## Data Storage

Tasks are stored in:

```text
tasks.txt
```

The file is automatically created when tasks are saved.

---

## Limitations

This project is intentionally simple and has a few limitations:

* Tasks are stored as plain text.
* No task completion status.
* No due dates.
* No task priorities.
* Removing a task requires typing its exact name.
* If duplicate task names exist, removing a task removes the first matching occurrence.
* No edit task functionality.
* No sorting or searching.

---

## Future Improvements

Possible future features:

* Save tasks using JSON
* Mark tasks as completed
* Remove tasks by number
* Edit existing tasks
* Add task priorities
* Add due dates
* Search tasks
* Colored terminal output

---

## License

This project is open source and available under the MIT License.
