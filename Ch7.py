'''
Ch7 - Common Python Libraries, Part 1

Numpy
    - python library for working with large, multi-dimensional arrays and matrices
    - need to import numpy to work with it

Creating arrays
    - different ways to create different arrays ( remember only first 3 maybe )
    - np.array(): from lists/tuples
    - np.zeros(): array of zeros
    - np.ones(): array of ones
    - np.full(): array with a specific value
    - np.eye(): identity matrix
    - np.random.rand(): array with random values
'''

import numpy as np 
arr = np.array([1, 2, 3])  # 1D array
matrix = np.array([[1, 2], [3, 4]])  # 2D array
zeros = np.zeros((2, 3))  # 2x3 array of zeros

print(arr) # output: [1 2 3]
print(matrix)   # output: [[1 2] 
                #           [3 4]]
print(zeros) # output: [[0. 0. 0.]
                    #   [0. 0. 0.]]

'''
Array Dimensions
    - 0D: scalar → np.array(5)
    - 1D: vector → np.array([1, 2, 3])
    - 2D: matrix → np.array([[1,2],[3,4]])
    - 3D: tensor → np.array([[[1],[2]],[[3],[4]]])

    - notice how for 0D, there are 0 square brackets, 1D has 1 outer square bracker, 2D has 1 outer with other inner brackets and 3D has 2 outer with other inner brackets 
'''                
third_dimension = np.array([[[1],[2]],[[3],[4]]])
print(third_dimension.ndim) # output: 3 i.e. number of dimensions
print(third_dimension)

'''
Data Types
    - numpy array has a single data type for all elements
    - you can set it manually, or let numpy do it for you automatically

    - int32, int64 = integer values
    - float32, float64 = decimal values
    - bool = boolean values
    - str_, unicode_ = string/text
    - complex64 = complex values

    - we can check the data type using arr.dtype
'''
import numpy as np

arr = np.array([1, 2, 3], dtype='float64')
print(arr.dtype)  # float64

# Type conversion can also be done by assigning a data type manually. We can do this using .astype() method
arr = np.array([1.1, 2.2, 3.3])
new_arr = arr.astype('int32')  # converts to integers
print(new_arr)  # [1 2 3]


'''
Array Attributes
    - useful properties of numpy arrays:
        - arr.shape: dimensions
        - arr.size: total number of elements
        - arr.ndim: number of dimensions
        - arr.dtype: data type
        - arr.itemsize: bytes per element
        - arr.nbytes: total bytes consumed
'''

arr = np.array([[1, 2], [3, 4]])
print(arr.shape, arr.ndim, arr.size)  # Output: (2, 2), 2, 4


'''
Indexing and Slicing
    - just like what we discussed in previous chapters, in strings and lists...
    - indexing and slicing are ways to access elements
'''
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1, 2])     # Output: 6
print(arr[:, 1:])    # all rows, columns from 1 onwards i.e. [2,3], [5,6]

'''
Array Copy and View
    - copy creates a new array, which looks like the old array, but is in fact totally independent and new
    - view really copies the old array, any changes in new array will also change the old array
'''

original = np.array([1, 2, 3])
view = original.view()
copy = original.copy()
view[0] = 100
print(original)  # Output: [100, 2, 3]

'''
Creating arrays from a numerical range
    - we can create an array within a numerical range by using .arange() or .linspace() functions
    
    - np.arange()
        - works similar to range(), but returns a numpy array
        - np.arange(start, stop, step)
        - eg: np.arange(1,20,2) will create an array: [1 3 5 7 9]
    
    - np.linspace()
        - generates evenly spaced values between start and stop
        - np.linspace(start, stop, no_of_values)
        - eg: np.linspace(0,8,5) will create an array: [0 2 4 6 8] i.e. 5 values evenly spaced where start is 0 and stops at 8
'''


'''
Array Broadcasting
    - lets numpy perform operations on array of different shapes by automatically expanding one of them to match the other
'''
# Example 1
a = np.array([1, 2, 3])
print(a + 5)  # [6 7 8]
# here, a has 3 values, but it is being added to a single value. So broadcasting happens automatically and 5 is stretched 3 times. Which means that behind the scenes, [1,2,3] is being added to [5,5,5] instead of just 5


# Example 2
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])

# b is broadcasted to match each row of a
print(a + b)
# Output:
# [[11 22 33]
#  [14 25 36]]

'''
Broadcasting is useful in scaling datasets and vectorizing loops
'''


'''
Iterating Over Arrays
    - using loops to print all the values of the numpy array
'''
# example 1
arr = np.array([1, 2, 3, 4])
for x in arr:
    print(x) # output: 1 2 3 4

# example 2, iterating when there is multidimensional array, we use .nditer() method
arr = np.array([[1, 2], [3, 4]])
for x in np.nditer(arr):
    print(x)    # output: 1 2 3 4


'''
Sorting and Searching
    - sorting can be done using .sort() method which works on 1D and 2D arrays
    - searching can be done using .where(), which returns indices where condition is True
'''
# example for sorting
arr = np.array([3, 1, 2])
print(np.sort(arr))  # [1 2 3]

