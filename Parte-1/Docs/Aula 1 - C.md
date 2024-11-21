# C - Aula 1

## Ferramenta - Conhecimento Base

Nesta aula, o foco será o entendimento da estrutura de dados em C e o uso da ferramenta para codificação e execução. Será necessário ter domínio sobre os conceitos de estrutura de dados, como arrays, listas, filas e pilhas. 

C é compilado, python é interpretado.

Uma **estrutura de dados** é uma forma organizada de armazenar e gerenciar informações para que possam ser usadas de forma eficiente. Em computação, elas permitem que dados sejam organizados de maneiras diferentes, dependendo da aplicação, facilitando operações como inserção, busca, remoção e atualização. Exemplos comuns de estruturas de dados incluem listas, pilhas, filas, árvores, grafos e tabelas hash. Cada tipo de estrutura de dados é otimizado para certos tipos de tarefas e acessos.

**Objetivo da Aula:**
- Compreender as bases da linguagem C.
- Aplicar a ferramenta (compilador) para desenvolvimento e execução de códigos.
- Entender a estrutura de dados e abstrações.

**Avaliação:**
- **Questões objetivas:** Baseadas no conhecimento de estrutura de dados e linguagem C.
- **Questões dissertativas:** Integram o conhecimento teórico e o uso prático da ferramenta (compilador).

---

## Processo de Compilação de um Script em C

Aqui está um diagrama simples que mostra os passos do processo de compilação de um código C:

1. **Escrita do Código**: O programador escreve o código-fonte em um editor de texto. O código geralmente é salvo com a extensão `.c`.
2. **Pré-processamento**: O compilador C chama o pré-processador para processar diretivas, como `#include` e `#define`. Isso gera um código intermediário.
3. **Compilação**: O compilador converte o código intermediário em assembly.
4. **Montagem**: O código assembly é transformado em código de máquina (objeto) pelo montador.
5. **Linkagem**: O linker combina os arquivos objeto e as bibliotecas necessárias para criar o executável final.

**Ferramentas utilizadas:**
- **GCC (GNU Compiler Collection):** Uma das ferramentas mais usadas para compilar códigos C.
- **Clang:** Outro compilador C/C++ amplamente utilizado.

---

## Código de Teste da Ferramenta

Aqui temos um exemplo de código que realiza a soma de dois números inseridos pelo usuário.

```c
#include <stdio.h>

int main(void) {
  int n1;
  int n2;
  printf("Digite um número\n");
  scanf("%i", &n1); 
  printf("Digite um outro número\n");
  scanf("%i", &n2); 

  int n3 = n1 + n2;

  printf("Soma: %d", n3);
  
  return 0;
}
```

### Explicação do Código
Este programa simples realiza a entrada de dois números inteiros e imprime a soma dos dois. É um exemplo típico de interação com o usuário via `scanf` e `printf`.

---

## Arquivo Header (`.h`)

No arquivo `.h`, criamos o **protótipo de função**. O protótipo de uma função declara a assinatura de uma função sem definir o corpo. Isso informa ao compilador que a função existe em algum lugar no código, possibilitando chamadas antes da implementação.

Exemplo de protótipo:

```c
// protótipo
int soma(int a, int b);

// implementação
int soma(int a, int b) {
    return a + b;
}
```

---

## Array

Aqui temos um exemplo de uso de array, onde o programa pede ao usuário para inserir valores e os exibe.

```c
int main()
{
    printf("Harray!!\n");
    int N = 3;
    int vetor[N];

    for (int i = 0; i < N; i++){
        printf("Informe o valor de v[%d]: ", i);
        scanf("%d", &vetor[i]);  // Correção para armazenar corretamente os valores no array
    }
    for (int i = 0; i < N; i++){
        printf("O valor informado de v[%d]: %d\n", i, vetor[i]);  // Correção para imprimir os valores corretos do array
    }

    return 0;
}
```

### Explicação do Código
- Um array é uma coleção de elementos do mesmo tipo.
- O código acima demonstra a criação de um array de inteiros e permite ao usuário preencher seus valores.
- O `scanf` armazena os valores no array, e o `printf` os exibe.

---

## Dados e Abstração de Dados

O exemplo abaixo utiliza estruturas (`structs`) para definir números complexos e realizar operações como soma e exibição.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
  float real;
  float imaginario;
} Complexo;

Complexo criarComplexo(float real, float imaginario) {
  Complexo N;
  N.real = real;
  N.imaginario = imaginario;
  return N;
}

void mostrarComplexo(Complexo N) {
  printf("%.2f + %.2fi\n", N.real, N.imaginario);
}

Complexo somarComplexos(Complexo N1, Complexo N2) {
  return criarComplexo(N1.real + N2.real, N1.imaginario + N2.imaginario);
}

