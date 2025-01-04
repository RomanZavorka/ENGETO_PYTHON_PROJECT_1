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

     +------+-------------+
     | user |   password  |
     +------+-------------+
     | bob  |     123     |
     | ann  |   pass123   |
     | mike | password123 |
     | liz  |   pass123   |
     +------+-------------+

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
6. The program shows a simple bar chart representing the frequency of different word lengths in the text.

Example of a chart:

     7| * 1
     8| *********** 11
     9| *************** 15
    10| ********* 9
    11| ********** 10

## Program output
A suitable text analyzer output should look like this:

    username:bob
    password:123
    ----------------------------------------
    Welcome to the app, bob
    We have 3 texts to be analyzed.
    ----------------------------------------
    Enter a number btw. 1 and 3 to select: 1
    ----------------------------------------
    There are 54 words in the selected text.
    There are 12 titlecase words.
    There are 1 uppercase words.
    There are 38 lowercase words.
    There are 3 numeric strings.
    The sum of all the numbers 8510
    ----------------------------------------
    LEN|  OCCURENCES  |NR.
    ----------------------------------------
     1|*             |1
     2|*********     |9
     3|******        |6
     4|***********   |11
     5|************  |12
     6|***           |3
     7|****          |4
     8|*****         |5
     9|*             |1
    10|*             |1
    11|*             |1
 
If the user is not registered:

    username:marek
    password:123
    unregistered user, terminating the program..


