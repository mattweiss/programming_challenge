from dag_node import dagNode
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
        _subgraphs: list of partitioned subgraphs
        _partitioned: Boolean indicate whether graph is in partitioned state or not

    Methods:

        getNodes: Returns dictionary of node objects
        getSubgraphs: Returns list of subgraphs
        setNode: Adds node to _nodes dictionary

        isPartitioned: Returns Boolean indicating whether graph is partitioned or not

        pathExists(start_node,end_node): Determine if path exists between two nodes
        
        partition: Generate list of subgraphs partitioned into entirely supported or unsupported nodes
        merge: Merge subgraphs into single graph

        nodeConnections: Group supported or unsupported nodes by subgraphs

    """

    def __init__(self,
                 node_data=None):

        self._nodes = dict()
        self._subgraphs = list()
        self._partitioned = False
        
        # populate nodes list if not node_data is not None
        # Otherwise, nodes can be added directly via method setNode()
        try:

            for node_name, node_attrs in node_data.items():
            
                self._nodes[node_name] = dagNode(name=node_name,**node_attrs)

        except:

            pass
                
    def getNodes(self):

        return self._nodes

    def getSubgraphs(self):

        return self._subgraphs

    def setNode(self,node):

        assert node is not None

        self._nodes[node.getName()] = node

    def isPartitioned(self):

        return self._partitioned
        
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

    def partition(self):

        if self._partitioned is True:

            print('Graph is already partitioned')
            return
        
        # separate supported and unsupported nodes
        supported_nodes = dict()
        unsupported_nodes = dict()

        for node_name, node in self._nodes.items():

            if node.isSupported():

                supported_nodes[node_name] = node

            else:

                unsupported_nodes[node_name] = node

        subgraph_sets = self.nodeConnections(supported_nodes,unsupported_nodes) + \
                        self.nodeConnections(unsupported_nodes,supported_nodes)

        # build partitions
        for subgraph in subgraph_sets:

            # create new subgraph
            self._subgraphs.append(DAG())

            # for each node pop node object from _nodes and add to subgraph
            for node in subgraph:

                self._subgraphs[-1].setNode(self._nodes.pop(node))

        # set partitioned state to true
        self._partitioned = True

    def merge(self):

        if self._partitioned is False:

            print('Graph is not partitioned')
            return

        # loop over subgraphs, adding each to _nodes and removing from subgraph
        for subgraph in self._subgraphs:

            for node_name, node in subgraph.getNodes().items():

                self._nodes[node_name] = node

        # set partitioned state to false
        self._partitioned = False
        
        # reset _subgraphs
        self._subgraphs = list()
                
    def nodeConnections(self,nodes,dead_arcs):

        node_set_list = list()

        # find connections between nodes
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

                
