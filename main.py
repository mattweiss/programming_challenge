from dag import DAG

from pdb import set_trace as st

# arc dictionary
node_dict = {
    'A':{'arcs':['B','C','D'],'supported':True},
    'B':{'arcs':['E','F'],'supported':False},
    'C':{'arcs':['E','F'],'supported':False},
    'D':{'arcs':['K'],'supported':True},
    'E':{'arcs':['G'],'supported':False},
    'F':{'arcs':['E','G','H','I'],'supported':True},
    'G':{'arcs':['J'],'supported':True},
    'H':{'arcs':['K'],'supported':True},
    'I':{'arcs':[None],'supported':True},
    'J':{'arcs':['K'],'supported':False},
    'K':{'arcs':[None],'supported':False},
}

# input and output nodes
input_node = 'A'
output_node = 'K'

# Build graph
graph = DAG(node_dict,input_node,output_node)

# Partition graph
node_set_list = graph.partitionGraph()
print(node_set_list)

