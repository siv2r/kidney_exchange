
import sys 
import shutil
from kidney_exchange import kidney_exchange
from jsonConversion import DataConvert
from precomputation import CyclePrecomputation
from kidney_exchange import maximize_pairwise_exchange
from kidney_exchange import maximize_total_transplants
from kidney_exchange import maximize_total_weight
from solution import print_solution
import datetime
import os
import sys 
import csv




names =[]
edges =[]
weight = {}
altruistic_donors = []

fnames = ['Total Patients',  'Altruistic Donors', 'Maximum cycle size',  'Maximum chain size', 'Transplants',  'Constraint']

def fillexcel(patients,altruistic_donors,max_cycle_length,max_chain_length,transplants,Constraint):
  with open('kidney.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([patients,altruistic_donors,max_cycle_length,max_chain_length,transplants,Constraint])

def pipeline(n):

  # with open('kidney.csv', 'a', newline='') as file:
  #   writer = csv.DictWriter(file, fieldnames=fnames)
  #   writer.writeheader()
  if len(sys.argv) != 2 :
      print("Error :Please specify number of nodes")
      sys.exit(-1)
  file_name = sys.argv[1]
  x = datetime.datetime.now()
  dirName = str(x)

  if not os.path.exists(dirName):
      os.mkdir(dirName)
  else:    
      print("Directory " , dirName ,  " already exists")
      sys.exit(-1)

  destination = dirName
  shutil.copy(file_name, destination)
  graph = dirName + '/' + "graph"
  f = open(graph, "w")




  json_convert = DataConvert()
  precomputation = CyclePrecomputation()

  names,edges,weight,altruistic_donors = json_convert.convert_altruistic(file_name)
  f.write(str(len(names)) + " "+ str(len(altruistic_donors)) + " " + str(len(edges)))
  for name in names:
    f.write(str(name)+ "\n")
  for altruistic_donor in altruistic_donors:
    f.write(str(altruistic_donor)+ "\n")
  for edge in edges :
    f.write("[" + edge[0] + " " + edge [1] + "] "  + str(weight[tuple(edge)]) + "\n")

  f.close()


  max_cycle_length = int(input("Maximum Cycle size"))
  max_chain_length = int(input("Altruistic Chain Length"))

  option = int(input("Choose option \n1.Maximize the number of effective pairwise exchange \n2.Maximize the total number of transplants\n3.Maximize the total number of backarcs\n4.Maximize the total weight\n5.Minimize the number of 3-way exchange\n6.Maximize the number of pairwise exchange"))


  #Basically maximizing the total number of cycles which does not involve altruistic donor
  if option == 1:
    cyclesAndChains = precomputation.findCyclesAndChains(names,max_cycle_length,max_chain_length ,altruistic_donors,edges)
    cycleandchain_wt = precomputation.findwt(cyclesAndChains,weight) 
    solution_values = maximize_pairwise_exchange(cyclesAndChains,names,dirName)
    transplants = print_solution(1, "Maximize the number of effective pairwise exchange", max_cycle_length, solution_valuesd, cyclesAndChains, altruistic_donors, edges, cycleandchain_wt, names,dirName)
    fillexcel(len(names),len(altruistic_donors),max_cycle_length,max_chain_length,transplants,"Maximize the number of effective pairwise exchange")

  #Maximize the number of patients that get a kidney. This will involve altruistic donors as well
  if option == 2:
    cyclesAndChains = precomputation.findCyclesAndChains(names,max_cycle_length,max_chain_length ,altruistic_donors,edges)
    cycleandchain_wt = precomputation.findwt(cyclesAndChains,weight) 
    solution_values = maximize_total_transplants(cyclesAndChains,names+altruistic_donors,dirName)
    transplants = print_solution(1, "Maximize the total number of transplants", max_cycle_length, solution_values, cyclesAndChains, altruistic_donors, edges, cycleandchain_wt, names,dirName)
    fillexcel(len(names),len(altruistic_donors),max_cycle_length,max_chain_length,transplants,"Maximize the total number of transplants")

  #No of backarcs in 3-way exchange should be maximized(a 3-way exchange can contain more than one backarc.)
  if option == 3:
    print("Yet to be done")

  #Maximize the total weight calculated by summing over all cycles and chains
  if option == 4:
    cyclesAndChains = precomputation.findCyclesAndChains(names,max_cycle_length,max_chain_length ,altruistic_donors,edges)
    cycleandchain_wt = precomputation.findwt(cyclesAndChains,weight) 
    solution_values = maximize_total_weight(cycles,names + altruistic_donors,cycle_wt,dirName)
    transplants = print_solution(1, "Maximize the total weight", max_cycle_length, solution_values, cyclesAndChains, altruistic_donors, edges, cycleandchain_wt, names,dirName)
    fillexcel(len(names),len(altruistic_donors),max_cycle_length,max_chain_length,transplants,"Maximize the total weight")


  if option == 5:
    print("Yet to be done")

  #Maximize the number of pairwise exchange plus unused altruists:-
  if option == 6:
    cyclesAndChains = precomputation.findCyclesAndChains(names,2,1 ,altruistic_donors,edges)
    cycleandchain_wt = precomputation.findwt(cyclesAndChains,weight) 
    solution_values = maximize_total_transplants(cyclesAndChains, names + altruistic_donors,dirName)
    transplants = print_solution(1, "Maximize pairwise exchange", 2, solution_values, cyclesAndChains, altruistic_donors, edges, cycleandchain_wt, names,dirName)
    fillexcel(len(names),len(altruistic_donors),max_cycle_length,max_chain_length,transplants,"Maximize the number of pairwise exchange")





if __name__ == "__main__":
   pipeline(1)
  
 

  



  




