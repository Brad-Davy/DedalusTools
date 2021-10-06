import matplotlib.pyplot as plt
import sys
from DedalusHelper.Dnumbers import KineticEnergy
from Decorators import timing



@timing
def main():

    fig = plt.figure(figsize =(10,6))
    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams['font.size'] = 18
    plt.rcParams['axes.linewidth'] = 2
    
    if len(sys.argv) == 2:
        kinetic = KineticEnergy(sys.argv[1])
        spectrum = kinetic.average_over_time(mode = 's')
        plt.plot(spectrum,color = 'black')
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel('Wave Number')
        plt.ylabel('Kinetic Energy')
        plt.show()
    
    else:
        print('Please specify the data file.')

if __name__ == '__main__':
    main()
