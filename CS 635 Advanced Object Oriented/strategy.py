import abc  # Python's built-in abstract class library

class QuackStrategyAbstract(object):
    """You do not need to know about metaclasses.
    Just know that this is how you define abstract
    classes in Python."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack(self):
        pass
        #"""Required Method"""

class LoudQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        pass
        print ("QUACK! QUACK!!")

class GentleQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        pass
        print ("quack!")

class LightStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def lights_on(self):
        pass
        #"""Required Method"""

class OnForTenSecondsStrategy(LightStrategyAbstract):
    def lights_on(self):
        print ("Lights on for 10 seconds")

class StudentStrategyAbstract(object):
    """You do not need to know about metaclasses.
    Just know that this is how you define abstract
    classes in Python."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def talk(self):
        print("this is talking")
        pass
        #"""Required Method"""

class walkStrategy(StudentStrategyAbstract):
    def quack(self):
        print("this is walking")