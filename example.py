# set up Oscar
from Oscar import Oscar
ACCESS_TOKEN ='copy the access token from your Account panel here'
scientist = Oscar(ACCESS_TOKEN)

# define your experiment hyperparameters' space here
experiment = {
  'name' : 'test',
  'parameters' : {
      'x' : { 'min' : -2, 'max' : 2 },
      'c' : [ 3, 4, 5 ]
    }
  }

# get a job suggestion
job = scientist.suggest(experiment)
print job

# do your complex job here
from random import randint
import math
duration = randint(1, 100)
loss = math.pow(job['x'] * job['c'], 2)
result = {
  'loss' : loss,
  'duration' : duration
}

# update Oscar
print result
scientist.update(job, result)