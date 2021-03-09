def puissance(a, b):
  return a ** b


x = puissance(2,3)
print(x)
#On peut aussi etre plus explicite
puissance(a=2, b=3)
#On peut utiliser les deux en meme temps:
puissance(2, b=3)

### Question 1 ###

def somme(a,b):
  return a+b

x = somme(2,3)
print(x)

def fonct(a,b,c):
  print(a, b,c)
  return a,b,c

fonct(1,2, c=4) # là ça marche, car on sait où mettre tous les chiffres..

### Question 2 ###

fonct(a=1,b=2,c=3)
# fonct(a=1,b=2,3)
# Ne marche pas, car l'ordinateur est perdue en quelque sorte dans l'affectation..
fonct(2,b=2,c=3)
fonct(b=1,a=2,c=3)

print("---------")

valeurs = 1,2
c = valeurs[0]
d = valeurs[1]

res = somme(c,d) # en general on donne le meme nom a la variable qu'au parametre.
#Cela facilite la lecture mais n'est pas obligatoire.
print(res)

#ou bien directement

c,d = valeurs
res = somme(c,d)
print(res)

res = somme(*valeurs)
print(res)

kw_valeurs = {'a': 0, 'b': 1}
res = somme(**kw_valeurs)
print(res)

print("---------")

valeurs = 1,
kw_valeurs = {'b':1}

res = somme(*valeurs, **kw_valeurs)

print(res)

### Question 3 ###

def fonctbis(a,b):
  print(a,b)
  return a,b

fonctbis(*valeurs,**kw_valeurs)

val = 1,
lav = 3,
alv = 5,

fonct(*val,*lav,*alv)

valbis = {'a': 2}
lavbis = {'b': 4}
alvbis = {'c': 6}

fonct(**valbis,**lavbis,**alvbis)
fonct(*val,*lav,**alvbis)
# fonct(*val,**lavbis,*alv)
# fonct(**valbis,*lav,*alv)
# Ne marche pas

### Question 3.1 ###

valeurs = [[2,3], [3,3]]

x = [i**j for i,j in valeurs]
print(x)

y = [puissance(*v) for v in valeurs]
print(y)

print(*valeurs) # --> [2,3] [3,3] donc deux listes donc nos deux arguments a et b ;)

print('---------')

def fonction_double(valeur = 0):
  return valeur * 2

fonction_double() # est valide
fonction_double(2)
m = fonction_double(valeur=4)
print(m)

print(1,2,3)
print(1,2,3, sep='_')

maliste = []
maliste.append(4) # rajoute le chiffre 4 /!\
print(maliste)

### Question 4 ###

maliste = []

def append_chaine(maliste=[],b=0):
  maliste.append(str(b))
  print(maliste)

append_chaine()
append_chaine()
append_chaine()

# Là il y a un effet de bord, puisque quand on execute plusieurs fois on a pas la meme chose !

### Question 5 ###

def append_chaine(maliste=[],b=0):
  maliste.append(str(b))
  print(maliste)

append_chaine()
append_chaine()
append_chaine()