from hill import hill_encrypt, hill_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt

def testar_algoritmos():
    texto_original = "testandoalgoritmos"
    chave_vigenere = "bruh"
    
    print("Texto original:", texto_original)
    
    texto_cifrado_hill = hill_encrypt(texto_original)
    print("\nCifra de Hill:")
    print("Texto cifrado:", texto_cifrado_hill)
    texto_decifrado_hill = hill_decrypt(texto_cifrado_hill)
    print("Texto decifrado:", texto_decifrado_hill)
    
    texto_cifrado_vigenere = vigenere_encrypt(texto_original, chave_vigenere)
    print("\nCifra de Vigenère (chave:", chave_vigenere, "):")
    print("Texto cifrado:", texto_cifrado_vigenere)
    texto_decifrado_vigenere = vigenere_decrypt(texto_cifrado_vigenere, chave_vigenere)
    print("Texto decifrado:", texto_decifrado_vigenere)

if __name__ == "__main__":
    testar_algoritmos()