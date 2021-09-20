from pythonisms import __version__

from pythonisms.pythonisms import *

def test_version():
    assert __version__ == '0.1.0'





def test_insert_and_print():
    
    num_one=LinkedList()
    num_one.insert(1)
    num_one.insert(2)
    num_one.insert(3)

    actual = num_one.__str__()
    excepted = "The LinkedList Representation is : {3} -> {2} -> {1} ->  + NULL"

    assert actual == excepted



def test_len_of_linked_list():
    num_one=LinkedList()
    num_one.insert(1)
    num_one.insert(2)
    num_one.insert(3)

    actual = num_one.__len__()
    excepted = 'The length linked list is  : 3'

    assert actual == excepted
