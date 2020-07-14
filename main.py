from dag import DAG

from pdb import set_trace as st

# arc dictionary
arc_dict = {
    'A':{'arcs':['B'],'supported':True},
    'B':{'arcs':['C','D'],'supported':False},
    'C':{'arcs':['F'],'supported':True},
    'D':{'arcs':['E'],'supported':False},
    'E':{'arcs':['F'],'supported':True},
    'F':{'arcs':[None],'supported':True},
}

# input and output nodes
input_node = 'A'
output_node = 'C'

# Build graph
graph = DAG(arc_dict,input_node,output_node)

# Partition graph
#graph.partitionGraph()

st()
