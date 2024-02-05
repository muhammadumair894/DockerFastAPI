#Code
from fastapi import FastAPI
import nest_asyncio
#from pyngrok import ngrok
import uvicorn


#from transformers import pipeline

#model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
#sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)


app = FastAPI()

@app.get('/enwi')
async def abc():
  st = ''
  for i in range(10):
    st += str(i * 2) + " "

  return st


#@app.get('/sentiment/{intput_text}')
#async def mlmodel(intput_text):
#
#  result = sentiment_task(intput_text)

#  return result

@app.get('/a/{name}/{password}')
async def abc(name, password):

  if int(password) == 123 and name == "abc":
    return "Correct password"
  else:
    return "Incorrect Password"

@app.get('/')
async def home():
  return "Hello Atom Camp"

#ngrok_tunnel = ngrok.connect(8000)
#print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
#uvicorn.run(app, port=8000)
