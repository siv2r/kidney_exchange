from itertools import combinations 
from itertools import permutations




class CyclePrecomputation:

	all_cycles = []
	cycles=[]

	def __init__(self):
		all_cycles = []
		cycles = []



	def find_cycles (self,Names,malength):
		for i in range(2,malength+1):
			comb = combinations(Names, i)
			temp = []
			for lis in comb :
				com = lis[1:]
				perm = permutations(com) 

				for per in perm:
					fin = []
					fin.append(lis[0])
					fin.extend(per)
					fin.append(lis[0])
					self.all_cycles.append(fin)	



	def find_chains(self,Names,malength,altruists):
		for node in altruists:
			for i in range(1,malength+1):
				comb = combinations(Names,i)
				temp = []
				for lis in comb:
					perm = permutations(lis)

					for per in perm:
						fin = []
						fin.append(node)
						fin.extend(per)
						self.all_cycles.append(fin)



	def check_cycle(self,cycle,edges) :
		for i in range(0,len(cycle)-1):
				edge = [cycle[i],cycle[i+1]]
				
				if  edge not in edges :
					return False

		return True



	def find_cycles_in_graph(self,edges):
		for cycle in self.all_cycles:
			if self.check_cycle(cycle,edges) == True:
				self.cycles.append(tuple(cycle))
	    		
		return self.cycles
		
	

	def findwt(self,cycles,weight):
		cycleswt ={}
		for cycle in cycles:
			wt =0
			for i in range(0,len(cycle)-1):
				edge = (cycle[i],cycle[i+1])
				wt =wt + weight[edge]
			cycleswt[cycle] = wt

		return cycleswt



	def findCyclesAndChains(self,names,max_cycle_length,max_chain_length,altruists,edges):
		self.find_cycles(names, max_cycle_length)
		self.find_chains(names,max_chain_length, altruists)
		self.find_cycles_in_graph(edges)
		
		return self.cycles



	def check_backarc(self,cycle, edges):
		for i in range(0,len(cycle) - 1):
			edge = [cycle[i+1],cycle[i]]
			if(edge in edges):
				return True

		return False
