import telepot
from bs4 import BeautifulSoup as soup
import requests

#token para o bot (Idwall-Andrey)
token = "788528548:AAGhgmDUNId8RGF6t2B1TyVEPD-tyr7gim8"

#conexão com o bot
bot = telepot.Bot(token)

#variavel para guardar o comando enviado no telegram
comando = []

#função implementada no desafio parte 1
def buscaDados(msg,id):

    subreddits = msg

    subs = subreddits.split(";")

    for subreddit in subs :
        aux = 0 #variavel de controle criada para saber se existem upvotes maiores que 5000 ou não
        upvotelist = [] #lista com os upvotes
        my_url = 'https://old.reddit.com/r/' + subreddit + '/'

        # abrir a conecxão com o servidor
        page_html = requests.get(my_url, headers = {'User-agent': 'your bot 0.1'})
        html = page_html.text
        # html parsing
        page_soup = soup(html, "html.parser")

        #usando a função findAll para procurar todos os upvotes no site
        upvotes =page_soup.findAll("div",{"class":"score unvoted"})

        #como os dados vindos do findAll estao em formato de texto. Foi necessário esse procedimento para tranformar os dados em inteiros
        for container in upvotes :
            upvote = container.text
            # Caso a potuação esteja com '•', substitui por 0
            if  '•' in upvote:
                upvote = upvote.replace('•', '0')
                upvotelist.append(int(upvote))

            # Caso a potuação possua um 'k' que equivale a 1000, substitui por o k por vazio e multiplica com 1000
            if 'k' in upvote:
                upvote = float(upvote.replace('k', '')) * 1000
                upvotelist.append(int(upvote))

            else:
                upvotelist.append(int(upvote))

        # usando a função findAll para procurar todos os títulos, das threads no site
        titles = page_soup.findAll("a",{"class":"title may-blank "})
        
        #Alguns titulos de ssubreddits apresentavam a classe diferente, por isso foi usado esse if, para tratar esses casos
        if len(titles) == 1:
            titles = page_soup.findAll("a", {"class": "title may-blank outbound"})
        
        for cont in range(0,len(upvotes)):

            if(upvotelist[cont]>=5000):

                aux = 1 #Caso exista 5000 ou mais upvotes a variável "aux" recebe "1" para controle
                bot.sendMessage(id,"----------------------------------------------------------------------------\n" +
                                "O subreddits é : "+ subreddit + "\n" + "Quantidade de upvotes é: "
                                + str(upvotelist[cont]) + "\n" + "O título da thread é : " + titles[cont].text +
                                "\n" + "O link para a thread é : https://old.reddit.com" + titles[cont].attrs['href'] +
                                "\n" + "Para acessar os comentários :https://old.reddit.com" + titles[cont].attrs['href'])

        if aux==0 :
            bot.sendMessage(id, "O subreddits " + subreddit + " não possuem threads com 5000 pontos ou mais")

#função para receber a mensagem do telegram e adequar o texto para a função buscaDados
def recebendoMsg (msg) :
    content_type, chat_type, chat_id = telepot.glance(msg)
    texto = msg['text']
    id = chat_id
    comando = texto.split(" ")

    if comando[0] == "/NadaPraFazer" :
        buscaDados(comando[1],id)

#função da biblioteca que fica procurando mensagens enviadas no telegram
bot.message_loop(recebendoMsg)

#laço infinito para ficar esperando mensagens enquanto o programa estiver rodando
while True :
    pass
