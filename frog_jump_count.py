''' Write a function to return total number of frog jumps .
- A frog can only jump if the next leaf is taller than the current one it is standing on.
- If the given list numbers represents the heights of different leaves, return the total
   number of jumps the frog can make.
- For example, if numbers = [20, 10, 40, 50],
1. Firstly, the frog can jump from 20 to 40.
2. Then, it can jump from 40 to 50.
-Thus, the frog can make a total of 2 jumps.
Note: The frog must always start from the first leaf.

input : numbers = [10, 20, 10, 30, 20, 40]
Output :3
Reason: Here,
1. Firstly, the frog can jump from 10 to 30.
2. Then, the frog can jump from 20 to 30.
3. Finally, the frog can jump from 30 to 40.
Thus, the frog can make a total of 3 jumps.

Input:[10, 20, 10, 30, 20, 40]
Output : 3

Input:[50, 40, 30, 20, 10]
Output :0

Input : [100, 50, 200, 100, 300, 150, 400, 200, 500]
Output :4

Input : [20, 10, 40, 50]
Output : 2
'''

def frog_jump(numbers):
    new=[]
    count =0
    for i in range(0,len(numbers)):
        if i==0:
            new.append(numbers[i])

        elif numbers[i]>numbers[i-1]:
            new.append(numbers[i])
            count+=1

    return count

    # if not assigned count variable
    # return len(new)-1




l = [20, 10, 40, 50]
print(frog_jump(l))