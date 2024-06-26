"""Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0."""


def expanded_form(num):
    e = ""
    l = []
    for i in str(num):
        l.append(i)
    l_2 = l.copy()
    for j in l:
        if j == "0":
            l_2.remove(j)
        else:
            e += j + "0" * (len(l_2) - 1) + " + "
            l_2.remove(j)
    return e[:-3]
