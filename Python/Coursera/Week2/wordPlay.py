# this is the program for creating your own custome class 
# 1. In Python str is a class having method instead of functions
# 2. Class method should have at leat one Parameter and first parameter should be of type class
# 3. Or First argument of method of a class is always an instance of the class
# Let's create a new class

class WordplayStr(str):
    # This class created from str class so it inherit all the properties of str and extra method which we will right in to this
    def same_start_and_end(self):
        """word_play->bool
        precondition: len(self)!=0
        Return whether self starts and ends with the same letter.
        """

        return self[0]==self[-1]


