<p>
<img width="260" height="170" src="https://www.flaticon.com/svg/static/icons/svg/2206/2206461.svg" align="right" >
</p>

# :colombia: 0x0A. i18n

- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps

## Prerequisites

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 `(version 3.7)`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style `(version 2.5)`
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- All your \*.py files should be executable
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions and methods should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Run

```
$ Python3.7 ./app.py
```

## Files

| Files            | Description                     |
| ---------------- | ------------------------------- |
| **0-app.py**     | Basic Flask app                 |
| **1-app.py**     | Basic Babel setup               |
| **2-app.py**     | Get locale from request         |
| **3-app.py**     | Parametrize templates           |
| **4-app.py**     | Force locale with URL parameter |
| **5-app.py**     | Mock logging in                 |
| **6-app.py**     | Use user locale                 |
| **7-app.py**     | Infer appropriate time zone     |
| **app.py**       | Display the current time        |
| **babel.cfg**    | Configuration babel             |
| **translations** | Translations of babel           |
| **messages.pot** | Logs babel                      |
| **templates**    | Templates                       |
