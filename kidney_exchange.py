	#!/usr/bin/python
# ---------------------------------------------------------------------------
# File: vertex_cover.py
# Version 12.9.0
# ---------------------------------------------------------------------------
# Licensed Materials - Property of IBM
# 5725-A06 5725-A29 5724-Y48 5724-Y49 5724-Y54 5724-Y55 5655-Y21
# Copyright IBM Corporation 2009, 2019. All Rights Reserved.
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with
# IBM Corp.
# ---------------------------------------------------------------------------
"""Input is a graph.

"""  
from __future__ import print_function

import sys

import cplex
from cplex.exceptions import CplexSolverError
from itertools import combinations 
from itertools import permutations
import datetime





def removechains(cycles):
	onlyCycles = []
	for cycle in cycles:
		if cycle[0] == cycle[-1]:
			onlyCycles.append(cycle)
	return onlyCycles



def maximize_pairwise_exchange(cycles,vertices,dirname):
	onlyCycles = removechains(cycles)
	solution_values = optimize_length(onlyCycles,vertices,dirname)
	print (solution_values)
	return solution_values



def maximize_total_transplants(cycles,vertices,dirname):
	solution_values = optimize_length(cycles,vertices,dirname)
	return solution_values



def maximize_total_weight(cycles,vertices,cycle_wt,dirname):
	solution_values = optimize_weight(cycles,vertices,cycle_wt,dirname)
	return solution_values



def optimize_length(cycles,vertices,dirname):
	prob = cplex.Cplex()
	prob.set_problem_name("KIDNEY EXCHANGE")

	names = []

	prob.set_problem_type(cplex.Cplex.problem_type.LP)

	obj =[]
	for cycle in cycles:
		obj.append(len(cycle))
	
	c={}
	i = 0
	for cycle in cycles:
		names.append("c_%s" % str(cycle))
		i = i+1

	prob.variables.add(obj=obj,names=names, lb=[0] * len(names),
                    ub=[1] * len(names),
                    types=["B"] * len(names))


	constraints = []
	constraint_names = []
	for v in vertices:
		constraint = []
		constraint_names = []
		i = 0
		for cycle in cycles:
			if v in cycle:
				constraint.append(names[i])
			i = i+1
		if constraint:
			constraint_names.append("v" + str(v))
			prob.linear_constraints.add(lin_expr=[cplex.SparsePair(constraint, [1] * len(constraint))],senses=['L'],rhs=[1],names=constraint_names)

	prob.objective.set_sense(prob.objective.sense.maximize)
	prob.write(dirname +"/" + "optimize_length.lp")

	prob.solve()

	return prob.solution.get_values()



def optimize_weight(cycles,vertices,weight,dirname):
	prob = cplex.Cplex()
	prob.set_problem_name("KIDNEY EXCHANGE")

	names = []

	prob.set_problem_type(cplex.Cplex.problem_type.LP)\

	obj =[]
	for cycle in cycles:
		obj.append(weight[tuple(cycle)])

	c={}
	i = 0
	for cycle in cycles:
		names.append("c_%s" % str(cycle))
		i = i+1

	prob.variables.add(obj=obj,names=names, lb=[0] * len(names),
                    ub=[1] * len(names),
                    types=["B"] * len(names))

	constraints = []
	constraint_names =[]
	for v in vertices:
		constraint = []
		i = 0
		for cycle in cycles:
			if v in cycle:
				constraint.append(names[i])
			i = i+1
		if constraint:
			names.append("v" + v)
			prob.linear_constraints.add(lin_expr=[cplex.SparsePair(constraint, [1] * len(constraint))],senses=['L'],rhs=[1],names=constraint_names)

	prob.objective.set_sense(prob.objective.sense.maximize)
	prob.write(dirname +"/" + "optimize_weight.lp")
	
	prob.solve()

	return prob.solution.get_values()



	
def kidney_exchange(names,edges,ma,weight,altruists):
	all_cycles = find_cycles(names,len(names),ma,altruists)
	cycles = find_cycles_in_graph(all_cycles,edges)
	print(cycles)
	cycleswt = findwt(cycles,weight)
	# print(cycleswt)
	e
	if int(a) == 1:
		solution_values = optimize_length(cycles,names,ma,altruists)
		solution(1,"size",ma,solution_values,cycles,altruists,edges,cycleswt,names)
	elif int(a) == 2:
		optimize_weight(cycles,names,cycleswt,ma)



if __name__ == "__main__":
	names = ['0','1','2','3']
	edges = [['0','1'],['1','0'],['0','3'],['3','2'],['2','0']]
	all_cycles = find_cycles(names,3,3)
	print(all_cycles)
	cycles = find_cycles_in_graph(all_cycles,edges)
	print("******************************************************************************************************")
	print(cycles)
	#optimize(cycles,names)