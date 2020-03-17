# Welcome to StrictDataFrame Documentation


## First steps

To begin our fist steps with the `StrictDataFrame` we need to import the module
and create a new `StrictDataFrame`
```python
import pandas as pd

from strictdf.StrictDataFrame import StrictDataFrame


df = pd.read_csv('some_csv_file.csv')
sdf = StrictDataFrame(df)
```


## StrictDataFrame API

Now that we have learnt how to create a new `StrictDataFrame`, we can start
digging into the `StrictDataFrame` API

### Accessing the original DataFrame
The original DataFrame can be accessed through the `old_df` property:
```python
original_df = sdf.old_df
```

### Accessing the parsed DataFrame
The parsed DataFrame can be accessed through the `new_df` property:
```python
original_df = sdf.new_df
```

### Displaying a report of the StrictDataFrane
The StrictDataFrame offers a `report()` method that will print a summary
indicating the size of the parsed DataFrame, and the number of removed rows:
```python
sdf.old_df.report()

# DataFrame having shape (120264, 11) (29736 rows removed from original)
```

### Getting a dict of dtypes of the StrictDataFrame
The StrictDataFrame has a `dtypes` property that can be used to retrieve a dict
containing the dtypes of all the columns within the parsed DataFrame:
```python
sdf.dtypes

# {'serious_dlqin2yrs': 'int64',
#  'revolving_utilization_of_unsecured_lines': 'float64',
#  'age': 'float64',
#  'number_of_time30-59_days_past_due_not_worse': 'int64',
#  'debt_ratio': 'float64',
#  'monthly_income': 'float64',
#  'number_of_open_credit_lines_and_loans': 'int64',
#  'number_of_times90_days_late': 'int64',
#  'number_real_estate_loans_or_lines': 'int64',
#  'number_of_time60-89_days_past_due_not_worse': 'int64',
#  'number_of_dependents': 'int64'}
```

## Owner
[@dbourdin](https://github.com/dbourdin)