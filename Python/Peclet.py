import sys
import numpy as np
from DedalusHelper.Dnumbers import Peclet


def main():
    
    if len(sys.argv) == 2:

        peclet = Peclet(sys.argv[1])

        time_series = peclet.determine_time_series()[100:]
        print('\n The Peclet number of this data set is {peclet_number} with a standard deviation in the data set of {std}.\n'.format(peclet_number = np.average(time_series),std = np.std(time_series)))

    else:
        print('Please specify the data file.')

if __name__ == '__main__':
    main()
