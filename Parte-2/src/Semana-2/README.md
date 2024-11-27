# **Criação de Humanos Virtuais em RV**

[Link para docs + detalhada](https://github.com/Gabi-Barretto/M12-Individual/blob/master/Parte-2/Docs/Semana%202%20-%20Pessoa%20Virtual.md)

## **Objetivo**
Desenvolver um humano digital interativo para aplicações educacionais em realidade virtual. O projeto inclui:

- Personalização do humano digital.
- Integração de áudio, texto e animações.
- Deploy funcional em dispositivos Meta Quest.

---

## **Diretórios do Projeto**
### Estrutura Principal:
- **`Bark`**:
  - **`audios`**: Contém os áudios gerados para o humano virtual.
  - **`scripts`**: Arquivos de código para a configuração de animações e sincronização.
  - **`texts`**: Textos utilizados para a narração.
  - **`texts-all`**: Versões integradas de textos narrativos.

- **`MetaHuman`**:
  - **`Andre.mhb`**: Arquivo do humano digital criado no MetaHuman Creator.

- **`Mídia`**:
  - **`audio.mp3`**: Áudio final utilizado no projeto.

---

## **Processo de Implementação**

### **1. Criação no MetaHuman Creator**
- Personalização visual do humano virtual, **Prof. André**, incluindo aparência e vestuário que refletem um educador acessível e profissional.
- **Arquivo gerado:** `Andre.mhb`.

### **2. Desenvolvimento da Narração**
- Ferramenta: **SpeechGen** ([speechgen.io](https://speechgen.io/pt/)).
  - **Configurações**:
    - Voz masculina didática e amigável.
    - Texto narrativo segmentado para fluidez.
  - **Áudio exportado:** `audio.mp3`.

### **3. Integração no Unreal Engine**
- Sincronização do áudio gerado (`audio.mp3`) com as animações faciais e gestuais do humano digital no Unreal Engine.
- Testes de funcionalidade no Meta Quest.

---

## **Resultado**
- O humano virtual foi configurado para atuar como educador em realidade virtual.
- A experiência inclui texto, áudio e animações sincronizadas para criar uma aula interativa sobre as regiões do Brasil.
