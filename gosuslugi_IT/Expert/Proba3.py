# -*- coding: utf-8 -*-
import re
definition = '(define (add x y) (x + y))'
expression = '(add 2 3)'

regex = r'\(define \((?P<func_args>.+)\) \((?P<function>.+)\)\)'
match = re.search(regex, definition)
d = match.groupdict() #{'func_args': 'add x y', 'function': 'x + y'}
name_func = d['func_args'].split()[0]  #add
args = d['func_args'].split()[1:]  #['x', 'y']
function = d['function']  #x + y

print(name_func)
print(args)
print(function)
