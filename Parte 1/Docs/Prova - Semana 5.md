## Objetivas

**Questão 1**

- **Resposta**: D) II e III, apenas
- **Explicação**:
  - **Afirmação I**: Incorreta. A parte integral não requer uma fila para acumular todos os erros desde o início. Um simples acumulador pode somar continuamente os erros ao longo do tempo.
  - **Afirmação II**: Correta. A parte proporcional ajusta a variável de controle em resposta ao erro atual, proporcional à diferença entre o valor desejado e o valor medido.
  - **Afirmação III**: Correta. A parte derivativa calcula a taxa de mudança do erro entre a amostra atual e a anterior, podendo utilizar uma estrutura que armazene os dois valores mais recentes, como uma pilha ou uma variável temporária.

---

**Questão 2**

- **Resposta**: D) \( kp \times \text{Erro} + ki \times \text{ITerm} + kd \times dErro \)
- **Explicação**:
  - Essa fórmula é a expressão correta para um controlador PID, somando os três componentes Proporcional, Integral e Derivativo. Outras alternativas estão incorretas por ausência ou pelo uso inadequado dos termos, como elevar o termo derivativo ao quadrado, o que não faz parte da estrutura padrão do PID.

---

**Questão 3**

- **Resposta**: A) As assertões I e II são proposições verdadeiras, e a II é uma justificativa da I.
- **Explicação**:
  - **Afirmação I**: Correta. A função de transferência do ramo direto \( G(s) = \frac{3,2}{s + 0,8} \) está corretamente especificada, com um ganho de 3,2 e uma constante de tempo de aproximadamente 1,25 segundos.
  - **Afirmação II**: Correta. A função de malha fechada \( T(s) = \frac{3,2}{s + 4} \) indica uma resposta mais rápida, com uma constante de tempo de 0,25 segundos.
  - A função de transferência de malha fechada reduz o tempo de estabilização, justificando a configuração do ramo direto. Assim, II justifica I.

---

**Questão 4**

- **Resposta**: C) I e IV
- **Explicação**:
  - **Afirmação I**: Correta. O tempo de pico está entre 2 e 3 segundos, como indicado no gráfico.
  - **Afirmação IV**: Correta. O sobressinal máximo está entre 0,2 m e 0,4 m, evidenciado pela amplitude inicial da resposta antes de estabilizar.
  - Outras afirmações são incorretas, pois o tempo de subida ocorre antes dos 2 segundos e o sistema tem comportamento típico de segunda ordem, não de primeira.

---

**Questão 5**

- **Resposta**: A) a variável X corresponde à ação de controle integral; a variável Y, à ação proporcional; e a variável Z, à ação derivativa.
- **Explicação**:
  - **X** acumula o erro ao longo do tempo, caracterizando a ação integral.
  - **Y** é diretamente proporcional ao erro, representando a ação proporcional.
  - **Z** calcula a diferença entre o erro atual e o erro anterior, caracterizando a ação derivativa.

---

**Questão 6**

- **Resposta**: A) Aumento do ganho integral (\( K_i \)), tornando a resposta mais lenta.
- **Explicação**:
  - O erro em regime permanente é corrigido pelo ganho integral, que acumula o erro ao longo do tempo, ajustando o sistema até atingir o valor de referência. Esse ajuste elimina o erro estacionário, embora possa tornar a resposta mais lenta.

---

**Questão 7**

- **Resposta**: B) \( K_p = 9 \frac{J_0^2 + k_1VJ_0 + k_2k_3V^2}{k_2VJ_0} \)
- **Explicação**:
  - Essa alternativa atende à condição de que a concentração de bactérias em regime permanente não seja inferior a 90% do valor de referência \( CR \), conforme a especificação do sistema de controle em malha fechada para o quimiostato. A constante \( K_p \) deve ser configurada para garantir essa condição de operação, e a fórmula correta é dada na alternativa B.

---

**Questão 8**

- **Resposta**: D) O erro estacionário seria infinito.
- **Explicação**:
  - Se a entrada \( CR(s) \) fosse uma rampa, o erro estacionário aumentaria continuamente, resultando em um valor infinito, uma vez que o sistema PID, para entradas rampa, não elimina o erro estacionário.

