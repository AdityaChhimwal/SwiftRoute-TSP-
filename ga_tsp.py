import random
import math

def distance(city1, city2):
    """
    Calculate Euclidean distance between two cities.
    Each city is a tuple: (latitude, longitude)
    """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(route, cities):
    """
    Calculate the total distance of a route.
    The route is a list of indices (order of visiting cities).
    """
    dist = 0
    for i in range(len(route)):
        from_city = cities[route[i]]
        to_city = cities[route[(i + 1) % len(route)]]  # return to start
        dist += distance(from_city, to_city)
    return dist

def create_route(num_cities):
    """
    Generate a random route by shuffling city indices.
    """
    route = list(range(num_cities))
    random.shuffle(route)
    return route

def initial_population(pop_size, num_cities):
    """
    Create the initial population of random routes.
    """
    return [create_route(num_cities) for _ in range(pop_size)]

def fitness(route, cities):
    """
    Higher fitness means shorter total distance.
    """
    return 1 / total_distance(route, cities)

def selection(population, cities):
    """
    Select the top 2 fittest routes to use as parents.
    """
    sorted_routes = sorted(population, key=lambda r: fitness(r, cities), reverse=True)
    return sorted_routes[:2]

def crossover(parent1, parent2):
    """
    Combine two parents to create a new route (child).
    Ordered Crossover (OX) is used.
    """
    start, end = sorted([random.randint(0, len(parent1) - 1) for _ in range(2)])
    child = [-1] * len(parent1)
    child[start:end] = parent1[start:end]

    pointer = 0
    for gene in parent2:
        if gene not in child:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = gene
    return child

def mutate(route, mutation_rate=0.01):
    """
    Randomly swap two cities in the route with a small chance.
    """
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

def run_ga(cities, population_size=100, generations=200):
    """
    Run the Genetic Algorithm and return the best route and its distance.
    """
    population = initial_population(population_size, len(cities))

    for _ in range(generations):
        parents = selection(population, cities)
        new_population = []
        while len(new_population) < population_size:
            p1 = random.choice(parents)
            p2 = random.choice(parents)
            child = crossover(p1, p2)
            mutate(child)
            new_population.append(child)
        population = new_population

    best = min(population, key=lambda r: total_distance(r, cities))
    return best, round(total_distance(best, cities), 2)
