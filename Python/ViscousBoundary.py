import matplotlib.pyplot as plt
import sys
from DedalusHelper.Dnumbers import KineticEnergy
from DedalusHelper.helper_2D import Data
from Decorators import timing
import h5py
import numpy as np

def derivative(data,z):
    derivative = []
    
    for i in range(len(data)-1):
        
        
        derivative.append((data[i+1]-data[i])/(z[i+1]-z[i]))
    return derivative

def determine_root(derivative,z):
    
    
    upper,lower,avg = 0,0,0
    zero_crossings = np.where(np.diff(np.sign(derivative)))[0]
    
    ## Determine the lower crossing ##
    x,y = [z[zero_crossings[0]],z[zero_crossings[0]+1]],[derivative[zero_crossings[0]],derivative[zero_crossings[0]+1]]
    m,b = np.polyfit(y,x,1)
    lower = b
    
    ## Determine the upper crossing ##
    x,y = [z[zero_crossings[-1]],z[zero_crossings[-1]+1]],[derivative[zero_crossings[-1]],derivative[zero_crossings[-1]+1]]
    m,b = np.polyfit(y,x,1)
    upper = b
    avg = (lower + (1-upper))/2
    return upper, lower, avg

@timing
def main():

    fig = plt.figure(figsize =(10,6))
    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams['font.size'] = 18
    plt.rcParams['axes.linewidth'] = 2
    
    
    if len(sys.argv) == 2:
        with h5py.File(sys.argv[1], mode='r') as file:
            # Load datasets
            u = np.copy(file['tasks']['u'])
            z = np.copy(file['tasks']['z'])

        z = z[0]
        z = z[0]
        Arr = np.zeros(len(z))
        for index,line in enumerate(u):
            line = Data(line).rotate_data()
            arr = [np.average(abs(lines)) for lines in line]
            Arr = Arr + arr
        
        Arr = Arr/np.shape(u)[0]
        
        plt.plot(Arr,z, color = 'black')
        plt.xlim(0,800)
        upper,lower,avg = determine_root(derivative(Arr,z),z)
        print('Most likley viscous boundarys exist at {lower} and {upper} giving an average thickness of {avg}.'.format(lower = lower, upper = upper, avg = avg))
        
        plt.plot(range(800), np.ones(800)*lower, 'k--')
        plt.plot(range(800), np.ones(800)*upper, 'k--')
    else:
        print('Please specify the data file.')



if __name__ == '__main__':
    main()
    plt.show()
