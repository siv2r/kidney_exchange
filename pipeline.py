
import sys 
from kidney_exchange import kidney_exchange
from jsonConversion import DataConvert
from precomputation import CyclePrecomputation
from kidney_exchange import maximize_pairwise_exchange
from kidney_exchange import maximize_total_transplants
from kidney_exchange import maximize_total_weight
from solution import print_solution










names =[]
edges =[]
weight = {}
altruistic_donors = []


    

def pipeline(n):
  if len(sys.argv) != 2 :
      print("Error :Please specify number of nodes")
      sys.exit(-1)
  file_name = sys.argv[1]

  json_convert = DataConvert()
  precomputation = CyclePrecomputation()


  names,edges,weight,altruistic_donors = json_convert.convert_altruistic(file_name)
  max_cycle_length = int(input("Maximum Cycle size"))
  max_chain_length = int(input("Altruistic Chain Length"))

  


  a = int(input("Choose option \n1.Maximize the number of effective pairwise exchange \n2.Maximize the total number of transplants\n3.Maximize the total number of backarcs\n4.Maximize the total weight\n5.Minimize the number of 3-way exchange\n6.Maximize the number of pairwise exchange"))

  if a == 1:
    cycles = precomputation.findCyclesAndChains(names,max_cycle_length,max_chain_length ,altruistic_donors,edges)
    cycle_wt = precomputation.findwt(cycles,weight) 
    solution_values = maximize_pairwise_exchange(cycles,names)
    print_solution(1, "Maximize the number of effective pairwise exchange", max_cycle_length, solution_values, cycles, altruistic_donors, edges, cycle_wt, names)

  if a == 2:
    cycles = precomputation.findCyclesAndChains(names,max_cycle_length,max_chain_length ,altruistic_donors,edges)
    cycle_wt = precomputation.findwt(cycles,weight) 
    solution_values = maximize_total_transplants(cycles,names+altruistic_donors)
    print_solution(1, "Maximize the total number of transplants", max_cycle_length, solution_values, cycles, altruistic_donors, edges, cycle_wt, names)

  if a == 3:
    print("Yet to be done")

  if a == 4:
    cycles = precomputation.findCyclesAndChains(names,max_cycle_length,max_chain_length ,altruistic_donors,edges)
    cycle_wt = precomputation.findwt(cycles,weight) 
    solution_values = maximize_total_weight(cycles,names + altruistic_donors,cycle_wt)
    print_solution(1, "Maximize the total weight", max_cycle_length, solution_values, cycles, altruistic_donors, edges, cycle_wt, names)

  if a == 5:
    print("Yet to be done")

  if a == 6:
    cycles = precomputation.findCyclesAndChains(names,2,1 ,altruistic_donors,edges)
    cycle_wt = precomputation.findwt(cycles,weight) 
    solution_values = maximize_total_transplants(cycles, names + altruistic_donors)
    print_solution(1, "Maximize pairwise exchange", 2, solution_values, cycles, altruistic_donors, edges, cycle_wt, names)










  # #convert(n)
  # convert_altruistic(n)
  # print(names)
  # print(altruistic)
  # kidney_exchange(names,edges,3,weight,altruistic)

      #print(data)
      # for p in data['data']:
      #     print(p['sources'])
      #     for q in p["matches"]:
      #       print(a1,"                                          ",q["recipient"])
      # a=extract_element_from_json(data, ["data", "sources"])
      # print (a)


if __name__ == "__main__":
   pipeline(1)
  
 

  



  




