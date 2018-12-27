## This repo is for practise numpy and maintain the progress 
Reference https://docs.scipy.org/doc/numpy-1.15.0/user/quickstart.html
- NumPy’s main object is the homogeneous multidimensional array
- It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
- In NumPy dimensions are called axes
- For example, the coordinates of a point in 3D space [1, 2, 1] has one axis. That axis has 3 elements in it, so we say it has a length of 3. In the example pictured below, the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.
[[ 1., 0., 0.],
 [ 0., 1., 2.]]

- NumPy’s array class is called ndarray. It is also known by the alias array.
- The more important attributes of an ndarray object are:
  # ndarray.ndim
      the number of axes (dimensions) of the array.
  # ndarray.shape
      the total number of elements of the array. This is equal to the product of the elements of shape.
  # ndarray.dtype
      an object describing the type of the elements in the array, numpy.int32, numpy.int16, and numpy.float64 are some examples.
  # ndarray.itemsize
      the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.

## Array Creation
- Using array function, array function will take a single list of numbers as argument
- array transform sequence of sequence in to 2D arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.
- The type of the array can also be explicitly specified at creation time
- The function zeros((R,C)) creates an array full of zeros.
- The function ones creates an array full of ones.
- Function empty creates an array whose initial content is random and depends on the state of the memory. By default, the dtype of the created array is float64.
- To create sequences of numbers, NumPy provides a function(arange(d1,d2)) analogous to range that returns arrays instead of lists.
- When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. 
- For this reason, it is usually better to use the function linspace that receives as an argument the number of elements that we want, instead of the step

## Basic Operation 
- Substraction a-b
- Square a**b
- Conditional opearation 
- Element wise product a*b
- Matrx product a@b
- *= and += operation are used to modify the exting array
- Uniary Opearion sum are used to find out sum of all element in to the array 
- min() used to find out the minium 
- max()used to find out max
- Sum of each column and row
- min or max of each column and row 
- cumulative sum along each row 
- sin ,cos,exp and sqrt are the universal function 
- Indexing, Slicing and Iterating
	One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences
	Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas
	Iterating over multidimensional arrays is done with respect to the first axis
## Indexing,Slicing and Iterating
- One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences
- Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas
- When fewer indices are provided than the number of axes, the missing indices are considered complete slices
- The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is an array with 5 axes, then.
##                                                        
	x[1,2,...] is equivalent to x[1,2,:,:,:],
	x[...,3] to x[:,:,:,:,3] and
	x[4,...,5,:] to x[4,:,:,5,:].
## Shape manupulation(Changing the shape of an array)
- An array has a shape given by the number of elements along each axis:
- Some method change the exiting array some leave remain same
## Reference 2: From Python to Numpy:
### Memory Layout
	An instance of class ndarray consists of a contiguous 1-D segment of computer memmory,combined with an indexing
	Scheme that maps N integres in to the location of an item in the block.
### Strides:
	Strides are the number of bytes you need to step in each dimension when traversing the array.
### Calculating strides:
	If you want to move across one array in dimension 0, you need to move across three items. Each item has size 2 bytes.         So the stride in dimension 0 is 2 bytes x 3 items = 6 bytes.

	Similarly, if you want to move across one unit in dimension 1, you need to move across 1 item. So the stride in
	dimension 1 is 2 bytes x 1 item = 2 bytes. The stride in the last dimension is always equal to the itemsize

### veiws and Copies: 
- concepts for the optimization of your numerical computations.
### Direct and indirect access(Indexing v/s Fancy Indexing):
-  Direct Indexing always returns a 'view' while fancy(Indirect) indexing always returns a 'copy'.
- Modifying the 'view' modifies the base array while this is not true when in Indirect indexing.
### view Indexing
	An array that does not own its data, but refers to another array’s data instead. For example, we may create a view 
	that only shows every second element of another array:
	>>> x = np.arange(5)
	>>> x
	array([0, 1, 2, 3, 4])

	>>> y = x[::2]
	>>> y
	array([0, 2, 4])

	>>> x[0] = 3 # changing x changes y as well, since y is a view on x
	>>> y
	array([3, 2, 4])
### Advanced Indexing (Copy):
	Advanced indexing always returns a copy of the data (contrast with basic slicing that returns a view).
	>>> x = np.array([[1, 2], [3, 4], [5, 6]])
	>>> x[[0, 1, 2], [0, 1, 0]]
	array([1, 4, 5])

### Miscellaneous Floating Point Special Values
- Special values defined in numpy: nan, inf,
- np.nan allows for vectorized operations; its a float value, while None, by definition, forces object type, which basically   disables all efficiency in numpy.
- diag(v, k=0) Extract a diagonal or construct a diagonal array
- unravel_index -> Converts a flat index or array of flat indices into a tuple of coordinate arrays
- np.ubyte-> Base class for numpy scalar types
