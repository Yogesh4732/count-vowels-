str1=input()
str2="aeiuoAEIOU"
for i in str2:
    if i in str1:
        if i=="a":
            print("a : {}".format(str1.count(i)))
        if i=="e":
            print("e : {}".format(str1.count(i)))
        if i=="i":
            print("i : {}".format(str1.count(i)))
        if i=="o":
            print("o : {}".format(str1.count(i)))
        if i=="u":
            print("u : {}".format(str1.count(i)))
        if i=="A":
            print("A : {}".format(str1.count(i)))
        if i=="E":
            print("E : {}".format(str1.count(i)))
        if i=="I":
            print("I : {}".format(str1.count(i)))
        if i=="O":
            print("O : {}".format(str1.count(i)))
        if i=="U":
            print("U : {}".format(str1.count(i)))
    
