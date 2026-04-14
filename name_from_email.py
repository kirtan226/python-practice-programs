''' Write a function to Reterive the name from an email address .
1. Define a function that takes a string as input.
2. Inside the function, split the email address at the ' @ ' symbol and take
    the first part. Then, replace any periods (' . ') with spaces.
3. Return the name extracted from the email address.

Input:'john.doe@example.com'
Output : 'john doe'
Reason: The name in the email address 'john.doe@example.com' is 'john
doe'. After splitting at '@', we get 'john.doe'. Replacing " with "', we get 'john doe'

Input : 'jane@example.com'
Output : 'jane'

Input : 'foo.bar@baz.com'
Output : 'foo bar'

Input : 'test.user@test.com'
Output : 'test user'
'''


def get_name_from_email(email):
    a = email.split('@')
    # print(a)
    if '.' in a[0]:
        name = a[0].replace('.', ' ')
        # print(name)
        return name
    else:
        return a[0]


get_name_from_email('test.user@test.com')
