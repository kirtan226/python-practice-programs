''' Write a function to filter and merge the given name and emails.
Input : "Alice" ,["alice@example.com", "alice@doe.com"] ,"Alice" ,["alice@doe.com", "alice@smith.com"]
Output : {"Alice": ["alice@doe.com", "alice@example.com", "alice@smith.com"]}

Input : "Bob" ,["bob@example.com"] , "Bob" ,["bob@example.com", "bob@doe.com"]
Output : {"Bob": ["bob@doe.com", "bob@example.com"]}

Input :"John",["john@example.com", "john@doe.com"],"John", ["john@doe.com", "john@smith.com"]
Output : {"John": ["john@doe.com", "john@example.com", "john@smith.com"]}
'''


def merge_accounts(*accs):
    new = list(accs)
    d = {}
    user = []
    all = []
    for i in new:
        if isinstance(i, str) and i.isalpha():
            # print('Char', i)
            user.append(i)
        elif isinstance(i, list):
            # print('List', i)
            all.extend(i)
    # print(user)
    # print(all)
    # print(d)

    common = []
    for i in user:
        for j in all:
            if i.lower() in j:
                if j not in common:
                    common.append(j)
                    common.sort()
        d[i] = common
    return d


s = "Bob", ["bob@example.com"], "Bob", ["bob@example.com", "bob@doe.com"]
print(merge_accounts(*s))
