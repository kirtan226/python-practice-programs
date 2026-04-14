''' Write a function to count the number of unique emails from a list of emails .

Input:['abc@gmail.com', 'xyz@yahoo.com', 'abc@gmail.com']
Output: 2

Input : ['test@domain.com', 'test@domain.com', 'test@domain.com']
Output : 1

Input : ['a@b.c', 'x@y.z', '1@2.3']
Output : 3

'''


def count_unique_emails(emails):
    new = []

    for i in emails:
        if i not in new:
            new.append(i)

    return len(new)


count_unique_emails(['abc@gmail.com', 'xyz@yahoo.com', 'abc@gmail.com'])