---

**Questão 9**

- **Resposta**: B) alterar a estrutura do controlador, fazendo com que a ação derivativa atue somente sobre o percurso de retroação.
- **Explicação**:
  - A ação derivativa no percurso direto pode amplificar variações abruptas como pulsos, resultando em picos indesejados. A atuação no percurso de retroação reduz o impacto direto sobre a saída, minimizando pulsos que causam desgaste.

---

**Questão 10**

- **Resposta**: B) 5
- **Explicação**:
  - O estudante dividiu a soma das notas por 5 em vez de 4, resultando em uma média que ficou 1 unidade menor. Para corrigir o erro, a média correta das notas é 5, conforme indicado na alternativa B.

---

## Dissertativas

**Questão 1**

1. **Identificar a Função de Transferência**:
   - A função de transferência é \( G(s) = \frac{16}{s^2 + 4s + 16} \), típica de um sistema de segunda ordem. Comparando com a forma padrão \( G(s) = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2} \), obtemos:
     - \(\omega_n = 4\)
     - \(\zeta = 0,5\), indicando que o sistema é **subamortecido** (com oscilações antes da estabilização).

2. **Calcular o Tempo de Acomodação (\(t_s\))**:
   - Utilizando \( t_s = \frac{4}{\zeta \omega_n} \):
     \[
     t_s = \frac{4}{0,5 \times 4} = 2 \text{ segundos}
     \]
   - **Conclusão**: Após 2 segundos, a balança se estabiliza, fornecendo uma leitura precisa do peso do caminhão.

---

**Questão 2**

1. **Análise Técnica da Função de Transferência**:
   - A função \( G(s) = \frac{16}{s^2 + 4s + 16} \) representa um sistema de segunda ordem. Calculamos:
     - **Frequência natural (\(\omega_n\))**: 4.
     - **Coeficiente de amortecimento (\(\zeta\))**: 0,5, caracterizando o sistema como **subamortecido**, com oscilações antes da estabilização.

2. **Parâmetros de Resposta do Sistema**:
   - **Sobressinal Máximo (\(M_p\))**:
     \[
     M_p = e^{\frac{-\zeta \pi}{\sqrt{1 - \zeta^2}}} \approx 16,3\%
     \]
   - **Tempo de Pico (\(t_p\))**:
     \[
     t_p = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}} \approx 0,91 \text{ segundos}
     \]
   - **Tempo de Acomodação (\(t_s\))**: 2 segundos.

3. **Considerações Técnicas**:
   - O sistema estabiliza em 2 segundos, suficiente para uma leitura precisa. Leituras feitas antes disso captam oscilações, levando a variações na medição.

4. **Conclusão do Parecer**:
   - **O sistema é adequado para leituras feitas após 2 segundos**, eliminando o impacto das oscilações iniciais e garantindo precisão na pesagem. Leituras antes disso podem resultar em discrepâncias, como visto nas balanças. Recomenda-se que as medições respeitem o tempo de acomodação.


**Questões**

1. **Questão 1**: D) II e III, apenas
2. **Questão 2**: D) \( kp \times \text{Erro} + ki \times \text{ITerm} + kd \times dErro \)
3. **Questão 3**: A) As assertões I e II são proposições verdadeiras, e a II é uma justificativa da I
4. **Questão 4**: C) I e IV
5. **Questão 5**: A) A variável X corresponde à ação de controle integral; a variável Y, à ação proporcional; e a variável Z, à ação derivativa
6. **Questão 6**: A) Aumento do ganho integral (\( K_i \)), tornando a resposta mais lenta
7. **Questão 7**: B) \( K_p = 9 \frac{J_0^2 + k_1VJ_0 + k_2k_3V^2}{k_2VJ_0} \)
8. **Questão 8**: D) O erro estacionário seria infinito
9. **Questão 9**: B) Alterar a estrutura do controlador, fazendo com que a ação derivativa atue somente sobre o percurso de retroação
10. **Questão 10**: B) 5