# Using the Python language, have the function MeanMode(arr) take the array of numbers stored in arr
# and return 1 if the mode equals the mean, 0 if they don't equal each other
# (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)).
# The array will not be empty, will only contain positive integers, and will not contain more than one mode.

"""The mode value in a dataset is the value that appears most frequently."""

def check(list):
    l=len(list)
    mean = sum(list)//l    #find the mean value

    repet_check={}
    for i in list:
        if i in repet_check:
            repet_check[i]+=1
        else:
            repet_check[i]=1

    mode=max(repet_check.values())  #find the maximum repeated value is dictionary

    if mode==mean:
        return 1
    else:
        return 0


print(check([1, 2, 2, 3, 3, 3, 4, 4, 5]))