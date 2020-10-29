## Author: Feras
## Description: A function that shuffles a list of numbers and returns a shuffled list

import random 
def shuffle(intLst):
    for i in range(len(intLst)-1, 0, -1): 
        j = random.randint(0,4)
        intLst[i], intLst[j] = intLst[j], intLst[i] 
    return intLst
print(shuffle([1,2,3,4,5]))