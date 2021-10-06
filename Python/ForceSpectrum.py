import numpy as np
import matplotlib.pyplot as plt
import sys,h5py
from DedalusHelper.spectral import helper_2d

def load_data(file_path):
    with h5py.File(file_path, mode='r') as file:
        ## Load datasets ##
        diffusion_term = abs(np.copy(file['tasks']['diffusion_term']))
        z_pressure = abs(np.copy(file['tasks']['z_pressure']))
        non_linear = abs(np.copy(file['tasks']['non-linear']))
        temperature = abs(np.copy(file['tasks']['Temperature']))

    return diffusion_term, z_pressure, non_linear, temperature


def main(file_path):

    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams['font.size'] = 18

    diffusion_term, z_pressure, non_linear, temperature = load_data(file_path)
    time_steps = np.shape(diffusion_term)[0]
    
    N = np.shape(diffusion_term)[1]
    
    diffusion = np.zeros(N)
    z = np.zeros(N)
    non = np.zeros(N)
    temp = np.zeros(N)
    
    for time_step in range(1,time_steps):

        diffusion += helper_2d(diffusion_term[time_step]).average_over_z()
        z += helper_2d(z_pressure[time_step]).average_over_z()
        non += helper_2d(non_linear[time_step]).average_over_z()
        temp += helper_2d(temperature[time_step]).average_over_z()
    
    fig = plt.figure(figsize = (12,6))
    plt.plot(diffusion/time_steps,label = 'Diffusion')
    plt.plot(z/time_steps,label = 'Pressure')
    plt.plot(non/time_steps, label = 'Non-Linear')
    plt.plot(temp/time_steps,label = 'Perturbation')
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.xlabel('Wave Number')
    plt.ylabel('Magnitude of the forces')
    plt.show()
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Please specify the data file.')
