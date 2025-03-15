#### WSGI : Interface to connect the web application and the server together 

# Dependencies :

    Werkzeug : A WSGI utility library for Python used to build web frameworks; provides routing, debugging, and request/response handling.


    Jinja: A fast, flexible templating engine for Python, often used in web applications to generate HTML dynamically.
   

    MarkupSafe: A library for handling safe HTML/XML escaping, ensuring that injected content does not break or introduce security risks.
   

    ItsDangerous: A library for securely signing data, used for creating tamper-proof tokens (e.g., in Flask sessions or password reset links).
   

    Click: A simple and composable command-line interface (CLI) library for Python, used to build user-friendly command-line tools.
   

    Blinker: A lightweight library for implementing signals and event-driven programming in Python, often used for decoupling components in applications.
   
# Step For Lesson :

    * Create Folder
    * type "py [-{version}] -m venv {Name}"
    * {Name}\Scripts\activate 
    * deactivate : to deacativate *
    * set FLASK_APP=server.py
    * Create server.py outside venv
    * Use bootstrap by using Link & Script
    * Use google font for better cloud hosting fonts
    * Do use jinja Ex. {{}}

# Functioning : 

    * server.py act as the backend
    * templates are where html and style located
    * using route as the url sub
    * layout are the mother and the rest are child extended
    * update is to update the team name
    * delete is to delete the team
    * Learn what is GET and POST requests
    * In an index there should atleast title and content
    
    
# Activate Shell 
- set FLASK_APP=server.py
- flask --app server.py shell