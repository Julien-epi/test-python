with open('data.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if '@' in line and line.endswith('.com'):
        print(line + ' est un email valide')
    else:
        print(line + ' n\'est pas un email valide')
