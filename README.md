# BUDGET
One of the Final Projects for [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

#### **Description**:
This was done with the guidance of the project specifications of [Freecodecamp](https://www.freecodecamp.org/). The program consists in basically 2 blocks of code on the file **budget.py**. **A class called 'Category'** that creates objects who represents both how much money are available for some category and how much i spent on that one. To do this i have a method called 'deposit' that can receive an amount and a description, another one called 'withdraw' that also accepts an amount (that will be converted to a negative number) and a description, one called 'transfer' that allows to transfer amounts between objects, one called 'get_balance' that returns how much money are still available, one called 'check_funds' that is used to validate both the withdraw and transfer methods based on the return of 'get_balance' and ,finally, a python's spetial method 'str' that creates a formated output on the terminal for each object. **The other block of code** is the function 'create_spend_chart', that returns a formated output on the terminal representing the percentages spent in each category based on the initial deposit (if applicable) of each object, all rounded to the lowest 10. In the **aux_functions.py** file i wrote some functions that abstract away some details of the implementation of the 'create_spend_chart' function. The **main.py** file is just to use the program. 
This project was tested using unit tests provided from [Freecodecamp](https://www.freecodecamp.org/), which are not included in this repository.  
