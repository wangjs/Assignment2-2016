import os
import getpass
import sys
import time

import numpy as np
import tensorflow as tf
from q2_NER import NERModel, test_NER, Config
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# %matplotlib inline

number_of_exp = 10
part1 = number_of_exp/2
part2 = number_of_exp - part1
lr1 = np.random.random_sample([part1]) / 1000
lr2 = np.random.random_sample([part2]) / 10000
LEARNING_RATE = np.concatenate((lr1, lr2))
LEARNING_RATE.sort()
results = []
times = []

for lr in LEARNING_RATE:
    config = Config(lr=lr)
    val_loss, duration = test_NER(config,
                                  save=False,
                                  verbose=False,
                                  debug=False)
    results.append(val_loss)
    times.append(duration)


LEARNING_RATE = list(LEARNING_RATE)
best_result = min(list(zip(results, LEARNING_RATE, times)))
result_string = """In an experiment with {0} random constants
the best learning rate constant is {1} with val_loss = {2}. Using
this constant the training will take {3} seconds""".format(number_of_exp,
                                                           best_result[1],
                                                           best_result[0],
                                                           best_result[2])
print(result_string)

# Make a plot of lr vs loss
plt.plot(LEARNING_RATE, results)
plt.xscale('log')
plt.xlabel("learning rate")
plt.ylabel("loss")
plt.savefig("NER_lr.png")
plt.show()
