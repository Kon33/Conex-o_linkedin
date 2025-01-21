# Automação com PyAutoGUI - Guia de Configuração e Utilização

Este guia detalha como configurar e usar um código em Python que automatiza ações na interface gráfica do computador utilizando a biblioteca **PyAutoGUI**.

---

## Pré-requisitos

Antes de começar, certifique-se de:

1. **Instalar a Biblioteca PyAutoGUI**:
   - Rode o seguinte comando no terminal para instalar:
     ```bash
     pip install pyautogui
     ```

2. **Entender a Lógica do Código**:
   - Este código realiza cliques automáticos em posições específicas da tela. Para isso, você precisará obter as coordenadas corretas para sua configuração.

---

## Passo 1: Configurar a Barra de Tarefas

1. Verifique em qual **slot** da barra de tarefas está o navegador que será utilizado. Por exemplo:
   - O primeiro ícone à direita do botão do Windows é o **slot 1**.
   - O segundo ícone é o **slot 2**.
   - Identifique o slot correspondente e substitua no código:
     ```python
     navegador_slot = "1"  # Substitua pelo número correto
     ```

---

## Passo 2: Obter Coordenadas do Mouse

Para garantir que o código clique nos locais corretos, siga os passos abaixo:

1. **Abra o Arquivo `co.py`**:
   - Esse script deve capturar a posição do mouse.

2. **Posicione o Mouse**:
   - Mova o cursor para o botão **"Minhas Conexões"** (ou qualquer outro alvo necessário).
   - Aguarde **10 segundos** com o cursor parado (o tempo é configurado no script).

3. **Capturar Coordenadas**:
   - Após os 10 segundos, o script exibirá as coordenadas do local onde o mouse estava posicionado. Anote as coordenadas fornecidas.

4. **Repita o Processo**:
   - Agora, mova o cursor para o botão **"Exibir Tudo"** ou outros alvos necessários em sequência.
   - Rode o `co.py` novamente e capture as coordenadas de cada botão.

---

## Passo 3: Substituir as Coordenadas no Código Principal

Abra o código principal do script (exemplo: `automacao.py`) e substitua as coordenadas capturadas no lugar das coordenadas padrão:

```python
# Exemplo de estrutura de cliques
pyautogui.click(x=123, y=456)  # Coordenadas para o botão "Minhas Conexões"
pyautogui.click(x=789, y=101)  # Coordenadas para o botão "Exibir Tudo"
