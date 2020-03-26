# Meme Propagation Agent-Based Model

(C) 2020 Mark M. Bailey

## About
This repository contains an ABM for meme propagation within social networks using Mesa.  Model parameters can be set in the 'model_params.py" file.  Produces a dataframe output of meme density over quasi-time (steps).

This is a work in progress and is for research purposes only.

## Model Description
This is based on a homophily model of behavior adoption.  The primary assumption is that, the greater the level of percieved affiliation (homophily) with neighbors who share the meme, the greater the probability that the interrogated agent will adopt the meme. Connection valences [-1,1] are used to approximate homophily between individual agents, where the sign indicates the valence of the relationship (negative relationships exist when individuals don't get along).  Individual agents are pseudorandomly assigned a valence value [-1,1] that determines their position on an idealized political spectrum.  Connection valences are calculated from the individual agent valences as follows: <br /><br />
Agents with valences of the same sign (aligned political views):<br />
`connection_valence = 1.0 - abs(agent_valence_1 - agent_valence_2)`<br /><br />
Agents with valences of opposite signs (unaligned political views):<br />
`connection_valence = -0.5*abs(agent_valence_1 - agent_valence_2)`<br /><br />
In this model, homophily is defined as follows:<br />
`homophily = sum(connection_valences of meme sharers in neighborhood)/sum(meme sharers in neighborhood)`<br />
Where the "neighborhood" is defined as the set of immediate connections of the interrogated agent.<br /><br />
If the homophily value is less than zero, the interrogated agent does not adopt the meme.  Otherwise, the homophily value represents the probability of the interrogated agent adopting the meme.

## Model Parameters
* density = network edge density.
* network_size = number of nodes in network.
* neg_bias = probability of node having a negative valence on an idealized, 1D political spectrum.
* meme_density = initial seed density of nodes that have shared the meme.
* steps = number of iterations in the model.
