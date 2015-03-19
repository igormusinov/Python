import numpy as np

def main():
    array = np.arange(1, 16, 1).reshape((5, 3), order = "F")
    new_array = array[[2, 4]]
    print new_array
   
if __name__ == '__main__':
    main()
