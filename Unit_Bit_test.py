####################################unubit-trie################################
class Node():
#creation d'un arbre
    def __init__(self,backup):
        self.backup = backup
        self.nextHop = None
        self.addr = None
        self.route = None
        self.left = None
        self.right = None

#algorithme de trie
class UniBit:

    def __init__(self):
        self.root = Node("none")  #a chaque root on va traverser on cree le noeud associe


    numberOfNodeCreated = 0# nombre de noeud cree
    i = -1
#fonction qui va creer et stocker les valeurs des noeuds traverser
    def put(self, addr, route, nextHop):
        return self._put(addr, route, nextHop, self.root)

#la fonction recursif de fonction put pour faire la creation
    def _put(self, addr, route, nextHop, noeud):
        self.i += 1
        if addr[self.i] == '1':
            if noeud.right == None:
                noeud.right = Node("none")    #creation du noeud droit
                self.numberOfNodeCreated +=1
                return self._put(addr, route, nextHop, noeud.right)
            elif noeud.right != None:
                return self._put(addr, route, nextHop, noeud.right)

        elif addr[self.i] == '0':
            if noeud.left == None:
                noeud.left = Node("none") #creation d'un noeud gauche
                self.numberOfNodeCreated +=1
                return self._put(addr, route, nextHop, noeud.left)  #stocker le noeud
            elif noeud.left != None:
                return self._put(addr, route, nextHop, noeud.left)

        elif addr[self.i] == '*':#si on trouve etoile a la fin de l'addr donc en stock ca valeur et on arrete la recherche
            if noeud.backup != "none":
                if noeud.nextHop != nextHop:
                    noeud.nextHop += ' et '+ nextHop
                noeud.route += ' et ' + route
                # s'il y a une address repete plusieurs fois on imprime
                # tous les routes et les interfaces de sortie associe a chaqu'une

            else:
                noeud.backup = addr
                noeud.route = route
                noeud.nextHop = nextHop
            self.i=-1#on return la meme valeur de i pour faire la meme chose la prochaine fois

    #fonction de recherche
    def lookup(self,addr):
        return self._lookup(addr, self.root)
    j=-1
    def _lookup(self, addr, noeud):

        self.j+=1
        if addr[self.j] !='*':

            if addr[self.j] == '1':
                if noeud.right != None:

                    return self._lookup(addr, noeud.right)
                elif noeud.right == None:
                    noeud.backup = addr[:self.j] + '*'
                    self.j=-1
                    return "route : "+noeud.route+"\naddr : "+noeud.backup+"\nnextHop : "+noeud.nextHop
                else:
                    return self._lookup(addr, noeud.right)
            elif addr[self.j] == '0':
                if noeud.left != None:

                    return self._lookup(addr, noeud.left)
                else:
                    noeud.backup = addr[:self.j] + '*'
                    self.j=-1
                    return "route : "+noeud.route+"\naddr : "+noeud.backup+"\nnextHop : "+noeud.nextHop

        elif addr[self.j] == '*':
            if noeud.backup == addr:
                self.j=-1
                return "route : "+noeud.route+"\naddr : "+noeud.backup+"\nnextHop : "+noeud.nextHop
            else:
                addr = addr[:-2] + '*'
                self.j = -1
                return self.lookup(addr)
