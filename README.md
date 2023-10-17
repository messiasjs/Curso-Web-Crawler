# Web Scraper de Notícias com Python
Este é um web scraper de notícias escrito em Python usando a biblioteca BeautifulSoup para extrair informações de um site da web e a biblioteca PyMongo para interagir com um banco de dados MongoDB. O código foi projetado para ser orientado a objetos para facilitar a manutenção e a compreensão.

# Pré-requisitos
Certifique-se de ter instalado as seguintes bibliotecas Python antes de executar o código:

- requests
- BeautifulSoup4
- pymongo
  
Você também precisa ter um servidor MongoDB em execução e fornecer a URL correta do servidor MongoDB no código. Certifique-se de ter o MongoDB instalado e configurado no seu sistema.

# Utilização
Clone o repositório:
```
git clone https://github.com/messiasjs/Curso-Web-Crawler.git
cd Curso-Web-Crawler
```

No arquivo crawler.py, você pode definir as URLs dos sites que deseja raspar. Edite a lista urls no início do arquivo:
````
urls = [
    "https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias",
    # Adicione mais URLs aqui, se necessário
]
````
No arquivo crawler.py, você pode definir a classe Noticia para armazenar as informações que deseja extrair das notícias. Personalize a classe Noticia de acordo com os dados que deseja coletar.

Personalize o método obter_imagem na classe WebScraper para extrair a imagem da notícia, dependendo da estrutura da página da web que está raspando.

Para executar o código, use o seguinte comando:

````
python crawler.py
````
O código irá raspar as notícias das URLs especificadas, extrair as informações e inseri-las no banco de dados MongoDB.

Para buscar dados no banco de dados MongoDB, você pode usar o método buscar_dado na classe WebScraper. Personalize o critério de busca de acordo com suas necessidades. Por exemplo:
````
criterio_busca = {"titulo": "Título da notícia que deseja buscar"}  # Substitua pelo título desejado
mensagem_busca = scraper.buscar_dado(criterio_busca)
print(mensagem_busca)
````
Lembre-se de que a busca no banco de dados só funcionará após a raspagem e a inserção de dados no MongoDB. Certifique-se de que o servidor MongoDB esteja em execução e configurado corretamente.
