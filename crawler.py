import requests
from bs4 import BeautifulSoup
import pymongo

class Noticia:
    def __init__(self, titulo, descricao, data, link, imagem):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.link = link
        self.imagem = imagem

class WebScraper:
    def __init__(self, urls):
        self.urls = urls
        self.noticias = []

    def obter_imagem(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        image = soup.find("div", {"id": "media"})
        return image.img['src'] if image else "Sem imagem"

    def extrair_noticias(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for news in soup.find_all("div", class_="conteudo"):
            titulo = news.find('a').text
            descricao = news.find('span', class_='descricao').text.strip().split('\n')[2]
            data = news.find('span', class_='data').text.strip()
            link = news.find('a')['href']
            imagem = self.obter_imagem(link)

            noticia = Noticia(titulo, descricao, data, link, imagem)
            self.noticias.append(noticia)

    def inserir_dado(self, dado):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["news-crawler"]
            collection = db["news"]
            resultado = collection.insert_one(dado.__dict__)
            client.close()
            return f"Dado inserido com sucesso. ID: {resultado.inserted_id}"
        except Exception as e:
            return f"Erro ao inserir dado: {str(e)}"

    def buscar_dado(self, criterio):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["news-crawler"]
            collection = db["news"]
            resultado = collection.find_one(criterio)
            client.close()
            if resultado:
                return f"Dado encontrado: {resultado}"
            else:
                return "Dado não encontrado."
        except Exception as e:
            return f"Erro ao buscar dado: {str(e)}"

    def raspar_e_inserir(self):
        for url in self.urls:
            self.extrair_noticias(url)
            for noticia in self.noticias:
                mensagem_insercao = self.inserir_dado(noticia)
                print(mensagem_insercao)

if __name__ == "__main__":
    urls = [
        "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias"
    ]

    scraper = WebScraper(urls)
    scraper.raspar_e_inserir()

    criterio_busca = {"titulo": "Presidente Lula conversa com o presidente do Egito"}  # Substitua pelo título desejado
    mensagem_busca = scraper.buscar_dado(criterio_busca)
    print(mensagem_busca)
