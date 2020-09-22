from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Mark')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

trainer.train("chatterbot.corpus.english.greetings")

trainer.train("chatterbot.corpus.english.conversations")

while True:
    question = input("You: ")
    response = chatbot.get_response(question)
    print("Bot: " + response)