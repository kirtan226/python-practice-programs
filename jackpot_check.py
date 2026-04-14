"""
To "hit the jackpot" means all four slots show the same symbol or number.
Example
input:[@, @, @, @]
output:True
Reason: All four slots show the same symbol @.

Input:[1, '@', 3, '#']
Output:False

Input:['#', '#', '#', '#']
Output:True
"""

def check_jackpot(slot_machine_outcome):
    if all(x == slot_machine_outcome[0] for x in slot_machine_outcome):
        return True
    else:
        return False

l = ['#', '#', '#', '#']
print(check_jackpot(l))


"""
def check_jackpot(slot_machine_outcome):
    count = 0 
    for _ in slot_machine_outcome[1:]:
        if _ == slot_machine_outcome[0]:
            count += 1
    if count == len(slot_machine_outcome) - 1:
        return True
    return False
    """