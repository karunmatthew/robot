This project simulates creation and movement of a robotic agent across a board <br/>
-----------------------
DOWNLOADING THE PROJECT

This project has been uploaded to GitHub at https://github.com/karunmatthew/robot.git <br/>
Clone the project by running <br/> ```git clone git@github.com:karunmatthew/robot.git```

--------------------
BUILDING THE PROJECT

Build the project by running <br/>  ```pip install -r requirements.txt```
All the dependencies for running this project has been included in the requirements.txt file <br/>

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

-------------
CONFIGURATION

The dimensions of the board within which the agent moves is controlled by values in a configuration file <br/>

-----------
ASSUMPTIONS
```
1. Only one agent can be placed at the board at a given point of time
2. Agent cannot move outside the board and commands to perform the same will be ignored
```

----------------
TESTING THE CODE

All the test files can be found under the 'test' folder. <br/>
Please run the command ```pytest``` on the root folder to execute all the test cases <br/>
