def one():
    print('It comes to one function')
    return 'January'

def two():
    print('it comes to the function february')
    return 'February'

def three():
    return 'March'


def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three
    }
    # get the function from switcher dictionary
    func = switcher.get(argument, lambda: 'Invalid month')
    # execute the function
    print(func())


numbers_to_months(2)

