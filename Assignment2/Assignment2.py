from __future__ import division
import glob
import math



def TRAINMULTINOMIALNB():
	vocab1,vocab2,vocab = {},{},{}
	words1,words2 = [],[]
	
	Nc1 = len(glob.glob('train/ham/*.txt'))
	Nc2 = len(glob.glob('train/spam/*.txt'))
	N = Nc1 + Nc2
	for filename in glob.glob('train/ham/*.txt'):
		with open(filename) as f:
			words1 += f.read().split()	

	for word in words1:
		if len(word) >= 5:
			if vocab1.has_key(word):
				vocab1[word] += 1
			else:
				vocab1[word] = 1

	for filename in glob.glob('train/spam/*.txt'):
		with open(filename) as f:
			words2 += f.read().split()

	for word in words2:
		if len(word) >= 5:
			if vocab2.has_key(word):
				vocab2[word] += 1
			else:
				vocab2[word] = 1

	vocab = dict(vocab1.items() + vocab2.items())



	prior = [0,0]
	prior[0] = Nc1/N
	prior[1] = Nc2/N


	Tct1,Tct2,condprob1,condprob2 = {},{},{},{}

	for v in vocab:
		if vocab1.has_key(v):
			Tct1[v] = vocab1[v]
		else:
			Tct1[v] = 0

	ETct = 0
	for v in vocab1:
		ETct += vocab1[v]
	for v in vocab:
		condprob1[v] = (Tct1[v]+1)/(len(vocab) +ETct)



	for v in vocab:
		if vocab2.has_key(v):
			Tct2[v] = vocab2[v]
		else:
			Tct2[v] = 0

	ETct = 0
	for v in vocab2:
		ETct += vocab2[v]
	for v in vocab:
		condprob2[v] = (Tct2[v]+1)/(len(vocab) +ETct)

	condprob = [condprob1,condprob2]

	return vocab,prior,condprob



def APPLYMULTINOMIALNB(V, prior, condprob, d):
	W = []
	with open(d) as f:
		words = f.read().split()
		for word in words:
			if V.has_key(word):
				W.append(word)

	score0 = prior[0]
	for t in W:
		score0 += math.log(condprob[0][t])

	score1 = prior[1]
	for t in W:
		score1 += math.log(condprob[1][t])

	if score0 >= score1:
		return "ham"
	return "spam"
	
if __name__ == '__main__':
	V,prior,condprob = TRAINMULTINOMIALNB()
	for d in glob.glob('test/ham/*.txt'):
		 APPLYMULTINOMIALNB(V,prior,condprob,d)
	