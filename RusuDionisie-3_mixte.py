import nashpy as nash
import numpy as np

# definim matricea de castiguri / pierderi
payoff_matrix = np.array([[50, 20, 10, 40],
                          [30, 40, 20, 10],
                          [40, 10, 30, 20],
                          [20, 30, 40, 30]])

# cream obiectul jocului cu matricea de castiguri / pierderi
game = nash.Game(payoff_matrix)

# calculam strategiile mixte de echilibru utilizand metoda lemke_howson
mixed_equilibrium = game.lemke_howson(initial_dropped_label=2)

# afisam strategiile mixte de echilibru
print("Stategia jucatorului A:", mixed_equilibrium[0])
print("Stategia jucatorului B:", mixed_equilibrium[1])
print("Valoarea jocului:", game[mixed_equilibrium[0],mixed_equilibrium[1]])
