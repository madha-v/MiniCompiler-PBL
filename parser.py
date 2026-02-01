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

# ---------------- PROGRAM ----------------

def p_program(p):
    '''program : program statement
               | statement'''
    pass

# ---------------- STATEMENTS ----------------

def p_statement_decl(p):
    'statement : INT ID SEMI'
    symbol_table[p[2]] = 0

def p_statement_decl_assign(p):
    'statement : INT ID ASSIGN expression SEMI'
    symbol_table[p[2]] = p[4]
    tac.append(f"{p[2]} = {p[4]}")

def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMI'
    if p[1] not in symbol_table:
        print(f"Semantic Error: {p[1]} not declared")
    tac.append(f"{p[1]} = {p[3]}")

def p_statement_print(p):
    'statement : PRINT LPAREN ID RPAREN SEMI'
    tac.append(f"print {p[3]}")

# ---------------- EXPRESSIONS ----------------

def p_expression_plus(p):
    'expression : expression PLUS term'
    t = new_temp()
    tac.append(f"{t} = {p[1]} + {p[3]}")
    p[0] = t

def p_expression_minus(p):
    'expression : expression MINUS term'
    t = new_temp()
    tac.append(f"{t} = {p[1]} - {p[3]}")
    p[0] = t

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    t = new_temp()
    tac.append(f"{t} = {p[1]} * {p[3]}")
    p[0] = t

def p_term_div(p):
    'term : term DIVIDE factor'
    t = new_temp()
    tac.append(f"{t} = {p[1]} / {p[3]}")
    p[0] = t

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# ---------------- FACTOR ----------------

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    if p[1] not in symbol_table:
        print(f"Semantic Error: {p[1]} not declared")
    p[0] = p[1]

def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# ---------------- ERROR ----------------

def p_error(p):
    print("Syntax Error")

parser = yacc.yacc()
