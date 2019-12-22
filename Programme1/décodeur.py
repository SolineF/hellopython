#! /usr/local/bin/python3

code = input("Saisissez un code à décoder.")
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

message_decode = ''
for lettre in code:
    trouvee = False
    for correspondance in tableau_correspondances:
        if lettre == correspondance[1]:
            message_decode += correspondance[0]
            trouvee = True
            break
    if trouvee == False:
        message_decode += lettre

print(message_decode)


