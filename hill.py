import numpy as np

def hill_encrypt(texto):
    matriz = np.array([[3, 3], [2, 5]])
    
    texto = ''.join(c for c in texto.lower() if c.isalpha())
    
    if len(texto) % 2 != 0:
        texto += 'x'
    
    resultado = ""
    
    for i in range(0, len(texto), 2):
        p1 = ord(texto[i]) - ord('a')
        p2 = ord(texto[i+1]) - ord('a')
        vetor = np.array([p1, p2])
        
        resultado_vetor = np.dot(matriz, vetor) % 26
        
        c1 = chr(resultado_vetor[0] + ord('a'))
        c2 = chr(resultado_vetor[1] + ord('a'))
        
        resultado += c1 + c2
    
    return resultado

def hill_decrypt(texto_cifrado):
    matriz_inversa = np.array([[15, 17], [20, 9]])
    
    texto_cifrado = ''.join(c for c in texto_cifrado.lower() if c.isalpha())
    
    resultado = ""
    
    for i in range(0, len(texto_cifrado), 2):
        c1 = ord(texto_cifrado[i]) - ord('a')
        c2 = ord(texto_cifrado[i+1]) - ord('a')
        vetor = np.array([c1, c2])
        
        resultado_vetor = np.dot(matriz_inversa, vetor) % 26
        
        p1 = chr(resultado_vetor[0] + ord('a'))
        p2 = chr(resultado_vetor[1] + ord('a'))
        
        resultado += p1 + p2
    
    return resultado