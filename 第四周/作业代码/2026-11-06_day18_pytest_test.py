def divide(a,b):
    if b == 0:
        return False
    c = a/b
    return c

def is_even(num):

    if num%2 == 0:
        return True

    return False

"""测试用例"""
def test_divide():
    assert divide(0,0) == 1
    assert divide(0,1) == 0
    assert divide(3,6) == 0.5

def test_iseven():
    assert is_even(0) == True
    assert is_even(1) == False
    assert is_even(3) == False