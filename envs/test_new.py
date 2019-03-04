import gym
import sys
import numpy as np
import task_registrations
import trial_hist
import matplotlib.pyplot as plt
# params = {'trial_dur': 5000, 'dt': 500,
#           'stim_ev': 0.1, 'rewards':(0.0, -.1, 1., -1.)}
env = gym.make(sys.argv[1])  # , **params)
if sys.argv[3] == 'trial_hist':
    env = trial_hist.TrialHistory(env)
env.reset()
observations = []
sides = []
for stp in range(int(sys.argv[2])):
    state, rew, done, info = env.step(env.action_space.sample())
    if done:
        env.reset()

    observations.append(state)
    if 'gt' in info.keys():
        sides.append(info['gt'])

obs = np.array(observations)
plt.figure()
plt.imshow(obs.T, aspect='auto')
plt.title('observations')
plt.show()
if len(sides) > 0:
    sides = np.array(sides).reshape((1, -1))
    plt.figure()
    plt.imshow(sides, aspect='auto')
    plt.title('sides')
    plt.show()
