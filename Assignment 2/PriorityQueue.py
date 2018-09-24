
#Author: Martin Miller
#redID: 817405999
#Professor: Whitney
#Class: CS 635 Advanced Object Oriented Design
#Description: The class below inputs students into a priority queue with O(log n) complexity.
#file: PriorityQueue.py
#Date: September 5th, 2018

class Strategy( object ):
    def __init__( self, aStrategicAlternative ):
        self.currentStrategy = ConcreteStrategyOne()
        self.max_GPA = 4.0
        self.max_units_taken = 150.0
    def calculate_rank( self, someArg ):
        return self.currentStrategy.calculate_rank( self, someArg)
    def changeStrategy(self, newStrategy):
        self.currentStrategy = newStrategy

class ConcreteStrategyOne():
    def calculate_rank( self, theUsefulThing ,someArg):
        return (someArg.GPA/theUsefulThing.max_GPA)*.3 + (someArg.units_taken/theUsefulThing.max_units_taken)*.7

class ConcreteStrategyTwo():
    def calculate_rank( self, theUsefulThing, someArg ):
        return (someArg.GPA/theUsefulThing.max_GPA)

class ConcreteStrategyThree():
    def calculate_rank( self, theUsefulThing, someArg ):
        return (someArg.units_taken/theUsefulThing.max_units_taken)

class PriorityQueue(Strategy):

    def __init__(self, master_list = []):
        self.master_list = []
        super().__init__(self)
        #self.rank = 0
        return

    def add_to_list(self, object):
        print("in add to list ---")
        print(object.rank)
        self.heap_queue2(object)
        return self.master_list

    def heap_queue2(self, insert):
        print(insert.rank)
        insert.rank = self.calculate_rank(insert)
        print("-----> this is rank")
        print(insert.rank)
        self.master_list.append(insert) 
        import math

        def heapify(self,end_index):

            parent_index = int(math.ceil(end_index/2-1))
            end_index = end_index

            if parent_index == -1:
                return
            print(self.master_list[parent_index].rank)
            if self.master_list[parent_index].rank < self.master_list[end_index].rank:
                self.master_list[parent_index].rank, self.master_list[end_index].rank = self.master_list[end_index].rank, self.master_list[parent_index].rank
                print("lalala")

            heapify(self,parent_index)



        end_index = int(len(self.master_list)-1)
        parent_index = int(math.ceil(end_index/2-1))
        

        print("parent index")
        print (parent_index)

        print("end index")
        print (end_index)
        print("--------")
        heapify(self,end_index)

    def heap_queue(self):
        
        def heap_recursion(self,n, i):
            
            largest_node = i 
            left_child = 2 * largest_node + 1     
            right_child = 2 * i + 2     
        
            if left_child < n and self.master_list[largest_node].rank < self.master_list[left_child].rank:
                largest_node = left_child
        
            if right_child < n and self.master_list[largest_node].rank < self.master_list[right_child].rank:
                largest_node = right_child
        
            if largest_node != i:
                self.master_list[i],self.master_list[largest_node] = self.master_list[largest_node],self.master_list[i]  # swap

                heap_recursion(self,n, largest_node)
        
        end = len(self.master_list)
        start = end // 2 - 1 

        for i in range(start, -1, -1):
            heap_recursion(self,end, i)

        for i in range(end-1, 0, -1):
            self.master_list[i], self.master_list[0] = self.master_list[0], self.master_list[i]
            heap_recursion(self,i, 0)
        
    def show_name(self):
        for x in self.master_list:
            print(x.name)

    # The show_name_redID function prints the names and redIDs of all the Student objects in master list.
    def show_name_redID(self):
        for x in self.master_list:
            # The .ljust(20) method is used for formatting purposes to make the data more readable.
            print("Name: " + str(x.name.ljust(20)) + "\t\tRedID: " + str(x.rank))

    # The method remove_from_queue removes the element with the highest priority. 
    # The design decision was made to not return the element (See method highest_priority() instead).
    # In Python pop() has O(1) complexity if its the last element.
    def remove_from_queue(self):
        
        def heap_down(self,index):
            end_index = int(len(self.master_list)-1)
            if index == end_index:
                print("first return")
                return

            #print("got here at all")
            #print(index)
            #print(end_index)
            if index + 1 == end_index:
                if self.master_list[index].rank > self.master_list[end_index].rank:
                    self.master_list[index].rank, self.master_list[end_index].rank = self.master_list[end_index].rank, self.master_list[index].rank
                    heap_down(self,index+1)

            if index +2 <= end_index:
                if self.master_list[index+1].rank > self.master_list[index+2].rank:
                        self.master_list[index].rank, self.master_list[index+1].rank = self.master_list[index+1].rank, self.master_list[index].rank
                        heap_down(self,index+1)
                else:
                        self.master_list[index].rank, self.master_list[index+2].rank = self.master_list[index+2].rank, self.master_list[index].rank
                        heap_down(self,index+2)
            #heap_down(self, index)

        index = 0
        end_index = int(len(self.master_list)-1)
        self.master_list[0].rank, self.master_list[end_index].rank = self.master_list[end_index].rank, self.master_list[0].rank
        heap_down(self,index)
        return self.master_list.pop()

    def remove_from_queueN(self, n):
        if self.master_list:
            for x in range(0,n):
                self.master_list.pop()
        return

    # Simple function to find the length of the master list.
    def list_length(self):
        return len(self.master_list)

    # The highest_priority returns the element with the highest priority. It does not remove it from
    # the master list (See method pop() instead.)
    def highest_priority(self):
        if self.master_list:
            return self.master_list[len(self.master_list)-1]
        else:
            # Return 1 if master_list is empty.
            return 1


