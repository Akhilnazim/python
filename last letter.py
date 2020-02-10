
def last(str):
    return str[-1]
#print(last('hello'))

def test():
    assert last('hello') == 'o'
    assert last('hai') == 'i'
    assert last('nazim') == 'm'
    print('your code is correct')


test()