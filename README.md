
# Knowledge Manager (Python Desktop App)

A simple but well‑structured **Desktop Knowledge Manager** built with Python and Tkinter.  
This project demonstrates clean project architecture, separation of concerns, and GUI application development practices such as modular design, service layers, data modeling, and JSON‑based data persistence.

The application allows users to **create, view, edit, and delete notes** through a graphical interface while storing the data locally in a JSON file.

This project was designed as a learning exercise to practice building maintainable Python desktop applications using a modular structure similar to real software projects.

---

## Features

- Create new notes
- View a list of saved notes
- Edit existing notes
- Delete notes
- Persistent data storage using JSON
- Simple and clean graphical interface with Tkinter
- Modular architecture (UI, models, services)
- Separation of UI logic and data storage logic

---

## Technologies

- Python 3
- Tkinter for GUI development
- JSON for local data storage
- Standard Python libraries (datetime, json, os)

---

## Project Structure

```
knowledge_manager/
│
├── main.py
├── models/
│   └── note.py
├── services/
│   └── storage_service.py
└── ui/
    └── app.py
```

*(Note: The `data/notes.json` file is generated automatically within the project directory upon the first save.)*

---

## Installation

Clone the repository:

```
git clone https://github.com/Abdolghader-Shokri/python-knowledge_manager.git
cd python-knowledge_manager
```

Create and activate a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate
```

---

## Running the Application

Run the program using:

```
python main.py
```

The graphical interface will open, allowing you to create and manage notes.

---

## Data Storage

All notes are stored locally in `data/notes.json` (created automatically).  
Each note is serialized as a JSON object containing:

- id
- title
- content
- created_at

---

## Learning Goals

This project was built to practice:

- Building desktop applications with Tkinter
- Designing modular Python project structures
- Separating UI logic from business logic
- Managing application data with JSON storage
- Applying object‑oriented programming principles
- Writing maintainable and scalable Python code

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
