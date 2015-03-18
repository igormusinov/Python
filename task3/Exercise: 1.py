import matplotlib.pyplot as plt
import numpy as npy

def main():
    x = npy.arange(-100, 100, 0.13)
    y = npy.cos(x)
    plt.plot(x, y)
    plt.show()
    matrix = npy.random.rand(30, 30)
    plt.imshow(matrix, cmap=plt.cm.gray)
    plt.show()
    
if __name__ == '__main__':
    main()
