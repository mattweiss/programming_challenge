dag_dict = {
    'A':{'arcs':['B'],'supported':True,'input':True,'output':False},
    'B':{'arcs':['C','D'],'supported':False,'input':False,'output':False},
    'C':{'arcs':['F'],'supported':True,'input':False,'output':False},
    'D':{'arcs':['E'],'supported':False,'input':False,'output':False},
    'E':{'arcs':['F'],'supported':True,'input':False,'output':False},
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
    'CF':True,

    'DA':False,
    'DB':False,
    'DC':False,
    'DD':False,
    'DE':True,
    'DF':True,

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
    'AB':False,
    'AC':False,
    'AD':False,
    'AE':False,
    'AF':False,

    'CA':False,
    'CB':False,
    'CC':False,
    'CD':False,
    'CE':False,    
    'CF':True,

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

pathExists_unsupported_dict = {

    'BA':False,
    'BB':False,
    'BC':False,
    'BD':True,
    'BE':False,
    'BF':False,

    'DA':False,
    'DB':False,
    'DC':False,
    'DD':False,
    'DE':False,
    'DF':False,
    'FF':False,
}

supported_node_connections = [{'A'}, {'C', 'F', 'E'}]
unsupported_node_connections = [{'B','D'}]

subgraphs_list = supported_node_connections + unsupported_node_connections
