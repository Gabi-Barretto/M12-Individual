# Documentação Completa: Análise Sintática

## 1. O que é Análise Sintática?

A análise sintática é uma fase crucial no processo de compilação, que ocorre logo após a análise léxica. Seu objetivo é verificar se a estrutura do código-fonte segue a gramática da linguagem, garantindo que a ordem e a organização dos tokens sejam corretas.

- **Função Principal**: Transformar o código-fonte em uma **árvore de derivação** ou **árvore sintática**.
- **Importância**: É fundamental para validar a semântica do código e detectar erros estruturais.

---

## 2. Gramáticas Formais e Linguagens

Para que a análise sintática funcione, é necessário definir as **regras de produção** da linguagem, que especificam como os tokens podem ser organizados.

- **Gramática Formal**: Conjunto de regras que define a estrutura válida da linguagem.
- **Linguagem Formal**: Conjunto de strings que são válidas de acordo com a gramática formal.
- **Símbolos**:
  - **Terminais**: Elementos básicos, como palavras-chave e operadores.
  - **Não-terminais**: Representam categorias gramaticais, como expressões e declarações.

### 2.1. Tipos de Gramáticas
1. **Gramática Livre de Contexto (GLC)**: Regras de produção que dependem apenas do símbolo não-terminal à esquerda. São amplamente utilizadas em compiladores.
2. **Gramática Sensível ao Contexto (GSC)**: Regras de produção que dependem do contexto, permitindo maior poder de expressão, mas sendo mais complexas de implementar.

---

## 3. Gramática Livre de Contexto (GLC)

### 3.1. Elementos da GLC
- **Terminais**: São os símbolos básicos que formam as cadeias válidas da linguagem.
- **Não-terminais**: Representam conjuntos de cadeias válidas e são usados para definir estruturas mais complexas.
- **Regras de Produção**: Têm o formato `A → α`, onde `A` é um não-terminal e `α` é uma sequência de terminais e não-terminais.

**Exemplo**: 
``` 
S → aSb | ε
```
Este exemplo representa uma linguagem que aceita cadeias formadas por uma sequência de `a`s seguida da mesma quantidade de `b`s, ou a cadeia vazia (ε).

---

## 4. Forma de Backus-Naur (BNF)

A BNF é uma notação formal que representa as regras gramaticais de forma compacta e precisa.

- **Objetivo**: Especificar a sintaxe de linguagens de programação.
- **Notação**: Usa símbolos `<...>` para representar não-terminais e `::=` para definir a regra.

**Exemplo de BNF**:
```
<expressão> ::= <expressão> + <termo> | <termo>
<termo> ::= <identificador> | <número> | ( <expressão> )
```
Essa definição representa uma expressão que pode ser composta por termos e operações aritméticas.

---

## 5. Técnicas de Parsing (Análise Sintática)

A análise sintática pode ser dividida em duas abordagens principais: **ascendente** e **descendente**.

### 5.1. Análise Sintática Ascendente
Constrói a árvore de derivação a partir dos tokens de entrada, da base para o topo.

- **Principais Técnicas**:
  - **Análise LR**: Inclui técnicas como LR(0) e LR(1), que utilizam tabelas de parsing.
  - **Análise Shift-Reduce**: Empilha e reduz tokens conforme as regras gramaticais são aplicadas.

### 5.2. Análise Sintática Descendente
Inicia a construção da árvore de derivação pela raiz e expande até os terminais.

- **Principais Técnicas**:
  - **Análise Recursiva Descendente**: Utiliza funções recursivas para implementar as regras gramaticais.
  - **Análise Preditiva**: Utiliza uma tabela para determinar qual regra aplicar em cada passo.

---

## 6. Exercícios e Questões Potenciais para Provas

Para ajudar no estudo, aqui estão algumas questões que podem ser cobradas na prova, com base no conteúdo abordado.

1. **O que é a análise sintática e qual é sua importância na compilação?**
   - *Resposta*: A análise sintática verifica a estrutura do código-fonte, assegurando que ele siga as regras da gramática da linguagem. É importante para validar a organização dos tokens e identificar erros de estrutura antes da execução.

2. **Explique a diferença entre gramática livre de contexto (GLC) e gramática sensível ao contexto (GSC).**
   - *Resposta*: A GLC é uma gramática em que as regras de produção dependem apenas do símbolo não-terminal à esquerda, sendo mais simples e comumente usada em compiladores. A GSC, por outro lado, depende do contexto em que o símbolo não-terminal está inserido, oferecendo maior expressividade, mas com mais complexidade.

3. **Dê um exemplo de uma regra em BNF que define uma expressão aritmética simples.**
   - *Resposta*: 
     ```
     <expressão> ::= <termo> | <expressão> + <termo> | <expressão> - <termo>
     <termo> ::= <identificador> | <número>
     ```

4. **Descreva a técnica de análise ascendente Shift-Reduce.**
   - *Resposta*: A análise Shift-Reduce utiliza uma pilha onde tokens são empilhados (shift) até que uma regra gramatical válida seja encontrada, momento em que os elementos correspondentes são reduzidos a um não-terminal (reduce), repetindo até formar a árvore de derivação completa.

5. **O que são símbolos terminais e não-terminais em uma gramática formal?**
   - *Resposta*: Terminais são os elementos básicos da linguagem, como palavras-chave e operadores. Não-terminais representam conjuntos de cadeias válidas que podem ser expandidas de acordo com as regras de produção para formar estruturas mais complexas.

6. **Qual é o papel da árvore de derivação na análise sintática?**
   - *Resposta*: A árvore de derivação representa a estrutura hierárquica do código de acordo com as regras gramaticais, mostrando como os tokens de entrada são agrupados para formar expressões válidas na linguagem.

7. **Explique o processo de análise preditiva e cite uma situação em que seria útil.**
   - *Resposta*: A análise preditiva utiliza uma tabela para escolher qual regra gramatical aplicar em cada passo. É útil em linguagens onde o próximo símbolo determina unicamente qual regra seguir, simplificando o parsing e reduzindo erros.