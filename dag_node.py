class dagNode():

    """

    Description:

        Class representing node in a directed acyclical graph

    Parameters:

        name: Unique name of node
        arcs: list of arcs
        supported: Boolean indicating whether node is supported or not
        input: Boolean indicating whether node is input node
        output: Boolean indicating whether node is output node

    Attributes:

        _name: Unique name of node
        _arcs: list of arcs
        _supported: Boolean indicating whether node is supported or not
        _input: Boolean indicating whether node is input node
        _output: Boolean indicating whether node is output node

    Methods:

       getName: Returns name
       getArcs: Returns list of arcs
       isSupported: Returns boolean indicateing whether node is supported or not
       isInput: Returns boolean indicateing whether node is input node or not
       isOnput: Returns boolean indicateing whether node is output node or not

    """

    def __init__(self,
                 name=None,
                 arcs=None,
                 supported=True,
                 input=False,
                 output=False):

        assert name is not None
        
        self._name = name
        self._arcs = arcs
        self._supported = supported
        self._input = input
        self._output = output

    def getName(self):

        return self._name

    def getArcs(self):

        return self._arcs

    def isSupported(self):

        return self._supported
    
    def isInput(self):

        return self._input

    def isOutput(self):

        return self._output
