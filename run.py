# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:13:19 2020

@author: metalcorebear
"""

from model import propagation_model
import model_params
import argparse
import os
#import pandas as pd

# Specify arguments
def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Enter the output path.', required=True)
    args = vars(parser.parse_args())
    output_path = str(args['output'])
    return output_path

# Generate output file name parameters
output_path = get_path()

density = model_params.parameters['density']
nodes = model_params.parameters['network_size']
neg_bias = model_params.parameters['neg_bias']

filename = 'ABM_' + str(density) + '_' + str(nodes) + '_' + str(neg_bias) + '.csv'
output_file = os.path.join(output_path, filename)

# Instantiate model
meme_model = propagation_model()

# Number of steps to run model.
steps = model_params.parameters['steps']

for i in range(steps):
    meme_model.step()

# Generate output    
output_data = meme_model.datacollector.get_model_vars_dataframe()
output_data.to_csv(output_file, encoding='UTF8')

print (output_data)
print('Filename:')
print(filename)

print('You are a great American!!')
