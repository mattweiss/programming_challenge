from dag_node import dagNode
from dag import DAG

from pdb import set_trace as st

# arc dictionary
lt_node_dict = {
    'A':{'arcs':['B'],'supported':True,'input':True},
    'B':{'arcs':['C','D'],'supported':False},
    'C':{'arcs':['F'],'supported':True},
    'D':{'arcs':['E'],'supported':False},
    'E':{'arcs':['F'],'supported':True},
    'F':{'arcs':[None],'supported':True,'output':True},
}

rd_node_dict = {
    'A':{'arcs':['B','C','D'],'supported':True,'input':True},
    'B':{'arcs':['E','F'],'supported':False},
    'C':{'arcs':['E','F'],'supported':False},
    'D':{'arcs':['K'],'supported':True},
    'E':{'arcs':['G'],'supported':False},
    'F':{'arcs':['E','G','H','I'],'supported':True},
    'G':{'arcs':['J'],'supported':True},
    'H':{'arcs':['K'],'supported':True},
    'I':{'arcs':[None],'supported':True},
    'J':{'arcs':['K'],'supported':False},
    'K':{'arcs':[None],'supported':False,'output':True},
}

node_dict = rd_node_dict

# Build graph
dag = DAG(node_dict)

# check paths
# for start_node in node_dict.keys():

#     for end_node in node_dict.keys():

#         if graph.pathExists(start_node,end_node):
        
#             print(start_node,end_node,graph.pathExists(start_node,end_node))
        
# Partition graph
dag.partition()

for subgraph in dag.getSubgraphs():

    print(subgraph.getNodes().keys())

# Merge subgraphs
dag.merge()
print(dag.getNodes().keys())
st()
