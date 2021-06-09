# Peakvis - WIP [![](https://img.shields.io/badge/JavaScript-yellow.svg)](https://www.javascript.com/) [![](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/)

PeakVis is a visualization tool that allows uploading a recorded video of a live broadcast together with a file of _tweets_, comments of 280 characters made on the social network _Twitter_, related to the recorded program. It is an interactive tool that syncs the video recording with a responsive line graph representing the total number of  _tweets_ from each moment, the top messages, a dynamic word cloud, and a semantic graph showing word correlation.

- [Requirements](#requirements)
- [Installation](#installation)
- [Execution](#execution)
  - [Inserting data into your application](#inserting-data-into-your-application)
  - [Inserting video into your application](#inserting-data-into-your-application)
  - [Processing the files](#processing-the-files)
- [Visualization elements](#visualization-elements)
  - [Highlight](#highlight)
  - [Tweets flow chart](#tweets-flow-chart)
  - [Video player](#video-player)
  - [Tweet box](#tweet-box)
  - [Word cloud](#word-cloud)
  - [Semantic Graph](#semantic-graph)
- [Dependencies](#dependencies)
- [Citation](#citation)
- [About the Authors](#about-the-authors)

## Requirements

To operate the Peakvis it is necessary to have the minimum requirements listed below:

- OS:
  -- Windows 7 or superior
  -- MacOS
  -- GNU (Linux OS)
- Python 3.7 or superior (https://www.python.org/downloads/)
- Node.js (https://nodejs.org/en/download/)
- Flask 2.0.0 (https://pypi.org/project/Flask/2.0.0/)

## Installation

To install the Peakvis project, you must first download the compressed folder, available on this same project page.

- Just click on the Download ZIP button.

![alt text](https://media.discordapp.net/attachments/830590281966682193/842819333834670110/howtodown.png)

After downloading the ZIP file, go to the file path, right click and select the better extraction option for you. The more common zipping programs for Windows are WinRAR and 7-Zip. MacOS and most Linux distros already have zipping tools.  
 ![alt text](https://media.discordapp.net/attachments/830590281966682193/843922715425112074/2.jpg) ![alt text](https://media.discordapp.net/attachments/830590281966682193/843922717374939139/1.jpg) ![alt text](https://media.discordapp.net/attachments/830590281966682193/843925251796107325/cats.jpg)

After unzipping the folder, go to the _\Peakvis-master\build\VisualizadorDAVINT_ path and open the file named **_VisualizadorDAVINT_**.
![alt text](https://cdn.discordapp.com/attachments/830590281966682193/842858029158498304/caminho_para_peakvis.png)
This will open the Peakvis home interface.

- The first time you open it **_is obrigatory to click on ajuda_** before anything else.
- Note: ajuda translates to help.
  ![alt text](https://media.discordapp.net/attachments/830590281966682193/842826420324663326/data_visualizer.png)
- Right after, click on "Instalar Dependências" and **wait** A command prompt will open and the Message must appear, informing that you have finished installing.
  ![alt text](https://media.discordapp.net/attachments/511284977409851402/725459031388586014/unknown.png)
  ![alt text](https://media.discordapp.net/attachments/511284977409851402/725459501049970819/unknown.png)
- Now you can click on the "Fechar" button and proceed.

## Execution

After installing all dependences you need, it is important to know that you need to have two files to use the main application:

- A .json file, containing all the _tweets_
- A .mp4 file shownig the event you want to analyze

Therefore, it will be explained how to insert and select them in the application.

### Inserting data into your application

To insert your .json file into the project, go to the **\Peakvis-master\bin\DATA\dados** path and insert your file in the folder.

- For demonstration, a JSON file named demo is already present in the folder.
- Just drag your .json file to this path.
  ![alt text](https://media.discordapp.net/attachments/830590281966682193/842853958002540554/demojson.png)

### Inserting video into your application

To insert your .mp4 file into the project, go to the **\Peakvis-master\bin\DATA\videos** path and insert your file in the folder.

- For demonstration, a video named demo is already present in the folder.
- Just drag your .mp4 file to this path.
  ![alt text](https://media.discordapp.net/attachments/830590281966682193/842851945352790056/demovideo2.png)

### Processing the files

After inserting the two files that you need to run the program, go back to the Peakvis home interface and click in Inicia. If you have closed the application, just open it again.

- A web application will open on your default browser.
- Write the name of your data and video file in the indicated textboxes
- By default the demo files are already written, but you can change just changing the names.
- **Both of the file names must contain the file type in the end (.json and .mp4)**
- Click into the Submit button and the application must generate all the visualization tools.

![alt text](https://media.discordapp.net/attachments/830590281966682193/842879502915731486/submit.png)

## Visualization elements

Along this section, the application functionalities and features will be approached for better comprehension. It is important to know that all the items are synced with the button.

### Highlight
- On the top left of the application, there is a slider button named Highlight. It controls the sensitivity of the traffic peaks of _tweets_ to show to the users, which can be interpreted as the most appealing or most commented moments.
- The further to the left the less rigorous the definition of Highlight become.
- The farther to the right the stricter the definition of Highlight is.
- By clicking on the Highlight button, all the needed changes are processed.
![alt text](https://media.discordapp.net/attachments/830590281966682193/842497651639189519/highlight_button.png)![alt text](https://media.discordapp.net/attachments/830590281966682193/842501041064640542/highlight-button2.png)

### Tweets line chart
- The _line chart of tweets_ shows the peaks of _tweets_ contained in the .json file as the first analysis graph. It is synced with the video and goes along with the .mp4 file time.
- Already watched segments are colored blue, as opposed to the default unwatched grey lines.
- The starting of the tweet peaks are indicated with a purple dot.
  ![alt text](https://media.discordapp.net/attachments/511284977409851402/725465708909035590/unknown.png?width=1442&height=299)

### Video player
- As the video player is synced with the other charts, you can pause and unpause any video at any time, pausing the other application elements too.
- You can set the volume, put it on full screen, download the video and set it as a picture-in-picture player.
  ![alt text](https://media.discordapp.net/attachments/830590281966682193/842865116814114816/videop.png)

### Tweet box
- As another element of the application, the _tweet box_ shows
the textual contents of the most retweeted _tweets_ at every second in a scrolling box.
- Besides the _tweet content_, it shows its date and time posted in brackets.
- It is also possible to access the _tweet addres_ by clicking on the highlighted "LINK" under its content.
![alt text](https://media.discordapp.net/attachments/830590281966682193/842865515357798460/tweets.png)

### Word cloud
- There is also a dynamic word cloud showing the most frequent words in the _tweets_ until the watched segment.
- The application ignores several words known as stopwords, such as articles and prepositions (for example: "the", "so", and "on").
- You can see and even set these words on the "STOPWORDS" file.
  ![alt text](https://cdn.discordapp.com/attachments/830590281966682193/842865784437866516/cloudword.png)

### Semantic graph
-The semantic graph connects the most related words between themselves.
- For example, the more related words to the word "final" are connected by grey lines, then linking words as "kaysar", "edição" and "#bbb18".
- The graph is generated in real-time, providing a smooth animation along the video time.
  ![alt text](https://media.discordapp.net/attachments/830590281966682193/842865964353191996/graphsem.png)


## Dependencies

| Library                                          | Version |
| ------------------------------------------------ | ------- |
| [pandas](https://pandas.pydata.org/)             | 1.2.4   |
| [numpy](https://numpy.org/)                      | 1.20.3  |
| [Flask](https://matplotlib.org/2.1.2/index.html) | 3.0.2   |

Internet access is necessary to load the JavaScript libraries. The following JavaScript libraries are used:

| Library                                      | Version |
| -------------------------------------------- | ------- |
| [d3](https://d3js.org/)                      | 5.9.7   |
| [d3 array](https://github.com/d3/d3-array)   | 1.2.4   |
| [d3 path](https://github.com/d3/d3-path)     | 1.0.7   |
| [d3 shape](https://github.com/d3/d3-shape)   | 1.3.5   |
| [d3 sankey](https://github.com/d3/d3-sankey) | 0.12.1  |
| [jquery](https://jquery.com/)                | 3.4.1   |
| [bootstrap](https://getbootstrap.com/)       | 3.3.6   |

## Citation

Please refer to this work by citing the dissertation indicate below.

Pedro Henrique M. Sanvido, Gabriela B. Kurtz, Carlos R. G. Teixeira, Pedro P. Wagner,Lorenzo P. Leuck, Milene S. Silveira, Roberto Tietzmann, Isabel H. Manssour. PeakVis: a Visual Analysis Tool for Social NetworkData and Video Broadcasts. IEEE International Conference on Computers, Software and Applicatins (COMPSAC), 2021.


## About the authors

We are members of the Data Visualization and Interaction Lab (DaVInt) at PUCRS:

- Pedro P. Wagner -- Undergraduate student in Computer Science.
- Arthur Henrique Henz -- Undergraduate student in Computer Science.
- Pedro Henrique M. Sanvido -- Master Student in Computer Science.
- Lorenzo P. Leuck -- Master Student in Communication.
- Carlos R. G. Teixeira -- PhD student in Communication.
- Gabriela B. Kurtz -- Professor and researcher of DaVInt -- 2017-current.
- Milene S. Silveira -- Professor and researcher of DaVInt -- 2017-current.
- Roberto Tietzmann -- Professor and researcher of DaVInt -- 2017-current.
- Isabel H. Manssour -- Researcher and Professor Coordinator of DaVInt -- 2017-current.

More information can be found [here](https://www.inf.pucrs.br/davint/).

> Written with [StackEdit](https://stackedit.io/).
