import unittest
import ast

from dag_node import dagNode

from pdb import set_trace as st

############
# User input
############

# name of node test file
test_file='node1.dat'

################
# End user Input
################

# open node test file
with open('unittests/'+test_file, 'r') as f:

    node_dict = ast.literal_eval(f.read())

# extract node name and attributes
node_name = next(iter(node_dict))
node_attrs = node_dict[node_name]

print('\n########################')
print('Class dagNode Unit Test')
print('Node Name: {node_name}'.format(node_name=node_name))
print('Node Attributes: {node_attrs}'.format(node_attrs=node_attrs))
print('########################\n')

class dagNodeUnitTest(unittest.TestCase):

    """

    Description: Unit test for dagNode class

    Parameters:

    Attributes:

        _test_desc: String describing test

    Methods:

        test_getName(): tests getName
        test_getArcs(): tests getArcs
        test_isSupported(): tests isSupported
        test_isInput(): tests isInput
        test_isOnput(): test isOutput

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
