
#Author: Martin Miller
#redID: 817405999
#Professor: Whitney
#Class: CS 635 Advanced Object Oriented Design
#Description: The class below inputs students into a priority queue.
#file: PriorityQueue.py
#Date: September 5th, 2018


class PriorityQueue:

    # Since this is a priority queue, only a "master list" is required to keep track of the students.
    # The list is defined as empty.
    def __init__(self):
        self.master_list = []
        return

    # The add_to_list function is used to add students, in a ranked order, to the priority queue.
    # The input parameters include the students information, however this info is passed to the
    # 'Student' structure before its added to the list.
    def add_to_list(self, name, redID, email, address, GPA, numberOfUnitsTaken):

        # The GPA and number of units is checked before adding it to the list. The design decision was
        # made to raise a value error, because this can be checked for in our Unit test.
        if GPA > 4.0 or GPA < 0.0:
            raise ValueError("The GPA is too high or too low!")
        elif numberOfUnitsTaken > 150 or numberOfUnitsTaken < 0.0:
            raise ValueError("The number of units taken is too high or too low!")

        # The function calls a binary search function to find where in the master list the student
        # should be added. This value is stored as the 'insertion number'.
        self.insertion_number = self.binary_search(0,self.list_length(),GPA,numberOfUnitsTaken)

        # The student object is created and added to the master list based on the insertion number
        # that was returned from the binary search.
        self.master_list.insert(self.insertion_number,Students(name, redID, email, address, GPA, numberOfUnitsTaken))
        return self.master_list

    # The rank calculator first normalizes the GPA and number of units, and then computes the rank.
    # The return value is rounded to 4 decimal places in increase readability for repeating decimals.
    def rank_calculator(self, GPA, numberOfUnitsTaken):
        return round((GPA/4.0)*.3 + (numberOfUnitsTaken/150)*.7,4)

    # The purpose of the binary search is to find where to add the Student object to the master list,
    # based on its ranking. The design decision was made to use a binary search. This is because
    # for a binary search, the data is halved with each iteration, by finding the midpoint, and
    # recursively searching the list greater or less then the midpoint. Therefore it has (log n) complexity.
    def binary_search(self,start,end,GPA,numberOfUnitsTaken):

        # First find the rank of the proposed Student object.
        self.rank = self.rank_calculator(GPA,numberOfUnitsTaken)

        # If the master list is currently empty, there is nothing to compare and the Student object
        # should be added in the zeroth spot.
        if not self.master_list:
            #print("should only happen once")
            return 0

        # This is the case where there is two objects in the master list. Find who has the higher ranking
        # and return the appropriate value.
        if (start+1) == end:
            if (self.rank_calculator(self.master_list[start].GPA,self.master_list[start].numberOfUnitsTaken)) > self.rank:
                return start
            else:
                return start+1

        # Find the median index of the list, if its not a whole number, minus one half.
        median = (end+start)/2
        if median%1 != 0:
            median = median-.5
        median = int(median)

        # Now for the recursion steps. The following if statement checks if the inserting Student rank is higher
        # or lower then the midpoint. If it is, recursively call the binary search on the upper (or lower)
        # half of the list. This process continues until the list is 1 or 2 objects long.
        if (self.rank_calculator(self.master_list[median].GPA,self.master_list[median].numberOfUnitsTaken)) < self.rank:
            self.rank = self.binary_search(median,end,GPA,numberOfUnitsTaken)  
            return self.rank
        elif (self.rank_calculator(self.master_list[median].GPA,self.master_list[median].numberOfUnitsTaken)) > self.rank:
            self.rank = self.binary_search(start,median,GPA,numberOfUnitsTaken)
            return self.rank
        else:
            return median

    # The show_name function simple prints the names.
    def show_name(self):
        for x in self.master_list:
            print(x.name)

    # The show_name_redID function prints the names and redIDs of all the Student objects in master list.
    def show_name_redID(self):
        for x in self.master_list:
            # The .ljust(20) method is used for formatting purposes to make the data more readable.
            print("Name: " + str(x.name.ljust(20)) + "\t\tRedID: " + str(x.redID))

    # The function pop_from_queue removes the element with the highest priority. It does not return it.
    def pop_from_queue(self):
        if self.master_list:
            self.master_list.pop()
        return

    # Simple function to find the length of the master list.
    def list_length(self):
        return len(self.master_list)

    # The highest_priority returns the element with the highest priority. It doesnt not remove it from
    # the master list.
    def highest_priority(self):
        if self.master_list:
            return self.master_list[-1]
        else:
            return 1

class Students:

    # The student structure is used as elements in the master list above it.
    # It contains all the parameters for each student, including their 'ranking' score.
    def __init__(self, name, redID, email, address, GPA, numberOfUnitsTaken):
        self.name = name
        self.redID = redID
        self.email = email
        self.address = address
        self.GPA = GPA
        self.numberOfUnitsTaken = numberOfUnitsTaken
        self.rank = 0

#List = PriorityQueue()
##List.add_to_list("Delta",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
#List.add_to_list("Echo",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0) 
#List.add_to_list("Indigo",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0)
#List.add_to_list("Helo",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
#List.add_to_list("SuperAlpha",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0)
#List.add_to_list("Gamma",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0)
#List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
#List.add_to_list("Bravo",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
#List.add_to_list("Gamma2",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
#List.add_to_list("SuperIndigo",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
#List.add_to_list("Fox",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
#List.add_to_list("Alpha",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
#List.add_to_list("Indigo",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0)
#List.add_to_list("Delta2",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
#List.add_to_list("Delta3",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
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


#List.pop()
##List.pop()
##List.pop()
#List.show_name_redID()
#print(List.highest_priority())


