num1 = 11
print(bin(num1))  # output: 0b1011
print(bin(num1 >> 1)) # output: 0b101
print(bin(num1 >> 2)) # output: 0b10

#int binary string back to decimal using (input binary string, base 2)
print(int(bin(num1 >> 1), 2))  #output 5 (binary = 101)