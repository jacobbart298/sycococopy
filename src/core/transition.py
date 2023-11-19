class Transition:

    def __init__(self, type, sender, receiver):
        self.type = type
        self.sender = sender
        self.receiver = receiver

    def getSender(self):
        return self.sender
    
    def getReceiver(self):
        return self.receiver
    
    def getType(self):
        return self.type
    
    def satisfies(self, other, _):
        return self.type == other.type and self.sender == other.sender and self.receiver == other.receiver
    
    def __eq__(self, other):
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver 

    def __hash__(self):
        return hash(self.type) + hash(self.sender) + hash(self.receiver)
    
    def __str__(self):
        return "send " + str(self.type) + " from " + str(self.sender) + " to " + str(self.receiver) 
    

class PredicateTransition(Transition):

    def __init__(self, type, sender, receiver, comparator=None, value=None):
        super().__init__(type, sender, receiver)
        self.comparator = comparator
        self.value = value

    def getComparator(self):
        return self.comparator
    
    def getValue(self):
        return self.value

    def satisfies(self, other, value):        
        isValueValid = False
        match self.comparator:
            case '<':
                isValueValid = value < self.value
            case '<=':
                isValueValid = value <= self.value
            case '>':
                isValueValid = value > self.value
            case '>=':
                isValueValid = value >= self.value
            case '!=':
                isValueValid = value != self.value
            case '==':
                isValueValid = value == self.value
        return super().satisfies(other, value) and isValueValid

    def __eq__(self, other):
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver and self.comparator == other.comparator and self.value == other.value

    def __hash__(self):
        return hash(self.type) + hash(self.sender) + hash(self.receiver) + hash(self.comparator) + hash(self.value)
    
    def __str__(self):
        return "send " + str(self.type) + "(" + str(self.comparator) + str(self.value) + ") from " + str(self.sender) + " to " + str(self.receiver)
