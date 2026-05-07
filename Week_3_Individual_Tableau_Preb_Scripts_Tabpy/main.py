import pandas as pd
def get_output_schema():
    return pd.DataFrame({
        'Employee_ID': prep_string(),
        'Employee_Name': prep_string(),
        'Department': prep_string(),
        'Age': prep_int(),
        'Salary': prep_decimal(),
        'Average_Salary_All_Employees': prep_decimal(),
        'Oldest_Employee_Name': prep_string(),
        'Oldest_Employee_Department': prep_string()
    })

def run_script(input_table):

    # Convert Age to integer
    input_table['Age'] = input_table['Age'].astype(int)

    # Filter only IT department employees
    it_employees = input_table[input_table['Department'] == 'IT'].copy()

    # Compute average salary
    avg_salary = input_table['Salary'].mean()

    # Find oldest employee
    oldest_employee = input_table.loc[input_table['Age'].idxmax()]

    # Add required columns
    it_employees['Average_Salary_All_Employees'] = avg_salary
    it_employees['Oldest_Employee_Name'] = oldest_employee['Employee_Name']
    it_employees['Oldest_Employee_Department'] = oldest_employee['Department']

    return it_employees