# example for sorting 2D array
arr = np.array([[3, 1], [2, 4]])
print(np.sort(arr, axis=1))  # Sorts each row: [[1 3], [2 4]]

# example for searching
arr = np.array([10, 20, 30, 40])
print(np.where(arr > 25))  # (array([2, 3]),)


'''
Statistical Functions
| Function      | Purpose                     | Example                    |
| ------------- | --------------------------- | -------------------------- |
| `np.mean()`   | Average                     | `np.mean([1,2,3]) → 2.0`   |
| `np.median()` | Middle value                | `np.median([1,3,2]) → 2.0` |
| `np.std()`    | Standard deviation (spread) | `np.std([1,2,3])`          |
| `np.var()`    | Variance                    | `np.var([1,2,3])`          |
| `np.sum()`    | Total sum of elements       | `np.sum([1,2,3]) → 6`      |
| `np.min()`    | Minimum                     | `np.min([1,2,3]) → 1`      |
| `np.max()`    | Maximum                     | `np.max([1,2,3]) → 3`      |


Numpy Finished!!!
'''


'''
Pandas
    - python library used for data analysis and manipulation

Series and DataFrames
    - series is a 1D labeled array
    - like a single column of data with labels
'''
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

'''
Output:
a    10
b    20
c    30
dtype: int64

    - Think of series as numpy array with names


    - data frames are like an excel sheet or SQL table
    - made of multiple series
    - each column can be a different type
'''

data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
}
df = pd.DataFrame(data)
print(df)

'''
Output:

    Name  Age
0  Alice   25
1    Bob   30


Key difference between Series and DataFrames
| Feature        | Series            | DataFrame                 |
| -------------- | ----------------- | ------------------------- |
| Dimensions     | 1D                | 2D                        |
| Looks like     | Column            | Table                     |
| Data structure | `pd.Series(data)` | `pd.DataFrame(data_dict)` |
| Indexing       | Single index      | Row + Column indexing     |




The head and tail functions
    - head returns the first 'n' rows 
    - default n = 5

    syntax:
    df.head() - returns 5 rows
    df.head(3) - returns first 3 rows


    - tail returns the last 'n' rows
    - default n = 5

    syntax:
    df.tail() - last 5 rows
    df.tail(2) - last 2 rows
''' 
import pandas as pd

df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Age': [21, 22, 23, 24, 25, 26]
})

print(df.head(2))  # Top 2 rows
print(df.tail(2))  # Bottom 2 rows


'''
Attributes

| Attribute  | Description                            | Example               |
| ---------- | -------------------------------------- | --------------------- |
| `.shape`   | Rows & columns as tuple `(rows, cols)` | `df.shape` → `(5, 3)` |
| `.columns` | Column names                           | `df.columns`          |
| `.index`   | Row labels (index)                     | `df.index`            |
| `.dtypes`  | Data types of each column              | `df.dtypes`           |
| `.ndim`    | Number of dimensions (1 or 2)          | `df.ndim` → `2`       |
| `.size`    | Total number of elements (rows × cols) | `df.size`             |
| `.values`  | Numpy array of data                    | `df.values`           |

'''
import pandas as pd

df = pd.DataFrame({'Name': ['A', 'B'], 'Age': [21, 22]})

print(df.shape)     # (2, 2)
print(df.columns)   # Index(['Name', 'Age'], dtype='object')
print(df.dtypes)    # Name: object, Age: int64


'''
Working with Missing Data
    - missing values are normally represented as NaN (not a number)

    - Detecting missing data
        | Function    | Purpose                     | Example        |
        | ----------- | --------------------------- | -------------- |
        | `isnull()`  | True where value is NaN     | `df.isnull()`  |
        | `notnull()` | True where value is NOT NaN | `df.notnull()` |

    - Removing missing data
        df.dropna()      # Drops rows with ANY NaN
        df.dropna(axis=1)  # Drops columns with ANY NaN

    - Filling missing data
        df.fillna(0)              # Replace NaN with 0
        df.fillna(method='ffill') # Forward fill (from above)
        df.fillna(method='bfill') # Backward fill (from below)

    - Check for missing data
        df.isnull().sum()   # Count NaNs per column
        df.isnull().any()   # True if any NaNs
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['A', 'B', None],
    'Age': [21, np.nan, 23]
})

print(df.isnull())     # Shows True for missing
print(df.dropna())     # Drops row with missing
print(df.fillna('X'))  # Replaces NaNs with 'X'


'''
Mergind dataframes
    - use the .join() method
    - use the .concat attribute
'''
# using join
df1 = df1.set_index('ID')
df2 = df2.set_index('ID')

joined = df1.join(df2)

# using concat
# Vertical (row-wise)
pd.concat([df1, df2], axis=0)

# Horizontal (column-wise)
pd.concat([df1, df2], axis=1)


'''
Working with CSV files
    - csv means comma-separated-values
    - when we open csv file, it opens mostly in excel
    - eg: rhythm, 21, male
    - Reading a csv file:
'''
import pandas as pd

df = pd.read_csv('data.csv')

'''
    - writing to a csv file
'''
df.to_csv('output.csv', index=False)

'''
Pandas Finished!!!
'''
