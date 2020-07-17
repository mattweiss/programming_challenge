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

my_node_dict = {
    'A':{'arcs':['B'],'supported':True},
    'B':{'arcs':['C'],'supported':False},
    'C':{'arcs':['D'],'supported':False},
    'D':{'arcs':[None],'supported':True},
    # 'E':{'arcs':[None],'supported':True},
}

node_dict = lt_node_dict

# Build graph
dag = DAG(node_dict)

# check paths
for start_node in node_dict.keys():

    for end_node in node_dict.keys():

        print(start_node,end_node,dag.pathExists(start_node,end_node))

# start_node = 'A'
# end_node = 'K'
# print(start_node,end_node,dag.pathExists(start_node,end_node))
