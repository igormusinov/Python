# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class Prog:
    def read_array(self, string):
        out = []
        out = string.split(" ")
        out = map(int, out)
        return out
    
    
    def maxim(self, array, x, y):
        ans = array[x]
        summ = 0
        for index in range(x, y + 1):
            summ = summ + array[index]
            ans = max (ans, summ)
            summ = max (summ, 0)
        print ans
        return 0

    
prog = Prog()
num_array = input()
string = raw_input()
array = prog.read_array(string)
num_command = input()

for i in range(0, num_command): 
    string = raw_input()
    command = prog.read_array(string)

    if command[0] == 0:
            array[command[1] - 1] = command[2]
    if command[0] == 1:
            prog.maxim(array, command[1] - 1, command[2] - 1)
