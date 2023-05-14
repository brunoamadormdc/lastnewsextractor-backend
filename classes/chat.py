import os
import openai
import nltk
import re
nltk.download('punkt')

openai.organization = os.getenv("OPEN_AI_ORG")
openai.api_key = os.getenv("OPEN_AI_KEY")

class Chat:
    def __init__(self):
        pass

    def chat_with_intelligence(self,prompt='',content=''):

        try:
            tokens = nltk.word_tokenize(content)
            if len(tokens) > 2500:
                tokens = tokens[:1500]
            
            tokens = ' '.join(tokens)
            
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt},
                    {"role": "user", "content": tokens},
                    {"role": "user", "content": 'Se o conteúdo acima estiver em outro idioma, por favor, traduza a resposta para o português'},
            ]
            )
            return completion.choices[0].message
        except:
            raise Exception('Ocorreu um erro ao gerar o resumo')
        
