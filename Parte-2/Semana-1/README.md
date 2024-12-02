# **Realidade Ampliada (RA) e Realidade Virtual (VR)**

## **1. Introdução**

### **1.1 O que é Realidade Ampliada (RA)?**
A Realidade Ampliada (RA) é uma tecnologia que combina elementos do mundo real com objetos virtuais, sobrepondo gráficos, sons e outros estímulos sensoriais ao ambiente físico. O conceito foi introduzido em 1992 por Thomas Preston Caudell, e Paul Milgram e Fumio Kishino criaram o "continuum real-virtual", que descreve a transição gradual do real para o virtual.

#### **Exemplos de Aplicações**
- **Educação**: Simulações de fenômenos científicos ou históricos.
- **Saúde**: Treinamentos cirúrgicos e diagnósticos assistidos.
- **Entretenimento**: Jogos interativos e experiências imersivas.

---

### **1.2 O que é Realidade Virtual (VR)?**
A Realidade Virtual (VR) transporta o usuário para ambientes completamente digitais e imersivos, permitindo interações por meio de dispositivos como óculos VR. No contexto deste projeto, a VR é explorada utilizando imagens 360° e elementos interativos no navegador.

---

### **1.3 Características**
| RA                                       | VR                                       |
|------------------------------------------|------------------------------------------|
| Integração do real com o virtual.        | Criação de ambientes digitais imersivos. |
| Interatividade em tempo real.            | Imersão total no ambiente virtual.       |
| Acessível com dispositivos móveis.       | Requer dispositivos especializados.      |

---

## **2. Ferramentas e Tecnologias**

### **2.1 Frameworks e Bibliotecas Utilizadas**
| Ferramenta       | Tipo        | Foco Principal                | Ideal Para                                   |
|-------------------|-------------|--------------------------------|---------------------------------------------|
| **A-Frame**       | Framework   | Criação de cenas 3D rápidas   | Prototipagem de RA e VR                     |
| **AR.js**         | Biblioteca  | Integração de RA no navegador | Prototipagem rápida com marcadores          |
| **WebXR API**     | Biblioteca  | RA e VR customizados          | Controle total de RA e VR                   |

#### **Outras Ferramentas**
- **Three.js**: Renderização 3D detalhada.
- **Unity com Vuforia**: Aplicações robustas de RA.
- **React 360**: Experiências interativas web.

---

## **3. Estrutura do Projeto**

### **3.1 Componentes Principais**
1. **Realidade Virtual (VR)**  
   Oferece uma experiência imersiva utilizando imagens 360° e interatividade com cursor.
   
2. **Realidade Ampliada (AR)**  
   Utiliza o marcador "HIRO" para exibir modelos 3D sobrepostos ao mundo real.

---

### **3.2 Organização de Arquivos**
#### **Portal Inicial (`index.html`)**
Apresenta a interface para escolher entre as experiências de RA e VR:
- **Botões de navegação**:
  - VR → `/Virtual/index.html`
  - AR → `/Augmented/exemplo-4.html`
- **Link para o marcador "HIRO"**:  
  [HIRO Marker](https://stemkoski.github.io/AR-Examples/markers/hiro.png)

---

#### **Realidade Ampliada (`Augmented/exemplo-4.html`)**
- **Tecnologias Utilizadas**:
  - A-Frame (v1.3.0)
  - AR.js
- **Funcionalidade**:
  - Detecta o marcador "HIRO" e exibe um modelo 3D em formato GLTF.

---

#### **Realidade Virtual (`Virtual/index.html`)**
- **Tecnologias Utilizadas**:
  - A-Frame (v1.6.0)
- **Funcionalidade**:
  - Renderiza um ambiente virtual 360° com interatividade baseada em cursor.

---

### **3.3 Tabela Resumida**
| Arquivo           | Tipo             | Função                                                |
|--------------------|------------------|-------------------------------------------------------|
| `index.html`       | Portal           | Interface inicial para escolha entre RA e VR.        |
| `exemplo-4.html`   | Realidade Ampliada | Renderização de RA usando o marcador "HIRO".         |
| `index.html` (VR)  | Realidade Virtual | Ambiente 360° com interatividade baseada em cursor. |

---

## **4. Exemplos Práticos**

### **4.1 Cena Básica em A-Frame (VR)**
```html
<!DOCTYPE html>
<html>
  <head>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-box position="0 1 -5" rotation="0 45 0" color="#4CC3D9"></a-box>
      <a-sphere position="2 1 -3" radius="1.25" color="#EF2D5E"></a-sphere>
      <a-light type="point" intensity="1" position="2 4 -3"></a-light>
      <a-plane position="0 0 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>
    </a-scene>
  </body>
</html>
```

---

### **4.2 RA com Marcadores usando AR.js**
```html
<!DOCTYPE html>
<html>
  <head>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/aframe-ar.js"></script>
  </head>
  <body>
    <a-scene embedded arjs>
      <a-marker preset="hiro">
        <a-box position="0 0.5 0" material="color: red;"></a-box>
      </a-marker>
      <a-entity camera></a-entity>
    </a-scene>
  </body>
</html>
```

---

## **5. Aplicações e Próximos Passos**

### **5.1 Aplicações**
- **Educação**: Simulações científicas interativas.
- **Saúde**: Treinamento médico em ambiente imersivo.
- **Turismo**: Tours virtuais de locais históricos ou culturais.
- **Entretenimento**: Jogos e narrativas imersivas.

---

### **5.2 Próximos Passos**
1. Experimentar bibliotecas avançadas como **Three.js**.
2. Desenvolver projetos robustos de RA utilizando **Unity com Vuforia**.
3. Integrar tecnologias de IA para reconhecimento de objetos em tempo real.

---

## **Link para Hospedagem no Glitch**:  

### **[Deploy no Glitch](https://tortoiseshell-regular-dance.glitch.me/)**