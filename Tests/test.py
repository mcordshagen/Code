import numpy as np
import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

test_dict = {"Max": "King", "Lars": "Larry"}
test_list = [1, 2, 4 , 4]

key_list = list(test_dict.keys())

print(type(key_list), key_list)

x_list = [False for x in test_list]

print(x_list)

tuple_list = [(1, 2), (3,4)]

n = 25
div = 5
print(int(n/div) + (n % div>0))


