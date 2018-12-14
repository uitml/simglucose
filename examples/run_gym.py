import gym
import numpy as np

# Register gym environment. By specifying kwargs,
# you are able to choose which patient to simulate.
# patient_name must be 'adolescent#001' to 'adolescent#010',
# or 'adult#001' to 'adult#010', or 'child#001' to 'child#010'
from gym.envs.registration import register
# register(
    # id='simglucose-adolescent2-v0',
    # entry_point='simglucose.envs:T1DSimEnvBatchStates',
    # kwargs={'patient_name': 'adolescent#002'}
# )

env = gym.make('simglucose-adolescent2-v0')

observation = env.reset()
meal = 0
for t in range(48):
    env.render(mode='human')
    print(observation)
    # Action in the gym environment is a scalar
    # representing the basal insulin, which differs from
    # the regular controller action outside the gym
    # environment (a tuple (basal, bolus)).
    # In the perfect situation, the agent should be able
    # to control the glucose only through basal instead
    # of asking patient to take bolus
    # action = env.action_space.sample()
    action = np.array([np.random.sample()/50])
    # if meal > 0:
        # action = np.array([meal/3])
    # else:
        # action = np.array([.03])

    observation, reward, done, info = env.step(action)
    meal = env.env.CHO_hist[-1]
    if done:
        print("Episode finished after {} timesteps".format(t + 1))
        break
