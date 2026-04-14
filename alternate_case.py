''' Write a function to convert a given string to SpongeCase .
Spongecase is a style of text where letters alternately appear in lower and upper case
. For example, the word Spongecase in spongecase would be sPoNgEcAsE.
1. Define a function which takes a single argument text
2. Inside the function, alternate the case of each letter in text, starting with lowercase.
Input : "programizpro123"
Output : 'pRoGrAmIzPr0123'


'''


def to_spongecase(text):
    st = ''
    t = list(text)
    for i in range(0, len(t)):
        if i % 2 == 0:
            st += t[i].lower()
        elif i % 2 != 0:
            st += t[i].upper()
        else:
            st += t[i]

    print(st)


to_spongecase("programizpro123")
