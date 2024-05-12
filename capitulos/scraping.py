import requests
from bs4 import BeautifulSoup

for i in range(400, 481):
  response = requests.get(f'https://centralnovel.com/the-beginning-after-the-end-capitulo-{i}/')

  content = response.content

  site = BeautifulSoup(content, 'html.parser')

  titulo = site.find('h1', attrs={'class': 'entry-title'})
  data = site.find('span', attrs={'class': 'updated'})
  chaptername = site.find('div', attrs={'class': 'cat-series'})


  # HTML da notícia
  noticia = site.find('div', attrs={'class': 'epcontent entry-content'})

  style1 = """
          .entry-title{
          text-align: center;

          };
          
          """


    # Escrever o conteúdo HTML no arquivo
  with open(f'{i}.html', 'w', encoding="utf-8") as arquivo:
      arquivo.write(f'<style>{style1}</style><body style="background-color: #222222; color: white;">{titulo}<h2 style="text-align: center;">{chaptername}</h2><p style="text-align: center;">Lançamento {data}</p>{noticia}</body>')
  print(f"Arquivo {i} criado com sucesso!")



