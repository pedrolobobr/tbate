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
          .entry-title {
          text-align: center;
          }
          .chapter-button {
          display: flex;
          justify-content: center;
          align-items: center;
          width: 100%;
          max-width: 100px;
          height: 50px;
          text-align: center;
          border-radius: 5px;
          color: white;
          font-weight: bold;
          margin: 10px auto; /* centraliza o botão na tela e adiciona uma margem */
          background: transparent;
          border: 1px solid #91C9FF;
          outline: none;
          text-decoration: none;
          top: 50%;
          }
          .chapter-button:hover {
            transition: 1s ease-in-out;
            background: black;
          }
          """

  script1 = """
            <script>
                window.onload = function() {
                var currentChapter = window.location.pathname.split('/').pop(); // Obtém o nome do arquivo atual
                var chapterNumber = parseInt(currentChapter.replace('', '').replace('.html', '')); // Extrai o número do capítulo do nome do arquivo

                // Se não for o primeiro capítulo, adiciona o botão do capítulo anterior
                if (chapterNumber > 400) {
                    var previousChapterNumber = chapterNumber - 1; // Calcula o número do capítulo anterior
                    var previousChapterFileName = previousChapterNumber + '.html'; // Cria o nome do arquivo do capítulo anterior

                    // Cria o botão de navegação para o capítulo anterior
                    var previousChapterButton = document.createElement('a');
                    previousChapterButton.href = previousChapterFileName;
                    previousChapterButton.innerText = 'Capítulo Anterior';
                    previousChapterButton.className = 'chapter-button'; // Adiciona a classe CSS ao botão

                    // Adiciona o botão de navegação ao início do corpo do documento
                    document.body.insertBefore(previousChapterButton, document.body.firstChild);
                }

                // Se não for o último capítulo, adiciona o botão do próximo capítulo
                if (chapterNumber < 480) {
                    var nextChapterNumber = chapterNumber + 1; // Calcula o número do próximo capítulo
                    var nextChapterFileName = nextChapterNumber + '.html'; // Cria o nome do arquivo do próximo capítulo

                    // Cria o botão de navegação para o próximo capítulo
                    var nextChapterButton = document.createElement('a');
                    nextChapterButton.href = nextChapterFileName;
                    nextChapterButton.innerText = 'Próximo Capítulo';
                    nextChapterButton.className = 'chapter-button'; // Adiciona a classe CSS ao botão

                    // Adiciona o botão de navegação ao final do corpo do documento
                    document.body.appendChild(nextChapterButton);
                }
            };
                
            </script>
          
            """
    # Escrever o conteúdo HTML no arquivo
  with open(f'{i}.html', 'w', encoding="utf-8") as arquivo:
      arquivo.write(f'<style>{style1}</style><body style="background-color: #222222; color: white; margin: 25px;">{titulo}<h2 style="text-align: center;">{chaptername}</h2><p style="text-align: center;">Lançamento {data}</p>{noticia}{script1}</body>')
  print(f"Arquivo {i} criado com sucesso!")



