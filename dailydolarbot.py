import tweepy
import requests
import time
from datetime import datetime, timedelta

#Chaves e permissões (Utilize suas próprias chaves da sua conta do twitter developer)
api_key = ''
api_secret_key = ''
acess_key = ''
acess_secret = ''

#Autenticar no Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)

#Criar objeto da API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

for i in range(33):
    #Requisição do site
    request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    request.dic = request.json()

    #Achar valor do dólar
    cotacao_dolar = request.dic['USDBRL']['bid']
    cotacao_dolar = float(cotacao_dolar)

    #Data e Hora
    data = datetime.now()
    horas = -6
    hora_utc = data + timedelta(hours=horas)
    data_utc_string = data.strftime("%d/%m/%Y")
    hora_utc_string = hora_utc.strftime("%H:%M:%S")

    #Tweet
    text = f"""💰💸 Atualização! 💸💰
        Dia: {data_utc_string} às {hora_utc_string} 
        US$ 1.00 é igual à R${cotacao_dolar:,.2f}
        .
        .
        .
        .
        .
        .
        .
        #dolar #real #money"""

    #Postar tweet
    api.update_status(text)
    print('Tweet publicado com sucesso')
    time.sleep(60*15)
