import nltk
from nltk.chat.util import Chat, reflections

# Definindo padrões e respostas
pares = [
    (r"oi|olá|oi tudo bem", ["Olá, como posso ajudar?", "Oi! Como você está?"]),
    (r"qual é o seu nome?", ["Meu nome é cuzão!", "Você pode me chamar de cuzão."]),
    (r"como você está?", ["Estou bem, obrigado por perguntar!", "Estou ótimo! E você?"]),
    (r"qual é a sua função?", ["Eu sou um chatbot, aqui para ajudar com suas dúvidas.", "Estou aqui para conversar e ajudar!"]),
    (r"tchau|até logo", ["Tchau! Tenha um ótimo dia!", "Até logo! Volte sempre!"]),
    (r"vai se foder", ["vai tomar no cu fdp arrombado do caralho"])
    
]

# Função para iniciar o chatbot
def chatbot():
    print("ChatBot: Olá, sou o ChatBot. Como posso ajudar você? (Digite 'tchau' para encerrar a conversa)")
    chat = Chat(pares, reflections)
    chat.converse()

# Executar o chatbot
if __name__ == "__main__":
    chatbot()
