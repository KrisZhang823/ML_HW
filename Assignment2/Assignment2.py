from __future__ import division
import numpy as np
import glob
import math
import random 

stopWords = {"a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"}
hamWords = []
spamWords = []
vocab1 = {}
vocab2 = {}
vocab = {}
hamtest = []
spamtest = []

def init():
	for filename in glob.glob('train/ham/*.txt'):
		with open(filename) as f:
			wordstemp = f.read().split()	
			hamWords.append(wordstemp)

	for filename in glob.glob('train/spam/*.txt'):
		with open(filename) as f:
			wordstemp = f.read().split()
			spamWords.append(wordstemp)

	for words in hamWords:
		for word in words:
			if vocab1.has_key(word):
				vocab1[word] += 1
			else:
				vocab1[word] = 1

	for words in spamWords:
		for word in words:
			if vocab2.has_key(word):
				vocab2[word] += 1
			else:
				vocab2[word] = 1

	for filename in glob.glob('test/ham/*.txt'):
		with open(filename) as f:
			wordstemp = f.read().split()
			hamtest.append(wordstemp)

	for filename in glob.glob('test/spam/*.txt'):
		with open(filename) as f:
			wordstemp = f.read().split()
			spamtest.append(wordstemp)
	
def TRAINMULTINOMIALNB(useStops):	
	Nc1 = len(glob.glob('train/ham/*.txt'))
	Nc2 = len(glob.glob('train/spam/*.txt'))
	N = Nc1 + Nc2

	vocabLocal = dict(vocab1.items() + vocab2.items())

	prior = [0,0]
	prior[0] = Nc1/N
	prior[1] = Nc2/N


	Tct1,Tct2,condprob1,condprob2 = {},{},{},{}

	for v in vocabLocal:
		if vocab1.has_key(v):
			Tct1[v] = vocab1[v]
		else:
			Tct1[v] = 0

	ETct = 0
	for v in vocab1:
		ETct += vocab1[v]
	for v in vocabLocal:
		condprob1[v] = (Tct1[v]+1)/(len(vocabLocal) +ETct)

	for v in vocabLocal:
		if vocab2.has_key(v):
			Tct2[v] = vocab2[v]
		else:
			Tct2[v] = 0

	ETct = 0
	for v in vocab2:
		ETct += vocab2[v]
	for v in vocabLocal:
		condprob2[v] = (Tct2[v]+1)/(len(vocabLocal) +ETct)

	condprob = [condprob1,condprob2]

	return vocabLocal,prior,condprob

def APPLYMULTINOMIALNB(V,prior,condprob,words,useStops):
	W = []
	if useStops:
		words = filter(lambda x: x not in stopWords,words)
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

def sigmoid(x):
	return 1.0/(1.0 + np.exp(-x))

def LogisticRegression(iterations,alpha,useStops):
	v = dict(vocab1.items() + vocab2.items())
	weights = v.fromkeys(v,1.0)
	rate = 0.0001
	for i in range(iterations):
		for words in hamWords:
			vocab = {}
			if useStops:
				words = filter(lambda x: x not in stopWords,words)
			for word in words: 
				if vocab.has_key(word):
					vocab[word] += 1
				else:
					vocab[word] = 1
					
			predicted = classify(weights,vocab)
			label = 1
			for key in weights: 
				weights[key] = weights[key] + rate*(label - predicted)*vocab.get(key,0) - rate*alpha*weights[key]

		for words in spamWords:
			vocab = {}
			if useStops:
				words = filter(lambda x: x not in stopWords,words)		
			for word in words: 
				if vocab.has_key(word):
					vocab[word] += 1
				else:
					vocab[word] = 1
			predicted = classify(weights,vocab)
			label = 0
			for key in weights: 
				weights[key] = weights[key] + rate*(label - predicted)*vocab.get(key,0) - rate*alpha*weights[key]

		# lik += label * Math.log(classify(x)) + (1-label) * Math.log(1- classify(x));
		# print "iteration: " + iterations + " " + weights + " mle: " + lik

	return weights

def classify(w,v):
	logit = 0.0
	for key in v:
		logit += w.get(key,0)*v.get(key,0)
	return (logit)
def classify2(w,v):
	logit = 0.0
	for key in v:
		logit += w.get(key,0)*v.get(key,0)
	return logit >=0 

def testLR(words,useStops,T,F,label):
	vocab = {}
	if useStops:
		words = filter(lambda x: x not in stopWords,words)
	for word in words: 
		if vocab.has_key(word):
			vocab[word] += 1
		else:
			vocab[word] = 1

	if classify2(weights,vocab):
		if label == 1:
			T += 1
		else:
			F += 1
	else:
		if label == 1:
			F += 1
		else:
			T += 1
	return T,F

if __name__ == '__main__':
	init()

	V1,prior,condprob = TRAINMULTINOMIALNB(False)
	t = f = 0
	for words in hamtest:
		if APPLYMULTINOMIALNB(V1,prior,condprob,words,False) == "ham":t += 1
		else :f += 1
	for words in spamtest:
		if APPLYMULTINOMIALNB(V1,prior,condprob,words,False) == "spam":t += 1
		else :f += 1

	print "Accuracy for Naive Bayes model before remove stopWords= "+ str(t/(t+f))

	V2,prior,condprob = TRAINMULTINOMIALNB(True)
	t = f = 0
	for words in hamtest:
		if APPLYMULTINOMIALNB(V1,prior,condprob,words,True) == "ham":t += 1
		else :f += 1
	for words in spamtest:
		if APPLYMULTINOMIALNB(V1,prior,condprob,words,True) == "spam":t += 1
		else :f += 1

	print "Accuracy for Naive Bayes model after remove stopWords= "+ str(t/(t+f))

	
	for i in range(10):
		T = F = 0
		alpha = random.randint(1,10)
		iterations = random.randint(1,10)

		weights = LogisticRegression(iterations,alpha/10.0,False)

		for words in hamtest:
			T,F = testLR(words,False,T,F,1)
		for words in spamtest:
			T,F = testLR(words,False,T,F,0)

		print "Accuracy for Logistic Regression model with iterations = " +str(iterations)+ " and alpha = "+str(alpha/10.0)+" before remove stopWords = "+ str(T/(T+F))	

		weights = LogisticRegression(iterations,alpha/10.0,True)
		for words in hamtest:
			T,F = testLR(words,True,T,F,1)
		for words in spamtest:
			T,F = testLR(words,True,T,F,0)


		print "Accuracy for Logistic Regression model with iterations = " +str(iterations)+ " and alpha = "+str(alpha/10.0)+" after remove stopWords = "+ str(T/(T+F))	
	