import numpy as np
from dedalus.tools import post
import sys, pathlib
from Decorators import timing



@timing
def main(file_path):
    post.merge_process_files(file_path, cleanup=True)
    set_paths = list(pathlib.Path(file_path).glob("analysis_s*.h5"))
    post.merge_sets("{file_path}/analysis.h5".format(file_path=file_path), set_paths, cleanup=True)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Please specify the data file.')
