string = "hhkbhkbhbhggyugyu"
g = [string[i]+string[i+1]+string[i+2] for i in range (0, len(string)-3, 3)]
print(g)