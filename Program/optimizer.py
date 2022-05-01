
##Class that has the implementation genetic algorithm.

from functools import reduce
from operator import add
import random
from network import Network

class Optimizer():
 

    def __init__(self, nn_param_choices, cut_amount=0.4,
                 random_select=0.1, mutate_chance=0.2):
    

#        parameters:
#            nn_param_choices (dict): Possible network hyber-paremters
#            cut_amount: Percentage of population to keep after
#                	 each generation
#            random_select: Probability of a rejected network
#                           remaining in the population
#            mutate_chance: Probability a network will be
#                            randomly mutated

     
        self.mutate_chance = mutate_chance
        self.random_select = random_select
        self.cut_amount = cut_amount
        self.nn_param_choices = nn_param_choices

    def create_population(self, count):
#	Create a population of random networks.

#	Args:
#            count: Number of networks to generate (the
#                   size of the population)

#        Returns:
#		Population of network objects


        pop = []
        for _ in range(0, count):
            # Create a random network.
            network = Network(self.nn_param_choices)
            network.create_random()

            # Add the network to population.
            pop.append(network)

        return pop

    @staticmethod
    
    
    def fitness(network):
#        Return the accuracy (fitness)
        return network.accuracy

    def grade(self, pop):
#        Find average fitness for a population.

#        parameters:
#            pop: The population of networks

#        Returns:
#             The average accuracy of the population

       
        summed = reduce(add, (self.fitness(network) for network in pop))
        return summed / float((len(pop)))

    def breed(self, mother, father):
#	breed two child networks    
#        parameters:
#            mother (dict): Network parameters
#            father (dict): Network parameters

#        Returns:
#             Two network objects

        
        children = []
        for _ in range(2):

            child = {}

            # select hyber-parameters for child network.
            for param in self.nn_param_choices:
                child[param] = random.choice(
                    [mother.network[param], father.network[param]]
                )

            # create a network object.
            network = Network(self.nn_param_choices)
            network.create_set(child)

            # Randomly mutate some of the children.
            if self.mutate_chance > random.random():
                network = self.mutate(network)

            children.append(network)

        return children

    def mutate(self, network):
#        Randomly mutate one hyber-parameter in network.

#        parameters:
#            network (dict): The network parameters to mutate

#        Returns:
#            (Network): A randomly mutated network object


        # Choose a random key.
        mutation = random.choice(list(self.nn_param_choices.keys()))

        # Mutate one of the params.
        network.network[mutation] = random.choice(self.nn_param_choices[mutation])

        return network

    def evolve(self, pop):
#        Evolve a population of networks.

#        parameter:
#            pop: A list of network parameters

#        Returns:
#           The evolved population of networks


        # calculate scores for each network.
        graded = [(self.fitness(network), network) for network in pop]

        # Sort the scores.
        graded = [x[1] for x in sorted(graded, key=lambda x: x[0], reverse=True)]

        # calculate number we want to keep for the next generation.
        cut_length = int(len(graded)*self.cut_amount)

        # The parents is a list of every network we want to keep.
        parents = graded[:cut_length]

        # randomly keep some networks.
        for individual in graded[cut_length:]:
            if self.random_select > random.random():
                parents.append(individual)

        # Now find out how many vacant places we have empty.
        parents_length = len(parents)
        desired_length = len(pop) - parents_length
        children = []

        # Add children, which are bred from two networks.
        while len(children) < desired_length:

            # select random female and male networks.
            male = random.randint(0, parents_length-1)
            female = random.randint(0, parents_length-1)

            # make sure they are not the same network
            if male != female:
                male = parents[male]
                female = parents[female]

                # Breed them.
                babies = self.breed(male, female)

                
                for baby in babies:
                    # Don't grow larger than desired length.
                    if len(children) < desired_length:
                        children.append(baby)

        parents.extend(children)

        return parents
