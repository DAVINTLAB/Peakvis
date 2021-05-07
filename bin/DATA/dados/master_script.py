import json
import datetime as dt
import re
import sys
from pathlib import Path
import numpy
import pandas as pd
from csv import DictReader


#PASSAR O DATASET PELO SANITIZE ANTES!!!!!!

file_name = sys.argv[1]
f_no_ext = Path(file_name).stem


if Path(f_no_ext + "_WC.txt").is_file() and Path(f_no_ext + "_RT.txt").is_file():
	print('done')
else:
	arq = open(file=file_name, mode='r', encoding="utf-8")
	wc = open(file=f_no_ext + "_WC.txt", mode='w', encoding="utf-8")
	toprt = open(file=f_no_ext + "_RT.txt", mode='w', encoding="utf-8")

	data = json.load(arq)
	arq.close()
	count = 0
	resp = []
	auxMap = dict()
	rts = dict()

	if 'retweets' in data[0]:
		rt_key = 'retweets'
	else:
		rt_key = 'retweet_count'


	#sanitize
	stopwords_list = []
	with open('stopwords/stopwords.txt', 'r', encoding='utf8') as f:
		stopwords_list.append(f.read().splitlines())
	stop_words = stopwords_list[0]

	for tweet in data:
		new_str = ""
		for w in tweet['text'].split(' '):
			if w.lower() not in stop_words:
				new_str.append(w)
			tweet['text'] = new_str

	#oi = dt.datetime.strptime(data[0]["created_at"], "%Y-%m-%d %H:%M:%S")
	#oi2 = dt.datetime.strptime(data[20176]["created_at"], "%Y-%m-%d %H:%M:%S")
	#print((oi - oi2).seconds)
	started_time = dt.datetime.strptime(data[len(data)-1]["created_at"], "%Y-%m-%d %H:%M:%S") + dt.timedelta(seconds=1)
	for i in range(len(data)-1,-1,-1):
		if dt.datetime.strptime(data[i]["created_at"], "%Y-%m-%d %H:%M:%S") >= started_time:
			started_time = dt.datetime.strptime(data[i]["created_at"], "%Y-%m-%d %H:%M:%S") + dt.timedelta(seconds=1)
			count = count + 1

			if count % 15 == 0:
				#word cloud
				resp = sorted(auxMap.items(), key=lambda x: x[1], reverse=True)
				if len(resp) < 30:
					tam = len(resp)
				else:
					tam = 30

				stringg = ""
				for j in range(tam):
					stringg = stringg + resp[j][0] + "," + str(resp[j][1]) + ","
				stringg = stringg[0:-1] + "\n"
				wc.write(stringg)
				#wc.write(str(resp[0:10])[1:-1].replace("(", " ").replace("),", ",").replace(")", " ") +"\n")

				#top retweets
				resp = sorted(rts.items(), key=lambda x: x[1], reverse=True)
				if len(resp) < 30:
					tam = len(resp)
				else:
					tam = 30

				stringg = ""
				for j in range(tam):
					stringg = stringg + resp[j][0] + "," + str(resp[j][1]) + ","
				stringg = stringg[0:-1] + "\n"
				toprt.write(stringg)
				#toprt.write(str(resp[0:10])[1:-1].replace("(", " ").replace("),", ",").replace(")", " ") +"\n")

		else:
			#word cloud
			aux = re.split(" |\n",data[i]["text"])
			for j in range(len(aux)):
				if aux[j] not in auxMap.keys():
					auxMap[aux[j]] = 1
				else:
					auxMap[aux[j]] = auxMap.get(aux[j]) + 1

			#top retweets
			if data[i]["username"] not in rts.keys():
				rts[data[i]["username"]] = data[i][rt_key]
			else:
				rts[data[i]["username"]] = rts.get(data[i]["username"]) + data[i][rt_key]

	wc.close()
	toprt.close()





if Path(f_no_ext + "grafos.csv").is_file() and Path(f_no_ext + "_RT.txt").is_file():
	print('done2')
else:
	f = open("stopwords/stopwords.txt", 'r')
	stopwords = [name.rstrip().lower() for name in f]


	arq = open(file=file_name, mode='r', encoding="utf-8")
	data = json.load(arq)
	vTweets = []

	for item in data:
		vTweets.append(item['text'])

	vFrases = []

	for idx,tweet in enumerate(vTweets):
	    tweet = re.sub(r"https?:\/\/(\S+)", "", tweet)
	    # tira toda a pontuação exceto arroba e jogo da velha
	    #tweet = re.sub(r"[^\P{P}@#]+", "", tweet)
	    # tira toda a pontuação
	    # frase = frase.translate(str.maketrans('','',string.punctuation))
	    tweet = " ".join([x for x in tweet.split(' ') if x.lower() not in stopwords])
	    tweet = tweet.rstrip()
	    tweet = tweet.strip()
	    tweet = tweet.lower()
	    vFrases.append(tweet)

	col1=[]
	col2=[]

	for frase in vFrases:
	    vPalavras = frase.split(' ')
	    nPalavras = len(vPalavras)

	    if nPalavras > 2:
	        nLinhas = 0
	        vNumeros = []
	        for i in range(nPalavras):
	            b = nPalavras-(i+1)
	            if b>0:
	                vNumeros.append(b)
	            nLinhas = nLinhas + b

	        nNumeros= len(vNumeros)
	        invNumeros = vNumeros[::-1]

	        c1 = []
	        for i in range(nNumeros):
	            for j in range(vNumeros[i]):
	                c1.append(vPalavras[i])
	        col1.extend(c1)


	        ordemC2 = []
	        for i in range(nNumeros):
	            for j in invNumeros:
	                ordemC2.append(j)
	            invNumeros.pop(0)

	        Mposicao = []
	        posicaoC2 = []
	        for i in range(int(nLinhas/nPalavras)):
	            for j in range(nPalavras):
	                posicaoC2.append(vPalavras[j])
	                Mposicao.append(j)

	        c2 =[]
	        c2[:] = [posicaoC2[i] for i in ordemC2]
	        col2.extend(c2)

	matriz = numpy.c_[col1,col2]
	df = pd.DataFrame(columns=["source","target"], data=matriz)
	df['source'].replace('', numpy.nan, inplace=True)
	df.dropna(subset=['source'], inplace=True)
	df['target'].replace('', numpy.nan, inplace=True)
	df.dropna(subset=['target'], inplace=True)
	df.to_csv(f_no_ext + '_grafos.csv', index=False)
