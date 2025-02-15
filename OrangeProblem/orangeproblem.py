import csv
import tkinter as t
from tkinter import messagebox

# function to load book datasheet

def load_books(file_name):
    books=[]
    try:
        with open(r"OrangeProblem\book_dataset.csv",'r',newline='\r\n') as f:
            reading = csv.DictReader(f)
            for row in reading:
                # parse the row, converting numeric fields to proper ty
                book = {
                    "Title": row["Title"],
                    "Release Year": int(row["Release Year"]),
                    "Rating": float(row["Rating"])
                }

                # add genre information (one-hot encoding)
                for genre in genres:
                    book[genre] = int(row[genre])
                books.append(book)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_name}' not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Error loading file: {e}")
    return  books


# function to filter books based on user preference
def recommended_books():
    selected_genres = [genre for genre, var in genre_vars.items() if var.get() == 1]
    if not selected_genres:
        messagebox.showinfo("No selection, please select genre")
        return
    filtered_books=[
        book for book in books
        if all(book[genre]==1 for genre in selected_genres)
    ]

    # display results
    result_text.delete(1.0, t.END)
    if filtered_books:

        # sort by rating (highest rating first)
        filtered_books .sort(key=lambda x:x["Rating"], reverse=True)

        # display the top match
        top_book = filtered_books[0]
        result_text.insert(
            t.END,
            f"Top Pick: {top_book["Title"]} ({top_book['Release Year']}) - Rating: {top_book['Rating']}\n\n"
        )
        # display other recommendations
        result_text.insert(t.END, "Recommended Book:\n\n")
        for book in filtered_books[:5]:
            result_text.insert(
                t.END,
                f"{book["Title"]} ({book['Release Year']}) - Rating: {book['Rating']}\n\n"
            )
    else:
        books.sort(key= lambda x:x["Rating"], reverse = True)
        result_text.insert(t.END,"No matches found. Showing top rated books:\n\n")
        for book in books[:5]:
            result_text.insert(
                t.END,
                f"{book["Title"]} ({book['Release Year']}) - Rating: {book['Rating']}\n\n"
            )

# function to clear all preferences
def clear_preferences():
    for var in genre_vars.values():
        var.set(0)
    result_text.delete(1.0, t.END)

# load the book data
genres = ["Action", "Comedy", "Drama", "Sci-Fi","Romance", "Animation"]
books = load_books("book_datasheet.csv")

# create main tkinter window
root = t.Tk()
root.title("Book Finder Assistant")
root.geometry("1500x900")
root.resizable(False,False)

# to add heading
t.Label(root,text = "Select your favourite genres", font=("Arial",16,"bold")).pack(pady=11)

# UI components
t.Label(root,text = "Select genres:", font=("Arial",14)).pack(pady=10)

# checkbox for each genre
genre_vars = {genre: t.IntVar() for genre in genres}
for genre, var in genre_vars.items():
    t.Checkbutton(root,text = genre, variable = var,font=('Arial',200,'bold')).pack(anchor = 'w',padx=20)

# adding buttons
t.Button(root, text= "Recommended", command= recommended_books).pack(pady=10)
t.Button(root, text= "Clear", command= clear_preferences).pack(pady=10)

# displaying the result
result_text = t.Text(root, wrap="word", height=20, width=50)
result_text.pack(pady=10)

# run the application
root.mainloop()