import numpy as np
from hill import Hill
from vigenere import Vigenere

def testar_algoritmos():
    texto_original = "hello"
    chave_vigenere = "bruh"

    matriz = np.array([[3,3], [2,5]])

    hill = Hill(matriz)
    vigenere = Vigenere(chave_vigenere)
    
    print("Texto original:", texto_original)
    
    texto_cifrado_hill = hill.hill_encrypt(texto_original)
    print("\nCifra de Hill:")
    print("Texto cifrado:", texto_cifrado_hill)
    texto_decifrado_hill = hill.hill_decrypt(texto_cifrado_hill)
    print("Texto decifrado:", texto_decifrado_hill)
    
    texto_cifrado_vigenere = vigenere.vigenere_encrypt(texto_original)
    print("\nCifra de Vigenère (chave:", chave_vigenere, "):")
    print("Texto cifrado:", texto_cifrado_vigenere)
    texto_decifrado_vigenere = vigenere.vigenere_decrypt(texto_cifrado_vigenere)
    print("Texto decifrado:", texto_decifrado_vigenere)

if __name__ == "__main__":
    testar_algoritmos()