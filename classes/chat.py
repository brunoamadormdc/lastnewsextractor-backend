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
            chunked = []
            prompt_response = []

            for i in range(0, len(tokens), 1000):
                chunked.append(' '.join(tokens[i:i+1000]))
                  
            for chunk in chunked:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Sou um redator e trabalho produzindo conteúdos."},    
                        {"role": "user", "content": prompt},
                        {"role": "user", "content": chunk},
                        {"role": "user", "content": 'Use o conteúdo gerado na resposta anterior, para gerar a próxima resposta, mantendo o contexto'},
                        {"role": "user", "content": 'Se o conteúdo estiver em outro idioma, traduza a resposta para o português do Brasil'}
                    ],
                    max_tokens=1000,
                    temperature=.5,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                prompt_response.append(completion["choices"][0]["message"]['content'].strip())

            resumo_consolidado = '<br><br>'.join(prompt_response)
                
            return resumo_consolidado
        
        except:
            raise Exception('Ocorreu um erro ao gerar o resumo')
        
