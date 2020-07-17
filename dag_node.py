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

        name: Unique name of node
        arcs: list of arcs
        supported: Boolean indicating whether node is supported or not
        input: Boolean indicating whether node is input node
        output: Boolean indicating whether node is output node

    Methods:

       getName: Returns name of node
       getArcs: Returns list of arcs
       isSupported: Returns boolean indicateing whether node is supported or not
       isInput: Returns boolean indicateing whether node is input node or not
       isOnput: Returns boolean indicateing whether node is output node or not

       setName: Sest name of node
       setArcs: Sets list of arcs
       setSupported: Sets boolean indicateing whether node is supported or not
       setInput: Sets boolean indicateing whether node is input node or not
       setOnput: Sets boolean indicateing whether node is output node or not

    """

    def __init__(self,
                 name=None,
                 arcs=None,
                 supported=True,
                 input=False,
                 output=False):

        assert name is not None
        
        self.name = name
        self.arcs = arcs
        self.supported = supported
        self.input = input
        self.output = output

    #############
    # Get Methods
    #############
    
    def getName(self):

        return self.name

    def getArcs(self):

        return self.arcs

    def isSupported(self):

        return self.supported
    
    def isInput(self):

        return self.input

    def isOutput(self):

        return self.output

    #############
    # Set Methods
    #############
    
    def setName(self,name=None):

        assert name is not None
        
        self.name = name

    def setArcs(self,arcs=None):

        assert arcs is not None
        assert isinstance(arcs,list)
        
        self.arcs = arcs

    def setSupported(self,supported=None):

        assert isinstance(supported,bool)
        
        self.supported = supported
    
    def setInput(self,input=None):

        assert isinstance(input,bool)
        
        self.input = input

    def setOutput(self,output=None):

        assert isinstance(output,bool)
                
        self.output = output
