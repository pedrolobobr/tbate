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

  div1 = """
   <div class="chapter-buttons">
                <a id="previous-chapter-button" class="chapter-button">Capítulo Anterior</a>
                <a href="../index.html" class="chapter-button">Home</a>
                <a id="next-chapter-button" class="chapter-button">Próximo Capítulo</a>
             </div> 
        """
  style1 = """
            .entry-title {
              text-align: center;
               }
            .chapter-buttons {
                display: flex;
                justify-content: center;
                gap: 10px;
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

        </style>
          """

  script1 = """
            <script>
                window.onload = function() {
                    var currentChapter = window.location.pathname.split('/').pop(); // Obtém o nome do arquivo atual
                    var chapterNumber = parseInt(currentChapter.replace('', '').replace('.html', '')); // Extrai o número do capítulo do nome do arquivo

                    // Se não for o primeiro capítulo, atualiza o link do botão do capítulo anterior
                    if (chapterNumber > 400) {
                        var previousChapterNumber = chapterNumber - 1; // Calcula o número do capítulo anterior
                        var previousChapterFileName = '' + previousChapterNumber + '.html'; // Cria o nome do arquivo do capítulo anterior
                        document.getElementById('previous-chapter-button').href = previousChapterFileName;
                    } else {
                        // Se for o primeiro capítulo, esconde o botão do capítulo anterior
                        document.getElementById('previous-chapter-button').style.display = 'none';
                    }

                    // Se não for o último capítulo, atualiza o link do botão do próximo capítulo
                    if (chapterNumber < 480) {
                        var nextChapterNumber = chapterNumber + 1; // Calcula o número do próximo capítulo
                        var nextChapterFileName = '' + nextChapterNumber + '.html'; // Cria o nome do arquivo do próximo capítulo
                        document.getElementById('next-chapter-button').href = nextChapterFileName;
                    } else {
                        // Se for o último capítulo, esconde o botão do próximo capítulo
                        document.getElementById('next-chapter-button').style.display = 'none';
                    }
                };
                </script>
          
            """    
          
                     

    # Escrever o conteúdo HTML no arquivo
  with open(f'{i}.html', 'w', encoding="utf-8") as arquivo:
      arquivo.write(f'<style>{style1}</style><body style="background-color: #222222; color: white; margin: 25px;">{titulo}<h2 style="text-align: center;">{chaptername}</h2><p style="text-align: center;">Lançamento {data}</p>{noticia}{div1}{script1}</body>')
  print(f"Arquivo {i} criado com sucesso!")



