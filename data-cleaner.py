import os
import pandas as pd
from PIL import Image
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
        self.column = None
        self.first_rows = None
        self.tree = None
        self.insights_text = None
        self.font = ctk.CTkFont(size = 18, weight= 'bold')
        self.welcome_text = "This is a simple data cleaning application. \nIt is capable of dealing with missing values, duplicates,\nand special characters(only in strings) in CSV files. \
                \n\n1. Select a file you want to modify.\n2. Select a column from dropdown \nand click 'Select Column' button.\n3. Choose an operation to perform and click Submit."
        # Load and Create Background Image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/images/bg_img_main.jpeg"),
                                     size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        
    # Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius = 0)
        self.main_frame.grid(row=0, column = 0, sticky='ns')
        
        # Welcome Part
        self.welcome_label = ctk.CTkLabel(self.main_frame, text="Welcome to Data Cleaner App!",
                                              font=self.font)
        self.welcome_label.grid(row = 0, column = 0, padx = 20, pady = (30, 0), columnspan = 2)     
        self.description_label = ctk.CTkLabel(self.main_frame, text=self.welcome_text)
        self.description_label.grid(row = 1, column = 0, padx = 20, pady = (10, 40), columnspan = 2)
        
        # File Selection Part 
        self.select_file_label = ctk.CTkLabel(self.main_frame, text="Select File to Open",
                                              font=self.font)
        self.select_file_label.grid(row = 2, column = 0, padx = 50, pady = 10, columnspan = 2)
        self.select_file_btn = ctk.CTkButton(self.main_frame, text="Select File", command=self.open_file)
        self.select_file_btn.grid(row = 3, column = 0, padx = 50, pady=10, columnspan = 2)
        self.filename_label = ctk.CTkLabel(self.main_frame, text="")
        self.filename_label.grid(row = 4, column = 0, padx = 50, pady=(0, 10), columnspan = 2)
        
        # Column Selection Part
        self.select_cols_label = ctk.CTkLabel(self.main_frame, text="Select a Column to Modify", font= self.font)
        self.select_cols_label.grid(row=5, column = 0, sticky='ns', padx=50, pady=10, columnspan = 2)
        self.column_selection = ctk.CTkComboBox(self.main_frame, values=[], state='readonly')
        self.column_selection.grid(row=6, column=0, padx=50, pady=10, columnspan = 2)
        self.select_cols_btn = ctk.CTkButton(self.main_frame, text="Select Column", command=self.selected_column_event)
        self.select_cols_btn.grid(row=7, column=0, padx=30, pady=10, columnspan = 2)
        self.select_cols_btn.configure(state="disabled")
        
    # Data Manipulation Frame
        self.clean_data_frame = ctk.CTkFrame(self, corner_radius=0)
        self.clean_data_frame.grid_columnconfigure(0, weight = 1)
        
        # Table with Samples
        self.tb_label = ctk.CTkLabel(self.clean_data_frame, text= "First 5 Samples", font=self.font)
        self.tb_label.grid(row = 0, column=0,  padx=30, pady= (75, 10))
        self.samples = ctk.CTkTextbox(self.clean_data_frame, width=250, height=230, state='disabled')
        self.samples.grid(row=1, column=2,  padx=30, pady = (0, 20))
        self.samples.configure(state='disabled')

        # Column Description
        self.tb_label = ctk.CTkLabel(self.clean_data_frame, text= "Column Description", font=self.font)
        self.tb_label.grid(row = 0, column=2,  padx=30, pady= (75, 10))
        self.insights = ctk.CTkTextbox(self.clean_data_frame, width=250, height=230, state='disabled')
        self.insights.grid(row=1, column=2,  padx=30, pady = (0, 20))
        self.insights.configure(state='disabled')
        
        # Cleaning Options
        # Initial values set
        self.nan_action, self.check_var1, self.check_var2 = ctk.StringVar(value='none'), ctk.StringVar(value='off'), ctk.StringVar(value='off')
        
        # Radio Buttons
        self.radio_delete_nan = ctk.CTkRadioButton(master=self.clean_data_frame, text="Delete NaN values", variable=self.nan_action, value='delete')
        self.radio_delete_nan.grid(row=2, column=0, padx=30, pady=10, sticky = 'w')   
        self.radio_fill_nan = ctk.CTkRadioButton(master=self.clean_data_frame, text="Fill NaN with 0", variable=self.nan_action, value='fill')
        self.radio_fill_nan.grid(row=3, column=0, padx=30, pady=10, sticky = 'w')
        
        # Checkbox buttons  
        self.checkbox_1 = ctk.CTkCheckBox(master=self.clean_data_frame, text="Remove duplicates", variable = self.check_var1, onvalue='on', offvalue='off')
        self.checkbox_1.grid(row=2, column=1, rowspan = 2, padx=10, pady=10, sticky = 'e')
        self.checkbox_2 = ctk.CTkCheckBox(master=self.clean_data_frame, text="Clean ?~()$#@!%&*; values", variable = self.check_var2, onvalue='on', offvalue='off')
        self.checkbox_2.grid(row=2, column=2, rowspan = 2, padx=10, pady=10)
        
        # Action buttons
        self.back_btn = ctk.CTkButton(self.clean_data_frame, text='Back', command = self.back_event, fg_color='#035E7B')
        self.back_btn.grid(row=4, column=0, padx=20, pady=10, sticky = 'w')
        self.submit_btn = ctk.CTkButton(self.clean_data_frame, text='Submit', command = self.clean_event, width=180, height=40)
        self.submit_btn.grid(row=4, column=1, padx=10, pady=10, sticky = '')
        self.clear_btn = ctk.CTkButton(self.clean_data_frame, text='Clear', command = self.clear_selection, fg_color='#EE6055')
        self.clear_btn.grid(row=4, column=2, padx=20, pady=10, sticky = 'e')
        
        
    # Open File Function                      
    def open_file(self):
        global df
        file = tk.filedialog.askopenfilename(
            title='Select a file',
            filetypes=(("CSV files", "*.csv"),)
        )
        if file:
            self.df = pd.read_csv(file)
            if len(self.df.columns) <= 1:
                self.df = pd.read_csv(file, sep=';')
            else: pass
            self.column_selection.configure(values=self.df.columns.tolist())
            self.select_cols_btn.configure(state="normal")
            self.original_filename = os.path.splitext(os.path.basename(file))[0]
            self.filename_label.configure(text=f"Selected file: {self.original_filename}")
            self.column_selection.set("")

   
    # Column Selection and Table Creation Function
    def selected_column_event(self):
        self.column = self.column_selection.get()
        if self.column == "":
            tk.messagebox.showinfo("Warning!", "Please choose a column!")
        else:
            self.main_frame.grid_forget()
            self.clean_data_frame.grid(row=0, column=0, sticky='ns')

            # Display selected column data in a table
            if self.tree:
                self.tree.destroy()
                
            self.tree = tk.ttk.Treeview(self.clean_data_frame, columns=('Value'), show='headings')
            self.tree.heading('Value', text=self.column)
            self.tree.grid(row=1, column=0,  padx=30, pady = (0, 20))
            for value in self.df[self.column].head(5):
                self.tree.insert('', tk.END, values=(value,))
        
            # Display some insights about the data
            insights_text = (f'{self.df[self.column].describe()} \n'
                            f'Number of values in the column: {self.df[self.column].count()} \n'
                            f'Null values in the column: {self.df[self.column].isnull().sum()} \n'
                            f'Data type: {self.df[self.column].dtype}')
            self.insights.configure(state='normal')
            self.insights.delete('1.0', tk.END)
            self.insights.insert(tk.END, insights_text)
            self.insights.configure(state='disabled')
        
            # Disable some functions based on data type
            if self.df[self.column].dtype != 'object':
                self.checkbox_2.configure(state='disabled')
            else: self.checkbox_2.configure(state='normal')


    # Data Cleaning Function
    def clean_event(self):
        if self.nan_action.get() == 'delete':
            self.df[self.column] = self.df[self.column].dropna()
            print('Cleaned successfully')
        elif self.nan_action.get() == 'fill':
            self.df[self.column] = self.df[self.column].fillna(value = 0)
            print('Filled Successfully')
        if self.check_var1.get() == 'on':
            self.df = self.df.drop_duplicates(subset=[self.column])
            print('Duplicates Removed')
        if self.check_var2.get() == 'on':
            self.df[self.column] = self.df[self.column].str.replace('[?~()$#@!%&*;]', '', regex=True)
            print("Special characters removed")
        if (self.nan_action.get() not in ['delete', 'fill']
            and self.check_var1.get() != 'on'
            and self.check_var2.get() != 'on'):
            tk.messagebox.showinfo("Warning!", "Select a cleaning operation and click Submit.")
        else:
            save_file = tk.messagebox.askyesno("Save File", "Do you want to download the cleaned data?")
            if save_file:
                self.save_cleaned_file()


    # Save Preprocessed File            
    def save_cleaned_file(self):
        save_path = tk.filedialog.asksaveasfilename(
            initialfile=self.original_filename + '_cleaned',
            defaultextension='.csv',
            filetypes=[("CSV files", "*.csv")],
            title="Save cleaned data"
        )
        if save_path:
            self.df.to_csv(save_path, index=False)
            tk.messagebox.showinfo("File Saved", "Cleaned data saved successfully!")
    

    # Clear Checkbox Selection Function 
    def clear_selection(self):
        self.checkbox_1.deselect()       
        self.checkbox_2.deselect()      
        self.radio_delete_nan.deselect()
        self.radio_fill_nan.deselect() 


    # Toggle Checkbox Selection Function
    def back_event(self):
        self.clean_data_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky='ns')
        self.clear_selection()

        
# Run App             
if __name__ == "__main__":
    app = App()
    app.mainloop()

