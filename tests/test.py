from myparkage import myModule

def test_top_n():

    """ 
Make top n works correctly
"""

    assert myModule.top_n([8,4,5,2,6,7,9], 4) == [9,8,7,6], "incorrect"
    assert myModule.top_n([11,6,9,13,24,55,45,42], 4) == [55,45,42,24], "incorrect"
    assert myModule.top_n([12,65,45,32,87,77,67], 4) == [87,77,67,65], "incorrect"

