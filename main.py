def puissance(a, b):
  return a ** b


x = puissance(2,3)
print(x)
#On peut aussi etre plus explicite
puissance(a=2, b=3)
#On peut utiliser les deux en meme temps:
puissance(2, b=3)

### Question 1 ###

def somme(x,y):
  return (x+y)

x = somme(2,3)
print(x)

def fonct(a,b,c):
  print(a, b,c)
  return a,b,c

fonct(1,2, c=4) # là ça marche, car on sait où mettre tous les chiffres..

### Question 2 ###

