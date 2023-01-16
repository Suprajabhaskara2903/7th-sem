# program = '''

# '''
# keywords = {'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double' 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'}
# operators = {'!', '<', '>', '=', '+', '-', '/', '*', '%'}
# delimiters = {';', ',', '\n', '\t', ' '}
# brackets = {'(', ')', '{', '}', '[', ']'}
# names = {}
# for i in operators:
#     names[i] = 'operator'
# for i in keywords:
#     names[i] = 'keyword'
# for i in brackets:
#     names[i] = 'bracket'
# for i in delimiters:
#     names[i] = 'delimiter'
# i = 0
# tokens = {}
# token = ""
# while(i < len(program)):
#     if program[i] in names:
#         tokens[program[i]] = names[program[i]]
#         if token in keywords:
#             tokens[token] = 'keyword'
#         else:
#             tokens[token] = 'identifier'
#         token = ""
#         i += 1
#         continue
#     token += program[i]
#     i += 1
# for token in tokens:
#     print(token + " " + tokens[token])

import numpy as np

a = np.array([1,2,3])

b= np.array([4,5,6])

C = a*b

d = np.dot(a,b)

print(c,d)