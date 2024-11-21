# Análise Léxica e Algoritmo de Thompson

## 1. Introdução à Análise Léxica
A análise léxica é a primeira etapa do processo de compilação. Seu objetivo é transformar o código-fonte em uma sequência de tokens, que são as menores unidades de significado na linguagem, como palavras-chave, identificadores, operadores, e símbolos.

### 1.1. Funções Principais
- **Identificação de Tokens**: Um token representa uma unidade lexical como `if`, `else`, variáveis, números, etc.
- **Criação da Tabela de Símbolos**: Armazena informações sobre cada token identificado.
- **Reconhecimento de Padrões com Regex**: Expressões regulares são usadas para definir padrões e facilitar o reconhecimento de tokens específicos.

---

## 2. Tokens e Expressões Regulares

### 2.1. O que é um Token?
Tokens são elementos básicos da linguagem, como:
- **Palavras-chave**: `if`, `while`, `return`
- **Identificadores**: Nomes de variáveis, funções, etc.
- **Operadores**: `+`, `-`, `*`, `/`
- **Delimitadores**: `(`, `)`, `{`, `}`, `;`

### 2.2. Expressões Regulares (Regex)
As expressões regulares (regex) definem padrões para a identificação dos tokens. Elas são uma linguagem formal usada para descrever cadeias de caracteres.

**Exemplos de Regex para Tokens Comuns**:
- Identificadores: `[a-zA-Z_][a-zA-Z0-9_]*`
- Números inteiros: `[0-9]+`
- Palavras-chave: `if|else|while|for`

---

## 3. Algoritmo de Thompson

O Algoritmo de Thompson é utilizado para converter uma expressão regular em um autômato finito não-determinístico (AFND). Este autômato pode então ser usado para reconhecer padrões no texto.

### 3.1. Conceitos Básicos
- **Autômato Finito Não-Determinístico (AFND)**: Um modelo matemático que representa uma sequência de estados com transições baseadas em entradas, mas que pode ter múltiplos caminhos para um mesmo símbolo.
- **Autômato Finito Determinístico (AFD)**: Similar ao AFND, mas com um único caminho para cada símbolo a partir de um estado.

### 3.2. Construção do AFND com o Algoritmo de Thompson
O algoritmo constrói o AFND a partir de partes menores da expressão regular, combinando-as para formar um autômato completo:
1. **Símbolos**: Cada símbolo individual é representado por um estado inicial e um estado final com uma transição direta.
2. **Operador OU (`|`)**: Cria caminhos alternativos no autômato.
3. **Concatenação**: Conecta o estado final de uma sub-expressão ao estado inicial da próxima.
4. **Kleene Star (`*`)**: Cria um ciclo que permite a repetição da sub-expressão zero ou mais vezes.

---

## 4. Regras e Aplicações do Algoritmo de Thompson

### 4.1. Regras para Construção de AFND
- **Símbolo `ε`**: Representa uma transição vazia, usada para conectar estados sem consumir símbolos da entrada.
- **Operador `|` (União)**: Permite que uma expressão regular escolha entre múltiplas opções.
- **Concatenação**: Permite que a expressão siga uma sequência definida de símbolos.
- **Kleene Star (`*`)**: Permite repetição da expressão zero ou mais vezes.

### 4.2. Exemplo Prático
Para a expressão regular `(a|b)c*`, o algoritmo de Thompson gera um AFND que:
- Tem dois caminhos alternativos para `a` ou `b`.
- Permite que o símbolo `c` seja repetido zero ou mais vezes após `a` ou `b`.

---

## 5. Aplicações Práticas
O Algoritmo de Thompson é usado principalmente no desenvolvimento de **scanners** e **analisadores léxicos** de compiladores, permitindo que sejam reconhecidos padrões de tokens definidos por expressões regulares.

---

## 6. Exercícios de Prática

### Questões de Exemplo
1. **Construa um AFND para a expressão regular `a|b`.**
   - *Resposta*: O autômato começa em um estado inicial, com um caminho para `a` e outro para `b`, ambos levando ao estado final.

2. **Como o operador `*` modifica o autômato para a expressão `b*`?**
   - *Resposta*: Cria um ciclo no autômato que permite zero ou mais repetições de `b`.

3. **Explique o uso da concatenação em `ab` no Algoritmo de Thompson.**
   - *Resposta*: Em `ab`, o estado final de `a` é conectado ao estado inicial de `b`, criando uma sequência obrigatória.

### Exercícios Adicionais
1. Desenhe o AFND para as seguintes expressões usando o Algoritmo de Thompson:
   - `a|b.c`
   - `a*`
   - `(a|b)*c`