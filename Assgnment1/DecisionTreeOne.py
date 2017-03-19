
class ClassName(object):
	

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
				# g -= (a/K)*(a0*a1/(a*a))
				g -= (a/K)*(-a0/a * math.log(a0/a,2))
			if b != 0:
				# g -= (b/K)*(b0*b1/(b*b))
				g -= (a/K)*(-a1/a * math.log(a1/a,2))

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