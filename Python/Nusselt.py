import sys
import numpy as np
from DedalusHelper.Dnumbers import Nusselt
from Decorators import timing

@timing
def main():
    
    if len(sys.argv) == 2:

        nusselt = Nusselt(sys.argv[1])

        time_series = nusselt.determine_time_series()[100:]
        
        if sum(np.array(time_series).imag) > 0:
            print('     This is a complex data set, make sure in the analysis task this is set to real. ')
        else:
            print('\n       The Nusselt number of this data set is {nusselt_number} with a standard deviation in the data set of {std}.\n'.format(nusselt_number = np.average(time_series),std = np.std(time_series)))

    else:
        print('     Please specify the data file.')

if __name__ == '__main__':
    main()
