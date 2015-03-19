import numpy as np

def main():
    array = np.arange(1, 16, 1).reshape((5, 3), order = "F")
    print array
    new_array = array[[2, 4]]
    print new_array
    #b = a[[2, 4]]
    #print b

if __name__ == '__main__':
    main()
