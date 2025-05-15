# IA-Generativa

# Chatbot com Gemini da Google AI

Este projeto é um chatbot simples que utiliza o modelo Gemini da Google AI para interagir com o usuário. Originalmente desenvolvido no Google Colab, foi migrado para um ambiente local utilizando o VS Code.

## Funcionalidades

* Permite conversas interativas com o modelo Gemini.
* Mantém o histórico da conversa durante a sessão.
* Possui uma instrução de sistema para definir o comportamento do assistente.

## Pré-requisitos

* **Python 3.6 ou superior:** Certifique-se de ter o Python instalado em seu sistema.
* **pip:** O gerenciador de pacotes do Python.
* **Biblioteca `google-generativeai`:** Necessária para interagir com a API do Google AI. Instale-a utilizando o pip:
    ```bash
    pip install google-generativeai
    ```
* **Chave de API do Google AI:** Você precisará obter uma chave de API do Google AI para autenticar seu acesso aos modelos. Siga as instruções na [documentação da Google AI](https://ai.google.dev/) para criar um projeto e obter sua chave.

## Configuração

1.  **Clone o repositório (se aplicável):** Se este projeto estiver em um repositório GitHub, clone-o para o seu computador.
2.  **Instale as dependências:** Certifique-se de ter a biblioteca `google-generativeai` instalada (veja em "Pré-requisitos").
3.  **Configure a chave de API:** Existem duas maneiras principais de configurar a chave de API:

    * **Variável de ambiente (recomendado):** Defina uma variável de ambiente chamada `GOOGLE_API_KEY` com o valor da sua chave de API.
        * **No Linux/macOS:**
            ```bash
            export GOOGLE_API_KEY="SUA_CHAVE_DE_API"
            ```
            Para tornar essa configuração permanente, adicione a linha ao seu arquivo de configuração do shell (e.g., `.bashrc`, `.zshrc`).
        * **No Windows:** Utilize o Painel de Controle para editar as variáveis de ambiente do sistema ou do usuário.
    * **Diretamente no código (para testes locais):** No arquivo `ia_chatbot.py`, você pode substituir a linha comentada:
        ```python
        if not api_key:
            api_key = "SUA_CHAVE_DE_API"
        ```
        pela sua chave real entre as aspas. **Atenção:** Esta não é a forma mais segura para produção.

## Execução

Para executar o chatbot, navegue até o diretório do projeto no seu terminal e execute o script Python:

```bash
python ia_chatbot.py
