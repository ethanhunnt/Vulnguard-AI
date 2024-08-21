string = ''
with open("code.txt") as f:
    for line in f:
		string = string + line.rstrip()

print string

