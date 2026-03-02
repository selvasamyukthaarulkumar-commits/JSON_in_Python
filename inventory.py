import json 
# new book
new_book = {
    "title": "Atomic Habits", 
    "author": "James Clear",
      "price": 14.99,
        "in_stock": True
}
# Task 1 - Read file 
with open("inventory.json","r") as file:
    inventory = json.load(file)
print("Total books:", len(inventory)) 
# task 2 - Add new book
inventory.append(new_book)
with open("inventory.json","w")as file:
    json.dump(inventory,file, indent=4)
#task 3 - Display books
for book in inventory:
    print("Title:", book["title"], "| Author:",book["author"], "|Price : $", book["price"])    

