from main import *

def test_list_comp1():
    assert list_comp1() == [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

def test_list_comp2():
    assert list_comp2() == [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93]

def test_list_comp3():
    assert list_comp3("Hello world, how are you?") == 4
    assert list_comp3("Go Austin High Maroons!") == 3
    assert list_comp3("I hate making unit tests.") == 4

def test_list_comp4():
    assert list_comp4("Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams") == ['Y', 'l', 'l', 'w', ' ', 'Y', 'k', 's', ' ', 'l', 'k', ' ', 'y', 'l', 'l', 'n', 'g', ' ', 'n', 'd', ' ', 'y', 'w', 'n', 'n', 'g', ' ', 'n', 'd', ' ', 'y', 's', 't', 'r', 'd', 'y', ' ', 't', 'h', 'y', ' ', 'y', 'd', 'l', 'd', ' ', 'w', 'h', 'l', ' ', 't', 'n', 'g', ' ', 'y', 'k', 'y', ' ', 'y', 'm', 's']
    assert list_comp4("Hello world, how are you?") == ['H', 'l', 'l', ' ', 'w', 'r', 'l', 'd', ',', ' ', 'h', 'w', ' ', 'r', ' ', 'y', '?']
    assert list_comp4("It's Friday!") == ['t', "'", 's', ' ', 'F', 'r', 'd', 'y', '!']

def test_list_comp5():
    assert list_comp5(["hi", 4, 8.99, 'apple', ('t,b','n')]) == [(0, "hi"), (1, 4), (2, 8.99), (3, 'apple'), (4, ('t,b','n'))]
    assert list_comp5(["a","b","c","d","e"]) == [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
    assert list_comp5(["one", "two", "three"]) == [(0, 'one'), (1, 'two'), (2, 'three')]

def test_list_comp6():
    assert list_comp6([1, 2, 3, 4],[2, 3, 4, 5]) == [2, 3, 4]
    assert list_comp6([1,2,3,4,5],[6,7,8,9,10]) == []
    assert list_comp6([2,4,6,8,10,12],[2,1,4,3,6,5]) == [2,4,6]

def test_list_comp7():
    assert list_comp7([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 7, 1, 12]) == [(1, 1), (2, 2), (7, 7)]

def test_list_comp8():
    assert list_comp8("The quick brown fox jumps over the lazy dog") == ['The', 'fox', 'the', 'dog']
    assert list_comp8("I ate a carrot for lunch.") == ['I', 'ate', 'a', 'for']
    assert list_comp8("Okay, let's do this!") == ['do']

