from ipaddress import *
from random import *

def random_ipv4(a, b):

    bits = randint(a, b)
    addr = IPv4Address(bits)
    addr_str = str(addr)
    global Mask
    Mask = randint(0, 30)
    ip_add = IPv4Network(addr_str+"/"+str(Mask),strict=False)
    return str(ip_add.network_address)+"/"+str(Mask)

def Ip_generate():
    i =0
    while i <1001:
####### classA ######
        for i in range(0,50):
            ip = random_ipv4(16777216, 2147483646)
            return ip

###### classB #####
        for i in range(0,30):
            ip = random_ipv4(2147483649, 3221225470)
            return ip

##### classC #####
        for i in range(0,20):
            ip = random_ipv4(3221225473, 3758096382)
            return ip
        i = i+1
def Mac_generate(t=""):

    global Mask

    if t == 'classA':
        Mask = randint(8,32)

    elif t == 'classB':
       Mask = randint(16,32)

    elif t == 'classC':
        Mask = randint(24,32)

    else:
        Mask = Mask
    net_id=int(Mask/8)
    s=Mask%8
    l=[]
    #ici on va ajoutet les octets 255 pour la partie net-id
    for i in range(net_id):
        l.append("255")
    #pour la separation du masque
    if s != 0:
        a=0
        for i in range(s):
            a+=2**(7-i)
        l.append(str(a))
    #ici on va ajoutet les octets 0 pour la partie host-id
    while len(l) < 4:
        l.append("0")
    addr_str=".".join(l)
    return addr_str
