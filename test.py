'''
FINAL PROJECT TBA

Group 10 Members : 
- Romario Viegas Francisco Marcal (1301225492)
- Muhammad Akmal Mutohar (1301224209)
- Laode Muhammad Fathir (1301224446)

PROJECT TITLE 
CREATION OF A SIMPLE PARSER TO CHECK THE VALIDITY OF INDONESIAN SENTENCE STRUCTURES 
'''


import sys
from collections import defaultdict

# This PDA accept the category S, P, O, K l like below :    

# S : aku, saya, dia, mereka, kita
# P : memakan, meminum, menonton, mendengar, membaca
# O : ikan, buku, bola, musik, tinju
# K : dikolam, dirumah, diperpustakaan, disekolah, dibandung

# Define the transition tables and terminal states
PDA_STATES = defaultdict(dict)
PDA_TERM = defaultdict(bool)

# Global variable declaration
S, P, O, K = defaultdict(dict), defaultdict(dict), defaultdict(dict), defaultdict(dict)
ST, PT, OT, KT = defaultdict(bool), defaultdict(bool), defaultdict(bool), defaultdict(bool)

# Recognize a given string whether they are valid or not using DFA
def recognize_token(string, tt, ts):
    ix = 0
    n = len(string)
    current_state = 1

    while ix < n:
        cs = tt[current_state]
        valid = string[ix] in cs
        if valid:
            current_state = cs[string[ix]]
            ix += 1
        else:
            return False

    # Check whether our last data is in terminal states
    return current_state in ts

def get_token_category(string):
    if recognize_token(string, S, ST):
        return 'S'
    if recognize_token(string, P, PT):
        return 'P'
    if recognize_token(string, O, OT):
        return 'O'
    if recognize_token(string, K, KT):
        return 'K'
    return 'x'  # x means invalid

# Validate whether a given string structure is valid or not using PDA
# List of valid structures:
# S - P - O - K
# S - P - K
# S - P - O
# S - P

# The layout is considered valid when the stack is empty at the end of the input
def pda_structure(input_string):
    stack = []

    for ch in input_string:
        if ch == 'S':
            stack.append('S')
        elif ch == 'P':
            if stack and stack[-1] == 'S':
                stack.pop()
                stack.append('P')
            else:
                return False
        elif ch == 'O':
            if stack and stack[-1] == 'P':
                stack.pop()
                stack.append('O')
            else:
                return False
        elif ch == 'K':
            if stack and (stack[-1] == 'P' or stack[-1] == 'O'):
                stack.pop()
            else:
                return False
        else:
            return False

    # Accept the input if the stack is empty or has 'P' or 'O' remaining
    return not stack or (len(stack) == 1 and (stack[-1] == 'P' or stack[-1] == 'O'))

def valid_structure(string):
    layout = ''.join(get_token_category(s) for s in string.split())
    print(layout)
    return pda_structure(layout)

if __name__ == "__main__":
    # S : aku, saya, dia, mereka, kita
    S[1] = {'a': 2, 'd': 3, 'k': 4, 's': 6, 'm': 5}
    S[2] = {'k': 7}
    S[3] = {'i': 8}
    S[4] = {'i': 9}
    S[5] = {'e': 10}
    S[6] = {'a': 11}
    S[7] = {'u': 12}
    S[9] = {'t': 8}
    S[8] = {'a': 12}
    S[10] = {'r': 13}
    S[11] = {'y': 8}
    S[13] = {'e': 14}
    S[14] = {'k': 8}
    ST[12] = True

    #P : memakan, meminum, menonton, mendengar, membaca
    P[1] = {'m': 3}
    P[3] = {'e': 4}
    P[4] = {'n': 6, 'm': 5}
    P[6] = {'d': 10, 'o': 11}
    P[11] = {'n': 16}
    P[16] = {'t': 21}
    P[21] = {'o': 17}
    P[17] = {'n': 2}
    P[5] = {'a': 7, 'b': 8, 'i': 9}
    P[7] = {'k': 12}
    P[12] = {'a': 17}
    P[8] = {'a': 13}
    P[13] = {'c': 18}
    P[18] = {'a': 2}
    P[9] = {'n': 14}
    P[14] = {'u': 19}
    P[19] = {'m': 2}
    P[10] = {'e': 15}
    P[15] = {'n': 20}
    P[20] = {'g': 22}
    P[22] = {'a': 23}
    P[23] = {'r': 2}
    PT[2] = True

    # O : ikan, buku, bola, musik, tinju
    O[1] = {'i': 2, 'b': 3, 'b': 4, 'm': 5, 't': 6}
    O[2] = {'k': 7}
    O[3] = {'u': 8}
    O[4] = {'o': 9}
    O[5] = {'u': 10}
    O[6] = {'i': 11}
    O[7] = {'a': 12}
    O[8] = {'k': 13}
    O[9] = {'l': 14}
    O[10] = {'s': 15}
    O[11] = {'n': 16}
    O[12] = {'n': 17}   
    O[13] = {'u': 17}
    O[14] = {'a': 17}
    O[15] = {'i': 18}
    O[16] = {'j': 19}
    O[18] = {'k': 17}
    O[19] = {'u': 17}
    OT[17] = True
    
    # K: dikolam, dirumah, diperpustakaan, disekolah, dikampung
    K[1] = {'d': 13}
    K[13] = {'i': 15}
    K[15] = {'k': 17, 'r': 19, 's': 20, 'p': 18, 'b': 34}
    K[17] = {'o': 22}
    K[22] = {'l': 27}
    K[27] = {'a': 31}
    K[31] = {'m': 3}
    K[19] = {'u': 24}
    K[24] = {'m': 4}
    K[20] = {'e': 25}
    K[25] = {'k': 29}
    K[29] = {'o': 33}
    K[33] = {'l': 4}
    K[4] = {'a': 7}
    K[7] = {'h': 3}
    K[18] = {'e': 23}
    K[23] = {'r': 28}
    K[28] = {'p': 32}
    K[32] = {'u': 2}
    K[2] = {'s': 6}
    K[6] = {'t': 8}
    K[8] = {'a': 9}
    K[9] = {'k': 10}
    K[10] = {'a': 11}
    K[11] = {'a': 12}
    K[12] = {'n': 3}
    K[34] = {'a': 35}
    K[35] = {'n': 36}
    K[36] = {'d': 37}
    K[37] = {'u': 38}
    K[38] = {'n': 39}
    K[39] = {'g': 3}
    KT[3] = True

    in_string = input("Enter the string to validate: ")
    print(f"The string is: {in_string}")
    valid = valid_structure(in_string)
    if valid:
        print("The string is valid")
    else:
        print("The string is not valid")


