class IllegalTransitionException(Exception):

    def __init__(self, transitionHistory):
        self.transitionHistory = transitionHistory
        
    def __str__(self):
        failedTransition, itemFailedTransition = self.transitionHistory[len(self.transitionHistory)-1]
        message = f"\nTRANSITION FAILURE: send {str(failedTransition.getType())}({str(itemFailedTransition)}) from {str(failedTransition.getSender())} to {str(failedTransition.getReceiver())} is not enabled in current state!\n"
        count = 1
        for transition, item in self.transitionHistory:
            message += f"{str(count)}: send {str(transition.getType())}({str(item)}) from {str(transition.getSender())} to {str(transition.getReceiver())}\n"
            count += 1
        return message