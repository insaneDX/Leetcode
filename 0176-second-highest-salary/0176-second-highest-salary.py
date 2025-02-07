import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get the unique salaries in descending order
    unique_salaries = employee['salary'].unique()
    unique_salaries.sort()
    unique_salaries = unique_salaries[::-1]

    if len(unique_salaries) < 2:
        return pd.DataFrame({
            'SecondHighestSalary':[None]
        })

    second_highest = unique_salaries[1] # 0th index will be max

    return pd.DataFrame({
            'SecondHighestSalary':[second_highest]
        })