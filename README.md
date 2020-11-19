# python-project

L’objectif de ce projet c’est de construire une table de routage qui contient
un certain nombre aléatoire des adresses IP appartient au réseau, du masque de sousréseau de l'IP, de la passerelle et du nom de l'interface de sortie. Ces détails sont
utilisés pour transmettre un paquet à l'extérieur du réseau afin de se connecter à
l'internet. Ce projet va consacrer pour donner une idée sur la manière dont le système
faire la recherche pour transmettre un paquet.

•randem_ip :
Créer des adresses aléatoires de diffèrent classe {classA, classB, classC}et le masque associe à chaque adresse

•ipgenerate:
générer les différents adresses IP et les arranger dans le fichier input.txt

•ip_to_binairie:
conversion des adresses IP quand a en binaire pour faciliter le travail de lookup, puis en met le résultat dans le fichier binary.txt

•Unit_Bit_test:
La classe d'insertion compare la valeur du nœud au nœud parent Si aucun nœud n'existe pour cette adresse il doit l'ajouter en tant que nœud gauche ou droit. Si le nœud existe déjà, les informations de transmission sont mises à jour.
