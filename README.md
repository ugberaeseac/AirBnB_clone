**AirBnB Console**

Welcome to the AirBnB Console, a command-line interface
for managing AirBnB-like objects!

**Description**

The AirBnB Console is a Python-based command interpreter that allows you to
create, manage, and manipulate objects representing different components of
an AirBnB-like system. You can create and manage instances of various classes,
perform CRUD(Create, Read, Update, Delete)operations, and
interact with a JSON-based data storage system.

**Command Interpreter**

**How to Start**

1. Clone this repository to your local machine

git clone https: // github.com/your-username/AirBnB_clone.git

2. Navigate to the AirBnB_clone directory
cd AirBnB_clone

3. cd AirBnB_clone
./console.py


**How to Use**
Once you've started the AirBnB Console, you'll see the(hbnb) prompt.
You can enter various commands to interact with the console.

**Here are some available commands**

- * **create**: Creates a new instance of a class and
saves it to the JSON file.

- * **show**: Displays the details of a specific instance.

- * **destroy**: Deletes an instance.

- * **all**: Displays details of all instances or all
instances of a specific class.

- * **update**: Updates the attributes of an instance.


Use the help command in the console to get more
information about each command.

**Examples**

1. Create a new instance of the BaseModel class
-(hbnb) create BaseModel

2. Show details of a specific instance
-(hbnb) show BaseModel 1234-5678

3. Delete an instance
-(hbnb) destroy BaseModel 1234-5678

4. Show details of all instances
-(hbnb) all

5. Update an attribute of an instance
-(hbnb) update BaseModel 1234-5678 name "New Name"
