
#Author: Martin Miller
#redID: 817405999
#Professor: Whitney
#Class: CS 635 Advanced Object Oriented Design
#Description: The class below inputs students into a priority queue with O(log n) complexity.
#file: PriorityQueue.py
#Date: September 5th, 2018


class PriorityQueue:

    # Since this is a priority queue, a "master list" is required to keep track of the students.
    # The list is defined as empty. The rank will be used to prioritize the students.
    def __init__(self):
        self.master_list = []
        self.rank = 0
        return

    # The add_to_list method is used to add students, in a ranked order, to the priority queue.
    # The input parameters include the students information, however this info is passed to the
    # 'Student' structure before its added to the list.
    def add_to_list(self, name, redID, email, address, GPA, units_taken):

        # The GPA and number of units is checked before adding it to the list. The design decision was
        # made to raise a value error, because this can be checked for in our Unit test.
        if GPA > 4.0 or GPA < 0.0:
            raise ValueError("The GPA is too high or too low!")
        elif units_taken > 150 or units_taken < 0.0:
            raise ValueError("The number of units taken is too high or too low!")

        # Add the new student to the end of the master_list. This is an O(1) complexity operation.
        self.master_list.append(Students(name, redID, email, address, GPA, units_taken))

        # Call the heap_queue() method to build a priority queue with a heap structure.
        self.heap_queue()
        return self.master_list

    # The rank calculator first normalizes the GPA and number of units, and then computes the rank.
    # The return value is rounded to 4 decimal places in increase readability for repeating decimals.
    def rank_calculator(self, GPA, units_taken):
        return round((GPA/4.0)*.3 + (units_taken/150)*.7,4)

    # The heap_queue builds a heap function of the student objects, using the students rank as the 
    # metric. The heap is built with O(log n) complexity.
    def heap_queue(self):
        
        def heap_recursion(self,n, i):
            
            # Assume the root is the largest (this may not be true.)
            largest_node = i 

            # Establish the left and right child nodes.
            left_child = 2 * largest_node + 1     
            right_child = 2 * i + 2     
        
            # Check if the left child is larger then the root.
            if left_child < n and self.master_list[largest_node].rank < self.master_list[left_child].rank:
                largest_node = left_child
        
            # Check if the right child is larger then the root.
            if right_child < n and self.master_list[largest_node].rank < self.master_list[right_child].rank:
                largest_node = right_child
        
            # If the right or left child are larger, change the placement with the root.
            if largest_node != i:
                self.master_list[i],self.master_list[largest_node] = self.master_list[largest_node],self.master_list[i]  # swap

                # Continue heap recursion on the sub-heap. (Reduced in tier size)
                heap_recursion(self,n, largest_node)
        
        # The heap is constructed as a array, find the length of that array.
        end = len(self.master_list)
        start = end // 2 - 1 

        # The first objective is to build a heap structure. For the first for-loop this is 
        # putting together the tiers, and nothing is sorted at this time.
        for i in range(start, -1, -1):
            heap_recursion(self,end, i)

        # Iterate through the heap.
        for i in range(end-1, 0, -1):
            # The current node trades places with the root, and the recursive heap function is called.
            self.master_list[i], self.master_list[0] = self.master_list[0], self.master_list[i]
            heap_recursion(self,i, 0)

    # The show_name function simple prints the names.
    def show_name(self):
        for x in self.master_list:
            print(x.name)

    # The show_name_redID function prints the names and redIDs of all the Student objects in master list.
    def show_name_redID(self):
        for x in self.master_list:
            # The .ljust(20) method is used for formatting purposes to make the data more readable.
            print("Name: " + str(x.name.ljust(20)) + "\t\tRedID: " + str(x.redID))

    # The method remove_from_queue removes the element with the highest priority. 
    # The design decision was made to not return the element (See method highest_priority() instead).
    # In Python pop() has O(1) complexity if its the last element.
    def remove_from_queue(self):
        if self.master_list:
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


class Students:

    # The student structure is used as elements in the master list above it.
    # It contains all the parameters for each student, including their 'ranking' score.
    def __init__(self, name, redID, email, address, GPA, units_taken):
        self.name = name
        self.redID = redID
        self.email = email
        self.address = address
        self.GPA = GPA
        self.units_taken = units_taken
        self.rank = PriorityQueue.rank_calculator(self,GPA,units_taken)

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
print(List.highest_priority())
'''

