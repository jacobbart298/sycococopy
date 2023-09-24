
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

    def __eq__(self, other):
        return self.type == other.type and self.sender == other.sender and self.receiver == other.receiver 

    def __hash__(self):
        return hash(self.type) + hash(self.sender) + hash(self.receiver)
    
    def __str__(self):
        return "send " + str(self.type) + " from " + str(self.sender) + " to " + str(self.receiver) 