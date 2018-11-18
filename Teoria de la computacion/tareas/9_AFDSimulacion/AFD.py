'''
Instituto Tecnologico Jose Mario Molina Pasquel y Henriquez Campus Zapopan
Teoria de la Computacion
Automata Finito Determinista
David Castro Ruiz

Instrucciones:
        cadena          - Cadena a evaluar el automata
        edo_inicial     - Numero del estado actual, a partir del cual evaluara <<cadena>>
        alfabeto        - Diccionario que posee las reglas de transicion del automata
        edo_final       - Lista con los estados finales
'''


class Automata:
    def __init__(self, _cadena, _inicial, _final, _alfabeto):
        self.cadena = _cadena
        self.edo_final = _final
        self.alfabeto = _alfabeto
        self.edo_inicial = _inicial
        self.dict = {}


def AFD(automata):
    if automata.cadena == "":
        return automata.edo_inicial in automata.edo_final
    else:
        entrada = automata.cadena[0]
        if (automata.edo_inicial, entrada) in automata.alfabeto:
            q = 'Q%d' % (automata.edo_inicial - 1)
            if q not in automata.dict:
                automata.dict.update({q: []})
            automata.dict[q].append('(Q%d -%s);' % (automata.alfabeto[(automata.edo_inicial, entrada)] - 1, entrada))
            automata.edo_inicial = automata.alfabeto[(automata.edo_inicial, entrada)]
            automata.cadena = automata.cadena[1:]
            return AFD(automata)
        else:
            return False


def print_results(automata):
    print("+--------------+-------STRING--------+---------------+")
    print automata.cadena
    result = AFD(automata)
    print("+--------------+--Transition Table---+---------------+")
    for i in sorted(automata.dict):
        from_state = '%s: ' % i
        one_line = ''
        for value in automata.dict[i]:
            one_line += value
        print from_state + one_line
    print("+--------------+-------RESULT--------+---------------+")
    print '                        %s\n\n' % result


# Ejecicios de la practica Simulacion

def M4():
    '''
    1)  a2:
    conjunto de palabras que tienen al menos un 1 y un numero par de 0s siguiente al ultimo 1'''
    a1 = Automata
    a1.edo_inicial = 1
    a1.edo_final = [3]
    a1.alfabeto = {(1, '0'): 1,
                   (1, '1'): 2,
                   (2, '0'): 3,
                   (2, '1'): 2,
                   (3, '0'): 2,
                   (3, '1'): 3,
                   }
    a1.dict = {}

    test = ['00001',
            '0100',
            '00100000',
            '010101010']

    for t in test:
        a1.cadena = t
        print_results(a1)


def M5():
    '''
    2)  a2:
        conjunto de palabras que contengan al menos dos pares del estado inicial
        q0:1 q1:2 q2:3 q3:4 q4:5'''

    a2 = Automata
    a2.edo_inicial = 1
    a2.edo_final = [4, 2]
    a2.alfabeto = {(1, 'a'): 4,
                   (4, 'a'): 4,
                   (4, 'b'): 5,
                   (5, 'b'): 5,
                   (5, 'a'): 4,
                   (1, 'b'): 2,
                   (2, 'b'): 2,
                   (2, 'a'): 3,
                   (3, 'a'): 3,
                   (3, 'b'): 2,
                   }

    a2.dict = {}

    test = ['aabba',
            'bababab',
            'abaaab',
            'aababb']

    for t in test:
        a2.cadena = t
        print_results(a2)


# M4()
M5()
