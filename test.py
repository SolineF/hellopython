#! /usr/local/bin/python3

message = input("Saisissez un message à coder.")
tableau_correspondances = [ 
    ['a', 'm'],
    ['b', 'n'],
    ['c', 'o'],
    ['d', 'p'],
    ['e', 'q'],
    ['f', 'r'],
    ['g', 's'],
    ['h', 't'],
    ['i', 'u'],
    ['j', 'v'], 
    ['k', 'w'],
    ['l', 'x'],
    ['m', 'y'],
    ['n', 'z'],
    ['o', 'a'],
    ['p', 'b'],
    ['q', 'c'],
    ['r', 'd'],
    ['s', 'e'],
    ['t', 'f'],
    ['u', 'g'],
    ['v', 'h'],
    ['w', 'i'],
    ['x', 'j'],
    ['y', 'k'],
    ['z', 'l'],
    ['A', 'M'],
    ['B', 'N'],
    ['C', 'O'],
    ['D', 'P'],
    ['E', 'Q'],
    ['F', 'R'],
    ['G', 'S'],
    ['H', 'T'],
    ['I', 'U'],
    ['J', 'V'], 
    ['K', 'W'],
    ['L', 'X'],
    ['M', 'Y'],
    ['N', 'Z'],
    ['O', 'A'],
    ['P', 'B'],
    ['Q', 'C'],
    ['R', 'D'],
    ['S', 'E'],
    ['T', 'F'],
    ['U', 'G'],
    ['V', 'H'],
    ['W', 'I'],
    ['X', 'J'],
    ['Y', 'K'],
    ['Z', 'L']]

code = ''

for lettre in message:
    trouvee = False
    for correspondance in tableau_correspondances:
        if lettre == correspondance[0]:
            code += correspondance[1]
            trouvee = True
            break
    if trouvee == False:
        code += lettre

print(code)

