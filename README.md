I. INTRODUCTION

Genetic algorithms (GAs) are search and optimization techniques inspired by the principles of natural evolution, first introduced by John Holland in the 1970s. 
[1]. These algorithms mimic the process of natural selection to evolve solutions over successive generations. A genetic algorithm typically involves two main processes: 
the selection of individuals for the next generation and the generation of new individuals through crossover and mutation operations. 
[2]. The selection mechanism plays a critical role by determining which individuals are chosen to reproduce and how many offspring each will contribute. 
The underlying principle of this strategy is that fitter individuals have a greater chance of being selected as parents.


II. Procedure:

1. Initialize a random population of n chromosomes, representing potential solutions to the problem.
2. Fitness Evaluation- Assess the fitness value *f(x)* of each chromosome x in the population.
3. Generate New Population-Create a new population by repeating the following steps until it is fully populated:
   a. Selection- Choose two parent chromosomes from the current population based on their fitness scores—individuals with higher fitness have a greater chance of being selected.
   b. Crossover- With a certain crossover probability, perform crossover on the selected parents to produce new offspring. If crossover does not occur, offspring are exact copies of the parents.
   c. Mutation- Apply mutation to the offspring at each gene (locus) with a given mutation probability.
   d. Acceptance- Insert the new offspring into the new population.
4. Replacement- Use the newly created population as the current population for the next iteration.
5. Termination Check- If a predefined stopping condition is met (e.g., maximum number of generations or satisfactory fitness), terminate the algorithm and return the best solution found.
6. Repeat- Otherwise, return to Step 2 and repeat the process.


III. How Genetic Algorithms Work

1. Encoding Solutions
Each potential route is represented as a sequence or permutation of locations along the commute. For example, a route could be encoded as “A-B-C-D-E-F,” where each letter corresponds to a specific location such as a street, intersection, or landmark.

2. Initialization
Begin by generating an initial population of possible routes. These can be created randomly or based on known routes. Each route in this initial population is a candidate solution.

3. Evaluation
Assess the quality of each route by evaluating factors such as total distance, traffic congestion, and travel time. The evaluation function assigns a fitness score to each route—lower scores typically indicate better solutions (e.g., shorter or faster routes).

4. Selection
Select a set of routes to serve as parents for the next generation. Routes with better fitness scores are more likely to be selected. Popular selection methods include tournament selection, roulette wheel selection, and rank-based selection.

5. Crossover
Generate new routes (offspring) by combining parts of two parent routes. For example, segments of two parent routes might be swapped to produce offspring that inherit characteristics from both parents.

6. Mutation
Introduce small random changes to the offspring to maintain diversity and avoid local optima. Examples of mutation include swapping two locations in a route, inserting a new location, or shuffling a segment of the route.

7. Creating a New Generation
Form a new population using the offspring from the crossover and mutation steps, along with some of the best-performing individuals from the previous generation. This ensures that strong solutions are preserved and propagated.

8. Termination
Repeat the process of selection, crossover, and mutation for a predefined number of generations or until a termination condition is met—such as achieving a route with an acceptably low travel time or distance.

9. Final Solution
Once the algorithm ends, the best-performing route in the final population is considered the optimal or near-optimal solution for your commute.


IV. Examples of Genetic Algorithms

1. DeepMind (Google) – Protein Structure Prediction
DeepMind, a subsidiary of Google, applied genetic algorithms in the development of AlphaFold, a revolutionary AI system capable of accurately predicting 3D protein structures. This breakthrough has significant implications for biology, drug discovery, and disease research, offering a deeper understanding of protein functions.

2. Tesla – Autonomous Driving Optimization
Tesla integrates genetic algorithms into the optimization of neural networks that power its self-driving technology. By evolving and refining these networks, GAs contribute to improving the safety, efficiency, and decision-making capabilities of Tesla’s autonomous vehicles.

3. Amazon – Logistics and Fulfillment Optimization
Amazon uses genetic algorithms to enhance its logistics and order fulfillment processes. GAs help solve complex routing and scheduling challenges, allowing Amazon to optimize delivery routes, reduce shipping times, and meet customer demands efficiently.

