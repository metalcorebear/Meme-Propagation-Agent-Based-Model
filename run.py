# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:13:19 2020

@author: metalcorebear
"""

from model import propagation_model
import model_params
#import matplotlib.pyplot as plt
#import numpy as np

meme_model = propagation_model()

# Number of steps to run model.
steps = model_params.parameters['steps']

for i in range(steps):
    meme_model.step()
    
output_data = meme_model.datacollector.get_model_vars_dataframe()

print (output_data)
