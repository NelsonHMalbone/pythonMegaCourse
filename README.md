# Python Mega Course

### Module 1

### todos
- Add print statements to show what each item is in list 
- add date of contract/batch
- add maintance part (for when user gets to maintaining own units)
- add contract num for each run (06-07 completed)
- add a calc to have user enter how many (mainly used for when user gets to adding length indicator and such)
  - trains to be used like d2s d6s slugs and such
  - input weight and length of each contract
  - prints out total weight and lenght including the trains being used
- will need to add a batch so that if user is doing multiple jobs in one trip it will show in one whole group
- will need to add a json file for the train parts.
#### Day 1
Day 1 is a building a todo app but instead of building a todo app
im going to be building a app for a game called Derail Valley its a pc game about hauling frieght 
to different parts of the map. 

This day is going over some basic of python

#### 05-10
going over the basics of python. basic inputs in such

instead of doing the todo list project, setting up to do my own some what of a simular project 
for a game that i will be getting here so. many inputs to fill in in to track. 

we installed the input options as the course is doing.

#### 05-14
working on storing the inputs into a list with [] 
ex: 
    user_prompt = 'Enter a todo'
    todo1 = input(user_prompt)
    todo2 = input(user_prompt)
    todo3 = input(user_prompt)
    todos = [todo1, todo2, todo3] data types for list to store inputs

#### 05-17
bonus example folder contains bonus code examples for each day small additional projects
start section 2 working with while and new python methods
creating a list outside of the while loop to store input
using dir(str) in console will show you all the methods for str data type
using the help("example".capitalize)
finshed day 2 starting day 3

#### 05-24 
starting to work on day 3 
main focus is using match case and for loops

to add a to new run or to view all runs.
first ask user to add a new run or to view

to stop a program use the "break" 

to get rid of [] and '' would do a statement of for item in category_list
so using the strip method it will strip whitespaces and such 
this also does not change the variables white spaces

#### 05-29
finishing up the vod 33 of section 3 day 3.
with the case 'show' you can use the "|" and type in another word like 'display'
so that bitwise or another word is operator will match so that oine will be true
dont need another case or if statement with the same line of code 

#### 05-31
finished up section 3 day 3 
worked with more for loops in the the way they interate over a list and work
today we are starting on section 4 day 4
working with list-indexing and tuples
 
so had to change the for loop from 
for item in items do this 
to using for key, value in category_data.items()
this approach keeps the inputs label and easy to display and manage
did have to add a tuple to capture all the infomation to get and add titles of what each section was

#### 06-07
worked on restructing the data and the list and placed them inside the added section
in the all categories will capture everything from the category data, so tht the 
the user can choice which entry to pick 

#### 06-13
working on a edit section still its been a few days. 
before this commit we got a error a type error on line 70 which is just
-existing_category_list because we are looking for a number in not a string its erroring because it dont see a number
adjust the input for numbers to only accept nums or ints.
prints out a dictionary with a key and value.