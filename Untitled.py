
from chatterbot.trainers import ListTrainer #Method to train the chatbot
from chatterbot import ChatBot # import chart bot
import os # import OS module

bot = ChatBot('Test') # create a chatbot called Test
bot.set_trainer(ListTrainer) 
for _file in os.listdir('/Users/vijay/Documents/ChatBot/test'): # Path of training file 
    chats = open('test/' + _file, 'r', encoding='latin-1').readlines()
    
    bot.train(chats) # Train the chatbot
    
while True:
    request = input('You: ')
    response = bot.get_response(request)
    
    print('Bot: ', response)