int main(void) {

  Complexo N1, N2, N3;

  N1 = criarComplexo(3, 6);
  N2 = criarComplexo(4, 8);

  N3 = somarComplexos(N1, N2);

  mostrarComplexo(N3);
  return 0;
}
```

### Explicação do Código
- **Struct:** Uma estrutura que agrupa diferentes tipos de dados.
- **Complexo:** É uma estrutura que contém números reais e imaginários.
- Operações são realizadas utilizando funções que manipulam esses números.

---

## Diferença entre Vetor e Lista

**Vetor:** 
- É uma estrutura de dados com tamanho fixo.
- Os elementos estão organizados em posições contíguas da memória.

**Lista:**
- Pode ter tamanho dinâmico.
- Cada elemento aponta para o próximo, formando uma cadeia de elementos.

---

## Implementação de Estruturas de Dados

### Lista:

Operações típicas:
- **Criar lista**: Inicializa uma lista vazia.
- **Inserir/remover**: Adiciona ou remove elementos.
- **Busca**: Pesquisa um elemento específico.
- **Destruição**: Remove todos os elementos, liberando memória.
- **Checagem**: Verifica se a lista está cheia ou vazia.

### Fila:

- **Inserção ao final**: Elementos são inseridos no fim.
- **Remoção do início**: O primeiro a entrar é o primeiro a sair (FIFO).

### Pilha:

- **Último a entrar, primeiro a sair (LIFO)**: O último elemento inserido é o primeiro a ser removido.

Exemplo de implementação de pilha:

```c
#include <stdio.h>
#include <string.h>
#define MAX 10

typedef struct {
  int topo;
  float dados[MAX];
} Pilha;

Pilha criarPilha() {
  Pilha p;
  p.topo = 0;
  return p;
};

Pilha inserirPilha(float valor, Pilha p) {
  if (p.topo < MAX) { // Adicionada verificação para evitar overflow
    p.dados[p.topo] = valor;
    p.topo++;
  }
  return p;
};

Pilha retirarPilha(Pilha p, float *valor) {
  if (p.topo > 0) { // Adicionada verificação para evitar underflow
    *valor = p.dados[p.topo - 1];
    p.topo--;
  }
  return p;
};

void mostrarPilha(Pilha p) {
  for(int i = 0; i < p.topo; i++) {
    printf("[ %.2f ]\n", p.dados[i]);
  }
};

int main(void) {

  Pilha duracell;
  duracell = criarPilha();

  duracell = inserirPilha(2, duracell);
  duracell = inserirPilha(3, duracell);
  duracell = inserirPilha(4, duracell);

  float valor;
  duracell = retirarPilha(duracell, &valor);
  printf("Valor retirado: %.2f\n", valor);

  mostrarPilha(duracell);

  return 0;
}
```

### Explicação do Código:
- **Pilha:** A estrutura `Pilha` contém um array e um topo que controla a posição atual.
- Operações de inserção (`push`) e remoção (`pop`) são controladas pelo valor do topo da pilha.

---

### Ponteiros e Endereços

Como mencionado anteriormente, um **ponteiro** é uma variável que armazena o endereço de outra variável. Em C, isso permite manipulações mais eficientes, especialmente ao lidar com grandes estruturas de dados, como arrays e estruturas complexas, sem a necessidade de copiar grandes blocos de memória.

**Exemplo detalhado de uso de ponteiros:**

```c
#include <stdio.h>

int main() {
    int var = 10;       // Uma variável normal
    int *ptr = &var;    // Um ponteiro que armazena o endereço de 'var'

    // Exibe o valor da variável 'var'
    printf("Valor de var: %d\n", var);

    // Exibe o endereço de memória de 'var'
    printf("Endereço de var: %p\n", (void*)&var);

    // Exibe o valor armazenado no ponteiro 'ptr'
    printf("Valor armazenado em ptr (endereço de var): %p\n", (void*)ptr);

    // Exibe o valor de 'var' através do ponteiro usando a desreferenciação
    printf("Valor de var acessado via ponteiro: %d\n", *ptr);

    return 0;
}
```

### Explicação:
- `int *ptr`: Declara um ponteiro para uma variável inteira. O símbolo `*` é usado tanto para declarar o ponteiro quanto para acessar o valor apontado (desreferenciar).
- `&var`: O operador `&` retorna o endereço da variável `var`, que é armazenado em `ptr`.
- `*ptr`: Desreferencia o ponteiro `ptr` para acessar o valor que ele aponta, ou seja, o valor de `var`.

---

## Conceitos Avançados: Structs e Ponteiros (Fora da aula)

Agora vamos combinar **structs** e **ponteiros**, um conceito essencial em C para manipulação eficiente de dados. O uso de ponteiros com estruturas permite a criação de listas encadeadas, filas, pilhas e outras estruturas dinâmicas.

Exemplo de uso de ponteiros com structs:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int dia;
    int mes;
    int ano;
} Data;

void mostrarData(Data *d) {  // Recebemos um ponteiro para a struct
    printf("Data: %02d/%02d/%d\n", d->dia, d->mes, d->ano);
}

int main() {
    // Alocamos memória para uma struct do tipo Data
    Data *dataHoje = (Data *)malloc(sizeof(Data));

    // Preenchemos a struct através do ponteiro
    dataHoje->dia = 17;
    dataHoje->mes = 10;
    dataHoje->ano = 2024;

    // Exibimos os dados
    mostrarData(dataHoje);

    // Liberamos a memória alocada
    free(dataHoje);

    return 0;
}
```

