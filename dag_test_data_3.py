dag_dict = {
    'A':{'arcs':['B'],'supported':True,'input':True,'output':False},
    'B':{'arcs':['C','D','E'],'supported':True,'input':False,'output':False},
    'C':{'arcs':[None],'supported':False,'input':False,'output':False},
    'D':{'arcs':[None],'supported':False,'input':False,'output':False},
    'E':{'arcs':['F'],'supported':False,'input':False,'output':False},
    'F':{'arcs':[None],'supported':True,'input':False,'output':True},
}

pathExists_dict = {

    'AA':False,
    'AB':True,
    'AC':True,
    'AD':True,
    'AE':True,
    'AF':True,

    'BA':False,
    'BB':False,
    'BC':True,
    'BD':True,
    'BE':True,
    'BF':True,

    'CA':False,
    'CB':False,
    'CC':False,
    'CD':False,
    'CE':False,    
    'CF':False,

    'DA':False,
    'DB':False,
    'DC':False,
    'DD':False,
    'DE':False,
    'DF':False,

    'EA':False,
    'EB':False,
    'EC':False,
    'ED':False,
    'EE':False,
    'EF':True,

    'FA':False,
    'FB':False,
    'FC':False,
    'FD':False,
    'FE':False,
    'FF':False,
}

pathExists_supported_dict = {

    'AA':False,
    'AB':True,
    'AC':False,
    'AD':False,
    'AE':False,
    'AF':False,

    'BA':False,
    'BB':False,
    'BC':False,
    'BD':False,
    'BE':False,
    'BF':False,

    'FA':False,
    'FB':False,
    'FC':False,
    'FD':False,
    'FE':False,
    'FF':False,
}

pathExists_unsupported_dict = {

    'CA':False,
    'CB':False,
    'CC':False,
    'CD':False,
    'CE':False,    
    'CF':False,

    'DA':False,
    'DB':False,
    'DC':False,
    'DD':False,
    'DE':False,
    'DF':False,

    'EA':False,
    'EB':False,
    'EC':False,
    'ED':False,
    'EE':False,
    'EF':False,
}

supported_node_connections = [{'A','B'}, {'F'}]
unsupported_node_connections = [{'C'},{'D'},{'E'}]

subgraphs_list = supported_node_connections + unsupported_node_connections
