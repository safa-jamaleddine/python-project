from randem_ip import *
import random

i = 0
with open("input.txt",'w') as file1:

    print("ROUTE"+20*" "+" DESTINATION ADDRESS"+20*" "+"CLASS"+40*" "+"MASK"+45*" "+" OUTPUT INTERFACE", file=file1)

    ####### classA ######

    while i <1000:
        ip = Ip_generate()
        for i in range(0,500):
            ROUTE = "P"+str(i)
            ip = random_ipv4(16777216, 2147483646)
            mask = Mac_generate()
            add = ip.split('/')
            if add[0] != '0.0.0.0':
                s =ROUTE+(30-len(ROUTE))*" "+ ip +(25-len(ip))*" "+"\t\tclassA\t"+ 40*" "+ mask+(45-len(mask))*" "+random.choice(["G1","G2","ETH0","G0"])
                print(s, file=file1)

            else:
                continue

        ###### classB #####

        for i in range(500, 800):
            ROUTE = "P"+str(i)
            ip = random_ipv4(2147483649, 3221225470)
            mask = Mac_generate()
            add = ip.split('/')
            if add[0] != '0.0.0.0':
                s =ROUTE+(30-len(ROUTE))*" "+ ip +(25-len(ip))*" "+"\t\tclassB\t"+ 40*" "+ mask+(45-len(mask))*" "+random.choice(["G1","G2","ETH0","G0"])
                print(s, file=file1)

            else:
                continue

        ##### classC ####

        for i in range(800, 1000):
            ROUTE = "P"+str(i)
            ip = random_ipv4(3221225473, 3758096382)
            mask = Mac_generate()
            add = ip.split('/')
            if add[0] != '0.0.0.0':
                s =ROUTE+(30-len(ROUTE))*" "+ ip +(25-len(ip))*" "+"\t\tclassC\t"+ 40*" "+ mask+(45-len(mask))*" "+random.choice(["G1","G2","ETH0","G0"])
                print(s, file=file1)

            else:
                continue

        i = i+1
    s1 ='P1001'+23*" "+ '0.0.0.0/0' +19*" "+"\t\tDEFAULT\t"+ 40*" "+ '0.0.0.0'+32*" "+random.choice(["G1","G2","ETH0","G0"])
    print(s1, file=file1)
