'''
Convention
==========
The name of the file in which there is need to
carry pytest must begin with 'test'

Function in the application are called as unit.
name of the function must began with 'test'
'''
def test_square():
    x=2
    assert x**2==4

def test_cube():
    x=5 
    assert x**3==125