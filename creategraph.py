'''
*PRAGNYA SRINIVASAN
*pragnya.srini@gmail.com
*
'''
from subprocess import check_call
import sys
import os
import multiplayer_graph

#Call the python file that parses JSON data and creates a DOT file
os.system("python multiplayer_graph.py")
dotfile = raw_input("Enter the dot file again")
dott =  dotfile + ".dot"
graphn = raw_input("Enter the graphname your want to create ")
graphname =  graphn+ ".png"
check_call(['dot','-Tpng',dott,'-o',graphname])
