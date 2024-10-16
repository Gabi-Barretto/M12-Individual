# C - Aula 1

Ferramenta - conhecimento base.

Entender estrutura de dados.

Todas as questôes objetivas serão sobre conhecimento base, dissertativa sera conhecimento base + ferramenta. 

Source code .c - crie um diagrama simples mostrando os passos até acomplicação de um script em c ( gpt complete )

Código de teste da ferramenta.

```
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

No arquvio .h, criamos o protótipo de função. (Assinatura do método?) (gpt complete)

Array:

```
int main()
{
    printf("Harray!!\n");
    int N = 3;
    int vetor[N];

    for (int i = 0; i < N; i++){
        printf("informe o valor de v[%d]: ", i);
        scanf("%d", &vetor[N]);
    }
    for (int i = 0; i < N; i++){
        printf("o valor informado de v[%d]: %d", i, N);
    }

    return 0;
}
```

Dados e abstração de Dados:

```
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

Por definição qual a diferença de vetor e lista, um vetor pode conter direção e sentido, e a lista tem uma ligação netre um valor seguido do outro.

Lista:
- Criar lista
- Inserir e remover da lista.
- Busca na lista.
- Destruição da lista.
- Tamanho, e ainformação de se está cheia ou vazia.

Fila:
- Inserção sempre ao final da fila.
- First in, first out.
- Abstração do comportamento, queremos alimentar ela com os nosso dados. 

Pilha:
- Last in, first out.
- Entrada é como a fila, mas último elemento a entrar é o primeiro a sair.

Classe agrupa comportamento e atributos.

Variaveis criadas na main só existem dentro da main.

Ideia de ponterios e endereços. (gpt complete)

```
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
  p.dados[p.topo] = valor;
  p.topo++;
  return p;
};

Pilha retirarPilha(Pilha p, float *valor) {
  *valor = p.dados[p.topo - 1];
  p.topo--;
  return p;
};

void mostrarPilha(Pilha p){
  for(int i = 0; i < p.topo; i++){  // Corrigido aqui
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
  printf("Valor retirado: %.2f\n", valor);  // Adicionada esta linha para mostrar o valor removido

  mostrarPilha(duracell);

  return 0;
}
```
