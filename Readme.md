Implementation of genetic algorithm to solve hyper-parameters optimization problem

The main program is found in main.py.
Ubuntu 20.0 operating system was used to run the program but it can be run in windows as well.
in order to run in ubuntu we can install Anaconda which is available as well in windows.
https://docs.anaconda.com/anaconda/install/

1. after installing from anaconda-navigator we create a new environment and name it anything (i.e keras).
2. from the new environment we click run. it will prompt a menue, we select open terminal.
3. the terminal will now run the new environment, to make sure everything is correct we should see the name of the environment in bracket at the beginning of the line.

********note: installing anaconda and creating an environment from the navigator can also be done in windows once we run the terminal the proceeding steps are the same************
 
now that our environment is setup with python 3 and ready we start installing dependencies. there main ones that don't come by default are keras and tqdm.
4. type "pip3 install Keras" or "pip install Keras" to install keras.
5. once done, install "pip3 install tqdm" or "pip install tqdm".

now that everything is installed. we enter to the directory where the Algorithms_project is located and type "python3 main.py"
inside the main.py we can see the genetic algorithm configuration is set to:
								    generations = 10  # Number of times to evole the population.
    								    population = 10  # Number of networks in each generation.
  								    dataset = 'mnist'
these can be changed to reduce the time it takes to run as it took 9 hours in my machine to complete. I would suggest to make the number of generations to 5.  								 
