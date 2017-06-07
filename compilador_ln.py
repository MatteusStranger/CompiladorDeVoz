#coding: utf-8

tokens = (
    'ADD', 'SUB', 'MUL', 'DIV', 'VV','NUMERO'
    )

# Tokens

t_ADD =  r'adição | adicionar | adicione | adiciona | somar | some | soma ' \
         r'| acumular | acumule | acumula'

t_SUB = r'tirar | tire | tira | diminuição | diminuir | diminua | redução ' \
        r'| reduzir | reduza | reduz | subtração | subtrair | subtraia'

t_MUL = r'multiplicar | multiplicação | multiplique | multiplica | vezes'

t_DIV = r'dividir | divisão | divide | divida | sobre'

t_VV  = r'valores | valor'

def t_NUMERO(t):
    r'um | dois | três | quatro | cinco | seis | sete | oito | nove | dez'
    try:
        if(t.value == 'um'):
            t.value = int(1)
        elif(t.value == 'dois'):
            t.value = int(2)
        elif(t.value == 'três'):
            t.value = int(3)
        elif(t.value == 'quatro'):
            t.value = int(4)
        elif(t.value == 'cinco'):
            t.value = int(5)
        elif(t.value == 'seis'):
            t.value = int(6)
        elif(t.value == 'sete'):
            t.value = int(7)
        elif(t.value == 'oito'):
            t.value = int(8)
        elif(t.value == 'nove'):
            t.value = int(9)
        elif(t.value == 'dez'):
            t.value = int(10)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t" \
           "| por" \
           "| e"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules
precedence = ()

# dictionary of names
names = { }

def p_S(t):
    '''S : ADD NUMERO S2 S1
         | SUB NUMERO S2 S1
         | MUL NUMERO S2 S1
         | DIV NUMERO S2 S1'''
    t[0] = ('S',t[1],t[2],t[3],t[4])

def p_S1(t):
    '''S1 : ADD NUMERO S4 S1
          | SUB NUMERO S4 S1
          | MUL NUMERO S4 S1
          | DIV NUMERO S4 S1
          | NUMERO S2 S
          |'''
    if(len(t.slice) == 5):
        t[0] = ('S1',t.slice[1].value,t.slice[2].value,t.slice[3].value,t.slice[4].value)
    elif(len(t.slice) == 3):
        t[0] = ('S1',t.slice[1].value,t.slice[2].value,t.slice[3].value)
    else:
        t[0] = ('S1','Vazio')

def p_S2(t):
    '''S2 : VV'''
    t[0] = ('S2',t[1])

def p_S4(t):
    '''S4 : VV
          |'''
    if(t[0] != None):
        t[0] = ('S4',t[1])
    else:
        t[0] = ('S4','Vazio')

def p_error(t):
    print("Syntax error at '%s'" % t)

import ply.yacc as yacc
parser = yacc.yacc()

'''while True:
    try:
        s = raw_input()   # Use raw_input on Python 2
    except EOFError:
        break

    parser.parse(s)'''

s = 'some dois valores'

print parser.parse(s)

s = 'some dois valores divida por três'

print parser.parse(s)

s = 'multiplica um valor por um valor sobre um valor'

print parser.parse(s)

s = 'subtraia dois valores e divida por um valor'

print parser.parse(s)