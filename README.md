# 🎹 Piano de Cauda - Simulação Interativa 3D

Projeto desenvolvido para a disciplina de **Computação Gráfica** (Avaliação A3), focado na renderização e manipulação de objetos tridimensionais complexos utilizando o pipeline gráfico do OpenGL.

## 🚀 Tecnologias Utilizadas
* **Python 3.1x**
* **Pygame**: Gerenciamento de janela e eventos de entrada.
* **PyOpenGL**: Interface com a API gráfica para renderização em tempo real.
* **OpenCV**: Processamento de imagens e texturas.
* **Math/NumPy**: Cálculos trigonométricos para movimentação de câmera.

## 🛠️ Funcionalidades Implementadas
- [x] **Renderização de Malha Complexa**: Carregamento de arquivo `.obj` com suporte a múltiplos materiais.
- [x] **Câmera Orbital Interativa**: Sistema de visualização baseado em coordenadas esféricas (Yaw/Pitch).
- [x] **Iluminação Dinâmica**: Implementação do modelo de Phong (Luz Ambiente, Difusa e Especular).
- [x] **Mapeamento de Reflexo**: Efeito de verniz "Piano Black" utilizando *Sphere Mapping*.
- [x] **Controles Amigáveis**: Interface via teclado para navegação no espaço 3D.

## Comandos
| Tecla | Ação |
| :--- | :--- |
| `Setas Esq/Dir` | Orbitar horizontalmente (Yaw) |
| `Setas Cima/Baixo` | Inclinar câmera verticalmente (Pitch) |
| `W/S` | Aproximar/Afastar câmera (Zoom In/Zoom Out) |
| `A/D` | Aumentar/Dimunir escala |

## 🏗️ Arquitetura do Projeto
- `main.py`: Ponto de entrada, configuração do contexto e loop principal.
- `camera.py`: Lógica matemática da câmera e transformações de visão.
- `mesh.py`: Motor de renderização que processa vértices, normais e materiais.
- `loadMesh.py`: Parser para importação de modelos 3D (.obj).
- `textures/`: Repositório de mapas de textura e reflexo.

---
**Desenvolvido por:** Gabriel Fleischmann Funck (@gabrielfleischmann) e Luiza Fioravante Regina Soares (@Lulizza)
