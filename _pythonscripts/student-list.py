import pandas as pd
#import ace_tools as tools  # Assuming ace_tools is used for displaying results

# Load student data from Excel file
file_path = "students.xlsx"  # Ensure the file is in the same directory or provide full path
df_students = pd.read_excel(file_path)

# Convert DataFrame to list of dictionaries (students array)
students_list = df_students.to_dict(orient="records")

# Display extracted student data
#tools.display_dataframe_to_user(name="Student Data from Excel", dataframe=df_students)

# Example print to verify structure
print(students_list)
