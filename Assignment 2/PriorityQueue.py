
#Author: Martin Miller
#redID: 817405999
#Professor: Whitney
#Class: CS 635 Advanced Object Oriented Design
#Description: The class below inputs students into a priority queue with O(log n) complexity.
#file: PriorityQueue.py
#Date: September 5th, 2018

import math
import copy

class Strategy( object ):
    def __init__( self, aStrategicAlternative ):
        self.currentStrategy = ConcreteStrategyOne()
        self.max_GPA = 4.0
        self.max_units_taken = 150.0
    def calculate_rank( self, comparable_object ):
        if (0.0 <= comparable_object.GPA <= self.max_GPA and 0.0 <= comparable_object.units_taken <= self.max_units_taken) == True:
            return self.currentStrategy.calculate_rank( self, comparable_object)
        else:
            raise ValueError

    def changeStrategy(self, newStrategy):
        self.currentStrategy = newStrategy

class ConcreteStrategyOne():
    def calculate_rank( self, Strategy ,comparable_object):
        return ((comparable_object.GPA/Strategy.max_GPA)*.3 + (comparable_object.units_taken/Strategy.max_units_taken)*.7)

class ConcreteStrategyTwo():
    def calculate_rank( self, Strategy, comparable_object ):
        return (comparable_object.GPA/Strategy.max_GPA)*1.0

class ConcreteStrategyThree():
    def calculate_rank( self, Strategy, comparable_object ):
        return (comparable_object.units_taken/Strategy.max_units_taken)*1.0

class PriorityQueue(Strategy):

    def __init__(self, queue = []):
        self.queue = []
        super().__init__(self)
        return

    def add_to_list(self, object):
        self.heappush(object)
        return self.queue

    def heappush(self, insert):
        insert.rank = self.calculate_rank(insert)
        self.queue.append(insert) 
        def heapify(self,end_index):

            parent_index = int(math.ceil(end_index/2-1))
            end_index = end_index

            if parent_index == -1:
                return
            if self.queue[parent_index].rank <= self.queue[end_index].rank:
                self.queue[parent_index], self.queue[end_index] = self.queue[end_index], self.queue[parent_index]

            heapify(self,parent_index)

        end_index = int(len(self.queue)-1)    
        heapify(self,end_index)
        
    def show_name(self):
        for x in self.queue:
            print(x.name)

    def show_name_rank(self):
        for x in self.queue:
            print("Name: " + str(x.name.ljust(20)) + "\t\tRank: " + str(x.rank))

    def remove_from_queue(self):
        
        if not self.queue:
            return

        index = 0
        end_index = int(len(self.queue)-1)
        self.queue[0], self.queue[end_index] = self.queue[end_index], self.queue[0]
        self.heap_down(index)
        return self.queue.pop()

    def heap_down(self,index):
        end_index = int(len(self.queue)-1)
        if index == end_index:
            #print("first return")
            return

        if index + 1 == end_index:
            if self.queue[index].rank > self.queue[end_index].rank:
                self.queue[index], self.queue[end_index] = self.queue[end_index], self.queue[index]
                self.heap_down(index+1)

        if index +2 <= end_index:
            if self.queue[index+1].rank > self.queue[index+2].rank:
                self.queue[index], self.queue[index+1] = self.queue[index+1], self.queue[index]
                self.heap_down(index+1)
            else:
                self.queue[index], self.queue[index+2] = self.queue[index+2], self.queue[index]
                self.heap_down(index+2)

    def highest_priority(self):
        if self.queue:
            return self.queue[0]

    def pop(self):
        self.queue.pop()

    def __str__(self):
        return  list(map(lambda x: (x.redID,x.name), self.queue))

class Student():

    def __init__(self, name, redID, email, address, GPA, units_taken):
        self.name = name
        self.redID = redID
        self.email = email
        self.address = address
        self.GPA = GPA
        self.units_taken = units_taken
        self.rank = 0

class Iterator(PriorityQueue):

    def __init__(self, iterator_list):
        super().__init__(self)
        self.n = -1
        self.iterator_list = iterator_list
        return

    def __next__(self):
        self.n = self.n + 1
        return self.iterator_list.queue[self.n].name

class Command:

    def __init__(self, object):
        self.object = object

class CutCommand(Command):
    def __init__(self, object, n = 0):
        super().__init__(object)
        self.n = n
        self.cut_command_stack = []
        self.number_removed = []

    def execute(self):
        self.number_removed.append(self.n)
        for x in range(self.n):
            self.cut_command_stack.append(self.object.remove_from_queue())

    def undo(self):
        print(len(self.cut_command_stack))
        for x in range(self.number_removed.pop()):
            self.object.add_to_list(self.cut_command_stack.pop())

class AddCommand(Command):
    def __init__(self, object, student_list):
        super().__init__(object)
        self.student_list = student_list
        self.number_added = []

    def execute(self):
        self.number_added.append(len(self.student_list))
        for x in range(0,len(self.student_list)):
            self.object.add_to_list(self.student_list.pop())

    def undo(self):
        for x in range(0,self.number_added.pop()):
            self.object.pop()

