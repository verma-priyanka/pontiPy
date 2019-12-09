#---------------------------------------------------------------------------------------------
# Project Name: Pontius Matrix
# Collaborators: Priscilla Ahn, Max Enger, Jordan Frey, Priyanka Verma
# Purpose: Automation of Pontius Matrix Creation
# Created: 10/28/2019
# Input: Contingency Table from PM
# Python Version: Python 3.7
#---------------------------------------------------------------------------------------------

class pontiPy(object):
    def __init__(self, dataframe):
        """Return a new pandas dataframe object."""
        self.dataframe = dataframe
        column_names = []
        for col in self.dataframe.columns:
            column_names.append(col)
        self.dataframe['Col Sum'] = self.dataframe.sum(axis=1)
        self.dataframe.loc['Row Sum'] = self.dataframe.sum(axis=0)

    # Function to compute Hits
    def hit(self, category = None):
        _hits = []
        for i in range(len(self.dataframe)-1):
            # Hits = Diagonal cells
            _hits.append(self.dataframe.iloc[i][i])
        # if no category is specified
        # len-1 because total hit sum is included in list
        if category is None:
            return sum(_hits[0:len(_hits)-1])
        # List to build contingency table in the contingency() function
        elif category == 'CONTINGENCY':
            # replace last item with total hits
            # right now it is the sum of the matrix
            _hits[len(_hits)-1] = sum(_hits[0:len(_hits)-1])
            return _hits
        # if category is specified, return hits for that category
        else:
            # return
            return _hits[category]

    # Function to compute false alarms
    def false_alarm(self, category = None):
        _false_alarm = []
        # subtract one to get # of categories
        # removes row sum from the length
        df_length = (len(self.dataframe) - 1)
        for i in range(len(self.dataframe)):
            # False alarms = Column Sum - Hits for each category
            _false_alarm.append(self.dataframe.iloc[i][df_length]-self.dataframe.iloc[i][i])
        # if no category is specified
        # len-1 because total false alarm sum is included in list
        if category is None:
            return sum(_false_alarm[0:len(_false_alarm)-1])
        # List to build contingency table in the contingency() function
        elif category == 'CONTINGENCY':
            # add sum of false alarms to list as last item
            _false_alarm[len(_false_alarm)-1] = sum(_false_alarm[0:len(_false_alarm)-1])
            return _false_alarm
        # if category is specified, return false alarm for that category
        else:
            return _false_alarm[category]

    # Function to compute miss
    def miss(self, category = None):
        _miss = []
        df_length = len(self.dataframe)-1
        for i in range(len(self.dataframe)):
            # miss = Row Sum - Hits for each category
            _miss.append(self.dataframe.iloc[df_length][i]- self.dataframe.iloc[i][i])
        # if no category is specified
        if category is None:
            return sum(_miss[0:len(_miss)-1])
        # List to build contingency table in the contingency() function
        # add sum of misses to list as last item
        elif category == 'CONTINGENCY':
            _miss[len(_miss)-1] = sum(_miss[0:len(_miss)-1])
            return _miss
        # if category is specified, return miss for that category
        else:
            return _miss[category]

    # Function to compute Exchange between ALL, ONE or TWO categories
    """
       1. If no category is specified (Total must be false):
            Sum of total exchange is returned
       2. If total is False and 1 category is specified:
            Return is exchange for that category with all other categories + a total value in dict
       3. If Total is True and 1 category is specified:
            Return is total exchange for that category
       4. If 2 categories are specified (Total must be false):
            Return exchange between 2 categories
    """
    def exchange(self, category1 = None,category2 = None, Total = False):
        _exchange = {}
        _categories = range(len(self.dataframe)-1)
        for i in _categories:
            # Create a list for every category
            _catlist = []
            # Exchange calculated between 2 categories
            for j in _categories:
                if i != j:
                    # Create list with each exchange value for category 1
                    _catlist.append(min(self.dataframe.iloc[i][j],self.dataframe.iloc[j][i]))
            # Append exchange list for each category to dictionary
            _exchange[i]=_catlist
        # A condensed list of category and exchange sum for each
        ex_by_category = ({k: sum(v) for k, v in _exchange.items()})
        if category1 is None and Total is False:
            # Total exchange
            return sum(ex_by_category.values())
        elif Total is True and category2 is None:
            return ex_by_category[category1]
        # If one category is specified
        # Return is exchange with all categories
        # Total must be false since it only applies to ONE category
        elif category1 is not None and category2 is None and Total is False:
            # Dictionary to return exchanges between cat 1 and all other categories
            # Also returns a total exchange for category
            _single_category = {}
            # iterate through number of categories
            for i in range(len(_exchange[category1])):
                # Exchange at index 0 = exchange of 0 with category 1 since exchange cannot happen with itself
                # Size of list with exchange is # of categories - 1
                # If index of list item == category 1, the exchange is for the category after
                # Example: Parameter is Category 2
                # Exchange for Category 2: {'Category 0': 0, 'Category 1': 30, 'Category 3': 40, 'Total Exchange': 70}
                if i != category1:
                    # key for dictionary
                    _cat_key = 'Category ' + str(i)
                    # If i == category, the else statement added that category to dict
                    # So this addition will be i+1
                    if _cat_key in _single_category.keys():
                        _cat_key = 'Category ' + str(i + 1)
                        _single_category[_cat_key] = _exchange[category1][i]
                    # if category i not in dictionary, add to dictionary
                    else:
                        _single_category[_cat_key] = _exchange[category1][i]
                # Exchange at index 0 = exchange of 0 with category 1
                # When index == category1 parameter, the key will be incremented by 1
                # Category 1 Exchange with Category 0 = index 0 in list
                else:
                    _cat_key = 'Category ' + str(i+1)
                    _single_category[_cat_key] = _exchange[category1][i]
            _single_category['Total Exchange'] = sum(_single_category.values())
            return _single_category

        # To calculate exchange within pairs, it needs to find the index of the categories in dict
        else:
            # Categories provided as params cannot be the same since exchange happens in pairs
            if category1 == category2:
                return 'No Exchange Within The Same Category. Provide Two Different Categories.'
            # When cat1 == 0, the index should be 0 for the
            if category1 != 0 and category2 != 0 :
                # Exchange is with the inverse cell position for the two categories
                # The index of other category will be -1 in the second pairing
                return min(_exchange[category1][category2-1],_exchange[category2-1][category1])
            # If cat 1 is 0, return MIN (0[cat2-1], cat2[0])
            elif category1 == 0:
                return min(_exchange[category1][category2-1], _exchange[category2][category1])
            # If cat 2 is 0, return MIN (cat1[0], cat2[cat-1])
            elif category2 == 0:
                return min(_exchange[category1][category2], _exchange[category2][category1-1])

    # Function to compute quantity between all or one category
    # Requires at least 1 category in parameter
    def quantity(self, category = None, label = False):
        if category is not None:
            # Returned as a dictionary
            # If no category is specified, return total quantity
            _quantity = {}
            # Calculate quantity by subtracting false alarms from misses
            _q_by_category = self.miss(category) - self.false_alarm(category)
            # Quantity Labels
            # If greater than 0, it is a miss quantity
            if _q_by_category > 0:
                _quantity['Miss'] = abs(_q_by_category)
            # If greater than 1, it is a false alarm quantity
            elif _q_by_category < 0:
                _quantity['False Alarm'] = abs(_q_by_category)
            # If 0, quantity is 0
            else:
            # if it isn't a miss or false alarm quantity
                _quantity['Blank'] = abs(_q_by_category)

         # If no category is specified: return the absolute sum of all quantity
        # Divide sum quantity by 2
        # Label is off by default
        if category is None:
            _categories = range(len(self.dataframe) - 1)
            _quantity_sum = 0
            for i in _categories:
                _quantity_sum += abs(self.miss(i)-self.false_alarm(i))
                return int(_quantity_sum/2)
        # If True: it returns the quantity value for that category
        elif label is True:
            return _quantity
        # If False (Default): it returns a dictionary
        # Dictionary Key = Miss/False Alarm/Blank label
        # Dictionary Value = Quantity value for the key
        elif label is False:
            return list(_quantity.values())[0]

    # Function to compute size for all or one category
    # Axis must be specified when category is specified
    # Determines if row or col sum for category will be returned
    def size(self, category = None, axis= None, Total = False):
        # size of the data frame is returned
        if category is None and axis is None:
            return self.dataframe.at['Row Sum', 'Col Sum']
        # return col or row sum for category depending on axis
        # An axis (x or y) must be provided with a category
        elif category is not None and axis is not None:
            if Total is False:
                # If x is specified, return col sum for category
                if axis.lower() == 'x':
                    _col_sum = self.dataframe['Col Sum'][category]
                    return _col_sum
                # If y is specified, return row sum for category
                elif axis.lower() == 'y':
                    _row_sum = self.dataframe.loc['Row Sum'][category]
                    return _row_sum
                # if axis isn't specified, return the sum of col and row sum for category
            else:
                # Get row
                if axis.lower() == 'x':
                    _col_sum = self.dataframe.iloc[category]
                    x_dict = _col_sum.to_dict()
                    # Remove col sum and False Alarms if they exist
                    x_dict.pop('Col Sum', None)
                    x_dict.pop('False Alarms', None)
                    return x_dict
                # If y is specified, return col for category
                elif axis.lower() == 'y':
                    # list of i
                    index_list = self.dataframe.index
                    for col in index_list:
                        pos = (self.dataframe.index.get_loc(col))
                        if pos == category:
                            y_dict = self.dataframe.get(col).to_dict()
                            # Remove Row Sum and Misses if they exist in dictionary
                            y_dict.pop('Row Sum', None)
                            y_dict.pop('Misses', None)
                            return y_dict
        else:
            return(self.size(category, axis = 'x') + self.size(category, axis = 'y'))

    # Function to compute difference for all or one category
    def difference(self, category = None):
        # if no category is specified, return total size-hits
        if category is None:
            _total_diff = self.size() - self.hit()
            return _total_diff
        # if category is specified: return size-2*hits for that category
        else:
            return self.size(category) - 2*(self.hit(category))

    # Function to compute total shift or shift for one category
    def shift(self, category = None):
        if category is None:
            # loop each category
            total_shift = 0
            for i in range(len(self.dataframe)-1):
                total_shift += (self.difference(i) - self.quantity(i) - self.exchange(i, Total = True))
            return total_shift
            # divide by 2
            # return self.quantity()/2
        else:
            return self.difference(category)-self.quantity(category)-self.exchange(category)

    # Generate final matrix
    # This function will call previous functions
    def matrix(self):
        _matrix = self.dataframe
        miss_row = self.miss('CONTINGENCY')
        # Add a blank item since the False Alarm column will not have misses
        # This is required since the list size will differ from matrix size
        miss_row.append('')
        # Add False alarm to matrix
        _matrix["False Alarms"] = self.false_alarm('CONTINGENCY')
        # Add Misses to matrix
        _matrix.loc['Misses'] = miss_row
        return _matrix