### Explicação:
- **Alocação Dinâmica:** `malloc()` aloca memória suficiente para armazenar uma `Data`. Isso permite manipular estruturas em tempo de execução, sem precisar saber o tamanho em tempo de compilação.
- **Acesso a membros via ponteiro:** Usamos o operador `->` para acessar os membros da struct quando lidamos com ponteiros.
- **Liberação de memória:** `free()` é usado para liberar a memória alocada dinamicamente.

---

## Estruturas Dinâmicas: Lista Encadeada

Uma **lista encadeada** é uma estrutura de dados composta por nós, onde cada nó contém um valor e um ponteiro para o próximo nó. É uma maneira eficiente de lidar com dados dinâmicos, já que o tamanho da lista pode crescer ou diminuir conforme necessário, sem a necessidade de um tamanho pré-definido (como em arrays).

Aqui está um exemplo de implementação de uma lista encadeada em C:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

No* criarNo(int valor) {
    No *novoNo = (No *)malloc(sizeof(No));
    novoNo->valor = valor;
    novoNo->proximo = NULL;
    return novoNo;
}

void inserirNoInicio(No **cabeca, int valor) {
    No *novoNo = criarNo(valor);
    novoNo->proximo = *cabeca;
    *cabeca = novoNo;
}

void mostrarLista(No *cabeca) {
    No *temp = cabeca;
    while (temp != NULL) {
        printf("%d -> ", temp->valor);
        temp = temp->proximo;
    }
    printf("NULL\n");
}

void liberarLista(No *cabeca) {
    No *temp;
    while (cabeca != NULL) {
        temp = cabeca;
        cabeca = cabeca->proximo;
        free(temp);
    }
}

int main() {
    No *lista = NULL; // Inicializa lista vazia

    inserirNoInicio(&lista, 10);
    inserirNoInicio(&lista, 20);
    inserirNoInicio(&lista, 30);

    mostrarLista(lista);

    liberarLista(lista); // Libera a memória alocada
    return 0;
}
```

### Explicação:
- **Estrutura `No`:** Cada nó da lista contém um valor e um ponteiro para o próximo nó.
- **`inserirNoInicio`:** Adiciona um novo nó no início da lista.
- **`mostrarLista`:** Percorre a lista exibindo seus elementos.
- **`liberarLista`:** Libera a memória de cada nó da lista.

---

## Abstração: Fila Dinâmica

A **fila dinâmica** é uma estrutura de dados onde a inserção ocorre no final e a remoção no início, seguindo o conceito FIFO (First In, First Out). Vamos ver como implementar uma fila dinâmica em C usando structs e ponteiros:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

typedef struct {
    No *inicio;
    No *fim;
} Fila;

Fila* criarFila() {
    Fila *f = (Fila *)malloc(sizeof(Fila));
    f->inicio = NULL;
    f->fim = NULL;
    return f;
}

void inserirFila(Fila *f, int valor) {
    No *novoNo = (No *)malloc(sizeof(No));
    novoNo->valor = valor;
    novoNo->proximo = NULL;
    if (f->fim == NULL) {
        f->inicio = novoNo;
        f->fim = novoNo;
    } else {
        f->fim->proximo = novoNo;
        f->fim = novoNo;
    }
}

int removerFila(Fila *f) {
    if (f->inicio == NULL) {
        printf("Fila vazia\n");
        return -1;
    }
    No *temp = f->inicio;
    int valor = temp->valor;
    f->inicio = f->inicio->proximo;
    if (f->inicio == NULL) {
        f->fim = NULL;
    }
    free(temp);
    return valor;
}

void mostrarFila(Fila *f) {
    No *temp = f->inicio;
    while (temp != NULL) {
        printf("%d -> ", temp->valor);
        temp = temp->proximo;
    }
    printf("NULL\n");
}

int main() {
    Fila *fila = criarFila();

    inserirFila(fila, 10);
    inserirFila(fila, 20);
    inserirFila(fila, 30);

    mostrarFila(fila);

    printf("Removendo: %d\n", removerFila(fila));
    mostrarFila(fila);

    return 0;
}
```

### Explicação:
- **Fila Dinâmica:** Utiliza uma estrutura `Fila` que contém dois ponteiros: um para o início e outro para o final da fila.
- **Inserção e Remoção:** A inserção é feita no final da fila e a remoção no início.
- **Gerenciamento de Memória:** A função `removerFila` libera a memória do nó removido.

---

## Considerações Finais

Esses exemplos demonstram como trabalhar com conceitos essenciais de C, como arrays, structs, ponteiros, e a implementação de estruturas dinâmicas (listas encadeadas, pilhas e filas). A chave para trabalhar com esses conceitos é entender a memória e como os ponteiros permitem manipular dados de forma eficiente.

Esse material oferece uma base sólida para compreender as estruturas de dados em C e como utilizá-las para resolver problemas mais complexos, desde a manipulação de arrays até a criação de estruturas dinâmicas eficientes.