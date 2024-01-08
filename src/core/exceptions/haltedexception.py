from src.core.exceptions.sycococopyexception import SycococopyException

'''
HaltedException is used to prevent further transitions when an IllegalTransitionException
has been raised previously.
'''

class HaltedException(Exception):
    pass