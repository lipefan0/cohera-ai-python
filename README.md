# Exemplo de Utilização da API Cohere em uma Página Web

Este projeto demonstra como utilizar a API da Cohere para integrar inteligência artificial em uma página web simples. Através deste exemplo, você aprenderá a configurar uma página web que se comunica com a API da Cohere e exibe respostas geradas pela IA.

## Funcionalidades

- **Formulário Web Simples:** Uma página com um formulário contendo um campo de texto (`textarea`) e um botão de envio.
- **Integração com a API Cohere:** O backend utiliza a API da Cohere para processar as entradas do usuário e gerar respostas inteligentes.
- **Exibição de Resultados:** As respostas da API são exibidas na própria página web após o envio do formulário.

## Tecnologias Utilizadas

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **API:** Cohere

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- Python 3.x
- Pip (gerenciador de pacotes Python)
- Flask
- Acesso à API da Cohere (você precisará de uma chave de API)

## Configuração do Projeto

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/lipefan0/cohera-ai-python.git)
   cd cohera-ai-python
   ```
2. **Configurando o arquivo .env:**
   Crie um arquivo .env e edite:
   ```env
   AI_SECRET_KEY="sua_api_key_cohera"
   ```
3. **Execute o arquivo python**
4. **Abra o Navegador:**
    Acesse http://localhost:5000 para ver a página web em funcionamento.

## Estrutura do Projeto
- **ai-cohere.py:** Código do servidor Flask que manipula as requisições e interage com a API da Cohere.
- **templates/index.html:** Contém o arquivo HTML para o frontend.
- **.env:** Arquivo de configuração para armazenar a chave da API.

## Exemplos de Uso
1. Abra a página web no navegador.
2. Digite um texto no campo textarea.
3. Clique no botão de envio para ver a resposta gerada pela API da Cohere exibida na página.

## Contribuições
Sinta-se à vontade para abrir issues e pull requests se você encontrar bugs ou tiver sugestões de melhorias!
