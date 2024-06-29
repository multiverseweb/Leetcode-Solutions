import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.pivot(weather,values="temperature",index="month",columns="city")
    return df
