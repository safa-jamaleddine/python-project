with open("input.txt",'r') as file1:
    file1.readline()
    with open("binary.txt", "w") as file2:
        print("ROUTE"+20*" "+" DESTINATION-ADDRESS"+40*" "+"CLASS"+50*" "+" OUTPUT-INTERFACE", file=file2)

        while 1:
            ip = file1.readline()
            if ip =="":
                break
            else:
                p = ip.split()
                m = p[1].split("/")
                mask = int(m[1])
                ###convertir IP to bin###
                l = m[0].split(".")
                ip_bin = ""
                for a in l:
                    x = bin(int(a))
                    x = x[2:]
                    for i in range(8-len(x)):
                        x = "0"+x
                    ip_bin += x
                ip_bin = ip_bin[:int(mask)]+"*"

                file2.write(p[0]+(30-len(p[0]))*" ")
                file2.write(ip_bin + (55-len(ip_bin))*" ")
                file2.write("\t")
                file2.write('\t'+p[2] + (30-len(p[2]))*" ")
                file2.write("\t")
                file2.write("\t\t"+p[4])
                file2.write("\n")

