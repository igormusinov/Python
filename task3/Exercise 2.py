import numpy as np

def main():
#not the best way
    a = np.array([[4, 3], [2, 1], [4, 3], [2, 1]])
    r = np.tile(a, 3)
    print r

if __name__ == '__main__':
    main()
