# **Criação de Humanos Virtuais em Realidade Virtual (RV)**

## **Visão Geral**
Este projeto tem como objetivo criar um humano digital interativo para aplicações educacionais em realidade virtual, com foco na personalização visual, animação sincronizada e funcionalidade em dispositivos Meta Quest. Ao final, o humano digital, denominado **Prof. André**, atuará como um professor interativo, educando alunos em uma experiência imersiva sobre geografia.

---

## **Links Importantes**
- [Documentação Completa](https://github.com/Gabi-Barretto/M12-Individual/blob/master/Parte-2/Semana-2/docs/Semana%202%20-%20Pessoa%20Virtual.md)
- [MetaHuman Creator](https://www.unrealengine.com/en-US/metahuman-creator)

---

## **Objetivos do Projeto**
- Desenvolver um **humano digital** com aparência personalizada e justificativa de design.
- Criar animações sincronizadas com narrações interativas e didáticas.
- Realizar o deploy do humano digital para **Meta Quest** e testar a funcionalidade completa.
- Apresentar um cenário educacional virtual inovador para alunos em locais remotos.

---

## **Estrutura do Projeto**
A organização do projeto foi feita de forma modular, abrangendo os seguintes diretórios principais:

### **Diretórios e Arquivos**
- **`MetaHuman`**: Contém o humano digital criado no MetaHuman Creator.
  - `Andre.mhb`: Arquivo de personalização do humano digital.
- **`Midia`**: Armazena imagens e recursos visuais.
  - `image.png`, `image-1.png`: Screenshots do humano digital e cenas do projeto.

---

## **Etapas do Desenvolvimento**

### **1. Planejamento e Justificativa**
Definição do contexto, propósito e descrição detalhada do humano virtual, incluindo aspectos técnicos e pedagógicos. O humano digital, **Prof. André**, foi projetado para atuar como educador interativo em geografia.

### **2. Criação no MetaHuman Creator**
- Personalização visual do Prof. André:
  - Aparência: **Adulto, tom de pele médio, vestuário formal, óculos.**
  - Expressões faciais amigáveis e gestos didáticos.
- Arquivo gerado: `Andre.mhb`.

![Prof. André](./midia/image.png)
![Prof. André em ação](./midia/image-1.png)

### **3. Desenvolvimento de Áudio e Narração**
- **Ferramenta Utilizada**: [SpeechGen](https://speechgen.io/pt/).
- Configuração:
  - Voz masculina, tom amigável e pausas fluentes.
- Resultado: Áudio sincronizado para integração no Unreal Engine.

### **4. Integração no Unreal Engine**
- Importação do humano digital gerado no MetaHuman Creator.
- Sincronização do áudio (`audio.mp3`) com as animações labiais e gestuais.
- Configuração de cenas interativas no Unreal Engine.

### **5. Teste e Deploy**
- Teste em dispositivos Meta Quest para validação da experiência imersiva.
- Ajustes finais para sincronização e usabilidade.

---

## **Ferramentas Utilizadas**
- **MetaHuman Creator**: Personalização do humano digital.
- **SpeechGen**: Geração de áudio narrativo.
- **Unreal Engine**: Integração de animação e deploy.
- **Meta Quest**: Dispositivo para teste e deploy.

---

## **Resultados**
O Prof. André foi configurado com sucesso como um educador virtual interativo. Ele está apto a ensinar sobre as regiões do Brasil em um cenário imersivo, utilizando áudio narrado e animações sincronizadas para engajar os alunos.