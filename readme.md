# ENGETO_PYTHON_PROJECT_1
## Project assignment
### Introduction
In this project, the goal is to create a text analyzer - a program that is able to process text of any given length and determine information about its structure. Within the project, three texts were assigned for analysis (the texts are available in the code preview).
### Requirements
The text analysis program must meet the following points:
1. The code must contain a header with the contact details of the author of the project
2. When program is run, it requests a login name and password from the user
3. The program checks whether the entered login details match any of the registered users:
* If the user is registered, the program greets him and allows him to analyse the texts
* If the user is not registered, the program notifies the user and then shuts down.
Registered users are:

 

4. Registered user is allowed to choose between three texts stored in the TEXTS variable:
* If the user selects a text number that is not in the input, the program notifies the user and shuts down
* If the user enters an input other than a number, the program also notifies the user and shuts down
5. For selected text the following statistics are calculated:
* Total word count
* Count of words beginning with a capital letter
* Count of words written in capital letters
* Count of words written in lower case letters
* Count of numbers (not digits)
* The total sum of all numbers (not digits) in the text
6. The program shows a simple bar chart representing the frequency of different word lengths in the text. For example:
 
## Program output
A suitable text analyzer output should look like this:

 
If the user is not registered:

 


