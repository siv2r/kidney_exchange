# kidney_exchange
Implementation for Kidney Exchange problem using python and cplex.

# Problem
Given a pair of patient and donor where the donor is willing to donate his kidney yet may not be compatible; given a large pool of such pairs, by what method can a trade occur with the goal that the quantity of transplants is maximized.

# Prerequisites
* Python 3
* Cplex

# Input
1. A json file which consists of data represnting donors and patients and their comaptibility with score. 
2. Maximum Cycle size 
3. Maximum chain length
4. Optimality criteria through which you want to implement kidney exchange.

# How to run?
Command  : python pipelin.py "json file"
I have already a json file genjson-0.json. You can keep any json file.

For example :- python pipeline.py genjson-0.json

# Output
The output should be mostly self-explanatory.
The valid exchanges are printed as well as a visual graph is also saved as an image.
