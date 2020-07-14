from node import Node

from pdb import set_trace as st

class DAG():

    """

    Description:

        Directed acyclical graph class

    Parameters:

        arcs: Dictionary containing node names as keys and dictionary as keys, which contains:
              (a) list of nodes connect via arcs as values
              (b) supported or unsupported boolean
        inputNode: Name of input node
        outputNode: Name of output node

    Attributes:

        # arcs: Dictionary containing node names as keys and list of nodes connect via arcs as values
        _nodes: Dictionary of node objects
        _inputNode: Name of input node
        _outputNode: Name of output node

    Methods:

        getArcs : Returns dictionary of nodes and arc relations
        getNodes: Returns list of node objects
        getInputNode: Returns input node name
        getOutputNode: Returns output node name
        pathExists(start_node,end_node): Determine if path exists between two nodes
        partitionGraph(): Generate list of subgraphs partitioned into entirely supported or unsupported nodes

    """

    def __init__(self,
                 node_data=None,
                 inputNode=None,
                 outputNode=None):

        #assert arcs is not None
        assert node_data is not None
        assert inputNode is not None
        assert outputNode is not None

        #self._arcs = arcs
        self._inputNode = inputNode
        self._outputNode = outputNode

        self._nodes = dict()
        
        # populate nodes list
        for node_name, node_attrs in node_data.items():
            
            # self._nodes.append(Node(name=node_name,
            #                         supported=self._arcs[node_name]['supported']))
            self._nodes[node_name] = Node(name=node_name,
                                          arcs=node_attrs['arcs'],
                                          supported=node_attrs['supported'])

    def getArcs(self):

        #return self._arcs
        pass
        
    def getNodes(self):

        return self._nodes

    def getInputNode(self):

        return self._inputNode

    def getOutputNode(self):

        return self._outputNode
    
    def pathExists(self,start_node=None,end_node=None):

        """
        Note: start_node==end_node returns False
        """
        
        #if end_node in self._arcs[start_node]
        if end_node in self._nodes[start_node].getArcs():

            path_exists = True
            
        else:

            #for node in self._arcs[start_node]:
            for node in self._nodes[start_node].getArcs():
            
                if node == None:

                    path_exists = False
                
                else:
                
                    path_exists = self.pathExists(node,end_node)

        return path_exists

    # def partitionGraph(self):

    #     # separate supported and unsupported nodes
    #     supported_nodes = list()

    #     for node in self.getNodes():

    #         supported_nodes.append(node.getName())

    #     # find connections between supported nodes
    #     for start_node in supported_nodes:

    #         for end_node in supported_nodes:

    #             print(start_node,end_node,self.pathExists(start_node,end_node))
