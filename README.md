Finished Development: 01/16/2022

# Summary
This project was designed to help reduce the amount of boilerplate code that is needed to write for testing code. The 
user would type in the path of the file that they wanted to test and then through the GUI design the test cases. At the 
time I thought it would be incredibly useful, but I soon realized that for sufficiently complicated code, the simplistic 
system I implemented was not sufficient. It was still a fun project to work on, however. I worked on it for around one 
week. This was built upon my game engine, which used pygame for rendering (I copied the 'game engine' between projects 
at the time - the game engine is now a python library 'game-qu'). Most of the new code I wrote for this project is 
in the 'logic' and 'gui' modules. I also wrote 'set_upper.py' and 'game_runner.py' for this project.

# How to Use
Type in the path of the file you want to test in the initial text box labeled 'File Location.' Click the left arrow key 
to see all the functions that can be tested. Click any specific function to test that specific function. All but the last 
text box in the 'Test Specific Function' screen are the parameters for that specific test case. The last text box is the 
expected output when the function is called with those parameters. Once you are done with all the test cases, press 
'Ctrl + d' to have the application generate the tests. The tests will be outputted in 'output.txt'

# Images
## Choose File Screen
![Choose File Screen](documentation/Choose%20File%20Screen.png)

## All Functions Screen
![All Functions Screen](documentation/All%20Functions%20Screen.png)


## Test Specific Function Screen
![Testing Specific Function Screen](documentation/Test%20Specific%20Function%20Screen.png)

## Example Output
![Example Output](documentation/Example%20Output.png)

# How to Run
- Install pygame by typing 'pip install pygame'
- Run 'game_runner.py' in the root directory of the project