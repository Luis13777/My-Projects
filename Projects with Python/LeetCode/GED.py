import random


def f(x, theta):
    return theta*x**(theta - 1)

#calcular a distribuição w

def generate_random_value(theta):
    # Gerar um número aleatório entre 0 e 1
    rand = random.random()
    
    return rand**(1/theta)

# Gerar 10 valores aleatórios seguindo a FDP
num_values = 10
theta = 4
random_values = [generate_random_value(theta) for _ in range(num_values)]
print("Valores gerados seguindo a FDP:")
print(random_values)


amostra = [0.443, 0.555, 0.727, 0.359, 0.118, 0.542, 0.449, 0.767, 0.822, 0.917, 0.700, 0.684, 0.772, 0.853, 0.977, 0.507, 0.811, 0.990, 0.998, 0.791, 0.827, 0.828, 0.906, 0.471, 0.775, 0.040, 0.873, 0.479, 0.643, 0.091, 0.953, 0.119, 0.379, 0.882, 0.538, 0.951, 0.886, 0.553, 0.688, 0.858, 0.630, 0.595]

