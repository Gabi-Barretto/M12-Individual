### Documentação do Projeto de Realidade Virtual e Aumentada

Este projeto utiliza tecnologias de Realidade Virtual (VR) e Realidade Aumentada (AR) para criar experiências interativas. Ele combina as funcionalidades da biblioteca A-Frame para renderização de cenas 3D e AR.js para integração de realidade aumentada baseada em marcadores.

---

### **Descrição Geral**
O projeto é dividido em dois principais componentes:

1. **Realidade Virtual (VR):**  
   Oferece uma experiência imersiva utilizando imagens 360° e interatividade com cursor.

2. **Realidade Aumentada (AR):**  
   Requer um marcador do tipo "HIRO" para exibir um modelo 3D na câmera em um ambiente do navegador.

---

### **Configuração no Glitch**
O projeto foi hospedado no Glitch e pode ser acessado no seguinte link:  
[Deploy no Glitch](https://tortoiseshell-regular-dance.glitch.me/)

---

### **Arquivos Principais**

#### **1. `index.html` (Portal de Escolha)**  
Este arquivo apresenta uma interface simples para escolher entre Realidade Virtual e Realidade Aumentada.

- **Elementos Importantes:**
  - Botões para redirecionamento:
    - **VR:** Aponta para o arquivo `Virtual/index.html`.
    - **AR:** Aponta para o arquivo `Augmented/exemplo-4.html`.
  - Link para download do marcador "HIRO" necessário para AR:  
    [HIRO Marker](https://stemkoski.github.io/AR-Examples/markers/hiro.png)
  - Estilização amigável e responsiva.

---

#### **2. `exemplo-4.html` (Realidade Aumentada)**

- **Funcionalidade:**
  - Usa a biblioteca **AR.js** para realidade aumentada.
  - Modelo 3D importado no formato GLTF é exibido sobre o marcador "HIRO".
  - Configuração com `a-marker` para detecção do marcador e `a-entity` para renderizar o modelo.

- **Tecnologias Utilizadas:**
  - A-Frame (versão 1.3.0): Para renderizar a cena 3D.
  - AR.js: Para integração com a realidade aumentada.

---

#### **3. `index.html` (Realidade Virtual)**

- **Funcionalidade:**
  - Cria um ambiente VR com:
    - **Imagem 360° como céu** usando `a-sky`.
    - **Texto 3D** posicionado em diferentes locais com `a-text`.
    - **Interatividade:** Câmera e cursor permitem ações baseadas em clique.
  - Utiliza uma imagem personalizada para o céu 360°.

- **Tecnologias Utilizadas:**
  - A-Frame (versão 1.6.0): Para renderizar a cena virtual.

---

### **Ferramentas e Tecnologias**
1. **A-Frame:**  
   Framework para criação de experiências 3D e VR na web.
   - Versões utilizadas: 1.3.0 e 1.6.0.
   - Documentação: [A-Frame Docs](https://aframe.io/docs/)

2. **AR.js:**  
   Framework de código aberto para AR baseada na web. Suporta renderização com marcadores e localização.
   - Documentação: [AR.js](https://ar-js-org.github.io/AR.js-Docs/)

3. **Marcador HIRO:**  
   Marcador padrão para demonstrações de AR.js. Pode ser obtido no link [HIRO Marker](https://stemkoski.github.io/AR-Examples/markers/hiro.png).

---

### **Passos para Execução**
1. Acesse o portal inicial no link do Glitch.
2. Escolha uma das opções:
   - **Realidade Virtual:** Explorar o ambiente 360° e interagir com elementos.
   - **Realidade Aumentada:** Exibir o modelo 3D sobre o marcador "HIRO".
3. Para AR, imprima ou exiba o marcador "HIRO" em uma tela e permita que a câmera detecte.

---

### **Estudos Recomendados**
- **A-Frame:** Entender o uso de `a-scene`, `a-assets`, e entidades básicas como `a-text` e `a-sky`.
- **AR.js:** Aprender sobre o funcionamento de `a-marker` e a renderização de modelos GLTF.
- **Modelos 3D (GLTF):** Preparação e otimização de modelos 3D para web.
- **Hospedagem no Glitch:** Passos para publicar e depurar projetos web.