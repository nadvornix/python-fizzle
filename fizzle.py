
'''TODO:
- better unicode support
- write docs

'''

def DL_distance(s1,s2,substitutions=[],symetric=True):
	"""
	Return DL distance between s1 and s2.
	substitutions is list of tuples of characters (what, substituted by what, cost), 
		maximal value of substitution is 2 (ie: cost deletion & insertion that would be otherwise used)
		eg: substitutions=[('a','e',0.4),('i','y',0.3)]
	symetric=True mean that cost of substituting A with B is same as B with A

	"""
	from collections import defaultdict
	subs=defaultdict(lambda :1)
	for a,b,v in substitutions:
		subs[(a,b)]=v
		if symetric:
			subs[(b,a)]=v
	
	#import array
	row=(1+len(s2))*[0.]
	matrix=[[i+j for j in range(len(s2)+1)] for i in range(len(s1)+1)]	#matrix |s1|+1 x |s2|+1
	# print matrix
	# print len(matrix),len(row)

	for i in range(len(s1)):
		for j in range(len(s2)):
			ch1,ch2=s1[i],s2[j]
			if ch1==ch2:
				cost = 0
			else:
				cost = subs[(ch1,ch2)]
	# 		print s1[i],s2[j],[matrix[i][j+1]+1, 	#deletion
	# 						  matrix[i+1][j]+1,	#insertion
	# 						  matrix[i][j]+cost	#substitution or no change
	# 						]
			matrix[i+1][j+1]=min([matrix[i][j+1]+1, 	#deletion
							  matrix[i+1][j]+1,	#insertion
							  matrix[i][j]+cost	#substitution or no change
							])

			if i>=1 and j>=1 and s1[i]==s2[j-1] and s1[i-1]==s2[j]:
				matrix[i+1][j+1] = min([matrix[i+1][j+1],
									matrix[i-1][j-1]+cost])

	print "     ",
	for i in s2:
		print i,"",
	print 
	for i,r in enumerate(matrix):
		if i==0:
			print " ",r
		else:
			print s1[i-1],r
	return matrix[-1][-1]

def match_list(s, l):
	'''
	returns list of elements of l with each element having assigned distance from s
	'''
	return map( lambda x:(DL_distance(s,x),x), l)

def pick_one(s, options, num=1):
	''' picks one string from options best matching with s 
		- if num is set then returns top num results instead of one
	'''
	pass #TODO


if __name__=="__main__":
	print DL_distance('dayme', 'dayne', substitutions=[('a','e',0.4),('i','y',0.3),('m','n',0.5)])

	# print match_list("Levenshtein", ["Levenshtain","Levenstein","Levinstein","Levistein"])
