# Em automações ou análises de dados, o passo a passo costuma ser linear: primeiro uma etapa, depois outra.
# Em um site ou chatbot , o passo a passo representa:
# • O que existirá dentro do sistema .
# • Como o usuário vai interagir com esses elementos
# • Como o sistema deve responder


# Planejamento do projeto:
# Streamlit -> Biblioteca usada para desenvolver front-end e back-end apenas com python.
# OpenAI -> IA usada
# Passo 1: Elementos do Sistema
import streamlit as st
    # • Título do sistema: visível na parte superior da página.
st.write('# Chatbot com IA') # markdown
    # • Campo de mensagem(input do chat) espaço onde o usuário digita mensagens.
texto_usuario = st.chat_input('Digite sua mensagem  ')

# Passo 2: Funcionamento do Chat(Ciclo de funcionamento)
    # • Exiba a mensagem enviada na tela, construindo visualmente o histórico da conversa.
# verifica e cria lista de historico se necessário
if not 'historico_mensagens' in st.session_state:
    st.session_state['historico_mensagens'] = []

# percorre a lista de mensagens dentro do histórico e exibe elas na interface
for mensagem in st.session_state['historico_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)

# Quando enviado um texto não nulo, pela caixa de texto, exibe/guarda no historico a mensagem e resposta da ia
if texto_usuario:
    st.chat_message('user').write(texto_usuario)
    mensagem_usuario = {'role': 'user', 'content': texto_usuario}
    st.session_state['historico_mensagens'].append(mensagem_usuario)
    
    # • Envie a mensagem para a Inteligência Artificial, que processará a pergunta e gerará a resposta .
    from openai import OpenAI

    chatbot_ia = OpenAI(api_key='placeholder')
    resposta_ia = chatbot_ia.chat.completions.create(
        messages= st.session_state['historico_mensagens'],
        model= 'gpt-4o'
    )
    texto_ia = resposta_ia.choices[0].message.content
    st.chat_message('ai').write(texto_ia)
    mensagem_ia = {'role': 'ai', 'content': texto_ia}
    st.session_state['historico_mensagens'].append(mensagem_ia)

    # • Mostre a resposta retornada pela IA no chat.
