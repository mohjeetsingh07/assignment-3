s1 = "Python is a case sensitive language"

#finding length of the string
print(len(s1))
#reversing the order of the string
print(s1[::-1])
#using slice
s2 = s1[10:27]
print(s2)
#replacing text
print(s1[0:10]+"object oriented"+s1[27:35])
#finding index
print(s2.index("a"))
#removing white spaces
print(s1.replace(" ",""))
