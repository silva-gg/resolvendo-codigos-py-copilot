# Resolvendo Códigos em Python com o Github Copilot

Olá!! Aqui veremos algumas resoluções de códigos em python utilizando o Github Copilot.

### Atenção ⚠️ 

Não tem acesso ao Github Copilot?! Não tem problema!! 
Que tal utilizar o [ChatGPT](https://chat.openai.com/) como seu copiloto de estudos ??

---

## 🤖 Como o GitHub Copilot Cloud Agent foi Utilizado

Este repositório foi desenvolvido utilizando o **GitHub Copilot Cloud Agent**, uma ferramenta avançada de IA que auxiliou na resolução automatizada dos desafios. O processo de desenvolvimento seguiu estas etapas:

### Processo de Resolução

1. **Análise Inicial** 📋
   - O agente analisou o README.md para entender os 6 desafios propostos
   - Identificou arquivos existentes e a estrutura do repositório
   - Criou um plano detalhado de implementação

2. **Implementação das Soluções** 💻
   - Completou os 3 arquivos existentes (concat_dados.py, repet_txt.py, ope_mat.py)
   - Criou 3 novos arquivos para os desafios restantes (par_impar.py, media_notas.py, palindromo.py)
   - Cada solução inclui:
     - Funções reutilizáveis e bem documentadas
     - Interface de linha de comando (CLI) via função `main()`
     - Docstrings explicativas
     - Tratamento de casos especiais (ex: divisão por zero)

3. **Criação de Testes Automatizados** 🧪
   - Desenvolveu 25 testes unitários cobrindo todos os desafios
   - Implementou testes para casos normais e casos extremos (edge cases)
   - Garantiu 100% de taxa de aprovação dos testes

4. **Configuração de CI/CD** 🔄
   - Criou workflow do GitHub Actions (`.github/workflows/test.yml`)
   - Configurou testes automatizados em múltiplas versões do Python (3.8, 3.9, 3.10, 3.11)
   - Implementou validações de estrutura de arquivos e sintaxe Python
   - Aplicou práticas de segurança (permissões explícitas)

5. **Documentação Completa** 📚
   - Adicionou README detalhado no diretório `resolucoes_code/`
   - Incluiu exemplos de uso para cada desafio
   - Documentou como executar testes e usar as funções

6. **Revisão de Qualidade e Segurança** 🔒
   - Executou revisão automatizada de código
   - Realizou varredura de segurança com CodeQL
   - Corrigiu todas as vulnerabilidades identificadas
   - Validou a sintaxe de todos os arquivos Python

### Benefícios do Uso do Copilot Cloud Agent

✅ **Velocidade**: Todos os 6 desafios foram implementados rapidamente  
✅ **Qualidade**: Código limpo, bem estruturado e testado  
✅ **Segurança**: Análise automatizada de vulnerabilidades  
✅ **Documentação**: Documentação completa e exemplos práticos  
✅ **CI/CD**: Pipeline de integração contínua configurado  
✅ **Boas Práticas**: Seguindo convenções Python e padrões de código

### Como Executar os Desafios

```bash
# Executar uma solução específica
python resolucoes_code/concat_dados.py

# Executar todos os testes
python -m unittest test_desafios -v

# Importar e usar as funções
python
>>> from resolucoes_code.palindromo import verificar_palindromo
>>> verificar_palindromo("arara")
True
```

### Estrutura do Projeto

```
resolvendo-codigos-py-copilot/
├── README.md                      # Este arquivo
├── .github/
│   └── workflows/
│       └── test.yml              # Workflow de CI/CD
├── resolucoes_code/
│   ├── README.md                 # Documentação das soluções
│   ├── concat_dados.py           # Desafio 1: Concatenação
│   ├── repet_txt.py              # Desafio 2: Repetição
│   ├── ope_mat.py                # Desafio 3: Operações Matemáticas
│   ├── par_impar.py              # Desafio 4: Par ou Ímpar
│   ├── media_notas.py            # Desafio 5: Média de Notas
│   └── palindromo.py             # Desafio 6: Palíndromos
└── test_desafios.py              # Suite de testes (25 testes)
```

---

## 1 - Concatenando Dados 🐾

Descrição:
Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?! 

O que aprenderemos?

* Manipulação de Strings (string)
* Concatenação
* Entrada de dados
* Utilização eficiente do Github Copilot

<br>

## 2 - Repetindo Textos ✏️

Descrição:
Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

O que aprenderemos?

* Manipulação de Strings (string)
* Números Inteiros (int)
* Múltiplas repetições
* Entrada de dados
* Aproveitar as sugestões do Github Copilot

<br>

## 3 - Operações Matemáticas Simples 📐

Descrição:
Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

O que aprenderemos?

* Operações Matemáticas Básicas
* Entrada de dados
* Utilização eficiente do Github Copilot

<br>

## 4 - Verificando Números Pares e Ímpares 🧮

Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

O que aprenderemos?
* Utilização de condicionais em Python (if, else) para realizar verificações.
* Introdução ao conceito de operador de módulo (%) para verificar se um número é par ou ímpar.
* Exploração do uso de uma ferramenta de IA, como o Github Copilot, para otimizar a estrutura do código.


<br>

## 5 - Calculando Média de Notas 📚

Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

O que aprenderemos?
* Uso de variáveis para armazenar dados fornecidos pelo usuário.
* Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores.
* Prática na solicitação e manipulação de entrada do usuário.

<br>

## 6 - Verificando Palíndromos 🔄

Descrição: Vamos testar se uma palavra é um palíndromo?! 
Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

O que aprenderemos?
* Manipulação de strings em Python, especialmente invertendo uma string.
* Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
* Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.
