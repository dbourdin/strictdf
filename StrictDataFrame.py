import pandas as pd


class StrictDataFrame:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'Expected DataFrame, got {type(df)} instead')
        self.old_df = df.copy()
        self.new_df = None
