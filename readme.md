# Library Management System

The library management system is a python based application devloped t manage basic library activites. The system allows users to manage book and students issue and return books view issued boos genrate a library report and save data for furture use


FEATURES
-Add a new book
-View all books
-Search for a book using its id
-Return an issued book
-Genrate a library report
-Save data to a text file
-View currently issued books
-issue a book to student


PROJECT STRUCTURE

Library management system:
main.py
books.py
students.py
transactions.py
validation.py
reports.py
storage.py
library_data.txt


DESCRIPTION OF FILES

main.py

the main program file, it displays menu,accepts the users choice and calls the required functions from other modules


books.py

manages book records it contains functions to add view and search for books

students.py

manages student records. it contain functions to add view and find students

transactions.py

handles book transactions it conatins functions for issuing books returning books and view issued book

validation.py

checks whether the users menu choice is between 1 and 10

reports.py

genrate a simplle library report showing the total number of books and studnets and currently issued books

storage.py

handles data persistence it saves books studnets and issued books records and loads them when program starts

TECHNOLOGIES USED

python3.14.6
visual studio code
Text file handling
Python functions,lists,loop and condtions and modules

HOW TO RUN

make sure the python installed
open the project folder in visual studio code
open the terminal
run: python main.py

select an option from the menu
when option 10 is selected the current data is saved and program closes


DATA STORAGES

the project used a text file library_data.txt instead of database
the storage.py module writes the data into diffrent sections

BOOKS
STUDENTS
ISSUED_BOOKS

EXAMPLE MENU

==LIBRARY MANAGEMENT SYSTEM==

1.Add book
2.View books
3.Search book
4.Issue book
5.Return book
6.Add student
7.View students
8.View issued books
9.Library report
10.Exit




AUTHOR

name-Atharva sharma
Reg no-26BCE11003

This project demonstrates the use of python programming concepts to create a functional library management system. The modular dsegin makes the program easier to understand and maintain while allowing library data to be saved and loaded between program runs.