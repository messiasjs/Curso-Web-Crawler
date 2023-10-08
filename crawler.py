import requests
from bs4 import BeautifulSoup

noticias = []
# URL dos sites
urls = [
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias"
]

# Função para obter a imagem no link da noticia
def obter_imagem(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    image = soup.find("div", {"id": "media"})
    return image

# Função para extrair informaçoes do site
def extrair_noticias(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extrair informações específicas
    for news in soup.find_all("div", class_="conteudo"):
        
        if news:
            titulo = news.find('a')
            descricao = news.find('span', class_='descricao')
            data = news.find('span', class_='data')
            link = titulo['href']
            img = obter_imagem(link)

        noticia = dict()
        noticia['titulo'] = titulo.text
        noticia['descricao'] = descricao.text.strip().split('\n')[2]
        noticia['link'] = link
        if img:
            noticia['imagem'] =img.img['src']
        else :
             noticia['imagem'] = "Sem imagem"
        noticia['data'] = data.text.strip()
        noticias.append(noticia)
    return noticias

# Iterar pelas URLs e exibir informações
for url in urls:
    for info in extrair_noticias(url):
        print(f"1. Título: {info['titulo']}")
        print(f"2. Descrição: {info['descricao']}")
        print(f"3. Link: {info['link']}")
        print(f"4. Imagem: {info['imagem']}")
        print(f"5. Data: {info['data']}")
        print("\n___________________________________\n\n")
