import os
import cohere
from dotenv import load_dotenv
from flask import Flask, render_template, request
from cohere import Client

app = Flask(__name__)

load_dotenv()

api_key = os.getenv('AI_SECRET_KEY')
client = Client(api_key=api_key)

def obter_resposta(enunciado):
    # Remova a validação temporariamente para testar
    # if not enunciado.strip():
    #     return "Por favor, insira uma pergunta válida."

    prompt = f"Questão: {enunciado}"
    chat_history = []

    try:
        response_generator = client.chat_stream(
            message=prompt,
            chat_history=chat_history
        )

        resposta = ""
        for message in response_generator:
            print(f"Tipo de mensagem recebido: {type(message)}")
            if isinstance(message, cohere.types.streamed_chat_response.StreamedChatResponse_TextGeneration):
                resposta += message.text
            elif isinstance(message, cohere.types.streamed_chat_response.StreamedChatResponse_StreamEnd):
                break

        return resposta.strip()

    except Exception as e:
        return f"Erro: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    resposta = ""
    if request.method == 'POST':
        enunciado = request.form['enunciado']
        print(f"Enunciado recebido: {enunciado}")  # Log do enunciado recebido
        resposta = obter_resposta(enunciado)
        print(f"Resposta retornada: {resposta}")  # Log da resposta retornada
    return render_template('index.html', resposta=resposta)


if __name__ == '__main__':
    app.run(debug=True)
