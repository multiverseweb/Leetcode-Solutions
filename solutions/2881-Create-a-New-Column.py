import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.insert(2, "bonus", [2*i for i in employees['salary']], True)
    return employees
