
## My Way to Procced for Pandas

### Reference 1: https://towardsdatascience.com/quick-dive-into-pandas-for-data-science-cc1c1a80d9c4
### Reference 2: https://www.datacamp.com/courses/pandas-foundations
### Reference 3: https://assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf
### Reference 4: https://media.readthedocs.org/pdf/pandasguide/latest/pandasguide.pdf

### Pandas Data Structures:
- Series:
	A series is a 1-D array which is very similiar to a Numpy Array, 
	Sereis are built on the top of NumPy array objects,Series can have 
	Access level with which it can be indexed
    WhenEver Series are created from dictionary pandas set keys as the index.
    panadas series can hold a variety of object type instead of Numpy
    
### Grabbing information from Series.

- To grabing the information from series is same as we grab info from dictionary in Python.

### Performing Arithmetic operations on Series.
- Operations on Series are done based off the index.
- When we use any of the mathematical operations such as -, +, /, *, pandas does the computation using the value of the index.
- The resulting value is thereafter converted to a float so that you do not loose any information
### DataFrames:
- A DataFrame is a two-dimensional data structure in which the data is aligned in a tabular form i.e. in rows and columns.
- Pandas DataFrames make manipulating your data easy.
- You can select, replace columns and rows and even reshape your data.

#### Creating DataFrame from a dictionary Of Series.
#### Creating DataFrame from a dictionary Of list.
#### Selecting Columns from DataFrames
- Using bracket notation [], we can easily grab objects from a DataFrame.
#### Removing rows/columns from a DataFrame:
- We can remove a row or a column using the .drop() function.
- we have to specify the axis=0 for row, and axis=1 for column.
### Selecting Rows in a DataFrame:
- To select rows, we have to call the location of the rows using .loc[], which takes in the label name or .iloc[].
- which takes in the label name or .iloc[] which takes in the index position of the row.
### Conditional selection: 



   