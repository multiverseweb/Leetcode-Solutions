import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    size=players.shape
    return [size[0],size[1]]
