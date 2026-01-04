# Soluções dos Desafios Python

Este diretório contém as soluções para os 6 desafios propostos no projeto.

## 📋 Desafios Implementados

### 1. Concatenando Dados 🐾
**Arquivo:** `concat_dados.py`

Recebe dois dados do usuário e os concatena em uma única string.

**Função principal:** `concatenar_dados(dado1, dado2)`

**Exemplo:**
```python
concatenar_dados("Python", "3") # Retorna: "Python3"
```

---

### 2. Repetindo Textos ✏️
**Arquivo:** `repet_txt.py`

Recebe uma string e um número inteiro, retornando a string repetida o número de vezes informado.

**Função principal:** `repetir_texto(texto, vezes)`

**Exemplo:**
```python
repetir_texto("Oi ", 3) # Retorna: "Oi Oi Oi "
```

---

### 3. Operações Matemáticas Simples 📐
**Arquivo:** `ope_mat.py`

Realiza operações matemáticas básicas (soma, subtração, multiplicação e divisão) entre dois números.

**Funções disponíveis:**
- `somar(num1, num2)`
- `subtrair(num1, num2)`
- `multiplicar(num1, num2)`
- `dividir(num1, num2)`

**Exemplo:**
```python
somar(5, 3)        # Retorna: 8
multiplicar(4, 5)  # Retorna: 20
```

---

### 4. Verificando Números Pares e Ímpares 🧮
**Arquivo:** `par_impar.py`

Verifica se um número inteiro é par ou ímpar.

**Função principal:** `verificar_par_impar(numero)`

**Exemplo:**
```python
verificar_par_impar(4)  # Retorna: "par"
verificar_par_impar(7)  # Retorna: "ímpar"
```

---

### 5. Calculando Média de Notas 📚
**Arquivo:** `media_notas.py`

Calcula a média aritmética de três notas.

**Função principal:** `calcular_media(nota1, nota2, nota3)`

**Exemplo:**
```python
calcular_media(8.5, 9.0, 7.5) # Retorna: 8.333333
```

---

### 6. Verificando Palíndromos 🔄
**Arquivo:** `palindromo.py`

Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente).

**Função principal:** `verificar_palindromo(palavra)`

**Exemplo:**
```python
verificar_palindromo("arara")  # Retorna: True
verificar_palindromo("python") # Retorna: False
```

---

## 🧪 Testes

Todos os desafios possuem testes automatizados no arquivo `test_desafios.py` na raiz do projeto.

Para executar os testes:
```bash
python -m unittest test_desafios -v
```

## 🚀 Como Usar

Cada arquivo pode ser executado individualmente:

```bash
python resolucoes_code/concat_dados.py
python resolucoes_code/repet_txt.py
python resolucoes_code/ope_mat.py
python resolucoes_code/par_impar.py
python resolucoes_code/media_notas.py
python resolucoes_code/palindromo.py
```

Ou você pode importar as funções em seus próprios scripts:

```python
from resolucoes_code.palindromo import verificar_palindromo

resultado = verificar_palindromo("radar")
print(resultado)  # True
```

---

## ✅ Validação Automatizada

O projeto inclui um workflow do GitHub Actions (`.github/workflows/test.yml`) que:
- Executa automaticamente todos os testes
- Valida a sintaxe Python
- Verifica a presença de todos os arquivos de solução
- Testa em múltiplas versões do Python (3.8, 3.9, 3.10, 3.11)
