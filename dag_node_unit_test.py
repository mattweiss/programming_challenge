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

    """

    def test_getName(self):

        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.getName(),node_name)

    def test_getArcs(self):

        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.getArcs(),node_attrs['arcs'])

    def test_isSupported(self):

        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.isSupported(),node_attrs['supported'])    

    def test_isInput(self):

        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.isInput(),node_attrs['input'])

    def test_isOutput(self):

        dag_node = dagNode(node_name,**node_attrs)

        self.assertEqual(dag_node.isOutput(),node_attrs['output'])  

if __name__ == '__main__':

    unittest.main()
