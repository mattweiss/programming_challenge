from node import Node
import itertools
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

        _nodes: Dictionary of node objects
        _inputNode: Name of input node
        _outputNode: Name of output node
        _subgraphs: list of partitioned subgraphs

    Methods:

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

        assert node_data is not None
        assert inputNode is not None
        assert outputNode is not None

        self._inputNode = inputNode
        self._outputNode = outputNode

        self._nodes = dict()
        
        # populate nodes list
        for node_name, node_attrs in node_data.items():
            
            self._nodes[node_name] = Node(name=node_name,
                                          arcs=node_attrs['arcs'],
                                          supported=node_attrs['supported'])
        
    def getNodes(self):

        return self._nodes

    def getInputNode(self):

        return self._inputNode

    def getOutputNode(self):

        return self._outputNode
    
    def pathExists(self,start_node=None,end_node=None,dead_arcs=[]):

        """
        Note: start_node==end_node returns False
        """
        
        if end_node in self._nodes[start_node].getArcs():

            path_exists = True
            
        else:

            for node in self._nodes[start_node].getArcs():

                if node == None or node in dead_arcs:

                    path_exists = False
                
                else:
                
                    path_exists = self.pathExists(node,end_node)

        return path_exists

    def partitionGraph(self):

        # separate supported and unsupported nodes
        supported_nodes = dict()
        unsupported_nodes = dict()

        for node_name, node in self._nodes.items():

            if node.isSupported():

                supported_nodes[node_name] = node

            else:

                unsupported_nodes[node_name] = node

        supported_sets = self.nodeConnections(supported_nodes,unsupported_nodes)
        unsupported_sets = self.nodeConnections(unsupported_nodes,supported_nodes)
                
        return node_set_list


    def nodeConnections(self,nodes,dead_arcs):

        node_set_list = list()
        
        # find connections between supported nodes
        for start_node in nodes.keys():

            node_set = set(start_node)
            
            for end_node in nodes.keys():

                if self.pathExists(start_node,end_node,dead_arcs.keys()):

                    node_set.update(end_node)

            node_set_list.append(node_set)

        # merge supported node sets
        for s1, s2 in itertools.combinations(node_set_list, 2):

            if s1.intersection(s2):

                s1.update(s2)

                try:

                    node_set_list.remove(s2)

                except:

                    pass

        return node_set_list

                
