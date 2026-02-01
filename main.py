
from lexer import lexer
from parser import parser, tac, symbol_table
from optimizer import optimize
from targetcode import generate

print("Enter your program (end with empty line):")
lines=[]
while True:
    line=input()
    if line=="":
        break
    lines.append(line)

data="\n".join(lines)

parser.parse(data)

print("\nSYMBOL TABLE:",symbol_table)

print("\nTHREE ADDRESS CODE:")
for i in tac:
    print(i)

opt = optimize(tac)

print("\nOPTIMIZED CODE:")
for i in opt:
    print(i)

print("\nTARGET CODE:")
for i in generate(opt):
    print(i)
