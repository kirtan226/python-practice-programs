"""write a python function that takes arguments as list , elemnt of list and new element to be insert .
replace the old element with new element and remove old element ."""

def replace_item(lst, old_item, new_item):
    if old_item in lst:
        n = lst.index(old_item)

        lst.insert(n, new_item)
        lst.remove(old_item)
    return lst

l=['cat', 'dog', 'elephant']
old='dog'
new='lion'
print(replace_item(l, old, new))