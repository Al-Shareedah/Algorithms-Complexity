#Class that holds networks.
import random
import logging
from train import train_and_score

class Network():


    def __init__(self, nn_param_choices=None):
#        Initialize our network.

#        parameters:
#            nn_param_choices (dict): Parameters for the network, includes:
#                nb_neurons : [64, 128, 256]
#                nb_layers : [1, 2, 3, 4]
#                activation : ['relu', 'elu']
#                optimizer : ['rmsprop', 'adam']
       
        self.accuracy = 0.
        self.nn_param_choices = nn_param_choices
        self.network = {}  # (dic): represents MLP network parameters

    def create_random(self):
    
#       Create a random network.
        for key in self.nn_param_choices:
            self.network[key] = random.choice(self.nn_param_choices[key])

    def create_set(self, network):
#        Set network properties.

#        parameters:
#            network (dict): The network parameters

        
        self.network = network

    def train(self, dataset):
#        Train the network and store the accuracy.

#        parameters:
#            dataset (str): Name of dataset to use.

        
        if self.accuracy == 0.:
            self.accuracy = train_and_score(self.network, dataset)

    def print_network(self):
#       Print out a network.
        logging.info(self.network)
        logging.info("Network accuracy: %.2f%%" % (self.accuracy * 100))
