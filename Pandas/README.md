
#### My Way to Procced for Pandas

#### Reference 1: https://towardsdatascience.com/quick-dive-into-pandas-for-data-science-cc1c1a80d9c4
#### Reference 2: https://www.datacamp.com/courses/pandas-foundations
#### Reference 3: https://assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf
#### Reference 4: https://media.readthedocs.org/pdf/pandasguide/latest/pandasguide.pdf

#### Pandas Data Structures:
- Series:
	A series is a 1-D array which is very similiar to a Numpy Array, 
	Sereis are built on the top of NumPy array objects,Series can have 
	Access level with which it can be indexed
    WhenEver Series are created from dictionary pandas set keys as the index.
    panadas series can hold a variety of object type instead of Numpy
    
#### Grabbing information from Series.

- To grabing the information from series is same as we grab info from dictionary in Python.

#### Performing Arithmetic operations on Series.
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
- 
### Selecting Rows in a DataFrame:
- To select rows, we have to call the location of the rows using .loc[], which takes in the label name or .iloc[].
- which takes in the label name or .iloc[] which takes in the index position of the row.
#### Conditional Selection:
- Pandas allows you to perform conditional selection using bracket notation [].
#### Multi-level index (MultiIndex) and Index Hierarchy.
- A MultiIndex is simply an array of tuples where each tuple is unique. It can be created from a list of arrays (using MultiIndex.from_arrays), 
  an array of tuples (using MultiIndex.from_tuples), or a crossed set of iterables (using MultiIndex.from_product).

#### Missing Data:
- Pandas can find row/column with missing data(NaN) and drop that (by Default) row or column(axis=1)
- It can also fill the data wherever It will find NaN
## Groupby:
- groupby allows group together rows based of a column, So that you can perform aggregate function(sum,mean,mode,sd)
#### count(): It count the frequency 
#### describe()-> To get the overview of what a DF looks like
#### Pandas also concatenate the DF
#### merge():-> merge the DF.
#### join()
### The apply() method:
- It used to call custome function on data frame
- function broadcasted on each element 
- we can also apply built-in function to df
### Data I/O :
- Pandas used to read/write the files:(csv,excel,html or sql)
##### For reading from html we need to install some libs like below
	conda install lxml
	conda install html5lib
	conda install BeautifulSoup4



   
