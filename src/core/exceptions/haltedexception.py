'''
HaltedException is used to prevent further transitions being made when an IllegalTransitionException
has been raised previously, needed because the EventLoop may continue to run briefly 
'''

class HaltedException(Exception):
    pass