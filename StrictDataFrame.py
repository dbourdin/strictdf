import pandas as pd


class StrictDataFrame:
    """
    StrictDataFrame class is used to generate a clean DataFrame that respects
    strict types on it's columns.
    """
    def __init__(self, df):
        """
        This is the init method for the StaticDataFrame. This will return a new
        StaticDataFrame object, containing the old DataFrame and a new
        DataFrame with parsed columns
        :param df: pd.DataFrame
            DataFrame that needs to be parsed
        :return: StrictDataFrame
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'Expected DataFrame, got {type(df)} instead')
        self.old_df = df.copy()
        self.new_df = None
