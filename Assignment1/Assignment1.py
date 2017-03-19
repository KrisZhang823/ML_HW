from __future__ import division
from __future__ import print_function
import math
import random
import sys
import csv
from sys import maxint



class TreeNode(object):
	def __init__(self):
		self.id = None
		self.left = None
		self.right = None
		self.res = -1




attrs = ['XB','XC','XD','XE','XF','XG','XH','XI','XJ','XK','XL','XM','XN','XO','XP','XQ','XR','XS','XT','XU','Class']
data = []
validData = []
test = []

def readData(fileName1,fileName2,fileName3):
	with open(fileName1) as csvfile:
		reader = csv.DictReader(csvfile)	
		for row in reader:
			data.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
				row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
				,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))

	with open(fileName2) as csvfile:
		reader = csv.DictReader(csvfile)	
		for row in reader:
			validData.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
				row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
				,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))

	with open(fileName3) as csvfile:
		reader = csv.DictReader(csvfile)	
		for row in reader:
			test.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
				row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
				,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))
	



# with open("data_sets1/training_set.csv") as csvfile:
# 	reader = csv.DictReader(csvfile)	
# 	for row in reader:
# 		data1.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
# 			row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
# 			,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))



# with open("data_sets1/validation_set.csv") as csvfile:
# 	reader = csv.DictReader(csvfile)	
# 	for row in reader:
# 		validData1.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
# 			row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
# 			,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))


# with open("data_sets1/test_set.csv") as csvfile:
# 	reader = csv.DictReader(csvfile)	
# 	for row in reader:
# 		test1.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
# 			row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
# 			,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))

# data2 = []

# with open("data_sets2/training_set.csv") as csvfile:
# 	reader = csv.DictReader(csvfile)	
# 	for row in reader:
# 		data2.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
# 			row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
# 			,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))


# validData2 = []
# with open("data_sets2/validation_set.csv") as csvfile:
# 	reader = csv.DictReader(csvfile)	
# 	for row in reader:
# 		validData2.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
# 			row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
# 			,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))

# test2 = []
# with open("data_sets2/test_set.csv") as csvfile:
# 	reader = csv.DictReader(csvfile)	
# 	for row in reader:
# 		test2.append(list([row['XB'],row['XC'],row['XD'],row['XE'],row['XF'],row['XG'],row['XH'],
# 			row['XI'],row['XJ'],row['XK'],row['XL'],row['XM'],row['XN'],row['XO'],row['XP'],row['XQ']
# 			,row['XR'],row['XS'],row['XT'],row['XU'],row['Class']]))


def buildTree2(data,attrs,visited):
	# print (visited)
	K = len(data)
	K0 = 0
	K1 = 0
	for d in data:
		if d[20] == "0":
			K0 += 1
		else:
			K1 += 1


	root = TreeNode()

	if len(visited) == 20:
		if K0 > K1:
			root.res = 0
		else:
			root.res = 1
		return root

	if K0 == 0:
		root.res = 1
		return root
	elif K1 == 0:
		root.res = 0
		return root

	H =  K0*K1/(K*K)
	

	G = -maxint
	attrIdex = 0
	for i in xrange(20) :
		if i in visited:
			continue
		a  = 0
		a0 = 0
		a1 = 0
		b  = 0
		b0 = 0
		b1 = 0
	 	for d in data:
			if d[20] == "0":
				a += 1
				if d[i] == "0":
					a0 += 1
				else:
					a1 += 1
			else:
				b += 1
				if d[i] == "0":
					b0 += 1
				else:
					b1 += 1
		g = H 
		if a != 0:
			g -= (a/K)*(a0*a1/(a*a))
		if b != 0:
			g -= (b/K)*(b0*b1/(b*b))
		# g = H
		# print G
		if G < g :
			attrIdex = i
			G = g

	data0 = []
	data1 = []
	for d in data:
		if d[attrIdex] == "0":
			data0.append(d)
		else:
			data1.append(d)

	visited.add(attrIdex)

	nVisited = set(visited)

	if len(data0) > len(data1):
		root.res = -1
	else:
		root.res = -2
	root.id = attrIdex
	root.left = buildTree2(data0,attrs,nVisited)
	root.right = buildTree2(data1,attrs,nVisited)

	return root

def buildTree1(data,attrs,visited):
		"""
		:type data : list<list<Integer>>
		:type attrs : list
		:type visited : set
		:rtype TreeNode
		"""	

		K = len(data)
		K0 = 0
		K1 = 0
		for d in data:
			if d[20] == "0":
				K0 += 1
			else:
				K1 += 1

		root = TreeNode()

		if len(visited) == 20:
			if K0 > K1:
				root.res = 0
			else:
				root.res = 1
			return root
		else:
			if K0 == 0:
				root.res = 1
				return root
			elif K1 == 0:
				root.res = 0
				return root

		H =  -K0*K1 * math.log(K0/K,2) - K1/K * math.log(K1/K,2)
		
		G = -maxint
		attrIdex = 0
		for i in xrange(20) :
			if i in visited:
				continue
			a  = 0
			a0 = 0
			a1 = 0
			b  = 0
			b0 = 0
			b1 = 0
		 	for d in data:
				if d[20] == "0":
					a += 1
					if d[i] == "0":
						a0 += 1
					else:
						a1 += 1
				else:
					b += 1
					if d[i] == "0":
						b0 += 1
					else:
						b1 += 1
			g = H 
			if a != 0:
				if a0 !=0:	
					g -= (a/K)*(-a0/a * math.log(a0/a,2))
				if a1 != 0:
				 	g -= (a/K)*(-a1/a * math.log(a1/a,2)) 
			if b != 0:
				 
				if b0 != 0:
					g -= (b/K)*(-b0/b * math.log(b0/b,2))
				if b1 != 0:
					g -= (b/K)*(-b1/b * math.log(b1/b,2)) 
				 

			if G < g :
				attrIdex = i
				G = g

		data0 = []
		data1 = []
		for d in data:
			if d[attrIdex] == "0":
				data0.append(d)
			else:
				data1.append(d)

		visited.add(attrIdex)

		nVisited = set(visited)

		if len(data0) > len(data1):
			root.res = -1
		else:
			root.res = -2
		root.id = attrIdex
		root.left = buildTree1(data0,attrs,nVisited)
		root.right = buildTree1(data1,attrs,nVisited)

		return root
				
