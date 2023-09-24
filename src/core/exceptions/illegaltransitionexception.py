class IllegalTransitionException(Exception):

    def __init__(self, transitionHistory):
        self.transitionHistory = transitionHistory
        
    def __str__(self):
        message = f"TRANSITION FAILURE: {str(self.transitionHistory[len(self.transitionHistory)-1])} is not enabled in current state\n\nTransition History:\n"
        count = 1
        for transition in self.transitionHistory:
            message += str(count) + ": " + str(transition) + "\n"
            count += 1
        return message