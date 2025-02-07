import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Sort the salaries in descending order and remove duplicates
    sorted_unique_salaries = employee['salary'].sort_values(
        ascending=False
    ).drop_duplicates()
    
    # Return the second highest salary or None if there isn't one
    second_highest_salary = None if sorted_unique_salaries.size < 2 else sorted_unique_salaries.iloc[1]
    
    return pd.DataFrame({
        'SecondHighestSalary': [second_highest_salary]
    })

# # Write your MySQL query statement below
# SELECT max(salary) AS SecondHighestSalary 
# FROM employee 
# WHERE salary < (
#     SELECT max(salary) FROM employee
#     )
