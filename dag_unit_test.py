import unittest
import ast

from dag import DAG
from dag_node import dagNode

from pdb import set_trace as st

############
# User input
############

# dictionaries used for testing
from dag_test_data_3 import dag_dict, pathExists_dict, pathExists_supported_dict, pathExists_unsupported_dict, supported_node_connections, unsupported_node_connections, subgraphs_list

################
# End user Input
################

print('\n########################')
print('Class DAG Unit Test')
print('########################\n')

class dagUnitTest(unittest.TestCase):

    """

    Description: Unit test for dagNode class

    Parameters:

    Attributes:

    Methods:

        test_getNodes
        test_setNode
        test_pathExists
        test_isPartitioned
        test_nodeConnections
        test_partition
        test_merge

        nodeAttrsCompare: Compares dagNode object's attributes with truth provided by dictionary
        separateNodes: return two dictionaries containing all supported and all unsupported nodes respectively
        dagNodesEqual: determines if two dagNode objects have same values for all attributes

    """

    def test_getNodes(self):

        # DAG object initialized by test dictionary
        dag = DAG(dag_dict)

        # check each dagNode object in DAG object
        # if the returned nodes match those in the test dicitionary getNodes is returning the correct nodes
        self.nodeAttrsCompare(dag,dag_dict)
        
    def test_setNode(self):

        # DAG object initialized with no nodes
        dag = DAG()

        # add first node from test dictionary
        node_name = list(dag_dict.keys())[0]
        node_attrs = dag_dict[node_name]
        dag_node = dagNode(node_name,**node_attrs)
        dag.setNode(dag_node)

        # check each dagNode object in DAG object
        # if the returned nodes match those in the test dicitionary getNodes is returning the correct nodes
        self.nodeAttrsCompare(dag,dag_dict)

    def test_pathExists(self):
        
        # DAG object initialized by test dictionary
        dag = DAG(dag_dict)

        # loop over each pair of nodes and check if path exists between them regardless of being supported or unsupported
        for start_node_name,start_node_attrs in dag.getNodes().items():

            for end_node_name,end_node_attrs in dag.getNodes().items():

                self.assertEqual(dag.pathExists(start_node_name,end_node_name),pathExists_dict[str(start_node_name+end_node_name)])
                    
        # dictionaries holding supported and unsupported nodes
        supported_nodes, unsupported_nodes = self.separateNodes(dag)

        # loop over each pair of supported nodes and check if path exists between them without crossing unsupported node
        for start_node_name,start_node_attrs in supported_nodes.items():

            for end_node_name,end_node_attrs in supported_nodes.items():

                self.assertEqual(dag.pathExists(start_node_name,end_node_name,unsupported_nodes.keys()),pathExists_supported_dict[str(start_node_name+end_node_name)])
                    
        # loop over each pair of unsupported nodes and check if path exists between them without crossing supported node
        for start_node_name,start_node_attrs in unsupported_nodes.items():

            for end_node_name,end_node_attrs in unsupported_nodes.items():

                self.assertEqual(dag.pathExists(start_node_name,end_node_name,supported_nodes.keys()),pathExists_unsupported_dict[str(start_node_name+end_node_name)])
                
    def test_isPartitioned(self):
        
        # DAG object initialized by test dictionary
        dag = DAG(dag_dict)

        # test initilization of self.partitioned to False
        self.assertFalse(dag.isPartitioned())

    def test_nodeConnections(self):

        # DAG object initialized by test dictionary
        dag = DAG(dag_dict)

        # dictionaries holding supported and unsupported nodes
        supported_nodes, unsupported_nodes = self.separateNodes(dag)

        # check sets of connected nodes among supported and unsupported nodes
        self.assertEqual(dag.nodeConnections(supported_nodes,unsupported_nodes),supported_node_connections)
        self.assertEqual(dag.nodeConnections(unsupported_nodes,supported_nodes),unsupported_node_connections)

    def test_partition(self):
        
        # Two identical DAG objects initialized by test dictionary
        dag1 = DAG(dag_dict)
        dag2 = DAG(dag_dict)
        
        # partition
        dag1.partition()

        # test isPartitioned is True
        self.assertTrue(dag1.isPartitioned())

        # test isPartitioned is working correctly
        self.assertEqual(dag1.partitioned,dag1.isPartitioned())

        # If correctly partitioned, keys in each partitioned subgraph should match those in subgraphs_list
        # Each time a correct match is make between the names of nodes in a subgraph and an element of subgraphs_list
        # that element is removed from subgraphs_list
        for subgraph in dag1.subgraphs:

            subgraph_name_set = set(subgraph.getNodes().keys())

            if subgraph_name_set in subgraphs_list:

                subgraphs_list.remove(subgraph_name_set)

                for subgraph_name in subgraph_name_set:

                    # ensure key,value pairs in subgraphs in dag1 match those in dag2
                    # this is to ensure the key,value pairs were not mixed up during partition
                    self.dagNodesEqual(subgraph.getNodes()[subgraph_name],dag2.getNodes()[subgraph_name])
                    
        #self.assertEqual(subgraphs_list,[])

    def test_getSubgraphs(self):
        
        # DAG object initialized by test dictionary
        dag = DAG(dag_dict)

        # partition
        dag.partition()

        # getSubgraphs is working correcctly
        self.assertEqual(dag.getSubgraphs(),dag.subgraphs)

    def test_merge(self):
        
        # Two identical DAG objects initialized by test dictionary
        dag1 = DAG(dag_dict)
        dag2 = DAG(dag_dict)
        
        # partition
        dag1.partition()
        
        # merge
        dag1.merge()

        # isPartitioned is False
        self.assertFalse(dag1.isPartitioned())
        
        # isPartitioned is working correctly
        self.assertEqual(dag1.partitioned,dag1.isPartitioned())
        
        # subgraphs is empty list
        self.assertEqual(dag1.subgraphs,[])

        # if merger was correct done dag1 and dag2 should have equal node-by-node comparision
        for node_name in dag1.getNodes().keys():

            self.dagNodesEqual(dag1.getNodes()[node_name],dag2.getNodes()[node_name])

    def nodeAttrsCompare(self,dagObj,test_dict):

        # check each dagNode object in DAG object
        # if the returned nodes match those in the test dicitionary getNodes is returning the correct nodes
        for node_name, node_obj in dagObj.getNodes().items():

            # check attributes of each node with truth
            self.assertEqual(node_obj.getArcs(),test_dict[node_name]['arcs'])
            self.assertEqual(node_obj.isSupported(),test_dict[node_name]['supported'])
            self.assertEqual(node_obj.isInput(),test_dict[node_name]['input'])
            self.assertEqual(node_obj.isOutput(),test_dict[node_name]['output'])

    def separateNodes(self,dagObj):
        
        # dictionaries holding supported and unsupported nodes
        supported_nodes = dict()
        unsupported_nodes = dict()

        for node_name,node in dagObj.getNodes().items():

            if node.isSupported():

                supported_nodes[node_name] = node

            else:

                unsupported_nodes[node_name] = node


        return supported_nodes, unsupported_nodes

    def dagNodesEqual(self,node1,node2):

        self.assertEqual(node1.getArcs(),node2.getArcs())
        self.assertEqual(node1.isSupported(),node2.isSupported())
        self.assertEqual(node1.isInput(),node2.isInput())
        self.assertEqual(node1.isOutput(),node2.isOutput())
                                 
if __name__ == '__main__':

    unittest.main()
