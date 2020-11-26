

This project simulates creation and movement of a robotic agent across a board <br/>

-----------------------
DOWNLOADING THE PROJECT

This project has been uploaded to GitHub at https://github.com/karunmatthew/robot.git <br/>
Clone the project by running ```git clone git@github.com:karunmatthew/robot.git``` <br/>

--------------------
BUILDING THE PROJECT

This project requires python 3.6 or higher

Install the dependencies of the project by running 
```
  pip install -r requirements.txt
              OR
  python -m pip install -r requirements.txt
``` 
All the dependencies for running this project has been included in the requirements.txt file <br/>

-----------------------------------
CONFIGURING THE PROJECT ENVIRONMENT

The dimensions of the board within which the agent moves is controlled by values in a configuration file <br/>
The configuration file can be found in robot/config.py


-----
INPUT

The commands to move the agent needs to be provided as input in the form of a text file. <br/>
A sample command file can be found in 'input_data.txt' file in the project root folder. <br/>
```
PLACE 0 0 NORTH
MOVE
REPORT
PLACE 0 0 NORTH
LEFT
REPORT
PLACE 1 2 EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

-------------------
RUNNING THE PROJECT

Run the project by running the main.py file in the project root folder <br/>
``` python main.py ```


-----------
ASSUMPTIONS
```
1. Only one agent can be placed at the board at a given point of time
2. Agent cannot move outside the board and commands to perform the same will be ignored
```

----------------
TESTING THE CODE

All the test files can be found under the 'test' folder. <br/>
Please run the command ```pytest``` on the project root folder to execute all the test cases <br/>

In windows run  ```python -m pytest```
