''' write a function to convert the keys and values in a dictionary to seperate lists .
Input:{'val1':'key1','val2':'key2'}
Your Output:(['val1', 'val2'], ['key1', 'key2'])

Input:{'k1': 'v1', 'k2':'v2'}
Your Output:(['k1', 'k2'], ['v1', 'v2'])

Input:{}
Your Output:([], [])

'''

def dict_to_lists(d):
    key_list =[]
    value_list =[]
    for key,values in d.items():
        key_list.append(key)
        value_list.append(values)

    return key_list , value_list

d={'a': 1, 'b': 2, 'c': 3}
print(dict_to_lists(d))