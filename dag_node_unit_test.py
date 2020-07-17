import unittest
import ast

from dag_node import dagNode

from pdb import set_trace as st

############
# User input
############

# dictionaries used for testing
from dag_node_test_data_1 import node_dict

################
# End user Input
################

node_name = list(node_dict.keys())[0]
node_attrs = node_dict[node_name]

print('\n########################')
print('Class dagNode Unit Test')
print('########################\n')

class dagNodeUnitTest(unittest.TestCase):

    """

    Description: Unit test for dagNode class

    Parameters:

    Attributes:

        _test_desc: String describing test

    Methods:

        test_getName
        test_getArcs
        test_isSupported
        test_isInput
        test_isOnput
        test_setName
        test_setArcs
        test_setSupported
        test_setInput
        test_setOnput

    """

    def test_getName(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.getName(),node_name)

    def test_getArcs(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.getArcs(),node_attrs['arcs'])

    def test_isSupported(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.isSupported(),node_attrs['supported'])    

    def test_isInput(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.isInput(),node_attrs['input'])

    def test_isOutput(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.isOutput(),node_attrs['output'])  

    def test_setName(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        # test name
        test_name = 'Unit Test Node Name'
        
        # set name
        dag_node.setName(test_name)
        
        self.assertEqual(dag_node.name,test_name)
    
    def test_setArcs(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        # test arcs
        test_arcs = ['A',2,'X','%']
        
        # set arcs
        dag_node.setArcs(test_arcs)
        
        self.assertEqual(dag_node.arcs,test_arcs)
    
    def test_setSupported(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        # set True
        dag_node.setSupported(True)
        self.assertTrue(dag_node.supported)

        # set False
        dag_node.setSupported(False)
        self.assertFalse(dag_node.supported)

    def test_setInput(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        # set True
        dag_node.setInput(True)
        self.assertTrue(dag_node.input)

        # set False
        dag_node.setInput(False)
        self.assertFalse(dag_node.input)


    def test_setOutput(self):

        # create dagNode object from loaded node_dict
        dag_node = dagNode(node_name,**node_attrs)

        # set True
        dag_node.setOutput(True)
        self.assertTrue(dag_node.output)

        # set False
        dag_node.setOutput(False)
        self.assertFalse(dag_node.output)
        
if __name__ == '__main__':

    unittest.main()
