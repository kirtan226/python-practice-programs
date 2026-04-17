# Questions Marks

'''
- Have the function QuestionsMarks(str) take the str string parameter,
which will contain single digit numbers, letters, and question marks, and check if there are exactly 3
question marks between every pair of two numbers that add up to 10. If so, then your program should return the
string true, otherwise it should return the string false. If there aren('t any two numbers that add up to 10 in the
string, then your program should return false as well.)


For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because
there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
'''

def QuestionsMarks(strParam):
    first_digit = None
    first_digit_index = None
    found_pair = False
    # print(strParam)
    # print(enumerate(strParam))
    for index, ch in enumerate(strParam):
        print(f"index :-> {index}, ch :->{ch}")
        if ch.isdigit():
            current_digit = int(ch)

            if first_digit is None:
                first_digit = current_digit
                first_digit_index = index
            else:
                if first_digit + current_digit == 10:
                    found_pair = True

                    between_part = strParam[first_digit_index + 1:index]
                    question_count = between_part.count("?")

                    if question_count != 3:
                        return "false"

                # move forward to next digit
                first_digit = current_digit
                first_digit_index = index

    return "true" if found_pair else "false"


print(QuestionsMarks("aa6?9"))                     # false
# print(QuestionsMarks("acc?7??sss?3rr1??????5"))   # true
# print(QuestionsMarks("arrb6???4xxbl5???eee5"))    # true
# print(QuestionsMarks("acc3??7??sss?3rr1??????5")) # false