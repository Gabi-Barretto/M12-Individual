# Documentação: Criação de Humanos Virtuais em Realidade Virtual (RV)

## Objetivo

O objetivo desta atividade é desenvolver uma experiência imersiva utilizando um humano digital. Ao final, cada participante deverá apresentar uma **animação completa de um humano digital**, abrangendo:

- **Aparência personalizada.**
- **Justificativa de design.**
- **Integração de áudio e animação.**
- **Deploy funcional no Meta Quest para demonstração prática.**

---

### **Parte 1: Contextualização, Descrição e Justificativa**  

#### **Definição do Propósito**  
O humano virtual será utilizado como um **educador em realidade virtual**, focado no ensino de geografia para escolas remotas. Ele atuará como um professor interativo e imersivo, capaz de criar experiências educativas únicas e acessíveis para alunos que não possuem fácil acesso a recursos educacionais tradicionais.  

#### **Área de Aplicação**  
A área escolhida é a **educação em realidade virtual**, com ênfase no ensino remoto e imersivo. O avatar irá atuar como um **professor de geografia** em uma sala de aula virtual, trazendo uma abordagem inovadora ao processo de aprendizagem, com mapas interativos, simulações de fenômenos naturais e cenários 3D como vulcões, florestas e desertos.  

#### **Descrição Detalhada do Humano Virtual**  

- **Nome:** Prof. André  
- **Personalidade:** O Prof. André é um educador calmo, paciente e didático, com uma voz acolhedora e um tom motivador que incentiva os alunos a interagirem e explorarem o conteúdo. Ele está sempre disposto a esclarecer dúvidas e adaptar o ritmo das explicações para o nível dos alunos.  

- **Função:** Sua principal função é ensinar geografia de maneira interativa e personalizada, conduzindo os alunos em explorações virtuais que complementem o aprendizado teórico com experiências práticas.  

- **Cenário de Uso:** O avatar será usado em **salas de aula virtuais**, onde os alunos podem participar remotamente usando dispositivos de realidade virtual, como o Meta Quest. As aulas podem ser utilizadas tanto para ensino regular quanto em atividades de reforço escolar ou programas de alfabetização digital.  

#### **Justificativa da Escolha da Aparência**  

A aparência do Prof. André foi pensada para refletir confiança, acessibilidade e autoridade, sem ser intimidadora. A seguir, os detalhes que justificam as escolhas:  

1. **Aparência Adulta:** Representa maturidade e experiência, transmitindo confiança aos alunos e garantindo que ele seja reconhecido como uma figura de liderança em sala de aula.  
2. **Tom de Pele Médio:** Reflete diversidade e neutralidade, para que o avatar possa ser mais facilmente aceito por diferentes públicos culturais e sociais.  
3. **Óculos:** Adicionam um aspecto de intelectualidade e reforçam a imagem de um professor tradicional.  
4. **Vestuário Formal:** O Prof. André utiliza uma camisa social e calça preta, transmitindo profissionalismo e autoridade. O visual é formal o suficiente para inspirar respeito, mas não rígido a ponto de criar desconforto ou distância emocional.  
5. **Expressões Faciais Suaves:** Ele tem expressões amigáveis e engajantes, projetadas para manter a atenção e reduzir qualquer ansiedade ou desconforto que os alunos possam sentir em ambientes virtuais.  

Essa aparência busca criar um **equilíbrio entre formalidade e acolhimento**, essencial para manter a autoridade necessária em um ambiente educacional, sem deixar de ser acessível para estudantes de diferentes idades e contextos.  

#### **Objetivo Final da Justificativa**  
A aparência e o comportamento do Prof. André foram projetados para maximizar o engajamento dos alunos e proporcionar uma experiência educativa imersiva que seja eficiente, acessível e impactante, utilizando o poder da realidade virtual para transformar o aprendizado.  

![André](../Mídia/Andre.png)

--- 

### **Parte 2: Criação no MetaHuman Creator**  

[Link para o arquivo MetaHuman](https://github.com/Gabi-Barretto/M12-Individual/tree/master/Parte-2/src/Semana-2/src/model)

---

### **Parte 3: Idealizando a Animação**

#### **Roteiro Utilizado**
O texto foi criado com o objetivo de apresentar as cinco regiões do Brasil de forma didática e engajante. O Professor André conduz a aula de maneira amigável e educativa:

---

**Texto Utilizado**  
*Olá, eu sou o Professor André, e hoje vamos aprender algo muito importante sobre o nosso país, as cinco regiões do Brasil ... Vamos explorar juntos as diferenças e características de cada uma delas! ... Você sabia que o Brasil é dividido em cinco grandes regiões? ... Cada uma tem suas características próprias, como cultura, clima e economia. ... O Norte é a maior região, famosa por abrigar a Floresta Amazônica, o maior bioma do mundo! ... O Nordeste tem praias incríveis, é muito rico em cultura e história, e é o maior produtor de frutas tropicais do país. ... No Centro-Oeste, encontramos o Pantanal, a maior área alagada do planeta, e a capital do Brasil, Brasília! ... O Sudeste é a região mais populosa e industrializada do Brasil, com grandes cidades como São Paulo e Rio de Janeiro. ... E no Sul, temos um clima mais frio e paisagens lindas, como as serras gaúchas e catarinenses. ... E aí, gostaram dessa viagem pelo Brasil? ... Agora vocês já sabem um pouco mais sobre as nossas regiões e suas riquezas. ... Até a próxima aula!*

---

#### **Ferramenta Utilizada**
- **SpeechGen**: Gerador de texto para fala, acessível em [speechgen.io](https://speechgen.io/pt/).
- Configuração: 
  - **Voz Masculina** com tom amigável e didático.
  - Pausas indicadas no texto com "..." para fluidez na narração.

---

#### **Processo**
1. **Inserção do Texto**: O texto foi carregado na interface da ferramenta **SpeechGen**.
2. **Ajustes de Voz**: Selecionada uma voz que melhor representasse o Professor André, com entonação calma e didática.
3. **Exportação do Áudio**: Gerado em formato `.mp3` e segmentado por trechos.

---

#### **Resultado**
O áudio gerado foi claro, com pausas estratégicas, e compatível com a sincronização no MetaHuman no Unreal Engine. As animações labiais e gestuais foram configuradas para acompanhar o roteiro.