# Data Cleaner
## Introduction 
In today's data-driven world, we are surrounded by information, some of which is preprocessed while much of it is not. 
Most data that users encounter is unclean or, more professionally, not preprocessed. Professionals who often work with large datasets know techniques to clean and prepare the data efficiently —
developers would use only few lines of code, while manager will rely on excel to clean it. However, those unfamiliar with those techniques might have a hard time going through the web and finding optimal solution.
This project aims to bridge that gap. While it may not be a perfect solution, it provides an easy-to-use tool that delivers the desired output with just a few clicks.

## Functionality
Functionality includes: 
- Removing duplicates; Removing NaN values; 

- Filling NaN with 0; 

- Cleaning special characters such as %$?! and other.
## Installation and Running 
All the requirements are listed in the reuirements.txt file and can be installed by:
```
pip install -r /path/to/requirements.txt
```
To run the program: 
```
python data-cleaner.py
```
## Main Stages
This project was utilized using CustomTkinter and some Tkinter for Graphical User Interface, so the first step was a research on what functionality is available when using these libraries and what are limitations.
Next steps after research: 
- File Selection and Column Choice:
  - Utilizing file input handling mechanisms to allow users to upload and select CSV files. A frame was created for this page, along with some simple Pandas commands to upload and store the dataset.
  - When the dataset is loaded, only after, the user is able to select a column and submit his action. This was also done using the functionality of CustomTkinter, and basic pandas.
- Operation Selection:
  - Utilizing CustomTkinter and Pandas functionality, the project enables detailed presentation of column-specific information on a new page.
  - Implementing conditional logic and user interface components (such as checkboxes and radio buttons) to enable users to choose data cleaning operations.
  - Simple, but yet important buttons allow the user to clear the selection, go back to the previous page, or submit and process the data.
- Debugging:
  - Utilizing conditional logic, the project now supports parsing both comma-separated and semi-colon-separated datasets. 
  - Employing data type inference methods to detect whether columns contain numeric or string data, and based on that disable some options.  
  - Incorporating validation logic ensures that users cannot select empty columns.
  - Some other bug fixes. 
## Future work
While the program can assist users in achieving their desired results, enhancing user experience and expanding the program's functionality are crucial goals for future development.
Enhance user flexibility by allowing them to specify custom values for data-filling operations.
Implement an installer package and an application icon for easier accessibility to eliminate the need to run the tool through the command line.
Restructure the project architecture to adopt a multi-class-based approach. This aims to enhance modularity, code reusability, and maintainability, facilitating future updates and extensions.


<sub> Created by Yaroslav Hinda </sub>
