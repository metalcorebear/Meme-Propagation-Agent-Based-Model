# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:23:21 2020

@author: metalcorebear
"""

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import agent
import model_functions
import model_params

class propagation_model(Model):
    
    def __init__(self):
        super().__init__(Model)
        
        density = model_params.parameters['density']
        nodes = model_params.parameters['network_size']
        neg_bias = model_params.parameters['neg_bias']
        meme_density = model_params.parameters['meme_density']
        
        G = model_functions.build_network(density, nodes)
        self.grid = NetworkGrid(G)
        self.schedule = RandomActivation(self)
        
        self.running = True
    
        for node in range(nodes):
            new_agent = agent.tweeter(self.next_id(), node, self, neg_bias, meme_density)
            self.grid.place_agent(new_agent, node)
            self.schedule.add(new_agent)
    
        self.meme = 0
        self.datacollector = DataCollector(model_reporters={"meme_density": model_functions.compute_meme_density})
        self.datacollector.collect(self)
    
    def step(self):
        self.meme = 0
        self.schedule.step()
        
        self.datacollector.collect(self)
        
        if self.meme == self.schedule.get_agent_count():
            self.running = False
