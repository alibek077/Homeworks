#1 
import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Major:", student["major"])
    print()




# 3
import json

with open("books.json", "r", encoding="utf-8") as file:
    books = json.load(file)

print(" Current Books:")
for book in books:
    print(f"- {book['title']} by {book['author']}")

new_book = {"title": "New Book", "author": "New Author"}
books.append(new_book)
print("\n Added new book.")

for book in books:
    if book["title"] == "Book One":
        book["title"] = "Updated Book One"
        book["author"] = "Updated Author A"
        print(" Updated 'Book One'.")


title_to_delete = "Book Two"
books = [book for book in books if book["title"] != title_to_delete]
print(f" Deleted book titled '{title_to_delete}'.")

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, indent=4)

print("\n Updated Books:")
for book in books:
    print(f"- {book['title']} by {book['author']}")


