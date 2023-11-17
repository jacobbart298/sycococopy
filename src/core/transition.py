class Transition:

    def __init__(self, type, sender, receiver):
        self.type = type
        self.sender = sender
        self.receiver = receiver

    def satisfies(self, other):
        return self.type == other.type and self.sender == other.sender and self.receiver == other.receiver

    def getSender(self):
        return self.sender
    
    def getReceiver(self):
        return self.receiver
    
    def getType(self):
        return self.type
    
    def isValid(self, value):
        return True

    def __eq__(self, other):
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver 

    def __hash__(self):
        return hash(self.type) + hash(self.sender) + hash(self.receiver)
    
    def __str__(self):
        return "send " + str(self.type) + " from " + str(self.sender) + " to " + str(self.receiver) 
    

class PredicateTransition(Transition):

    def __init__(self, type, sender, receiver, operator=None, value=None):
        super().__init__(type, sender, receiver)
        self.operator = operator
        self.value = value

    def __str__(self):
        return "send " + str(self.type) + "(" + str(self.operator) + str(self.value) + ") from " + str(self.sender) + " to " + str(self.receiver)

    def getComparator(self):
        return self.operator
    
    def getValue(self):
        return self.value

    def isValid(self, value):
        match self.operator:
            case '<':
                return value < self.value
            case '<=':
                return value <= self.value
            case '>':
                return value > self.value
            case '>=':
                return value >= self.value
            case '!=':
                return value != self.value
            case '==':
                return value == self.value

    def __eq__(self, other):
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver and self.operator == other.comparator and self.value == other.value

    def __hash__(self):
        return hash(self.type) + hash(self.sender) + hash(self.receiver) + hash(self.operator) + hash(self.value)
    
    