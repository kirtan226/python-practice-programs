"""Print all of the numbers from 1 to 100. However, for any number divisible by three,
 print the word “Fizz,” for any number divisible by five, print the word “Buzz,” and
 for any number divisible by both three and five, print the word “FizzBuzz.”"""

def fizzbuzz(num):
    l=[]
    word = " "

    for i in range(1,num):
        if i%3==0 and i%5==0:
            # l.append("FIZZBUZZ")
            word="FIZZBUZZ"
        elif i%3==0:
            # l.append("FIZZ")
            word = "FIZZ"
        elif i%5==0:
            # l.append("BUZZ")
            word = "BUZZ"
        # else:
        #     l.append(str(i))

        if word!= " ":
            l.append(word)
        else:
            l.append(i)
    print(l)
n=int(input("Enter the number :"))
fizzbuzz(n)