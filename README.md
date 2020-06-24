# Peakvis

## Introdução
PeakVis é uma ferramente de vizualização, ***ainda em desenvolvimento***. Nela é possivel carregar o video gravado de uma transmissão ao vivo junto com os _tweets_, comentarios de 288 caracteres feitos na rede social _Twitter_, relacionados ao programa gravado. Feito isso o PeakVis gera diversos graficos rsponsivos ao programa de televisão recebido, entre esses gráficos estão o fluxo de dados e os autores dos _tweets_ mais citados durante o tempo da transmissão. Junto com os gráficos há a transmissão em si adjacente à um quadro com os _tweets_ do momento atual do vídeo.
![alt text](https://media.discordapp.net/attachments/511284977409851402/725449788212117504/imagem1.png?width=1270&height=720)

## Requisitos
 - Windows 7 ou superior
 - NodeJs (https://nodejs.org/pt-br/download/)
 
## Instalação
 - Após ter baixado os arquivos do diretório e baixado as depencias, Vá na pasta "bin" e rode o arquivo "VisualizadorDAVINT.exe". 
![alt text](https://media.discordapp.net/attachments/511284977409851402/725458375676264568/unknown.png)
 - Isso ira abrir a interface inicial do PeakVis.
![alt text](https://media.discordapp.net/attachments/511284977409851402/725458008666013796/unknown.png)
 - A primeira vez que for aberto ***é obrigatório clicar em ajuda*** antes de mais nada.
 ![alt text](https://media.discordapp.net/attachments/511284977409851402/725459031388586014/unknown.png)
 - Logo após, clique em "Instalar Dependências" e **aguarde** a Mensagem informando que terminou de instalar.
 ![alt text](https://media.discordapp.net/attachments/511284977409851402/725459501049970819/unknown.png)
 - Agora já pode clicar no botão "Fechar" na janela "Ajuda".
 ![alt text](https://media.discordapp.net/attachments/511284977409851402/725459031388586014/unknown.png)
 
 ## Execução
 - Apos instalar basta clicar em "Inicia" na janela "DAVINT Demo 1.0", caso tenha fechado o aplicativo, basta abrir novamente.
 ![alt text](https://media.discordapp.net/attachments/511284977409851402/725460151875797144/unknown.png)
 - O PeakVis vai abrir em uma nova aba de seu navegador.
 ![alt text](https://media.discordapp.net/attachments/511284977409851402/725460333942145044/unknown.png?width=1442&height=293)
 - Para ver os graficos e o video agora é apenas clicas em "Subimit".
 
 ## Funcionalidades
 - A Primeira funcioanlidade é a rigorosidade dos _Highlights_
   - ela é dada pelo slider no canto superior esquerdo do PeakVis.
   - Quanto mais para esquerda menos rigorosa fica a definição de _Highlight_.
   - Quanto mais para a direita mais rigorosa é a definição de _Highlight_.
![alt text](https://media.discordapp.net/attachments/511284977409851402/725464004113465434/unknown.png)
- A segunda funcionalidade é avançar para o proximo _highlight_ clicando no botão "highlight"
  - os _highlights_ são marcados por uma bolinha roxa no fluxo de _tweets_
  - a quantidade de _highlights_ é influenciada pelo slider de rigorosidade
   ![alt text](https://media.discordapp.net/attachments/511284977409851402/725463700164575313/unknown.png)
- A terceira funcionalidade é o gráfico de fluxo de _tweets_
  - Ele mostra a quantidade de _tweets_ feitos sobre o prgorama ao longo do tempo
  - A parte colorida em azul representa o que já passou 
  - A parte colorida em cinza mostra o que falta do video
 ![alt text](https://media.discordapp.net/attachments/511284977409851402/725465708909035590/unknown.png?width=1442&height=299)
 - A quarta funcionalidade é a caixa de _Tweet_
   - ela mostra os _tweets_ mais _retweetado_ no segundo do video
   - a cada segundo ela msotra um _tweet_ novo do que esta sendo falado no momento
![alt text](https://media.discordapp.net/attachments/511284977409851402/725467582336860189/unknown.png)
