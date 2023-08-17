# AirBnB clone - The console
![AirBnB](https://github.com/faustine-van/AirBnB_clone/assets/125466059/896d5806-6f47-4c9f-bf2e-ddd036bdc50a)
## First step: Write a command interpreter to manage your AirBnB objects.
![AirBnB_step1](https://github.com/faustine-van/AirBnB_clone/assets/125466059/0a70abba-f1b2-4829-afa4-117444718cb7)
### What’s a command interpreter?
Do you remember the Shell? It’
s exactly the same but limited to a specific use-case.
In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## How command interpreter works?

Execution
Your shell should work like this in interactive mode:

```$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## ALL FILES AND FOLDERS
```
vagrant@ubuntu-focal:~/all_files$ tree
.
├── AUTHORS
├── README.md
├── console.py
├── models
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── tests
    ├── __init__.py
    ├── test_console.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```
AUTHORS:
  - [MUHAYEMARIYA FAUSTINE](https://github.com/faustine-van/AirBnB_clone/edit/master/README.md)
