"""
Write a function to play the Loves me, loves me not game.
This game is traditionally played by plucking the petals off a flower one by one, saying
'Loves me' and 'Loves me not' alternately for each petal.
Return 'Loves me' or 'Loves me not' for each number from 1 to the input number.
If the current number is odd, return 'Loves me', otherwise return 'Loves me not.
input:4
output:['Loves me', 'Loves me not', 'Loves me', 'Loves me not']
Reason: The function returns 'Loves me' for odd numbers and 'Loves me not'
for even numbers. Since 4 is given as input, it returns these phrases four times in alternating order.
"""

def loves_me_not(n):
    love=[]
    for i in range(1,n+1):
        print(i)
        if i%2==0:
            love.append('Loves me not')
        elif i%2!=0:
            love.append('Loves me')
        elif n==len(love):
            break
    return love

n=int(input("Enter number of petal :"))
print(loves_me_not(n))
