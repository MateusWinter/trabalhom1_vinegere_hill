# Cifras de Hill e Vigenère

Este projeto implementa algoritmos de criptografia e descriptografia para as Cifras de Hill e Vigenère.

## Estrutura do Projeto

O projeto está organizado em três arquivos:
- `hill.py`: Contém as funções para criptografar e descriptografar usando a Cifra de Hill
- `vigenere.py`: Contém as funções para criptografar e descriptografar usando a Cifra de Vigenère
- `main.py`: Programa principal para testar os algoritmos

## Descrição

O programa contém quatro funções principais:
- `hill_encrypt`: Criptografa um texto usando a Cifra de Hill
- `hill_decrypt`: Descriptografa um texto usando a Cifra de Hill
- `vigenere_encrypt`: Criptografa um texto usando a Cifra de Vigenère
- `vigenere_decrypt`: Descriptografa um texto usando a Cifra de Vigenère

## Como funciona

### Cifra de Hill
- Usa uma matriz 2x2 para criptografar o texto: [[3,3], [2,5]]
- Usa a matriz inversa para descriptografar: [[15,17], [20,9]]
- Processa o texto em pares de letras

### Cifra de Vigenère
- Usa uma chave para determinar o deslocamento de cada letra
- O deslocamento depende da posição da letra na chave
- A chave se repete caso seja mais curta que o texto

## Requisitos
- Python 3.x
- NumPy

Para instalar o NumPy:
```
pip install numpy
```

## Como executar

1. Certifique-se de que todos os arquivos (`hill.py`, `vigenere.py` e `main.py`) estejam na mesma pasta
2. Execute o programa principal com o comando:
```
python main.py
```