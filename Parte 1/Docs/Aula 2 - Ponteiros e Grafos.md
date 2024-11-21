# C - Ponteiros

Aula sobre ponteiros e calculadora polonesa, utilizando C.
Outros exemplos, pilha de telas de um App Flutter.

``` c

#include <stdio.h>
#include <string.h>
#define MAX 10 // Define o tamanho máximo da pilha

// Estrutura da Pilha
typedef struct {
  int itens[MAX];
  int topo;
} Pilha;

// Inicializa a pilha
void inicializar(Pilha *p) {
  (*p).topo = -1;
  // p->topo = -1;
}

// Verifica se a pilha está cheia
int estaCheia(Pilha *p) {
  return (*p).topo == MAX - 1;
  // return p->topo == MAX - 1;
}

// Verifica se a pilha está vazia
int estaVazia(Pilha *p) {
  return (*p).topo == -1;
  // return p->topo == -1;
}

// Empilha um elemento
void empilhar(Pilha *p, int valor) {
  if (estaCheia(p)) {
    printf("Erro: Pilha está cheia.\n");
  } else {
    ++((*p).topo);
    (*p).itens[(*p).topo] = valor;
    // p->itens[++(p->topo)] = valor;
    printf("%d empilhado.\n", valor);
  }
}

// Desempilha um elemento
int desempilhar(Pilha *p) {
  if (estaVazia(p)) {
    printf("Erro: Pilha está vazia.\n");
    return -1; // Retorna um valor inválido para indicar erro
  } else {
    // return p->itens[(p->topo)--];
    return (*p).itens[((*p).topo)--];
  }
}

// Exibe o topo da pilha
int topo(Pilha *p) {
  if (estaVazia(p)) {
    printf("Erro: Pilha está vazia.\n");
    return -1;
  } else {
    return p->itens[p->topo];
  }
}

void exibePilha(Pilha p) {
  if (estaVazia(&p)) {
    printf("Pilha Vazia!\n");
    return;
  }
  int i;
  for (i = 0; i <= p.topo; i++) {
    printf("Posicao[%i]: %i\n", i, p.itens[i]);
  }
}

int tamanhoDaPilha(Pilha p) { return p.topo + 1; }
// Função principal
int main() {
  Pilha p;
  inicializar(&p);
  char opcao[MAX];
  int continuar = 1;
  do {
    printf("Informe valor: ");
    gets(opcao);

    if (!strcmp(opcao, "sair"))
      continuar = 0;

    else if (!strcmp(opcao, "+")) {

      if (tamanhoDaPilha(p) > 1) {
        int numero1, numero2, res;
        numero1 = desempilhar(&p);
        numero2 = desempilhar(&p);
        res = numero1 + numero2;
        empilhar(&p, res);
          
      } else {
        printf("Não tem itens suficiente...\n");
      }
      exibePilha(p);
    } else if (!strcmp(opcao, "-")) {

      if (tamanhoDaPilha(p) > 1) {
        int numero1, numero2, res;
        numero1 = desempilhar(&p);
        numero2 = desempilhar(&p);
        res = numero1 - numero2;
        empilhar(&p, res);
          
      } else {
        printf("Não tem itens suficiente...\n");
      }
      exibePilha(p);
    } else if (!strcmp(opcao, "/")) {

      if (tamanhoDaPilha(p) > 1) {
        int numero1, numero2, res;
        numero1 = desempilhar(&p);
        numero2 = desempilhar(&p);
        res = numero1 / numero2;
        empilhar(&p, res);
          
      } else {
        printf("Não tem itens suficiente...\n");
      }
      exibePilha(p);
    } else if (!strcmp(opcao, "*")) {

      if (tamanhoDaPilha(p) > 1) {
        int numero1, numero2, res;
        numero1 = desempilhar(&p);
        numero2 = desempilhar(&p);
        res = numero1 * numero2;
        empilhar(&p, res);
          
      } else {
        printf("Não tem itens suficiente...\n");
      }
      exibePilha(p);
    }
    else {
      int numero;
      numero = atoi(opcao);
      empilhar(&p, numero);
      exibePilha(p);
    }
  } while (continuar);
  return 0;
}

```


## Início de Grafos

Se tiver sentido nas setas se trata de DÍGRAFOS, caso não, GRAFOS.

![alt text](./Mídia/Grafos/grafos.png)

Para criar a matriz de adjacência dos grafos representados na imagem, podemos seguir os passos de acordo com cada grafo e suas arestas. A matriz de adjacência será uma tabela onde cada linha e coluna representa um vértice do grafo, e o valor na interseção indica se há uma aresta entre os vértices.

Como a imagem tem quatro subgrafos (a, b, c, d), cada um será representado por sua própria matriz de adjacência.

### Definições:
- Os vértices são \( V = \{A, B, C, D, E, F\} \).
- A matriz de adjacência é de ordem \( 6 \times 6 \), onde cada vértice \( V_i \) é uma linha/coluna.

Agora, desenhando as matrizes para cada grafo:

#### Grafo a) (Não orientado)
Neste grafo, as arestas são não orientadas. Assim, a matriz é simétrica:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 1 | 0 | 0 | 0 |
| B | 1 | 0 | 1 | 1 | 0 |
| C | 0 | 1 | 0 | 1 | 0 |
| D | 0 | 1 | 1 | 0 | 0 |
| E | 0 | 0 | 0 | 0 | 0 |

#### Grafo b) (Orientado)
Neste grafo, as arestas são orientadas, ou seja, a matriz de adjacência não é simétrica:

|   | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| A | 0 | 0 | 0 | 0 | 1 | 0 |
| B | 0 | 0 | 1 | 0 | 0 | 0 |
| C | 1 | 0 | 0 | 1 | 0 | 0 |
| D | 0 | 0 | 0 | 0 | 0 | 0 |
| E | 0 | 0 | 0 | 0 | 0 | 0 |
| F | 0 | 0 | 0 | 0 | 0 | 0 |

#### Grafo c) (Orientado)
Aqui, também temos um grafo orientado, onde as direções das setas são importantes:

|   | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| A | 0 | 0 | 0 | 0 | 0 | 0 |
| B | 1 | 0 | 0 | 0 | 1 | 0 |
| C | 1 | 0 | 0 | 0 | 1 | 0 |
| D | 0 | 0 | 0 | 0 | 0 | 1 |
| E | 0 | 0 | 0 | 0 | 0 | 0 |
| F | 0 | 0 | 0 | 0 | 0 | 0 |

#### Grafo d) (Não orientado)
Por último, temos outro grafo não orientado. Como é um grafo não orientado, a matriz será simétrica:

|   | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| A | 0 | 1 | 0 | 0 | 0 | 0 |
| B | 0 | 0 | 0 | 1 | 0 | 1 |
| C | 0 | 0 | 0 | 0 | 1 | 1 |
| D | 0 | 1 | 0 | 0 | 0 | 0 |
| E | 0 | 0 | 1 | 0 | 0 | 0 |
| F | 0 | 1 | 1 | 0 | 0 | 0 |

Essas tabelas representam as matrizes de adjacência dos grafos ilustrados na imagem.