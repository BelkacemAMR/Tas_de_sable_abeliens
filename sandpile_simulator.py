import numpy as np
def apply_gravity(sandpile):
    while True:
        unstable_piles = np.where(sandpile >= 4)
        if len(unstable_piles[0]) == 0:
           break
        for i, j in zip(unstable_piles[0], unstable_piles[1]):
            sandpile[i, j] -= 4
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if ni >= 0 and ni < sandpile.shape[0] and nj >= 0 and nj < sandpile.shape[1]:
                    sandpile[ni, nj] += 1



# Test du programme :

# Créer une pile de sable 3x3 pour tester
sandpile = np.array([[0, 0, 0],
                     [0, 4, 0],
                     [0, 0, 0]])

# Appeler la fonction apply_gravity pour tester
apply_gravity(sandpile)

# Afficher le résultat
print(sandpile)