def pruneTree(root,validData,L,K):
	best = root
	last = evaluation(validData,best)

	for i in xrange(random.randint(1,L)):
		newRoot = copyTree(best)

		for j in xrange(random.randint(1,K)):
			noneLeaves = []
			getNoneLeaves(newRoot,noneLeaves)
			if len(noneLeaves) == 0:
				break;
			# print(len(noneLeaves))
			P = random.randint(0,len(noneLeaves)-1)
			# print(P)
			removeNode = noneLeaves[P]
			replaceNode(removeNode)

		
		cur = evaluation(validData,newRoot)
		# printTree(newRoot,0)
		# print(last)

		if cur >= last:
			last = cur
			best = newRoot

	return best

def evaluation(validData,root):
	count = 0
	for d in validData:
		if evaluateDFS(root,d):
			count += 1

	return count/len(validData)
		

def evaluateDFS(root,data):
	if root is None:
		return
	if root.id != None:
		if data[root.id] == "0":
			return evaluateDFS(root.left,data)
		else:
			return evaluateDFS(root.right,data)
	else:
		return data[20] == str(root.res)
	
def replaceNode(removeNode):

	removeNode.id = None
	removeNode.left = None
	removeNode.right = None

	if removeNode.res == -1:
		removeNode.res = 0
	elif removeNode.res == -2:
		removeNode.res = 1
	else:
		return

	


def getNoneLeaves(root,list):
	if root.id is not None:
		list.append(root)
		getNoneLeaves(root.left,list)
		getNoneLeaves(root.right,list)
	

def copyTree(root):
	newRoot = TreeNode()
	newRoot.id = root.id
	newRoot.res = root.res
	if newRoot.id is None:
		return newRoot

	newRoot.left = copyTree(root.left)
	newRoot.right = copyTree(root.right)

	return newRoot



def printTree(root,level):
	if root is None:
		return

	if root.id is not None:
		sys.stdout.write('\n')
		p = level
		while p > 0:
			print ('|',end=' ')
			p -= 1
		sys.stdout.write(attrs[root.id] + " =" + " 0 : ")
		printTree(root.left,level+1)
		sys.stdout.write('\n')

		p = level
		while p > 0:
			print ('|',end=' ')
			p -= 1
		sys.stdout.write(attrs[root.id] + " =" + " 1 : ")
		printTree(root.right,level+1)
	else:
		sys.stdout.write(str(root.res))




kls =  [[100,20],[200,30],[50,10],[70,20],[250,50],[150,50],[20,10],[50,50],[90,20],[500,20]]
def main2(argv):
	trainingFile = argv[2]
	validationFile = argv[3]
	testFile = argv[4]
	isPrint = argv[5]
	readData(trainingFile,validationFile,testFile)
	for kl in kls:
		inputL = kl[0]
		inputK = kl[1]
		visited = set()
		root1 = buildTree1(data,attrs,visited)
		root2 = buildTree2(data,attrs,visited)
		prune1 = pruneTree(root1,validData,inputL,inputK)
		prune2 = pruneTree(root1,validData,inputL,inputK)
		print("L = "+str(inputL)+ " and "+"K = "+str(inputK))
		print("Accuracies of first post-pruned Decision Tree : " + str(evaluation(test,prune1)))
		print("Accuracies of second post-pruned Decision Tree : " + str(evaluation(test,prune2)))


def main(argv):
	inputL = int(argv[0])
	inputK = int(argv[1])

	trainingFile = argv[2]
	validationFile = argv[3]
	testFile = argv[4]
	isPrint = argv[5]

	readData(trainingFile,validationFile,testFile)

	visited = set()
	root1 = buildTree1(data,attrs,visited)
	root2 = buildTree2(data,attrs,visited)
	prune1 = pruneTree(root1,validData,inputL,inputK)
	prune2 = pruneTree(root1,validData,inputL,inputK)


	print("Accuracies of first Decision Tree : " + str(evaluation(test,root1)))
	print("Accuracies of first post-pruned Decision Tree : " + str(evaluation(test,prune1)))
	print("Accuracies of second Decision Tree : " + str(evaluation(test,root2)))
	print("Accuracies of second post-pruned Decision Tree : " + str(evaluation(test,prune2)))

	if isPrint == "yes":
		print("")
		print("First post-pruned Tree :")
		printTree(prune1,0)
		print("")
		print("second post-pruned Tree :")
		printTree(prune2,0)
		print("")
		# printTree(root1,0)

if __name__ == '__main__':
	main(sys.argv[1:])

    # visited = set()
    # root = buildTree(data1,attrs,visited)
    # prune = pruneTree(root,validData1,100,20)
    # print(evaluation(test1,prune))
    
	

    # visited = set()
    # root = buildTree(data2,attrs,visited)
    # prune = pruneTree(root,validData2,100,20)
    
    # print(evaluation(test2,prune))





		