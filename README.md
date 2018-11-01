# project-DB1
project for interaction with DB and adding data from trinter form

This is pllaning for future project:

This project contain tkinter form where will be few textboxes for entering information about the person 
big slider-textbo (or table) for output all data from DB

DB will be organized at localhost 

DB architecture:
  There few options:
    1) Option#1 - One table with all predifined coloumns 
    2) Dinamicaly create new table with one coloumn  <- THis option perhaps not valid at big scale 

Milestones:
  1) Create testDB table with initial set of coloumns for data enetering 
  2) Create *.py*// for connecting to DB and enter one set of data as **kvarg dictionary 
  3) Create tkinter form with a few textboxes and button for data entery 
  4) Secure separate threads for form existing and operations related with other functions under buttons 
  5) Add function for getting data from textboxes and record them to DB
  6) Add button with functionalyty to pull all the data from DB and present them at bigger textbox or table on the form 
  
  
Future V2 functionality:
  1) Work with csv file 
    a) add txtbox for path to the file entery or add windows finder window option
    b) after picking up correct csv file with proper formatting all the data from csv should be added to db 
    c) and when user pressing on "show DB data" button all the data from before and new data are displaying at big txtbox or table at the form.
    
   
    
