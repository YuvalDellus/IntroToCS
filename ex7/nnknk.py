

a = "GCAGATCCTAGCGTGCACGGGCTCTCCTGAGTCAGGAA"
result = ""

for l in a:
    if l == "G":
        temp = "C"
    if l == "C":
        temp = "G"
    if l == "A":
        temp = "U"
    if l == "T":
        temp = "A"

    result += temp

i = 0
temp = ""

for l in result:
    i += 1
    temp += l
    if i == 3:
        print(temp, end=" ")
        temp = ""
        i = 0