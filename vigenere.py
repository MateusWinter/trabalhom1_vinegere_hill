class Vigenere:
    def __init__(self, chave):
        self.chave = chave
        self.cifra = ""

    def vigenere_encrypt(self, texto):
        texto = ''.join(c for c in texto.lower() if c.isalpha())
        chave = ''.join(c for c in self.chave.lower() if c.isalpha())
        
        resultado = ""
        chave_indice = 0
        
        for char in texto:
            k = ord(chave[chave_indice % len(chave)]) - ord('a')
            char_encriptado = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            resultado += char_encriptado
            chave_indice += 1
        
        return resultado

    def vigenere_decrypt(self, texto_cifrado):
        texto_cifrado = ''.join(c for c in texto_cifrado.lower() if c.isalpha())
        chave = ''.join(c for c in self.chave.lower() if c.isalpha())
        
        resultado = ""
        chave_indice = 0
        
        for char in texto_cifrado:
            k = ord(chave[chave_indice % len(chave)]) - ord('a')
            char_decriptado = chr((ord(char) - ord('a') - k) % 26 + ord('a'))
            resultado += char_decriptado
            chave_indice += 1
        
        return resultado