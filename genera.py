import json
twt = False
i = 0
adver = ["Que","que","a","un","en","este","si","la","al","le","ya","mis","los","sí","de","=)",",","el","y","con",
			"Ya","ando","el","para","mas","bien"]

with open("tweet.json","r") as read_file:
	data = json.load(read_file)
	twt = data['Tweets']

def compati(matriz):
	print()
	print("***Enviando datos a base.json (compati con programa de clasificacion)***")
	print("")
	i = 0
	data = {}
	data["Probabilidades"] = []
	while i < len(matriz):
		data["Probabilidades"].append([matriz[i][0],matriz[i][4]])
		i = i + 1
	with open('base.json', 'w') as file:
		json.dump(data, file, indent=1)
	with open("base.json","r") as read_file:
		data = json.load(read_file)
		tw = data["Probabilidades"]
	return(tw)

#Matriz de Probabilidades
def matriz(twt,p,ntwt):
	i = 0
	s = 0
	n = 0
	matr = []
	print("La matriz de probabilidad es:")
	while i < len(p):
		j = 0
		while j < len(twt):
			if twt[j] == p[i]:
				s = s + 1
			n = ntwt - s
			j = j + 1
		t = s + n
		matr.append([p[i], n, s, t, s/t, n/t])
		s = 0
		n = 0
		i = i + 1
	print(matr)
	return compati(matr)

def advervios(tweet,adver):
	j = 0
	k = []
	C = []
	while j < len(tweet):
		i = 0
		while i < len(tweet[j]):
			if not tweet[j][i] in adver:
				s = tweet[j][i]
				k = k + [s]
			i = i + 1
		j = j + 1
	j = 0
	while j < len(k):
		if not k[j] in C:
			C = C + [k[j]]
		j = j + 1 
	return matriz(k,C, len(tweet))


def separar_true(twt,adver,t = []):
	i = 0
	while i < len(twt):
		tw = twt[i]
		Stream = tw['Stream']
		texto = tw['texto']
		if Stream == True:
			texto = texto.split()
			t = t + [texto]
		i = i +1
	return advervios(t,adver)

print(separar_true(twt,adver))