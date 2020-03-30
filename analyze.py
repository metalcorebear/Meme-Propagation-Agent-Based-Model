# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:51:24 2020

@author: metalcorebear
"""

import pandas as pd
import argparse
import matplotlib.pyplot as plt
import os
from functools import reduce
from datetime import date as datemethod
import numpy as np
import scipy

# Specify arguments
def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Enter the output path.', required=True)
    parser.add_argument('-a', '--average', help='Calculate average (True or False).', required=True)
    args = vars(parser.parse_args())
    output_path = str(args['output'])
    average_bool = str(args['average'])
    return output_path, average_bool

# Collect data files
def get_files(output_path):
    out_files = []
    for root, dirs, files in os.walk(output_path):
        for file_ in files:
            if ('.csv' and 'ABM') in file_:
                out_files.append(os.path.join(root, file_))
    return out_files

# Get file parameters
def get_params(out_files):
    basenames = []
    for file_path in out_files:
        basenames.append(os.path.basename(file_path))
    output = []
    for basename in basenames:
        b = basename.split('_')
        out_dict = {'basename':basename, 'density':b[1], 'n':b[2], 'neg_bias':b[3].split('.csv')[0]}
        output.append(out_dict)
    return output

# Import files
def import_files(out_files):
    file_dicts = get_params(out_files)
    dfs = []
    column_names = []
    i = 0
    for path_ in out_files:
        df = pd.read_csv(path_)
        for filename in file_dicts:
            if filename['basename'] == os.path.basename(path_):
                i += 1
                new_name = str(filename['density']) + '_' + str(filename['n']) + '_' + str(filename['neg_bias']) + '_' + str(i)
                column_names.append(new_name)
                df2 = df.rename(columns={'meme_density':new_name})
        dfs.append(df2)
    return dfs, column_names

# Concatenate dataframes
def concat_dfs(dfs, column_names, average_bool, output_path):
    df_out = reduce(lambda x, y: pd.merge(x, y), dfs)
    df_out = df_out[column_names]
    if average_bool:
        df_out['average'] = df_out.mean(axis=1)
        _, df_out, _ = df_fit(df_out, output_path)
    return df_out

def sigmoid(x,k,x0,c):
    y = c / (1 + np.exp(-k*(x-x0)))
    return y

def df_fit(df_out, output_path):
    x = list(df_out.index)
    x = np.array(x)
    y = list(df_out['average'])
    y = np.array(y)
    try:
        popt, pcov = scipy.optimize.curve_fit(sigmoid, x, y)
        perr = np.sqrt(np.diag(pcov))
    except:
        popt = np.array([0.0, 0.0, 0.0])
    df_out['fit'] = sigmoid(x, *popt)
    param_df = pd.DataFrame({'k':popt[0], 'k_err':perr[0], 'x0':popt[1], 'x0_err':perr[1], 'c':popt[2], 'c_err':perr[2]}, index=[0])
    param_df.to_csv(os.path.join(output_path, 'param_file.csv'))
    return popt, df_out, perr

# Plot output
def plot_output(df_out, output_path):
    today = datemethod.strftime(datemethod.today(), '%Y-%m-%d')
    plot_name = today + '.png'
    csv_name = today + '.csv'
    df_out.to_csv(os.path.join(output_path, csv_name), encoding='UTF8')
    ax = plt.subplot(111)
    for column in list(df_out.columns):
        if column == 'average':
            ax.plot(df_out[column], label=column)
        elif column == 'fit':
            ax.plot(df_out[column], label=column)
        else:
            ax.plot(df_out[column], '--', label=column)
    plt.title('ABM Model Output')
    plt.xlabel('Step')
    plt.ylabel('Meme Density')
    ax.legend()
    plt.savefig(os.path.join(output_path, plot_name), dpi=300)
    plt.close()
    

if __name__ == '__main__':
    print('Generating plot and output CSV file...')
    output_path, average_bool = get_path()
    out_files = get_files(output_path)
    dfs, column_names = import_files(out_files)
    df_out = concat_dfs(dfs, column_names, average_bool, output_path)
    plot_output(df_out, output_path)
    print('You are a great American!!')
    