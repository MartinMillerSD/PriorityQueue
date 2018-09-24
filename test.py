"""
Use strategy pattern to encapsulate a family of algorithms,
and let the algorithms vary independently from clients that
use it.
"""
from abc import ABCMeta
from abc import abstractmethod


class Context:
    """
    Context interface to a strategy object
    """
    
    def __init__(self, strategy):
        self._strategy = strategy
    
    def do_something(self):
        self._strategy.do_something()


class AbstractStrategy(metaclass=ABCMeta):
    """
    Strategy interface to a concrete strategy.
    """
    
    @abstractmethod
    def do_something(self):
        pass


class ConcreteStrategyA(AbstractStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def do_something(self):
        print("do something using A strategy.")


class ConcreteStrategyB(AbstractStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def do_something(self):
        print("do something using B strategy.")


if __name__ == "__main__":
    # A
    a_strategy = ConcreteStrategyA()
    context = Context(a_strategy)
    context.do_something()
    # B
    b_strategy = ConcreteStrategyB()
    context = Context(b_strategy)
    context.do_something()