# Cifras de Hill e Vigenère

Este projeto implementa algoritmos de criptografia e descriptografia para as Cifras de Hill e Vigenère.

## Estrutura do Projeto

O projeto está organizado em três arquivos:

- `hill.py`: Contém as funções para criptografar e descriptografar usando a Cifra de Hill (também inclui o gerador da matriz inversa modular)
- `vigenere.py`: Contém as funções para criptografar e descriptografar usando a Cifra de Vigenère
- `main.py`: Programa principal para testar os algoritmos com uma interface para tratar

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

## Como executar

1. Rodar o executável presente na pasta (descompactada)
2. Ao abrir o programa, haverá um campo para colocar o texto a ser cifrado ou decifrado.
3. Insira o texto no campo "Texto".
4. Para Vigenère, insira também a chave no campo abaixo.
5. Clique nos botões para criptografar ou descriptografar.
6. Apenas letras (sem espaços ou números) são permitidas.
7. Se for selecionada uma cifra o texto será atualizado para o texto cifrado
8. Se selecionado o deciframento, o resultado aparecerá no campo de resultado
9. Importante não misturar os métodos. Se realizar uma cifra de hill, não tente decifrar via vigenere e vice versa. Para os testes, sempre faça uma criptografia seguida de um decriptografia, para garantir que o texto inicial seja retornado no resultado da descriptografia.

## Requisitos (para executar localmente):

- Python 3.8+
- Bibliotecas: numpy, tkinter

$ pip install numpy tkinter
$ python main.py
