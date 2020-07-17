from dag_node import dagNode
import itertools
from pdb import set_trace as st

class DAG():

    """

    Description:

        Directed acyclical graph class

    Parameters:

        node_data: Dictionary whose keys are the names of the nodes in the DAG and values are each node's parameters as follows:
              
              arcs: list of nodes connect via arcs
              supported: boolean indicating whether node is supported
              input: boolean indicating whether node is an input node
              output: boolean indicating whether node is an output node

    Attributes:

        nodes: Dictionary of node objects
        subgraphs: list of partitioned subgraphs.  Each element in the list is itself an instance of a DAG object
        partitioned: Boolean indicate whether graph is in partitioned state or not

    Methods:

        getNodes: Returns dictionary of node objects
        getSubgraphs: Returns list of subgraphs
        isPartitioned: Returns Boolean indicating whether graph is partitioned or not

        setNode: Adds node to nodes dictionary
        setSubgraphs: Add subgraphs manually

        partition: Generate list of subgraphs partitioned into entirely supported or unsupported nodes
        merge: Merge subgraphs into single graph

        pathExists: Determine if path exists between two nodes
        nodeConnections: Group supported or unsupported nodes by subgraphs

    """

    def __init__(self,
                 node_data=None):

        self.nodes = dict()
        self.subgraphs = list()
        self.partitioned = False
        
        # populate nodes if node_data is not None
        # Otherwise, nodes can be added directly via setNode() method
        try:

            for node_name, node_attrs in node_data.items():
            
                self.nodes[node_name] = dagNode(name=node_name,**node_attrs)

        except:

            pass
    
    def getNodes(self):

        return self.nodes

    def getSubgraphs(self):

        return self.subgraphs

    def isPartitioned(self):

        return self.partitioned

    def setNode(self,node):

        assert node is not None

        self.nodes[node.getName()] = node

    def setSubgraphs(self,subgraphs=None):

        assert subgraphs is not None
        assert isinstance(subgraphs,list)

        for subgraph in subgraphs:

            assert isinstance(subgraph,DAG)

        self.subgraphs = subgraphs
        
    def partition(self):

        """
        Partition graph into subgraphs with only entirely supported or unsupported nodes in each subgraph
        """
        
        assert self.partitioned is not True
        
        # separate supported and unsupported nodes
        supported_nodes = dict()
        unsupported_nodes = dict()

        for node_name, node in self.nodes.items():

            if node.isSupported():

                supported_nodes[node_name] = node

            else:

                unsupported_nodes[node_name] = node

        # list of sets where elemetns of each set belong to a unique subgraph
        subgraph_sets = self.nodeConnections(supported_nodes,unsupported_nodes) + \
                        self.nodeConnections(unsupported_nodes,supported_nodes)

        # loop over subgraph sets
        for subgraph in subgraph_sets:

            # create new subgraph
            self.subgraphs.append(DAG())

            # for each node in subgraph pop node object from nodes dictionary and add to subgraph
            # this ensures nodes dictionary is empty if it has been partitioned
            for node in subgraph:

                self.subgraphs[-1].setNode(self.nodes.pop(node))

        # set partitioned state to true
        self.partitioned = True
    
    def merge(self):

        """
        Assemble subgraphs back into a single graph
        """
        
        assert self.partitioned is not False

        # loop over subgraphs, adding each to nodes and removing from subgraph
        for subgraph in self.subgraphs:

            for node_name, node in subgraph.getNodes().items():

                self.nodes[node_name] = node

        # set partitioned state to false
        self.partitioned = False

        # reset subgraphs
        self.subgraphs = list()
        
    def pathExists(self,start_node_name=None,end_node_name=None,dead_arcs=[]):

        """
        Determine is a path exists between two nodes in the graph.  Optionally, this can be conditioned upon not encountering a node in dead_arcs, a list of node names.

        start_node: staring node name
        end_node: ending node name
        dead_arcs: if path from start node to end node passes through element in this list return False
        """

        # path from a node to itself is defined as False
        if start_node_name == end_node_name:

            return False

        # if reached a leaf in tree or output
        if start_node_name is None:

            return False

        # if end node is in arcs of current start node and end node is not in dead_arcs True
        if end_node_name in self.nodes[start_node_name].getArcs():

            if end_node_name not in dead_arcs:
            
                return True

            else:

                return False

        # if end node is not in start node's arc recursively search over arc nodes
        for node in self.nodes[start_node_name].getArcs():

            if node in dead_arcs:

                return False

            if self.pathExists(node, end_node_name, dead_arcs):

                return True
            
        return False
    
    def nodeConnections(self,nodes,dead_arcs):

        """
        Returns names of all nodes that are part of the same subgraph.
        That is, all nodes of the same type (supported/unsupported) which can be reached without crossing through a node of the opposite type (unsupported/supported)
        """
        
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

                
