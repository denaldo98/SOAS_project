#  ---------------------------- 1 AGENT ----------------------------------#

# import libraries
import numpy as np
import utils as utl
import matplotlib.pyplot as plt
import pickle

# import environmnents
import environment
import environment_prey


# GRID SIZE
N = 10

# Q-LEARNING PARAMS
epsilon = 0.1
alpha = 0.1
gamma = 0.9

# TRAINING PARAMS
n_episodes = 20000 # num of episodes
max_steps = 5000 # max steps of each episode


# -------------------------- RUN EXPERIMENTS ----------------------------#

# CREATE ENVIRONMENT by passing the grid size
#env = environment.Environment(N) # with fixed prey
env = environment_prey.Environment(N) # with moving prey

# define NAME OF THE MODEL for saving files with correct names
#model_name = "single_Agent_" + "Fixed_Prey_" + "Grid_" + str(N)
model_name = "single_Agent_" + "Moving_Prey_" + "Grid_" + str(N)


# RUN THE FUNCTIONS defined in utils.py

# perform 1 TRAINING of n_episodes
#time_goal = utl.run_multiple_episodes(n_episodes, env, max_steps, epsilon, alpha)

# perform 1 TRAINING of n_episodes with GRAPHICAL SIMULATION
#time_goal = utl.run_training_simulation(n_episodes, env, max_steps, epsilon, alpha)

# repat TRAINING process n_processes time 
# with_prey parameter in the repeat_process() function is 1 if environment with moving prey
n_processes = 20
time_goal = utl.repeat_process(n_processes, n_episodes, max_steps, epsilon, alpha, 1, N)


'''
# SAVE environment object into file for later retrieval
# useful when performing 1 training of n_episodes to later see what the agents have learned
with open(model_name + "_env", "wb") as fp:
    pickle.dump(env, fp)
'''

# save TG into file for later retrieval
with open(model_name + "_list", "wb") as fp:
    pickle.dump(time_goal, fp)


# PLot TG over the episodes
utl.plot_time_to_goal(model_name, n_episodes, time_goal)
plt.clf()

# Plot TG averaged every 100 episodes
utl.plot_time_to_goal(model_name, n_episodes,  time_goal, avg=1)
plt.clf()



'''
# ---------- load environment for retrieving Q-table or for running simulation with the learned policy ---------- #
# select the name of the model to load
model_name = "single_Agent_" + "Fixed_Prey_" + "Grid_" + str(N)
with open(model_name + "_env", "rb") as fp:
    env = pickle.load(fp)

# retrieve Q-table
print(env.preds[0].Q)

# run simulation after training
#utl.run_simulation(env)



# ------------------------------------ COMPARISONS of different models learning ----------------------------------#

# ----------load TG lists for combined plot----------- #
# load TG lists for combined plot
# load model with fixed prey
model_name1 = "single_Agent_" + "Fixed_Prey_" + "Grid_" + str(N)
with open(model_name1 + "_list", "rb") as fp:
    tg1 = pickle.load(fp)

# load model with moving prey
model_name2 = "single_Agent_" + "Moving_Prey_" + "Grid_" + str(N)
with open(model_name2 + "_list", "rb") as fp:
    tg2 = pickle.load(fp)

# Plot comparison of TGs 
utl.plot_TG_comparison(model_name1, model_name2, tg1, tg2, n_episodes)
plt.clf()
'''

