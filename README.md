# project-DB1
project for interaction with DB and adding data from Tkinter form

This is planning for a future project:

This project contains Tkinter form where will be few text boxes for entering information about the person 
big slider-textbox (or table) for output all data from DB

DB will be organized at localhost 

DB architecture:
  There a few options:
    1) Option#1 - One table with all predefined columns 
    2) Dynamically create a new table with one column  <- THis option perhaps not valid at big scale 

Milestones:
  1) Create a testDB table with an initial set of columns for data entering 
  2) Create *.py*// for connecting to DB and enter one set of data as **kvarg dictionary 
  3) Create Tkinter form with a few textboxes and button for data entery 
  4) Secure separate threads for form existing and operations related with other functions under buttons 
  5) Add function for getting data from textboxes and record them to DB
  6) Add button with functionality to pull all the data from DB and present them at bigger textbox or table on the form 
  
  
Future V2 functionality:
  1) Work with csv file 
    a) add txtbox for a path to the file entry or add windows finder window option
    b) after picking up correct csv file with proper formatting all the data from csv should be added to db 
    c) and when user pressing on "show DB data" button all the data from before and new data are displaying at big textbox or table at the form.
    