4. Autodesk – Design and Engineering Optimization
Autodesk incorporates genetic algorithms into its computer-aided design (CAD) software. Users can employ GAs to optimize mechanical designs, identify the most efficient shapes, and generate lightweight yet structurally sound 3D models for engineering applications.

5. Uber – Dynamic Pricing Optimization
Uber developed an Evolutionary Optimizer using genetic algorithms to refine its dynamic pricing strategies. By analyzing historical and real-time demand data, GAs help Uber evolve pricing models that balance profitability with fairness for customers.

6. Boeing – Aerodynamic Wing Design
Boeing employs genetic algorithms in projects like the Blended Wing Body (BWB) and Transonic Truss-Braced Wing (TTBW) to explore optimal wing shapes and configurations. This approach enhances aerodynamic performance, reduces structural weight, and improves fuel efficiency in aircraft design.

7. Ford – Delivery Route Optimization
Ford Motor Company uses genetic algorithms to optimize vehicle routing for deliveries. By considering traffic patterns, package dimensions, and delivery schedules, GAs enable Ford to streamline logistics, reduce travel time, and enhance operational efficiency.

8. Siemens – Manufacturing Process Optimization
Siemens applies genetic algorithms to improve manufacturing processes. GAs are used to optimize production schedules, configure machinery, and design efficient workflow layouts, leading to reduced downtime, lower costs, and increased productivity in manufacturing facilities.

9. NVIDIA – GPU Architecture Design
NVIDIA leverages genetic algorithms to fine-tune the architectural parameters of its graphics processing units (GPUs). This optimization enhances GPU performance and energy efficiency, which is critical for both gaming and artificial intelligence applications.

10. Toyota – Supply Chain Management
Toyota uses genetic algorithms to streamline its global supply chain. GAs assist in optimizing production planning, inventory control, and logistics routing, resulting in improved efficiency, cost reduction, and better responsiveness across the supply chain.

Genetic Algorithms involve a heuristic process based on the concept of natural selection. These algorithms may not deliver the best possible solution, but they can quickly identify good approximations. 
It is difficult to estimate the amount of time it takes to complete a genetic algorithm since it is dependent on population size, number of generations, and other factors.


V. Travelling Sales Man Problem
The Traveling Salesman Problem (TSP) has long captivated the interest of mathematicians, computer scientists, and operations researchers. The challenge lies in finding the shortest possible route that allows a salesman to visit a given set of cities exactly once and return to the starting point. 
As the number of cities increases, the problem's complexity grows exponentially—a phenomenon known as combinatorial explosion. Over the years, various approaches have been explored to solve the TSP, including dynamic programming, branch-and-bound, genetic algorithms, and simulated annealing.

It is important to be aware that the Traveling Salesman Problem is an NP-hard problem, meaning no algorithm that is polynomial-time has been found to solve it. This is why the algorithms discussed above are either exact yet slow for larger instances or heuristic, providing close-to-accurate solutions quickly. 
This has caused the TSP to be a very interesting and difficult issue in the realm of computational optimization, causing scientists to keep on developing more effective and precise algorithms.


VI. Implementation

Population of 16 chromosomes is used. For encoding these chromosome permutation encoding is used - in chapter about encoding you can find, how to encode permutation of cities for TSP. 
TSP is solved on complete graph (i.e. each node is connected to each other) with euclidian distances. Note that after adding and deleting city it is necessary to create new chromosomes and restart whole genetic algorithm.
You can select crossover and mutation type. I will describe what they mean.

I. Crossover

One point - part of the first parent is copied and the rest is taken in the same order as in the second parent
Two point - two parts of the first parent are copied and the rest between is taken in the same order as in the second parent
None - no crossover, offspring is exact copy of parents

II. Mutation

Normal random - a few cities are chosen and exchanged
Random, only improving - a few cities are randomly chosen and exchanged only if they improve solution (increase fitness)
Systematic, only improving - cities are systematically chosen and exchanged only if they improve solution (increase fitness)
Random improving - the same as "random, only improving", but before this is "normal random" mutation performed
Systematic improving - the same as "systematic, only improving", but before this is "normal random" mutation performed
None - no mutation
