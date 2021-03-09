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
fonct(2,2,c=3)
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