class Invoker:
    def __init__(self):
        self.history = []

    def store_and_execute(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()


List  = PriorityQueue()
List.remove_from_queue()
List.changeStrategy(ConcreteStrategyTwo())
aStudent = Student("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
List.add_to_list(aStudent)
aStudent = Student("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
List.add_to_list(aStudent)
print(List.__str__())
'''
#ptest = PriorityQueue()

#https://www.youtube.com/watch?v=Fc1fLEk_Kr0
#https://www.youtube.com/watch?v=m9KCiLrCErs
#https://www.youtube.com/watch?v=WCm3TqScBM8&t=1s
#List = PriorityQueue()
aStudent = Student("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
List.add_to_list(aStudent)
aStudent = Student("Indie",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0)
List.add_to_list(aStudent)
aStudent = Student("Eric",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0)
List.add_to_list(aStudent)
aStudent = Student("Aaron",123456789, "email@sdsu.edu","123 Fake St",4.0,00.0)
List.add_to_list(aStudent)
aStudent = Student("GaryHigh",123456789, "email@sdsu.edu","123 Fake St",3.9,150.0)
List.add_to_list(aStudent)
aStudent = Student("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
List.add_to_list(aStudent)
List.show_name_rank()

List.add_to_list(aStudent)
aStudent = Student("Geofflow",123456789, "email@sdsu.edu","123 Fake St",0.1,0.0)
List.add_to_list(aStudent)
aStudent = Student("Issac",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
List.add_to_list(aStudent)
aStudent = Student("Frank",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
List.add_to_list(aStudent)
aStudent = Student("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
List.add_to_list(aStudent)

List.show_name_rank()

#List.add_to_list(aStudent)
#List.remove_from_queueN(2)

#List.show_name_redID()
#print("-----------------")
#List.remove_from_queue()
#List.show_name_redID()
#print("------------")

iter  = Iterator(List)
print(iter.__next__())

#print(List)
#for x in List.queue:
#    print(x)
print("-------")
List.show_name()
cut  = CutCommand(List, 5)
client = Invoker()
client.store_and_execute(cut)
print("------------------- removed 5")
List.show_name_rank()



#List.show_name()
cut2  = CutCommand(List, 3)
#client = Invoker()
client.store_and_execute(cut2)
print("------------------- removed 3")
List.show_name_rank()

print("--------------- did undo 3")
client.undo_last()
List.show_name_rank()

print("--------------- did undo 5")
client.undo_last()
List.show_name_rank()

print("-------- added 3 more below --- ")
Student_List = [Student("test1",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0), Student("test2",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0), Student("test3",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)]
add = AddCommand(List, Student_List)
client.store_and_execute(add)
#List.show_name()

Student_List = [Student("test4",123456789, "email@sdsu.edu","123 Fake St",4.0,150.0), Student("test5",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)]
add = AddCommand(List, Student_List)
client.store_and_execute(add)
List.show_name()
List.show_name_rank()

print(" --- undid the add ")
client.undo_last()
List.show_name()

print(" --- undid the add 2")
client.undo_last()
List.show_name()
List.show_name_rank()


aStudent2 = Student("Margin",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
add2  = AddCommand(List, aStudent2)
client.store_and_execute(add2)
print("--------- just added 1 add")
List.show_name()


print("----- add undo")
client.undo_last()
List.show_name()

print("---- what happens")
client.undo_last()
List.show_name()

List = PriorityQueue()


##List.add_to_list("Delta",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
List.add_to_list("Echo",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0) #60
List.add_to_list("Indigo",123456789, "email@sdsu.edu","123 Fake St",3.2,150.0) #256
List.add_to_list("Helo",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0) #210
List.add_to_list("SuperAlpha",123456789, "email@sdsu.edu","123 Fake St",0.8,10.0) #0
List.add_to_list("Gamma",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0) #190
List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0) #48
List.add_to_list("Bravo",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
List.add_to_list("Gamma2",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
List.add_to_list("SuperIndigo",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
List.add_to_list("Fox",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
List.add_to_list("Alpha",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
List.add_to_list("Indigo",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0)
List.add_to_list("Delta2",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
List.add_to_list("Delta3",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
#List.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",40.0,40.0)



List.add_to_list("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
List.add_to_list("Eric",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0)
List.add_to_list("Indie",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0)
List.add_to_list("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
List.add_to_list("Aaron",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0)
List.add_to_list("Gary",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0)
List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
List.add_to_list("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
List.add_to_list("Geoff",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
List.add_to_list("Issac",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
List.add_to_list("Frank",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
List.add_to_list("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
List.add_to_list("Ivan",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0)
List.add_to_list("Derek",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
List.add_to_list("Doug",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
List.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",4.0,150.0)

#a = 5
#b = 5
#This is a work of git
#still not working
#still trying to get a change
#things setup now?


#List.remove()
##List.remove()
##List.remove()
List.show_name_redID()
#print(List.highest_priority())


'''