class Student:

    # The student structure is used as elements in the master list above it.
    # It contains all the parameters for each student, including their 'ranking' score.
    def __init__(self, name, redID, email, address, GPA, units_taken):
        self.name = name
        self.redID = redID
        self.email = email
        self.address = address
        self.GPA = GPA
        self.units_taken = units_taken
        self.rank = 0

'''
        self.rank = self.rank_calculator(GPA,units_taken)

    def rank_calculator(self, GPA, units_taken):

        max_GPA = 4.0
        max_units_taken = 150
        if GPA > max_GPA or GPA < 0.0:
            raise ValueError("The GPA is too high or too low!")
        elif units_taken > max_units_taken or units_taken < 0.0:
            raise ValueError("The number of units taken is too high or too low!")
        return round((GPA/max_GPA)*.3 + (units_taken/max_units_taken)*.7,4)
        '''

##class RankCalculator()
class Iterator():

    def __init__(self, test):
        import copy
        self.list = copy.deepcopy(test)
        return

    def next(self):
        #for x in self.list:
        #print(len(self.list))
        print(type(self.list))
        for x in self.list.master_list:
            print(x.name)
        return

class ScreenCommand:

    def __init__(self, priorityQueue):
        self.priorityQueue = priorityQueue
        import copy
        #self.previous_state = copy.deepcopy(priorityQueue.master_list)
        #self.previous_state = []
        #print(len(self.previous_state))
        #self.screen = screen

        def execute(self):
            pass
        
        def undo(self):
            pass

class CutCommand(ScreenCommand):
    def __init__(self, priorityQueue, n = 0):
        super().__init__(priorityQueue)
        self.n = n
        import copy
        self.previous_state = copy.deepcopy(priorityQueue.master_list)

    def execute(self):
        import copy
        #self.previous_state.append(self.priorityQueue.master_list[:])
        print(len(self.previous_state))
        self.priorityQueue.remove_from_queueN(n = self.n)

    def undo(self):
        print("this was called")
        #print(len(self.priorityQueue))
        #print(len(self.previous_state))
        import copy
        #self.priorityQueue.master_list = copy.deepcopy(self.previous_state.pop())
        self.priorityQueue.master_list = copy.deepcopy(self.previous_state)

class AddCommand(ScreenCommand):
    def __init__(self, priorityQueue, Student):
        super().__init__(priorityQueue)
        self.Student = Student
        import copy
        self.previous_state = copy.deepcopy(self.priorityQueue.master_list)
        print(len(self.previous_state))

    def execute(self):
        import copy
        #self.previous_state.append(self.priorityQueue.master_list[:])
        #print(len(self.previous_state))
        self.priorityQueue.add_to_list(self.Student)
        #self.priorityQueue.remove_from_queueN(n = self.n)

    def undo(self):
        print("this was called")
        #print(len(self.priorityQueue))
        #print(len(self.previous_state))
        import copy
        #self.priorityQueue.master_list = copy.deepcopy(self.previous_state.pop())
        print(len(self.previous_state))
        #del self.priorityQueue.master_list
        self.priorityQueue.master_list = copy.deepcopy(self.previous_state)



class ScreenInvoker:
    def __init__(self):
        self.history = []

    def store_and_execute(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()


#ptest = PriorityQueue()

#https://www.youtube.com/watch?v=Fc1fLEk_Kr0
#https://www.youtube.com/watch?v=m9KCiLrCErs
#https://www.youtube.com/watch?v=WCm3TqScBM8&t=1s
List = PriorityQueue()
aStudent = Student("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
List.add_to_list(aStudent)
aStudent = Student("Indie",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0)
List.add_to_list(aStudent)
aStudent = Student("Eric",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0)
List.add_to_list(aStudent)
aStudent = Student("Aaron",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0)
List.add_to_list(aStudent)
aStudent = Student("Gary",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0)
List.add_to_list(aStudent)
aStudent = Student("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
List.add_to_list(aStudent)
aStudent = Student("Geoff",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
List.add_to_list(aStudent)
aStudent = Student("Issac",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
List.add_to_list(aStudent)
aStudent = Student("Frank",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
List.add_to_list(aStudent)
aStudent = Student("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
List.add_to_list(aStudent)
'''
aStudent = Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
List.add_to_list(aStudent)

List.add_to_list(aStudent)
List.add_to_list(aStudent)
List.add_to_list(aStudent)
#List.add_to_list(aStudent)
#List.remove_from_queueN(2)
'''
#List.show_name_redID()
#print("-----------------")
#List.remove_from_queue()
#List.show_name_redID()
#print("------------")
#iter  = Iterator(List)
#print(str(iter.next()))

#print(List)
#for x in List.master_list:
#    print(x)
'''

cut  = CutCommand(List, 2)
client = ScreenInvoker()
client.store_and_execute(cut)
print("------------------- removed 2")
List.show_name()

#print("--------------- added 2")
#client.undo_last()
#List.show_name()

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
'''

'''
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


"""
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
"""
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
