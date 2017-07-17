fname = "dj.txt"
num_lines = 0
with open("dj.txt", 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
