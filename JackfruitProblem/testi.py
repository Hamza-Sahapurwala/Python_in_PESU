import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

class RestaurantBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Booking System")
        self.root.geometry("800x600")

        # Frame for Restaurant Display
        self.restaurant_frame = ttk.LabelFrame(root, text="Restaurants")
        self.restaurant_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Listbox for restaurants
        self.restaurant_list = tk.Listbox(self.restaurant_frame, height=15, width=50)
        self.restaurant_list.pack(side="left", fill="y", padx=5, pady=5)
        self.restaurant_list.bind('<<ListboxSelect>>', self.display_restaurant_details)

        # Scrollbar for restaurant list
        self.scrollbar = ttk.Scrollbar(self.restaurant_frame, orient="vertical", command=self.restaurant_list.yview)
        self.scrollbar.pack(side="left", fill="y")
        self.restaurant_list.config(yscrollcommand=self.scrollbar.set)

        # Restaurant details display
        self.restaurant_details = tk.Text(self.restaurant_frame, height=15, width=50, state="disabled")
        self.restaurant_details.pack(side="right", fill="y", padx=5, pady=5)

        # Frame for Booking Section
        self.booking_frame = ttk.LabelFrame(root, text="Booking Section")
        self.booking_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Widgets for booking inputs
        self.date_label = ttk.Label(self.booking_frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.booking_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.time_label = ttk.Label(self.booking_frame, text="Time (HH:MM):")
        self.time_label.grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.booking_frame)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        self.party_label = ttk.Label(self.booking_frame, text="Party Size:")
        self.party_label.grid(row=2, column=0, padx=5, pady=5)
        self.party_entry = ttk.Entry(self.booking_frame)
        self.party_entry.grid(row=2, column=1, padx=5, pady=5)

        self.book_button = ttk.Button(self.booking_frame, text="Book Table", command=self.book_table)
        self.book_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame for User Management Section
        self.user_frame = ttk.LabelFrame(root, text="User Management")
        self.user_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.view_bookings_button = ttk.Button(self.user_frame, text="View Current Bookings", command=self.view_bookings)
        self.view_bookings_button.pack(pady=5)

        self.cancel_booking_button = ttk.Button(self.user_frame, text="Cancel Booking", command=self.cancel_booking)
        self.cancel_booking_button.pack(pady=5)

        # Load initial data
        self.restaurants = self.load_restaurants()
        self.display_restaurants()

    def load_restaurants(self):
        """Load restaurants from CSV file."""
        try:
            with open(r'JackfruitProblem\restaurants.csv', mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            messagebox.showerror("Error", "restaurants.csv file not found.")
            return []

    def display_restaurants(self):
        """Populate the listbox with restaurant names."""
        for restaurant in self.restaurants:
            self.restaurant_list.insert(tk.END, restaurant['name'])

    def display_restaurant_details(self, event):
        """Display details of the selected restaurant."""
        selected_index = self.restaurant_list.curselection()
        if selected_index:
            restaurant = self.restaurants[selected_index[0]]
            details = (f"Name: {restaurant['name']}\n"
                       f"Cuisine: {restaurant['cuisine_type']}\n"
                       f"Rating: {restaurant['rating']}\n"
                       f"Location: {restaurant['location']}\n"
                       f"Tables: {restaurant['table_configuration']}\n"
                       f"Hours: {restaurant['opening_hours']} - {restaurant['closing_hours']}")
            self.restaurant_details.config(state="normal")
            self.restaurant_details.delete("1.0", tk.END)
            self.restaurant_details.insert(tk.END, details)
            self.restaurant_details.config(state="disabled")

    def book_table(self):
        """Handle table booking process."""
        date = self.date_entry.get()
        time = self.time_entry.get()
        party_size = self.party_entry.get()

        if not date or not time or not party_size:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date or time format.")
            return

        # Assuming we save the booking to bookings.csv
        booking_id = f"B{int(datetime.now().timestamp())}"  # Simple unique ID
        selected_index = self.restaurant_list.curselection()

        if not selected_index:
            messagebox.showerror("Error", "No restaurant selected.")
            return

        restaurant = self.restaurants[selected_index[0]]
        try:
            with open(r'JackfruitProblem\bookings.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([booking_id, restaurant['restaurant_id'], date, time, party_size])
            messagebox.showinfo("Success", f"Table booked successfully! Booking ID: {booking_id}")
        except FileNotFoundError:
            messagebox.showerror("Error", "bookings.csv file not found.")

    def view_bookings(self):
        """View current bookings."""
        try:
            with open(r'JackfruitProblem\bookings.csv', mode='r') as file:
                reader = csv.reader(file)
                bookings = list(reader)
            bookings_text = "\n".join([f"ID: {b[0]}, Restaurant: {b[1]}, Date: {b[2]}, Time: {b[3]}, Party: {b[4]}" for b in bookings])
            messagebox.showinfo("Current Bookings", bookings_text if bookings else "No bookings found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "bookings.csv file not found.")

    def cancel_booking(self):
        """Cancel an existing booking."""
        booking_id = tk.simpledialog.askstring("Cancel Booking", "Enter Booking ID to cancel:")
        if not booking_id:
            return

        try:
            with open(r'JackfruitProblem\restaurants.csv', mode='r') as file:
                bookings = list(csv.reader(file))
            updated_bookings = [b for b in bookings if b[0] != booking_id]

            with open(r'JackfruitProblem\bookings.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_bookings)

            messagebox.showinfo("Success", "Booking canceled successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", "bookings.csv file not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantBookingSystem(root)
    root.mainloop()
