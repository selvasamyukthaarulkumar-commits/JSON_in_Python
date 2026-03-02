#Working with Files and JSON in Python
## Files
 -inventory.json
 Store book details in JSON format.
 Contains title , author , price , and stock availability. 
 -inventory.py
 Python program that reads and updates the JSON file.
## Explanation
Task 1 : Read files and print total books. 
 - Used 'with open()' to open the file
 - Used 'JSON.load()' to convert JSON data into python list.
 - Printed total number of book using         'len()' function.


 Task 2 : Added new book ans saved file.
 - Created a new book dictionary.
 - Used ' append()' method to add new book to list.
 - Used 'json.dump()' with 'indent=4' to save updated data. 

 
Task 3 : Displayed all books 
- Used for loop to iteratethrough books.