import numpy as np

def mod_inverse(a, mod):
    """
    Calcula o inverso modular de 'a' em relação a 'mod'
    Retorna None se o inverso modular não existir.
    """
    a = a % mod
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    return None

def modular_inverse_matrix(matrix, mod=26):
    """
    Calcula a inversa modular de uma matriz no módulo 'mod'.
    Retorna None se a matriz não for invertível módulo 'mod'.
    """
    det = int(round(np.linalg.det(matrix)))  # Determinante da matriz
    det_inv = mod_inverse(det, mod)  # Inverso modular do determinante

    if det_inv is None:
        raise ValueError("A matriz não tem inversa modular em módulo 26.")

    # Matriz adjunta
    adj = np.round(det * np.linalg.inv(matrix)).astype(int) % mod

    # Matriz inversa modular
    inv_matrix = (det_inv * adj) % mod
    return inv_matrix

class Hill:
    def __init__(self, matriz, matriz_inversa = 0):
        '''
        Inicialização do objeto com a chave (matriz), a matriz inversa e a verificação se o texto é ímpar iniciado como falso.
        '''
        self.matriz = matriz
        self.matriz_inversa = modular_inverse_matrix(matriz, 26)
        # self.matriz_inversa = matriz_inversa
        self.added_x = False  # Variável para determinar se um x foi adicionado ao final da cifra

        # Forçado para manter apenas matrizes quadradas de tamanho 2
        if len(matriz) != 2:
            raise ValueError("A matriz e sua inversa de devem ter o mesmo formato e tamanho 2")
            
    
    def hill_encrypt(self, texto):
        '''
        Realiza a criptografia de hill
        Cifra de hill parametrizada com tamanho da matriz quadrada = 2
        '''
        texto = ''.join(c for c in texto.lower() if c.isalpha())    # todos os caracteres do texto são passados para lowercase se forem [A-Za-z]. Se houver números ou caracteres especiais, os mesmos serão desconsiderados
        
        if len(texto) % 2 != 0:                 # se o texto tiver um número ímpar de caracteres, adiciona um 'x' ao final do texto
            texto += 'x'
            self.added_x = True                 # atualiza a variável added_x
        
        resultado = ""                          # inicializa o resultado da cifra como vazio
        
        for i in range(0, len(texto), 2):       # loop até o fim do texto claro com passo 2 definido pela matriz quadrada
            p1 = ord(texto[i]) - ord('a')       # realiza a subtração do valor do texto do ascii da primeira posição com a letra a em ascii para ter um valor de 0 a 25
            p2 = ord(texto[i+1]) - ord('a')     # realiza a subtração do valor do texto do ascii da segunda posição com a letra a em ascii para ter um valor de 0 a 25
            vetor = np.array([p1, p2])          # cria o vetor para multiplicação com a matriz
            
            resultado_vetor = np.dot(self.matriz, vetor) % 26       # multiplicação vetorial da matriz com o vetor de caracteres para gerar os valores cifrados módulo 26
            
            c1 = chr(resultado_vetor[0] + ord('a'))                 # retornando para o espaço do ascii (1º caracter)
            c2 = chr(resultado_vetor[1] + ord('a'))                 # retornando para o espaço do ascii (2º caracter)
            
            resultado += c1 + c2                # adiciona os caracteres cifrados ao resultado
        
        return resultado                        # retorna a cifra de hill

    def hill_decrypt(self, texto_cifrado):
        '''
        Decifragem de um texto cifrado pelo método de hill
        Cifra de hill parametrizada com tamanho da matriz quadrada = 2
        É esperado que o texto cifrado tenha um número par de caracteres.
        '''
        texto_cifrado = ''.join(c for c in texto_cifrado.lower() if c.isalpha()) # garante que o texto cifrado seja um texto com caracteres minúsculos e no espaço de [A-Za-z]
        
        resultado = ""                              # cria a variável para receber o resultado da decifragem 
        
        for i in range(0, len(texto_cifrado), 2):   # loop até o fim do texto cifrado com passo 2 definido pela matriz quadrada
            p1 = ord(texto_cifrado[i]) - ord('a')   # realiza a subtração do valor do texto do ascii da primeira posição com a letra a em ascii para ter um valor de 0 a 25
            p2 = ord(texto_cifrado[i+1]) - ord('a') # realiza a subtração do valor do texto do ascii da segunda posição com a letra a em ascii para ter um valor de 0 a 25
            vetor = np.array([p1, p2])              # cria o vetor para multiplicação com a matriz inversa
            
            resultado_vetor = np.dot(self.matriz_inversa, vetor) % 26   # multiplicação da matriz inversa com o vetor de caracteres para decifrar o texto cifrado módulo 26
            
            p1 = chr(resultado_vetor[0] + ord('a'))                     # retornando para o espaço ascii (1º caracter)
            p2 = chr(resultado_vetor[1] + ord('a'))                     # retornando para o espaço ascii (2º caracter)
            
            resultado += p1 + p2                    # adiciona os caracteres decifrados ao resultado

        if self.added_x and resultado[-1] == 'x':   # se x foi adicionado na cifra e o último caracter da cifra for x
            resultado = resultado[:-1]              # retorna o resultado desconsiderando o último caracter
    
        return resultado                            # retorna o texto decifrado