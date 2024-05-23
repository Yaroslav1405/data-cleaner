import os
import pandas as pd
import numpy as np
import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('green')
class App(ctk.CTk):
    width = 900
    height = 600
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Data Cleaner')
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)


        self.df = None
        self.selected_column = None
        self.first_rows = None

        # Create Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius = 0)
        self.main_frame.grid(row=0, column = 0, sticky='ns')
@@ -27,10 +30,36 @@ def __init__(self, *args, **kwargs):
        self.select_file_label.grid(row = 0, column = 0, padx = 30, pady = (150,15))
        self.select_file_btn = ctk.CTkButton(self.main_frame, text="Select File", command=self.open_file)
        self.select_file_btn.grid(row = 1, column = 0, padx = 30, pady=(15,15))
        # Create Data Manipulation frame





        # Create Column Selection Frame
        self.select_cols_frame = ctk.CTkFrame(self, corner_radius = 0)
        self.select_cols_frame.grid_columnconfigure(0, weight=1)
        self.select_cols_label = ctk.CTkLabel(self.select_cols_frame, text="Select a column to modify")
        self.select_cols_label.grid(row=1, column = 0, sticky='ns', pady=10, padx=100)
        self.column_selection = ctk.CTkComboBox(self.select_cols_frame, values=[], state='readonly')
        self.column_selection.grid(row=2, column=0, padx=100, pady=10)
        self.select_cols_btn = ctk.CTkButton(self.select_cols_frame, text="Select Column", command=self.selected_column_event)
        self.select_cols_btn.grid(row=3, column=0, padx=30, pady=(15,15))
        self.select_cols_btn.configure(state="disabled")
        self.back_button = ctk.CTkButton(self.select_cols_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=4, column=0, padx=30, pady=(15,15))

        # Create Data Manipulation Frame
        self.clean_data_frame = ctk.CTkFrame(self, corner_radius=0)
        self.clean_data_frame.grid_columnconfigure(0, weight=1)
        self.clean_data_label = ctk.CTkLabel(self.clean_data_frame, text="Clean Data in Column")
        self.clean_data_label.grid(row=0, column=0, pady=10, padx=100)
        self.first_rows_label = ctk.CTkLabel(self.clean_data_frame, text=self.first_rows)
        self.first_rows_label.grid(row=1, column=2)
        self.clean_data_btn = ctk.CTkButton(self.clean_data_frame, text="Clean Data", command=self.clean_data)
        self.clean_data_btn.grid(row=2, column=0, padx=100, pady=10)
        self.back_button_clean = ctk.CTkButton(self.clean_data_frame, text="Back", command=self.back_to_select_cols, width=200)
        self.back_button_clean.grid(row=3, column=0, padx=30, pady=(15, 15))

        self.tree = None

    def open_file(self):
        global df
@@ -39,39 +68,57 @@ def open_file(self):
            filetypes=(("CSV files", "*.csv"),)
        )
        if file:
            df = pd.read_csv(file)
            self.select_file_label.configure(text=f'Selected directory {file}')
           # self.select_cols_btn.config(state="normal")
            #select_cols()
            self.df = pd.read_csv(file)
            self.column_selection.configure(values=self.df.columns.tolist())
            self.select_cols_btn.configure(state="normal")
            self.next_event()

    def next_event(self):
        self.main_frame.grid_forget() # remove main frame
        self.select_cols_frame.grid(row=0, column=0, sticky='nsew', padx=100)
        self.select_cols_frame.grid(row=0, column=0, sticky='nsew', padx=300, pady=200)



    def back_event(self):
        self.select_cols_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky='ns')

    # def select_cols(self):
    #     # Destroy the current frame
    #     for widget in app.winfo_children():
    #         widget.destroy()

    def selected_column_event(self):
        self.column = self.column_selection.get()

        # print("Column selected: ", self.column)
        # self.first_rows = self.df[f'{self.column}'].head(5)
        # print(self.first_rows)    
        self.select_cols_frame.grid_forget()
        self.clean_data_frame.grid(row=0, column=0, sticky='nsew')
        if self.column:
            self.clean_data_frame_event()

    #     # Create a new frame with desired content
    #     new_frame = ctk.CTkFrame(app)
    #     new_frame.pack(pady=10)
    #     label = ctk.CTkLabel(new_frame, text="Select a column to modify")
    #     label.pack(pady=20)
    #     if 'df' in globals():
    #         column_options = df.columns.tolist()
    #         column_selection = ctk.CTkComboBox(new_frame, values=column_options, state='readonly')
    #         column_selection.pack(pady=10)
    #         select_cols_btn.configure(state="disabled")
    #     else:
    #         tk.messagebox.showinfo("Info", "Please select a CSV file first.")
    #     select_cols_btn = ctk.CTkButton(new_frame, text="Select Column", command=self.select_cols)
    #     select_cols_btn.pack(pady=10)

    def clean_data_frame_event(self):
        self.select_cols_frame.grid_forget()
        self.clean_data_frame.grid(row=0, column=0, sticky='nsew', padx=150, pady=100)

        # Display selected column data in a table
        if self.tree:
            self.tree.destroy()

        self.tree = tk.ttk.Treeview(self.clean_data_frame, columns=('Value'), show='headings')
        self.tree.heading('Value', text=self.column)
        self.tree.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

        for value in self.df[self.column].head(5):
            self.tree.insert('', tk.END, values=(value,))

    def back_to_select_cols(self):
        self.clean_data_frame.grid_forget()
        self.select_cols_frame.grid(row=0, column=0, sticky='nsew')

    def clean_data(self):
        # Implement data cleaning logic here
        pass    

if __name__ == "__main__":
    app = App()
    app.mainloop()