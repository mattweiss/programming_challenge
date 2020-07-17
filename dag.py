from dag_node import dagNode
import itertools
from pdb import set_trace as st

class DAG():

    """

    Description:

        Directed acyclical graph class

    Parameters:

        node_data: Dictionary containing node names as keys and dictionary as values, which contains the following keys:
              arcs: list of nodes connect via arcs
              supported: boolean indicating whether node is supported
              input: boolean indicating whether node is an input node (optional)
              supported: boolean indicating whether node is an output node (optional)

    Attributes:

        nodes: Dictionary of node objects
        subgraphs: list of partitioned subgraphs
        partitioned: Boolean indicate whether graph is in partitioned state or not

    Methods:

        getNodes: Returns dictionary of node objects
        getSubgraphs: Returns list of subgraphs
        isPartitioned: Returns Boolean indicating whether graph is partitioned or not
        setNode: Adds node to _nodes dictionary
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
        
        # populate self._nodes if node_data is not None
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

        subgraph_sets = self.nodeConnections(supported_nodes,unsupported_nodes) + \
                        self.nodeConnections(unsupported_nodes,supported_nodes)

        # build partitions
        for subgraph in subgraph_sets:

            # create new subgraph
            self.subgraphs.append(DAG())

            # for each node pop node object from nodes and add to subgraph
            # This ensures object's nodes list is empty if it has been partitioned
            for node in subgraph:

                self.subgraphs[-1].setNode(self.nodes.pop(node))

        # set partitioned state to true
        self.partitioned = True
    
    def merge(self):

        """
        Assemble subgraphs back into a single graph
        """
        
        assert self.partitioned is not False

        # loop over subgraphs, adding each to _nodes and removing from subgraph
        for subgraph in self.subgraphs:

            for node_name, node in subgraph.getNodes().items():

                self.nodes[node_name] = node

        # set partitioned state to false
        self.partitioned = False

        # reset _subgraphs
        self.subgraphs = list()
        
    def pathExists(self,start_node_name=None,end_node_name=None,dead_arcs=[]):

        """
        Determine is a path exists between two nodes in the graph.  Optionally, this can be conditioned upon not encountering an unsupported node if start node is supported and vice-versa.

        start_node: staring node name
        end_node: ending node name
        dead_arcs: if path from start node to end node passes through element in this list return False
        """

        # check if start node is directly connected to end node
        # if end_node_name in self.nodes[start_node_name].getArcs():

        #     return True
            
        # # otherwise, recursively search through graph
        # else:

        #     for node in self.nodes[start_node_name].getArcs():

        #         if node is None:

        #             continue
                
        #         return self.pathExists(node,end_node_name)

        # path = list()

        # path = path + [start_node_name]

        # if start_node_name == end_node_name:

        #     return path

        # if start_node_name is None:

        #     return None
        
        # for node in self.nodes[start_node_name].getArcs():

        #     newpath = self.pathExists(node, end_node_name)

        #     if newpath: return newpath

        # return None

        if start_node_name == end_node_name:

            return False

        if start_node_name is None:

            return False

        if end_node_name in self.nodes[start_node_name].getArcs():

            if end_node_name not in dead_arcs:
            
                return True

            else:

                return False
            
        for node in self.nodes[start_node_name].getArcs():

            if node in dead_arcs:

                return False
            
            newpath = self.pathExists(node, end_node_name, dead_arcs)

            if newpath: return newpath

        return False
    
    def nodeConnections(self,nodes,dead_arcs):

        """
        Returns names all nodes that are part of the same subgraph.
        That is, all nodes of the same type (supported or unsupported) which can be reached without crossing through a node of the opposite type (unsupported or supported)
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

                
