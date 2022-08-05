# -*- coding: utf-8 -*-

# Autor: Valquiria Scarelli Storer
#------------------------------------------------------------------

import math

# =========================================================
def main():
    '''
        Testes da classe Complexo. 
        Normalmente, a função main() é a primeira função
        a aparecer no arquivo. 
    '''
    
    cabecalho = '''Testes da classe Complexo
    
        Cada teste ou grupo de testes deve imprimir uma mensagem
        adequada para entender seu propósito, descrevendo a chamada 
        e a saída esperada.

        Exemplo: 
        Teste da criação usando valores default:
        c0 = Complexo( )
        print(f'Complexo( ) deve imprimir 0.0+j0.0. Resposta = {c0}')
        c1 = Complexo(2)
        print(f'Complexo(2) deve imprimir 2.0+j0.0. Resposta = {c0}')
    '''
    print(cabecalho)
    c0 = Complexo( )
    print(f'Complexo( ) deve imprimir 0.0 -- Resposta = {c0}')
    c1 = Complexo(2)
    print(f'Complexo(2) deve imprimir 2.0 -- Resposta = {c1}')
    # coloque a seguir os demais testes do seu grupo
    print('testes construtor')
    v1 = Complexo(1, 0)
    v2 = Complexo(3, 1)
    v3 = Complexo(-2, 1)
    v4 = Complexo(1, -5)
    v5 = Complexo(-9, -3)

    l = [v1, v2, v3, v4, v5]
    construtor = ['1.0', '3.0+j1.0', '-2.0+j1.0', '1.0-j5.0', '-9.0-j3.0']
    for i in range(5):
        print(f"{l[i]}, deve ser {construtor[i]}")


    print('\ntestes __mul__')
    for i in l:
       for j in l:
          print(f'{i} * {j} = {i * j}')

    print('\ntestes some')
    for i in l:
        for j in l:
            print(f'{i} + {j} = {i.some(j)}')

    print('\ntestes __str__')   
    for i in l:
      print(i)     

# ===================================================================
class Complexo:
    '''Classe utilizada para representar um número Complexo.

    Um complexo é representado por dois números reais. 
    Assim, cada objeto dessa classe terá dois atributos de estado:
 
       * `real`: um número real que corresponde à parte real
       * `imag`: um número real que corresponde à parte imaginária
 
    Você deverá escrever os métodos a seguir.
    '''

    #------------------------------------------------------------------------------
    def __init__(self, r = 0.0, i = 0.0):
        '''(Complexo, float, float) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os reais `r` e `i` que 
        representam o número complexo.

        Exemplos:

        >>> c0 = Complexo() # construtor chama __init__()
        >>> c0.real
        0.0
        >>> c0.imag
        0.0
        >>> c1 = Complexo(9)
        >>> print(c1.real, c1.imag)
        9.0 0.0
        >>> c2 = Complexo(9,4)
        >>> print(c2.real, c2.imag)
        9.0 4.0
        >>> 
        '''
        self.real = float(r)
        self.imag = float(i)
        
    #------------------------------------------------------------------------------        
    def __str__(self):
        '''(Complexo) -> str

        Recebe uma referencia `self` a um objeto da classe Complexo e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplos:

        >>> ini = Complexo(8)
        >>> fim = Complexo(9,4)
        >>> fim.__str__()
        '9.0+j4.0'
        >>> ini.__str__() # chamada do método __str__()
        '8.0'
        >>> str(ini) # função str() exibe a string criada por __str__()
        '8.0'
        >>> str(fim) 
        '9.0+j4.0'
        >>> print(fim) # exibe o string criado por __str__()
        9.0+j4.0
        >>> print(ini)
        8.0
        >>>         
        '''
        if self.imag == 0.0:
            return f"{self.real}"
        if self.imag < 0:
            sinal = "-"
        if self.imag > 0:
            sinal = '+'
        if self.real == 0.0:
            if self.imag > 0:
                return f"j{self.imag}"
            return f"{sinal}j{math.fabs(self.imag)}"
        
        return f"{self.real}{sinal}j{math.fabs(self.imag)}"  

    #------------------------------------------------------------------------------        
    def some(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado da soma self + other
        
        Exemplos:

        >>> c0 = Complexo(8)
        >>> c1 = Complexo(9,4)
        >>> c2 = c0.some(c1)
        >>> print(c2)
        17.0+j4.0
        >>>         
        '''
        somareal = self.real + other.real
        somaimag = self.imag + other.imag
        return Complexo(somareal, somaimag)
        

    #------------------------------------------------------------------------------        
    def __mul__(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado do produto self * other
        
        Exemplos:

        >>> comp0 = Complexo(1, 2)
        >>> comp1 = Complexo(3, 4)
        >>> comp2 = comp0 * comp1
        >>> print(comp2)
        -5.0+j10.0
        >>>         
        '''
        real = self.real*other.real - self.imag*other.imag
        imag = self.real*other.imag + self.imag*other.real
        return Complexo(real, imag)

# =========================================================
if __name__ == '__main__':
    main()