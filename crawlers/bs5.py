from bs4 import BeautifulSoup as soup
import requests

subreddits = "worldnews;programming;dogs;brazil;science;UnresolvedMysteries"
subs = subreddits.split(";")


for subreddit in subs :
    aux = 0 #variavel de controle criada para saber se existem upvotes maiores que 5000 ou não
    upvotelist = []
    my_url = 'https://old.reddit.com/r/' + subreddit + '/'

    # abrir a conecxão com o servidor
    page_html = requests.get(my_url, headers = {'User-agent': 'your bot 0.1'})
    html = page_html.text
    # html parsing
    page_soup = soup(html, "html.parser")

    #usando a função findAll para procurar todos os upvotes no site
    upvotes =page_soup.findAll("div",{"class":"score unvoted"})

    #como os dados vindos do findAll estao em formato de texto.Foi necessário esse procedimento para tranformar os dados em inteiros
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
    if len(titles)==1:
        titles = page_soup.findAll("a", {"class": "title may-blank outbound"})

    for cont in range(0,len(upvotes)):

        if(upvotelist[cont]>5000):
            aux = 1 #variavel de controle criada para saber se existem upvotes maiores que 5000 ou não

            print("O subreddits é : ", subreddit)
            print("Quantidade de upvotes é: ",upvotelist[cont])
            print("O título da thread é : ", titles[cont].text)
            print("O link para a thread é : https://old.reddit.com" + titles[cont].attrs['href'])
            print("Para acessar os comentários :https://old.reddit.com" + titles[cont].attrs['href'])
            print("\n---------------------------------------------------------------------------------------------------\n")

    if aux==0 :
        print("O subreddits " + subreddit + " ainda não existe threads com 5000 pontos ou mais ")




