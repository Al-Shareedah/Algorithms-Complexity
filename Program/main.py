##main program##
import logging
from optimizer import Optimizer
from tqdm import tqdm

# Setup logging.
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG,
    filename='log.txt'
)

def train_networks(networks, dataset):

###	Train each network, send parameter to network class.

##  parameter:
##      networks (list): Current population of networks
##	dataset (str): Dataset used for training/evaluating
    
    pbar = tqdm(total=len(networks))	##show progress bar
    for network in networks:
        network.train(dataset)
        pbar.update(1)
    pbar.close()

def get_average_accuracy(networks):
##   Get the average accuracy for a group of networks.

##    parameter:
##        networks (list): List of networks

##    Returns:
##        The average accuracy of a population of networks.

    total_accuracy = 0
    for network in networks:
        total_accuracy += network.accuracy

    return total_accuracy / len(networks)

def generate(generations, population, nn_param_choices, dataset):

##    Generate a network with the genetic algorithm.

##    parameters:
##      generations: Number of times to evole the population
##      population: Number of networks in each generation
##      nn_param_choices (dict): Parameter choices for networks
##      dataset: Dataset to use for training/evaluating

    
    optimizer = Optimizer(nn_param_choices)
    networks = optimizer.create_population(population)

    # Evolve generations.
    for i in range(generations):
        logging.info("***Doing generation %d of %d***" %
                     (i + 1, generations))

        # Train and get fitness for each networks.
        train_networks(networks, dataset)

        # calculate the average accuracy for current generation.
        average_accuracy = get_average_accuracy(networks)

        # Print out the average accuracy each generation in the log file.
        logging.info("Generation average: %.2f%%" % (average_accuracy * 100))
        logging.info('-'*80)

        # Evolve, unless last generation.
        if i != generations - 1:
            # Do the evolution.
            networks = optimizer.evolve(networks)

    # Sort final generation.
    networks = sorted(networks, key=lambda x: x.accuracy, reverse=True)

    # Print out the top 5 hyper-parameters & the scored accuracy.
    print_networks(networks[:5])

def print_networks(networks):
##	Print a list of networks.

##    Args:
##        networks: The last five networks

   
    logging.info('-'*80)
    for network in networks:
        network.print_network()

def main():

    generations = 10  # Number of times to evole the population.
    population = 10  # Number of networks in each generation.
    dataset = 'mnist'

    nn_param_choices = {
        'nb_neurons': [64, 128, 256, 512],
        'nb_layers': [1, 2, 3, 4],
        'activation': ['relu', 'elu', 'tanh', 'sigmoid'],
        'optimizer': ['rmsprop', 'adam', 'sgd', 'adagrad',
                      'adadelta', 'adamax', 'nadam'],
    }

    logging.info("***Evolving %d generations with population %d***" %
                 (generations, population))

    generate(generations, population, nn_param_choices, dataset)

if __name__ == '__main__':
    main()
