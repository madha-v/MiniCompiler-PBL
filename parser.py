import ply.yacc as yacc
from lexer import tokens

symbol_table = {}
tac = []
temp_count = 0

def new_temp():
    global temp_count
    t = f"t{temp_count}"
    temp_count += 1
    return t

def p_program(p):
    '''program : program statement
               | statement'''
    pass

# ---------- STATEMENTS ------------

def p_statement_decl(p):
    'statement : INT ID SEMI'
    symbol_table[p[2]] = 0

def p_statement_decl_assign(p):
    'statement : INT ID ASSIGN expression SEMI'
    symbol_table[p[2]] = p[4]
    tac.append(f"{p[2]} = {p[4]}")

def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMI'
    tac.append(f"{p[1]} = {p[3]}")

# -------- EXPRESSIONS ------------

def p_expression_plus(p):
    'expression : expression PLUS term'
    t = new_temp()
    tac.append(f"{t} = {p[1]} + {p[3]}")
    p[0] = t

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    t = new_temp()
    tac.append(f"{t} = {p[1]} * {p[3]}")
    p[0] = t

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]

def p_error(p):
    print("Syntax Error")

parser = yacc.yacc()
