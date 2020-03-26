# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:39:44 2020

@author: metalcorebear
"""

import random
import networkx as nx


#Random output generator
def coin_flip(ptrue):
    test = random.uniform(0.0,1.0)
    if ptrue == 0:
        out = False
    elif test < ptrue:
        out = True
    else:
        out = False
    return out


#Set agent political valence magnitude
def set_magnitude(neg_bias):
    magnitude = random.uniform(0.0, 1.0)
    if coin_flip(neg_bias):
        valence = -1.0*magnitude
    else:
        valence = magnitude
    return valence


#Set agent meme state
def set_meme(meme_density):
    if coin_flip(meme_density):
        meme = True
    else:
        meme = False
    return meme


#Calculate valence of relationship between two connected agents
def find_edge_valence(user_valence_1, user_valence_2):
    if user_valence_1*user_valence_2 >= 0:
        edge_valence = 1.0 - abs(user_valence_1 - user_valence_2)
    else:
        edge_valence = -1.0*abs(user_valence_1 - user_valence_2)/2.0
    return edge_valence


#Remove duplicate and self edges
def clean_edge_list(edge_list):
    temp = []
    for (a,b) in edge_list:
        if (a,b) not in temp and (b,a) not in temp:
            if (a,b) != (b,a):
                temp.append((a,b))
    output = 1*temp
    return output


#Instantiate social network
def build_network(density, n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    nodes_list = list(G.nodes())
    edge_list = []
    top_row = 0
    for node_1 in nodes_list:
        top_row += 1
        for node_2 in range(top_row):
            if coin_flip(density):
                edge = (node_1, node_2)
                edge_list.append(edge)
    edge_list = clean_edge_list(edge_list)
    G.add_edges_from(edge_list)
    return G

#Compute meme density at any point in time.
def compute_meme_density(model):
    N = float(model.num_agents)
    meme_state = float(model.meme)
    meme_density = meme_state/N
    return meme_density
