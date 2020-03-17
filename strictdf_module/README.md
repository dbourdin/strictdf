# StrictDataFrame
This is the source code of the `StrictDataFrame` module implementation.

In order to use the module, you'll need to build the python package and install
the dependency using `pip`.

##  Building redistributable package
In order to create the `.whl` wheel file, you'll need to run the setup.py:
```
$ python setup.py bdist_wheel
```
This will create a `dist` directory with the wheel file. You can now install
the dependency using this file.

## Install the package
You can now install the package using `pip install`:
```
$ pip install /path/to/project/dist/strictdf-0.0.1-py3-none-any.whl
```

After installing the dependency, you can now import and use our package.

## Using the package

First you need to create a new `StrictDataFrame`, using an existing
`pd.DataFrame`:
```python
import pandas as pd

from strictdf.StrictDataFrame import StrictDataFrame


df = pd.read_csv('some_csv_file.csv')
sdf = StrictDataFrame(df)
```

After initializing a `StrictDataFrame`, you now have a parsed DataFrame, and
can access the StrictDataFrame methods and properties.

If you need a report, you can easily get how many rows were deleted after
parsing the csv:
```python
sdf.report()
```

You can also access get the original DataFrame and the new DataFrame by
accessing the properties old_df (referencing the original) and new_df (the
parsed one):
```python
sdf.new_df
sdf.old_df
```

It's also possible to access a dtypes dict structure, holding the dtypes of all
the columns in the parsed DataFrame:
```python
sdf.dtypes
```
