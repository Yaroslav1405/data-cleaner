port os
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


        # Create Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius = 0)
        self.main_frame.grid(row=0, column = 0, sticky='ns')
        self.select_file_label = ctk.CTkLabel(self.main_frame, text="Select File to open",
                                              font=ctk.CTkFont(size = 18, weight= 'bold'))
        self.select_file_label.grid(row = 0, column = 0, padx = 30, pady = (150,15))
        self.select_file_btn = ctk.CTkButton(self.main_frame, text="Select File", command=self.open_file)
        self.select_file_btn.grid(row = 1, column = 0, padx = 30, pady=(15,15))
        # Create Data Manipulation frame




    def open_file(self):
        global df
        file = tk.filedialog.askopenfilename(
            title='Select a file',
            filetypes=(("CSV files", "*.csv"),)
        )
        if file:
            df = pd.read_csv(file)
            self.select_file_label.configure(text=f'Selected directory {file}')
           # self.select_cols_btn.config(state="normal")
            #select_cols()

    def next_event(self):
        self.main_frame.grid_forget() # remove main frame
        self.select_cols_frame.grid(row=0, column=0, sticky='nsew', padx=100)

    def back_event(self):
        self.select_cols_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky='ns')

    # def select_cols(self):
    #     # Destroy the current frame
    #     for widget in app.winfo_children():
    #         widget.destroy()

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

if __name__ == "__main__":
    app = App()
    app.mainloop()