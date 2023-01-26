import nashpy as nash
import numpy as np

# definim matricea de castiguri / pierderi
payoff_matrix = np.array([[50, 20, 10, 40],
                          [30, 40, 20, 10],
                          [40, 10, 30, 35],
                          [40, 43, 40, 45]])

# cream obiectul jocului cu matricea de castiguri / pierderi
game = nash.Game(payoff_matrix)

# calculam strategiile pure de echilibru utilizand metoda support_enumeration
pure_equilibrium = game.support_enumeration()

# afisam strategiile pure de echilibru
for eq in pure_equilibrium:
    print("Stategia jucatorului A:", eq[0])
    print("Stategia jucatorului B:", eq[1])
    print("Valoarea jocului:", game[eq[0],eq[1]])