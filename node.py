class Node():

    """

    Description:

        Class representing node in a graph

    Parameters:

        name: Unique name of node
        arcs: list of arcs
        supported: Boolean indicating whether node is supported or not

    Attributes:

        _name: Unique name of node
        _arcs: list of arcs
        _supported: Boolean indicating whether node is supported or not

    Methods:

       getName: Returns name
       getArcs: Returns list of arcs
       isSupported: Returns boolean indicateing whether node is supported or not

    """

    def __init__(self,
                 name=None,
                 arcs=None,
                 supported=True):

        assert name is not None
        
        self._name = name
        self._arcs = arcs
        self._supported = supported

    def getName(self):

        return self._name

    def getArcs(self):

        return self._arcs

    def isSupported(self):

        return self._supported
