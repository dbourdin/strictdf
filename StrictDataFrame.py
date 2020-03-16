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

        self.dtypes = {column: df.dtypes[column].__str__()
                       for column in df.columns}
        self._create_strict_data_frame(df)

    def _create_strict_data_frame(self, df):
        """
        This will create the new_df by correcting the column dtypes of the
        specified DataFrame.
        :param df: pd.DataFrame
        The original DataFrame to be parsed
        :return: None
        """
        self.new_df = df.dropna()
        self._parse_columns(self.new_df)

    def _parse_columns(self, df):
        """
        This will iterate through all the columns that require parsing, infer
        the data type for that column, and only save elements of that type.
        :param df: pd.DataFrame
            The pandas DataFrame that requires columns to be parsed into
            correct dtype.
        :return: None
        """
