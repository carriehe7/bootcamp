# 1. Create a ‘technological_terms’ tuple that will contain the following items:
# a. python
# b. pycharm IDE
# c. tuple
# d. collections
# e. string
technological_terms = ('python', 'pycharm IDE', 'tuple', 'collections', 'string')
print('technological terms tuple collection : ' +str(technological_terms))

# 2. Print the following sentence using cell extraction to the needed cells:
# “We are ninja developers. We write python code in pycharm IDE, and now practicing tuple collections topic, that contains string variables.”
# Instructions:
# a. Words marked in purple - usual extraction of cell by index
# b. Words marked in yellow - extraction by negative cell index
print('print sentence with cell extraction: We are ninja developers. We write ' +(technological_terms[0])
      +' code in ' +(technological_terms[-4])
      +', and now practicing ' +(technological_terms[2])
      +' collections topic, that contains ' +(technological_terms[-1]) +' variables.')

# 3. Insert the variables “float” and “list” into the tuple. Add them to the end of the collection
# (Hint : We studied how to add new cells on ‘list - advanced’ lecture)
technological_terms_list = list(technological_terms)
technological_terms_list.append('float')
technological_terms_list.append('list')
technological_terms = tuple(technological_terms_list)
print('add variables to collection : ' +str(technological_terms))

# 4. Create a single cell tuple with the number ‘1’ in it. Also, print out the ‘type’ of the data collection
single_cell_tuple = (1,)
print('single cell tuple : ' +str(single_cell_tuple))
print(type(single_cell_tuple))

