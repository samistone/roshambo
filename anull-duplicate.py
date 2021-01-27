number = input('enter a list:')
special = []
for i in number:
    if i not in special:
        special.append(i)
print(special)
