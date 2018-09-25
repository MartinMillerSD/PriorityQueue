#Author: Martin Miller
#redID: 817405999
#Professor: Whitney
#Class: CS 635 Advanced Object Oriented Design
#Description: The class below inputs students into a priority queue.
#file: test_PriorityQueue.py
#Testing file: PriorityQueue.py
#Date: September 5th, 2018

import unittest
import PriorityQueue
from PriorityQueue import Student
from PriorityQueue import ConcreteStrategyOne
from PriorityQueue import ConcreteStrategyTwo
from PriorityQueue import ConcreteStrategyThree

class TestPriorityQueue(unittest.TestCase):

    # setUp is run before every test. It defines a set of input data that can be tested.
    def setUp(self):

        # First establish the PriorityQueue class.
        self.queue = PriorityQueue.PriorityQueue()

        # Three different types of data are tested. The data below is in random order.
        # The names of the students are meant to be alphabetical in the final priority queue.
        #aStudent = Student("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        #self.queue.add_to_list(queue.Student("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0))
        self.queue.add_to_list(Student("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0))
        self.queue.add_to_list(Student("Indie",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0))
        self.queue.add_to_list(Student("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0))
        self.queue.add_to_list(Student("Aaron",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0))
        self.queue.add_to_list(Student("Gary",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0))
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))
        self.queue.add_to_list(Student("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0))
        self.queue.add_to_list(Student("Geoff",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0))
        self.queue.add_to_list(Student("Issac",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0))
        self.queue.add_to_list(Student("Frank",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0))
        self.queue.add_to_list(Student("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0))
        self.queue.add_to_list(Student("Ivan",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0))
        self.queue.add_to_list(Student("Derek",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0))
        self.queue.add_to_list(Student("Doug",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0))
        self.queue.add_to_list(Student("Jeff",123456789, "email@sdsu.edu","123 Fake St",3.9,150.0))

        # This set of data tests for repeated values, and to see if they cause issues.
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))

        # The data below is intentionally backwards in order to see if its sorts correctly.
        self.queue.add_to_list(Student("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0))
        self.queue.add_to_list(Student("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0))
        self.queue.add_to_list(Student("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0))
        self.queue.add_to_list(Student("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0))
        
    # tearDown destroys the input data after each test.
    def tearDown(self):
        pass 

    def test_add_to_list(self):

        # This function checks the ranking and makes sure its in increasing order.
        def compare_list_rank():
            comparison_rank = self.queue.queue[0].rank
            for x in self.queue.queue:
                self.assertGreaterEqual(comparison_rank, x.rank)
        
        # First check to see if the master list is in increasing order, then remove an element from 
        # the queue. Then recheck to make sure its in increasing order.
        compare_list_rank()
        #self.queue.remove_from_queue()
        #compare_list_rank()

        # The tests below check for bad data entry that exceeds the input specifications.
        # Example being too high a GPA or negative units.
        with self.assertRaises(ValueError):
            self.queue.add_to_list(Student("Jack",123456789, "email@sdsu.edu","123 Fake St",40.0,40.0))

        with self.assertRaises(ValueError):
            self.queue.add_to_list(Student("Jack",123456789, "email@sdsu.edu","123 Fake St",-1.0,40.0))

        with self.assertRaises(ValueError):
            self.queue.add_to_list(Student("Jack",123456789, "email@sdsu.edu","123 Fake St",4.0,500))

        with self.assertRaises(ValueError):
            self.queue.add_to_list(Student("Jack",123456789, "email@sdsu.edu","123 Fake St",4.0,-12.9))

        with self.assertRaises(ValueError):
            self.queue.add_to_list(Student("Jack",123456789,"email@sdsu.edu","123 Fake St",4.0,-12.9))


    # The test below checks the length of the master list, removes a value from it, then rechecks the 
    # length of the list. The length of the master list should be one less.
    def test_remove_from_queue(self):
        lengthlist_before_remove = len(self.queue.queue)
        self.queue.remove_from_queue()
        lengthlist_after_remove = len(self.queue.queue)
        self.assertEqual(lengthlist_before_remove,lengthlist_after_remove+1)
        

    def test_highest_priority(self):

        # The test below uses a student with the absolute highest ranking. Therefore it checks
        # to make sure the student is given the highest priority.
        self.queue.add_to_list(Student("Zack",123456789, "email@sdsu.edu","123 Fake St",4.0,150.0))
        self.queue.add_to_list(Student("Bob",123456789, "email@sdsu.edu","123 Fake St",2.0,10.0))
        self.assertEqual(self.queue.queue[0].name,"Zack")
        self.assertEqual(self.queue.queue[-1].name,"Bob")

        # The highest priority method returns a Student element but does not remove it from the master
        # list. The test below checks the size before and after the method.
        lengthlist_before = len(self.queue.queue)
        self.queue.highest_priority()
        lengthlist_after = len(self.queue.queue)
        self.assertEqual(lengthlist_before,lengthlist_after)

    #def test_show_name_redID(self):
        #self.queue.show_name_redID()

# A seperate class is created to test methods for an empty array.
class TestPriorityQueue_EmptyQueue(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue.PriorityQueue()

    def tearDown(self):
        pass

    # See if you can add a student object to an empty list successfully.
    def test_add_to_list(self):
        self.queue.add_to_list(Student("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0))
        self.assertIsNotNone(self.queue)

    # Since the master list is empty, using the remove method should not change the length list.
    # Additionally this list checks to see if any errors happen from using the method remove_from_queue() 
    # on an empty list.
    def test_show_name(self):
        lengthlist_before_remove = len(self.queue.queue)
        self.queue.remove_from_queue()
        lengthlist_after_remove = len(self.queue.queue)
        self.assertEqual(lengthlist_before_remove,lengthlist_after_remove)

    # The highest_priority() method should return 1 if the master list is empty.
    #def test_highest_priority(self):
     #   self.assertEqual(self.queue.highest_priority(),1)

    def test_strategy(self):

        temp = self.queue.highest_priority()
        self.queue.changeStrategy(ConcreteStrategyTwo())
        temp2 = self.queue.highest_priority()
        self.assertFalse(temp == temp)



# This test class checks if there is only one element in the priority queue, and how it handles it.
class TestPriorityQueue_OneElement(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue.PriorityQueue()
        self.queue.add_to_list(Student("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0))

    def tearDown(self):
        pass

    # The priority queue should be empty after removing a student.
    def test_show_name(self):
        lengthlist_before_remove = len(self.queue.queue)
        self.queue.remove_from_queue()
        self.assertEqual(lengthlist_before_remove-1,0)

# Establish and run the test cases.
if __name__ == '__main__':
    unittest.main()