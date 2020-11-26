from robot.robot_agent import Robot
import tkinter as tk
from tkinter import filedialog
from robot.config import Config

# choose file automatically through a dialog window
robot = Robot()
root = tk.Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(initialdir="./",
                                             title='Select the command file')
root.update()
root.destroy()

if len(input_file_path) > 0:
    robot.run(input_file_path)
else:
    robot.run(Config.INPUT_FILE_PATH)
