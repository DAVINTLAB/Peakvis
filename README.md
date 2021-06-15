# Peakvis [![](https://img.shields.io/badge/JavaScript-yellow.svg)](https://www.javascript.com/) [![](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)

PeakVis is a visualization tool that allows uploading a recorded video of a live broadcast together with a file of _tweets_, comments of 280 characters made on the social network _Twitter_, related to the recorded program. It is an interactive tool that syncs the video recording with a responsive line graph representing the total number of _tweets_ from each moment, the top messages, a dynamic word cloud, and a semantic graph showing word correlation.

- [Requirements](#requirements)
- [Installation](#installation)
- [Execution](#execution)
- [Inserting data into your application](#inserting-data-into-your-application)
- [Inserting video into your application](#inserting-data-into-your-application)
- [Processing the files](#processing-the-files)
- [Visualization elements](#visualization-elements)
- [Highlight](#highlight)
- [Tweet volume line chart](#tweet-volume-line-chart)
- [Video player](#video-player)
- [Most retweeted tweets](#most-retweeted-tweets)
- [Frequently said words](#frequently-said-words)
- [Semantic network](#semantic-network)
- [Dependencies](#dependencies)
- [Citation](#citation)
- [About the Authors](#about-the-authors)

## Requirements

To operate the Peakvis, it is necessary to have the minimum requirements listed below:

- OS:
- Windows 7 or superior
- MacOS
- GNU (Linux OS)
- Python 3.0 64-bit version
- pip (in Python 3.4 or superior, pip is already built-in)
## Installation

To install the Peakvis project, you can either download the compressed folder or clone the repository.

After downloading the project, go to the folder path via command prompt and install the dependencies using:

```
pip install -r requirements.txt --user
```

## Execution

After installing all dependencies that you need, it is important to know that you need to have two files to run the main application:

- A .json file, containing recorded _tweets_
- A video file showing the event you want to analyze

### Inserting data into your application

To insert your .json file into the project, go to the **\Peakvis-master\static\DATA\dados** path and insert your file in the folder.

- For demonstration, a JSON file named demo is already present in the folder.
- Just drag your .json file to this path.

![alt text](https://media.discordapp.net/attachments/830590281966682193/842853958002540554/demojson.png)

### Inserting video into your application

To insert your video file into the project, go to the **\Peakvis-master\static\DATA\videos** path and insert your file in this folder.

- For demonstration, a video named demo is already present in the folder.
- Just drag your video file to this path.

![alt text](https://media.discordapp.net/attachments/830590281966682193/852607212865191957/unknown.png)

### Processing the files

After inserting the two files that you need to run the program, go to folder path via command prompt and run the following command:

```
python server.py
```
- There is a chance you need to use the python3 command instead of python
- After that, the application will then be available at the following address: http://127.0.0.1:5000/
- Write the name of your data and video file in the indicated textboxes
- By default, the demo files are already configured, but you can change them just by rewriting
- **Both of the file names must contain the file type in the end (.json and .mp4, for example)**
- Click the Submit button and wait. The application must generate all the visualization elements

![alt text](https://media.discordapp.net/attachments/830590281966682193/842879502915731486/submit.png)

## Visualization elements

Along this section, the application functionalities and features will be approached for better comprehension. It is important to know that all the items are synced with the button.

### Highlight

- On the top left of the application, there is a slider button named Highlight. It controls the sensitivity of the traffic peaks of _tweets_ to show to the users, which can be interpreted as the most appealing or most commented moments.
- The further to the left, the less rigorous the definition of Highlight becomes.
- The farther to the right, the stricter the definition of Highlight is.
- By clicking on the Highlight button, all the needed changes are processed.

![alt text](https://media.discordapp.net/attachments/830590281966682193/842497651639189519/highlight_button.png)
![alt text](https://media.discordapp.net/attachments/830590281966682193/842501041064640542/highlight-button2.png)

### Tweet volume line chart

- The _line chart of tweets_ shows the peaks of _tweets_ contained in the .json file as the first analysis graph. It is synced with the video and goes along with the video time.
- Already watched segments are colored blue, as opposed to the default unwatched grey lines.
- The starting of the tweet peaks are indicated with a purple dot.

![alt text](https://media.discordapp.net/attachments/511284977409851402/725465708909035590/unknown.png?width=1442&height=299)

### Video player

- As the video player is synced with the other charts, you can pause and unpause any video at any time, pausing the other application elements too.
- You can set the volume, put it on full screen, download the video and set it as a picture-in-picture player.

![alt text](https://media.discordapp.net/attachments/830590281966682193/852608997794381894/unknown.png)

### Most retweeted tweets

- As another element of the application, the _tweet box_ shows the textual contents of the most retweeted _tweets_ every second in a scrolling box.
- Besides the _tweet content_, it shows its date and time posted in brackets.
- It is also possible to access the _tweet address_ by clicking on the highlighted "LINK" under its content.

![alt text](https://media.discordapp.net/attachments/830590281966682193/842865515357798460/tweets.png)

### Frequently said words

- There is also a dynamic word cloud showing the most frequent words in the _tweets_ until the watched segment.
- The application ignores several words known as stopwords, such as articles and prepositions (for example: "the", "so", and "on").
- You can see and even set these words on the "STOPWORDS" file.

![alt text](https://cdn.discordapp.com/attachments/830590281966682193/842865784437866516/cloudword.png)

### Semantic network

- The semantic network connects the most related words between themselves.
- For example, the more related words to the word "final" are connected by grey lines, then linking words as "kaysar", "edição" and "#bbb18"
- The graph is generated in real-time, providing a smooth animation along the video time.

![alt text](https://media.discordapp.net/attachments/830590281966682193/842865964353191996/graphsem.png)

## Dependencies

#### JavaScript

| Library | Version/source |
| ------------------------------------------------------------------------------------------ | -------------- |
| [D3](https://d3js.org/d3.v5.min.js) | 3.0.2 |
| [Plotly](https://cdn.plot.ly/plotly-latest.min.js) | 1.58.4 |
| [jQuery](http://code.jquery.com/jquery-1.8.3.min.js) | 3.0.2 |
| [MathJs](https://cdnjs.cloudflare.com/ajax/libs/mathjs/6.2.1/math.js) | 6.2.1 |
| [wordcloud2](https://cdnjs.cloudflare.com/ajax/libs/wordcloud2.js/1.1.1/wordcloud2.min.js) | 1.2.2 |

#### Python

| Library | Version/source |
| ------------------------------------------------------------- | ------------------------- |
| [flask](https://matplotlib.org/2.1.2/index.html) | 3.0.2 |
| [numpy](https://numpy.org/) | 1.20.3 |
| [pandas](https://pandas.pydata.org/) | 1.2.4 |
| [json](https://www.json.org/json-en.html) | - |
| [datetime](https://docs.python.org/3/library/datetime.html) | Lib/datetime.py |
| [pathlib](https://docs.python.org/3/library/pathlib.html) | Lib/pathlib.py |
| [csv](https://docs.python.org/3/library/csv.html) | Lib/csv.py |
| [itertools](https://docs.python.org/3/library/itertools.html) | /lib-dynload/itertools.so |
| [networkx](https://networkx.org/) | 2.5 |
| [regex](https://pypi.org/project/regex/) | 2021.4.4 |

## Citation

Please refer to this work by citing the dissertation indicate below.

Pedro Henrique M. Sanvido, Gabriela B. Kurtz, Carlos R. G. Teixeira, Pedro P. Wagner,Lorenzo P. Leuck, Milene S. Silveira, Roberto Tietzmann, Isabel H. Manssour. PeakVis: a Visual Analysis Tool for Social Network Data and Video Broadcasts. IEEE International Conference on Computers, Software and Applicatins (COMPSAC), 2021.

## About the authors

We are members of the Data Visualization and Interaction Lab (DaVInt) at PUCRS:

- Pedro P. Wagner -- Undergraduate student in Computer Science.
- Arthur Henrique Henz -- Undergraduate student in Computer Science.
- Pedro Henrique M. Sanvido -- Master Student in Computer Science.
- Lorenzo P. Leuck -- Master Student in Communication.
- Carlos R. G. Teixeira -- PhD student in Communication.
- Gabriela B. Kurtz -- Professor and researcher of DaVInt.
- Milene S. Silveira -- Professor and researcher of DaVInt.
- Roberto Tietzmann -- Professor and researcher of DaVInt.
- Isabel H. Manssour -- Researcher and Professor Coordinator of DaVInt.

More information can be found [here](https://www.inf.pucrs.br/davint/).
