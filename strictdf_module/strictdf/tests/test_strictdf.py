import pandas as pd
import pytest

from strictdf.StrictDataFrame import StrictDataFrame


def test_old_df_is_original_df():
    df = pd.DataFrame.from_dict({'column_1': [1, 2]})
    sdf = StrictDataFrame(df)
    pd.testing.assert_frame_equal(df, sdf.old_df)


def test_new_df_is_created_with_valid_dict():
    df = pd.DataFrame.from_dict({'column_1': [1, 2]})
    sdf = StrictDataFrame(df)
    assert isinstance(sdf.new_df, pd.DataFrame)


def test_not_using_dataframe_raises_exception():
    with pytest.raises(TypeError):
        StrictDataFrame('Not a pd.DataFrame')


def test_parse_str_values_from_mixed_str_column():
    str_values = ['string_1', 'string_2', 'string_3']
    non_str_values = [5, 6]
    df = pd.DataFrame.from_dict({'mixed_column': str_values + non_str_values})

    sdf = StrictDataFrame(df)
    assert all([isinstance(value, str) for value in sdf.new_df.mixed_column])

    assert all([any(value == sdf.new_df.mixed_column) for value in str_values])


def test_non_str_are_removed_from_mixed_str_column():
    str_values = ['string_1', 'string_2', 'string_3']
    non_str_values = [5, 6]
    df = pd.DataFrame.from_dict({'mixed_column': str_values + non_str_values})

    sdf = StrictDataFrame(df)
    assert not any([value in sdf.new_df.mixed_column
                    for value in non_str_values])


def test_parse_int_values_from_mixed_int_column():
    int_values = ['1', '2', '3']
    non_int_values = ['string_1', 'string_2']
    df = pd.DataFrame.from_dict({'mixed_column': int_values + non_int_values})

    sdf = StrictDataFrame(df)
    assert all([isinstance(value, int) for value in sdf.new_df.mixed_column])

    assert all([any(int(value) == sdf.new_df.mixed_column)
                for value in int_values])


def test_non_int_are_removed_from_mixed_int_column():
    int_values = ['1', '2', '3']
    non_int_values = ['string_1', 'string_2']
    df = pd.DataFrame.from_dict({'mixed_column': int_values + non_int_values})

    sdf = StrictDataFrame(df)
    assert not any([value in sdf.new_df.mixed_column
                    for value in non_int_values])


def test_parse_float_values_from_mixed_float_column():
    float_values = ['1.5', '2.5', '3.5']
    non_int_values = ['string_1', 'string_2']
    df = pd.DataFrame.from_dict(
        {'mixed_column': float_values + non_int_values}
    )

    sdf = StrictDataFrame(df)
    assert all([isinstance(value, float) for value in sdf.new_df.mixed_column])

    assert all([any(float(value) == sdf.new_df.mixed_column)
                for value in float_values])


def test_non_float_are_removed_from_mixed_float_column():
    float_values = ['1.5', '2.5', '3.5']
    non_int_values = ['string_1', 'string_2']
    df = pd.DataFrame.from_dict(
        {'mixed_column': float_values + non_int_values}
    )

    sdf = StrictDataFrame(df)
    assert not any([value in sdf.new_df.mixed_column
                    for value in non_int_values])


def test_parse_bool_values_from_mixed_bool_column():
    bool_values = ['true', 'True', 'False']
    non_bool_values = ['string_1', 'string_2']
    df = pd.DataFrame.from_dict(
        {'mixed_column': bool_values + non_bool_values}
    )

    sdf = StrictDataFrame(df)
    assert all([value.dtype == bool for value in sdf.new_df.mixed_column])


def test_all_parsed_bool_values_from_mixed_bool_column_are_bool():
    bool_values = [True, True, False]
    non_bool_values = ['string_1', 'string_2']
    df = pd.DataFrame.from_dict(
        {'mixed_column': bool_values + non_bool_values}
    )

    sdf = StrictDataFrame(df)
    assert all([any(value == sdf.new_df.mixed_column)
                for value in bool_values])


def test_non_bool_are_removed_from_mixed_bool_column():
    bool_values = ['true', 'True', 'False', 'false']
    non_bool_values = ['string_1', 'string_2']
    df = pd.DataFrame.from_dict(
        {'mixed_column': bool_values + non_bool_values}
    )

    sdf = StrictDataFrame(df)
    assert not any([value in sdf.new_df.mixed_column
                    for value in non_bool_values])


def test_bool_are_parsed_from_int_bool_column():
    int_bool_values = [1, 0, 0, True]
    df = pd.DataFrame.from_dict({'bool_column': int_bool_values})
    sdf = StrictDataFrame(df)
    assert all([isinstance(value, bool) for value in sdf.new_df.bool_column])


def test_bool_values_are_parsed_correctly_from_strings():
    correct_values = [True, True, False, False]
    bool_values = ['true', 'True', 'False', 'false']
    df = pd.DataFrame.from_dict({'bool_column': bool_values})

    sdf = StrictDataFrame(df)
    assert all([value == sdf.new_df.bool_column[index]
                for index, value in enumerate(correct_values)])


def test_bool_is_removed_if_is_not_int_bool_column():
    values = [1, 0, 0, 2, True]
    df = pd.DataFrame.from_dict({'int_column': values})
    sdf = StrictDataFrame(df)
    assert not any([isinstance(value, bool)
                    for value in sdf.new_df.int_column])


def test_report_is_displayed_properly(capsys):
    keep_values = [1, 2, 3]
    remove_values = ['remove', 'this']
    df = pd.DataFrame.from_dict({'column': keep_values + remove_values})
    sdf = StrictDataFrame(df)
    sdf.report()
    report_message = capsys.readouterr().out
    expected_report_message = (f'DataFrame having shape {sdf.new_df.shape}'
                               f' ({len(remove_values)} rows removed from '
                               f'original)\n')
    assert report_message == expected_report_message


def test_can_retrieve_dtypes_dict_from_strict_data_frame():
    values = [1, 0, 0, 2, True]
    df = pd.DataFrame.from_dict({'int_column': values})
    sdf = StrictDataFrame(df)

    dtypes_dict = sdf.dtypes
    assert isinstance(dtypes_dict, dict)


def test_dtypes_are_generated_correctly_for_each_column():
    int_column = [5, 8, 2, 2, True]
    str_column = ['string_1', 'string_2', 5, 'string_3', 'string_4']
    float_column = [1.5, 2.5, 3.5, False, 4.5]
    bool_column = ['true', 'True', 'False', 'false', 'not_a_bool']

    df = pd.DataFrame.from_dict({'int_column': int_column,
                                 'str_column': str_column,
                                 'float_column': float_column,
                                 'bool_column': bool_column})
    sdf = StrictDataFrame(df)

    dtypes_dict = sdf.dtypes
    assert dtypes_dict['int_column'] == 'int64'
    assert dtypes_dict['str_column'] == 'str'
    assert dtypes_dict['float_column'] == 'float64'
    assert dtypes_dict['bool_column'] == 'bool'
