from nltk import CFG, ChartParser
from nltk.tree import Tree

# Gramática de los dos lados
gramatica_izq = CFG.fromstring("""
    E -> E '+' T | E '-' T | T
    T -> T '*' F | T '/' F | F
    F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

gramatica_der = CFG.fromstring("""
    E -> T '+' E | T '-' E | T
    T -> F '*' T | F '/' T | F
    F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

def obtener_parser(direccion):
   
    if direccion == "izquierda":
        return ChartParser(gramatica_izq)
    else:
        return ChartParser(gramatica_der)

def derivacion_paso_a_paso(parser, expresion): #procesar una expresión utilizando el parser, que convierte esa expresión en una estructura organizada
  
    
    derivaciones = []
    for tree in parser.parse(expresion):
        for derivacion in tree.productions():
            derivaciones.append(str(derivacion))
    return derivaciones

def obtener_arbol(parser, expresion):
   
    arboles = []
    for tree in parser.parse(expresion):
        arboles.append(tree)
        tree.draw()
    return arboles

def construir_ast(tree):
    
    if isinstance(tree, str):  # verificar que es terminal, y si pasa esto ps se duelve tal cual 
        return tree
    if len(tree) == 1 and isinstance(tree[0], str):  # Si el nodo tiene solo un hijo y ese hijo es un valor terminal, lo devolvemos porque significa que ya no hay nada que procesar más.
        return tree[0]
    # Filtrar nodos para solo conservar operadores y terminales
    if len(tree) == 3:  # Operación binaria ps que se parece a algo asi ( a + b ) Si el nodo tiene exactamente tres elementos, con esto sabemos que tiene un operador y dos operandos >:D
        return Tree(tree[1], [construir_ast(tree[0]), construir_ast(tree[2])])
    elif len(tree) == 1:  # Paréntesis u otros
        return construir_ast(tree[0])
    return None
    

def obtener_ast(parser, expresion):
    for tree in parser.parse(expresion):
        ast = construir_ast(tree)
        ast.draw()  # Muestra el arbol Ast
        return ast

