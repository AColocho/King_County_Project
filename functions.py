def getYear(data):
    """ 
    Function takes in an array, pandas series, or list with dates in format MM/DD/YYYY and extracts year. 
    Format does not matter as long as the year is the last 2 or 4 digits after a /
    The function returns a list with all the dates in interger form. 
    """
    lst = []
    for date in data:
        date = str(date).split('/')
        date = int(date[-1])
        lst.append(date)
    return lst

def getFormula(target,dataFrame):
    """
    Function takes in the name of the target variable and a data frame to return the formula for a statsmodels OLS model.
    The function returns the formula as a string in the format of 'target ~ n1+n2+....+n#'
    """
    variables = ""
    for i in dataFrame:
        if (i != target) and (len(variables) == 0):
            variables += str(i)
        elif (i != target) and (len(variables) > 0):
            variables += "+{}".format(str(i))
    
    formula = "{} ~ {}".format(target,variables)
    return formula
