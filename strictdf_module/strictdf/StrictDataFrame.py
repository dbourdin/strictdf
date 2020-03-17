from collections import Counter

import pandas as pd

from strictdf.utils.parsing_utils import is_bool
from strictdf.utils.parsing_utils import is_float
from strictdf.utils.parsing_utils import is_int_boolean_column
from strictdf.utils.parsing_utils import is_integer
from strictdf.utils.parsing_utils import str_to_bool


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
        self._old_df = df.copy()
        self._create_strict_data_frame(self._old_df)

    @property
    def dtypes(self):
        return self._dtypes

    @property
    def new_df(self):
        return self._new_df

    @property
    def old_df(self):
        return self._old_df

    def _create_strict_data_frame(self, df):
        """
        This will create the new_df by correcting the column dtypes of the
        specified DataFrame.
        :param df: pd.DataFrame
        The original DataFrame to be parsed
        :return: None
        """
        self._dtypes = {column: df.dtypes[column].__str__()
                        for column in df.columns}
        self._new_df = df.dropna()
        self._parse_columns(self._new_df)

    @staticmethod
    def _get_columns_to_parse(df):
        """
        This will return a list of all columns that require parsing.
        Columns with dtype object will require parsing
        :param df: pd.DataFrame
            The pandas DataFrame to extract unparsed columns from
        :return: list
            List containing the name of all columns to be parsed
        """
        return [column for column in df.columns
                if df[column].dtype == 'object']

    def _infer_column_type(self, df_column):
        """
        This method will infer a column type based on the number of occurrences
        of each type on that column.
        :param df_column: pd.Series
            The column whose type will be inferred.
        :return: String, pd.Series
            String with the inferred data type, and pd.Series column
            with the parsed values.
        """
        type_counts = Counter()
        df_column_copy = df_column.copy()
        for index, value in enumerate(df_column_copy):
            parsed_value = self._infer_value_type(value)
            df_column_copy.iloc[index] = parsed_value

            type_counts[type(parsed_value).__name__] += 1

        if not type_counts:
            return

        # Corner case where 2 or more types have the same occurrence.
        if (len(type_counts) > 1 and type_counts.most_common()[0][1]
                == type_counts.most_common()[1][1]):
            print(f'The two most common types '
                  f'({type_counts.most_common()[0][0]} '
                  f'{type_counts.most_common()[1][0]}) '
                  f'have the same amount of occurrences on column '
                  f'{df_column.name}')

        return type_counts.most_common()[0][0], df_column_copy

    @staticmethod
    def _infer_value_type(value):
        """
        This method will receive a value, decide if it's a bool, int or float,
        and return the parsed value.
        :param value: object
            Any type can be received here, and this will be used to evaluate if
            the value is a bool, an int or a float.
        :return: int/float/bool/object
            It will return a value with the parsed type if it's int, float or
            bool, or the same one it had if no type can be inferred.
        """
        if is_bool(value):
            return str_to_bool(value)
        if type(value) == bool and value in (True, False):
            return bool(value)

        if is_float(value):
            value = float(value)
        if is_integer(value):
            value = int(value)
        return value

    def _parse_columns(self, df):
        """
        This will iterate through all the columns that require parsing, infer
        the data type for that column, and only save elements of that type.
        :param df: pd.DataFrame
            The pandas DataFrame that requires columns to be parsed into
            correct dtype.
        :return: None
        """
        columns_to_parse = self._get_columns_to_parse(df)
        for column in columns_to_parse:
            column_type, parsed_column = self._infer_column_type(df[column])

            new_column = pd.Series(pd.array(
                [value if type(value).__name__ == column_type
                 else None for value in parsed_column]),
                index=parsed_column.index
            )

            df[column] = new_column
            df = df.dropna()

            if column_type in ('str', 'bool'):
                self._dtypes[column] = column_type
                continue

            if column_type == 'float':
                df[column] = df[column].astype('float64')

            if column_type == 'int':
                df[column] = df[column].astype('int64')
                # There could be a corner case where all the values are 1/0 and
                # this could be a bool column instead. Setting column as type
                # int64 before helps doing this comparison.
                if is_int_boolean_column(df[column]):
                    df[column] = df[column].astype('bool')
                    self._dtypes[column] = 'bool'
                    continue

            self._dtypes[column] = df[column].dtypes.__str__()

        self._new_df = df

    def report(self):
        """
        Will print the row difference between the old_df and the new_df
        generated after parsing the original DataFrame.
        :return: None
        """
        row_dif = self._old_df.shape[0] - self._new_df.shape[0]
        print(f'DataFrame having shape {self._new_df.shape} ({row_dif} rows '
              f'removed from original)')
