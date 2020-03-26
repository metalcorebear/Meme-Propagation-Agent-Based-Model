# Meme Propagation Agent-Based Model

(C) 2020 Mark M. Bailey

## About
This repository contains an ABM for meme propagation within social networks using Mesa.  Model parameters can be set in the 'model_params.py" file.  Produces a dataframe output of meme density over time (steps).

This is a work in progress and is for research purposes only.

## Model Parameters
density = network edge density.
network_size = number of nodes in network.
neg_bias = probability of node having a negative valence on an idealized, 1D political spectrum.
meme_density = initial seed density of nodes that have shared the meme.
steps = number of steps to run the model.
