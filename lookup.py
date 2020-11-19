from Unit_Bit_test import *
with open("binary.txt", "r") as file2:
    arbre=UniBit()
    file2.readline()
    with open("lookup.txt", "w") as file4:
        while 1:
            f = file2.readline()

            if f == "":
                break
            else:
                p = f.split()
                arbre.put(p[1], p[0], p[3])
        print('\n'+10*"#"+"\n", file=file4)
        print(arbre.lookup("0011*"), file=file4)
        print('\n'+10*"#"+"\n", file=file4)
        print(arbre.lookup("0*"), file=file4)
        print('\n'+10*"#"+"\n", file=file4)
        print(arbre.lookup("1000*"), file=file4)
        print('\n'+10*"#"+"\n", file=file4)
        print(arbre.lookup("101101*"), file=file4)
        print('\n'+10*"#"+"\n", file=file4)
        print("Total of Node created is :",arbre.numberOfNodeCreated, file=file4)
