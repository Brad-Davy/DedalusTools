import matplotlib.pyplot as plt
import sys
from DedalusHelper.Dnumbers import KineticEnergy
from Decorators import timing
import h5py
import numpy as np


@timing
def main():

    fig = plt.figure(figsize =(10,6))
    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams['font.size'] = 18
    plt.rcParams['axes.linewidth'] = 2
    
    
    if len(sys.argv) == 2:
        with h5py.File(sys.argv[1], mode='r') as file:
            # Load datasets
            u = np.copy(file['tasks']['Θ'])
            z = np.copy(file['tasks']['z'])[-1]
            
            
            ## Create an array with the basic state in ##
    
        T = (1 - z[0])

        full_array = np.zeros(np.shape(u[0])[1])

        for data in u:
            avg = []
            data = np.rot90(data, k=1, axes=(0, 1))
            for lines in data:
                avg.append(np.average(lines))
        
            full_array = full_array + avg

        full_array = full_array/(2*np.amax(full_array))


        plt.plot(T + full_array[::-1] -0.5,z[0],color = 'black')
        
    else:
        print('Please specify the data file.')

if __name__ == '__main__':
    main()
    plt.show()
