import tkinter as tk
from tkinter import messagebox
import numpy as np
import string
import random
from hill import Hill
from vigenere import Vigenere

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifra de Hill e Vigenère")
        self.root.configure(padx=20, pady=20)  # Padding maior para as bordas

        tk.Label(root, text="Texto (apenas letras, sem espaços):").pack(pady=5)
        self.text_entry = tk.Entry(root)
        self.text_entry.pack(pady=5)

        tk.Label(root, text="Chave Vigenère (apenas letras):").pack(pady=5)
        self.key_entry = tk.Entry(root)
        self.key_entry.pack(pady=5)

        self.result_label = tk.Label(root, text="Resultado: ", wraplength=400)
        self.result_label.pack(pady=10)

        tk.Button(root, text="Criptografar Hill", command=self.hill_encrypt).pack(pady=5)
        tk.Button(root, text="Descriptografar Hill", command=self.hill_decrypt).pack(pady=5)
        tk.Button(root, text="Criptografar Vigenère", command=self.vigenere_encrypt).pack(pady=5)
        tk.Button(root, text="Descriptografar Vigenère", command=self.vigenere_decrypt).pack(pady=5)

        matriz = np.array([[3, 3], [2, 5]])
        self.hill = Hill(matriz)

    def hill_encrypt(self):
        texto = self.text_entry.get()
        cifrado = self.hill.hill_encrypt(texto)
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, cifrado)
        self.result_label.config(text=f"Texto cifrado (Hill): {cifrado}")

    def hill_decrypt(self):
        decifrado = self.hill.hill_decrypt()
        self.result_label.config(text=f"Texto decifrado (Hill): {decifrado}")

    def vigenere_encrypt(self):
        texto = self.text_entry.get()
        chave = self.key_entry.get()
        if not chave:
            messagebox.showerror("Erro", "A chave Vigenère não pode estar vazia!")
            return
        self.vigenere = Vigenere(chave)
        cifrado = self.vigenere.vigenere_encrypt(texto)
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, cifrado)
        self.result_label.config(text=f"Texto cifrado (Vigenère): {cifrado}")

    def vigenere_decrypt(self):
        texto = self.text_entry.get()
        chave = self.key_entry.get()
        if not chave:
            messagebox.showerror("Erro", "A chave Vigenère não pode estar vazia!")
            return
        self.vigenere = Vigenere(chave)
        decifrado = self.vigenere.vigenere_decrypt(texto)
        self.result_label.config(text=f"Texto decifrado (Vigenère): {decifrado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
