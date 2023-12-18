import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

class VehicleMonitoringApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Vehicle Monitoring Program")

        # List to store records
        self.records = []

        # GUI elements
        self.driver_name_label = tk.Label(master, text="Driver Name:")
        self.driver_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.driver_name_entry = tk.Entry(master)
        self.driver_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.color_label = tk.Label(master, text="Color:")
        self.color_label.grid(row=1, column=0, padx=10, pady=10)
        self.color_entry = tk.Entry(master)
        self.color_entry.grid(row=1, column=1, padx=10, pady=10)

        self.plate_number_label = tk.Label(master, text="Plate Number:")
        self.plate_number_label.grid(row=2, column=0, padx=10, pady=10)
        self.plate_number_entry = tk.Entry(master)
        self.plate_number_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button to add a record
        self.add_button = tk.Button(master, text="Add Record", command=self.add_record)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Text widget to display records
        self.records_text = tk.Text(master, height=10, width=40)
        self.records_text.grid(row=4, column=0, columnspan=2, pady=10)

        # Buttons for deleting and updating records
        self.delete_button = tk.Button(master, text="Delete Record", command=self.delete_record)
        self.delete_button.grid(row=5, column=0, pady=10)

        self.update_button = tk.Button(master, text="Update Record", command=self.update_record)
        self.update_button.grid(row=5, column=1, pady=10)

    def add_record(self):
        driver_name = self.driver_name_entry.get()
        color = self.color_entry.get()
        plate_number = self.plate_number_entry.get()

        if not driver_name or not color or not plate_number:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add data to the records list
        record = {
            "Driver Name": driver_name,
            "Color": color,
            "Plate Number": plate_number,
            "DateTime": current_datetime
        }
        self.records.append(record)

        messagebox.showinfo("Success", "Record added successfully.")

        # Update the displayed records
        self.update_records_display()

        # Clear entry fields after adding a record
        self.driver_name_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.plate_number_entry.delete(0, tk.END)

    def update_records_display(self):
        # Clear the text widget
        self.records_text.delete(1.0, tk.END)

        # Display records in the text widget
        for index, record in enumerate(self.records, start=1):
            record_str = f"{index}. Driver: {record['Driver Name']}, Color: {record['Color']}, Plate Number: {record['Plate Number']}, Date Time: {record['DateTime']}\n"
            self.records_text.insert(tk.END, record_str)

    def delete_record(self):
        # Ask user for the record index to delete
        index_to_delete = simpledialog.askinteger("Delete Record", "Enter the record index to delete:")

        if index_to_delete is not None and 1 <= index_to_delete <= len(self.records):
            del self.records[index_to_delete - 1]
            messagebox.showinfo("Success", f"Record at index {index_to_delete} deleted.")
            self.update_records_display()
        else:
            messagebox.showerror("Error", "Invalid index.")

    def update_record(self):
        # Ask user for the record index to update
        index_to_update = simpledialog.askinteger("Update Record", "Enter the record index to update:")

        if index_to_update is not None and 1 <= index_to_update <= len(self.records):
            # Fetch the existing record
            record_to_update = self.records[index_to_update - 1]

            # Ask for new data
            new_driver_name = simpledialog.askstring("Update Record", "Enter new Driver Name:", initialvalue=record_to_update["Driver Name"])
            new_color = simpledialog.askstring("Update Record", "Enter new Color:", initialvalue=record_to_update["Color"])
            new_plate_number = simpledialog.askstring("Update Record", "Enter new Plate Number:", initialvalue=record_to_update["Plate Number"])

            # Validate and update the record
            if new_driver_name and new_color and new_plate_number:
                # Update the record
                record_to_update["Driver Name"] = new_driver_name
                record_to_update["Color"] = new_color
                record_to_update["Plate Number"] = new_plate_number

                messagebox.showinfo("Success", f"Record at index {index_to_update} updated.")
                self.update_records_display()
            else:
                messagebox.showerror("Error", "All fields must be filled out.")
        else:
            messagebox.showerror("Error", "Invalid index.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleMonitoringApp(root)
    root.mainloop()
