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

class TestPriorityQueue(unittest.TestCase):

    # setUp is run before every test. It defines a set of input data that can be tested.
    def setUp(self):

        # First establish the PriorityQueue class.
        self.master_list = PriorityQueue.PriorityQueue()

        # Three different types of data is tested. The data below is random order.
        # The names of the students are meant to alphabetical in the final priority queue.
        self.master_list.add_to_list("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.master_list.add_to_list("Eric",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0)
        self.master_list.add_to_list("Indie",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0)
        self.master_list.add_to_list("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
        self.master_list.add_to_list("Aaron",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0)
        self.master_list.add_to_list("Gary",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0)
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.master_list.add_to_list("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
        self.master_list.add_to_list("Geoff",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
        self.master_list.add_to_list("Issac",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
        self.master_list.add_to_list("Frank",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
        self.master_list.add_to_list("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        self.master_list.add_to_list("Ivan",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0)
        self.master_list.add_to_list("Derek",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
        self.master_list.add_to_list("Doug",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.master_list.add_to_list("Jeff",123456789, "email@sdsu.edu","123 Fake St",3.9,150.0)

        # This set of data tests for repeated values, and to see if they cause issues.
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)

        # The data below is intentionally backwards order to see if its sorts correctly.
        self.master_list.add_to_list("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.master_list.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.master_list.add_to_list("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
        self.master_list.add_to_list("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        
    # tearDown destroys the input data after each test.
    def tearDown(self):
        pass 

    def test_add_to_list(self):

        # This function checks the ranking and makes sure its in increasing order.
        def compare_list_rank():
            comparison_rank = 0
            for x in self.master_list.master_list:
                self.assertGreaterEqual(x.rank,comparison_rank)
                comparison_rank = x.rank
        
        # First check to see if the master list is in increasing order, then remove an element from 
        # the queue. Then recheck to make sure its in increasing order.
        compare_list_rank()
        self.master_list.remove_from_queue()
        compare_list_rank()

        # The tests below check for bad data entry that exceeds the input specifications.
        # Example being too high a GPA or negative units.
        with self.assertRaises(ValueError):
            self.master_list.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",40.0,40.0)

        with self.assertRaises(ValueError):
            self.master_list.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",-1.0,40.0)

        with self.assertRaises(ValueError):
            self.master_list.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",4.0,500)

        with self.assertRaises(ValueError):
            self.master_list.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",4.0,-12.9)

        with self.assertRaises(ValueError):
            self.master_list.add_to_list("Jack",123456789,"email@sdsu.edu","123 Fake St",4.0,-12.9)

    # The ranking calculator is tested against known values.
    def test_rank_calculator(self):
        result = PriorityQueue.PriorityQueue.rank_calculator(self,2.0,30)
        self.assertEqual(result,.29)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,0.0,120)
        self.assertEqual(result,.56)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,2.0,0)
        self.assertEqual(result,.15)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,0,0)
        self.assertEqual(result,0.0)

    # The show_name function is tested to see if the types of parameters are whats expected.
    # This can be tricky in python, as the types are inferred, but may help debug an unseen issue.
    def test_show_name(self):
        for x in self.master_list.master_list:
            self.assertTrue(type(x.name) == type("string"))

        for x in self.master_list.master_list:
            self.assertTrue(type(x.redID) == int)

    # The test below checks the length of the master list, removes a value from it, then rechecks the 
    # length of the list. The length of the master list should be one less.
    def test_remove_from_queue(self):
        lengthlist_before_remove = len(self.master_list.master_list)
        self.master_list.remove_from_queue()
        lengthlist_after_remove = len(self.master_list.master_list)
        self.assertEqual(lengthlist_before_remove,lengthlist_after_remove+1)
        

    def test_highest_priority(self):

        # The test below uses a student with the absolute highest ranking. Therefore it checks
        # to make sure the student is given the highest priority.
        self.master_list.add_to_list("Zack",123456789, "email@sdsu.edu","123 Fake St",4.0,150.0)
        self.assertEqual(self.master_list.highest_priority().name,"Zack")
        self.assertEqual(self.master_list.master_list[-1].name,"Zack")

        # The highest priority method returns a Student element but does not remove it from the master
        # list. The test below checks the size before and after the method.
        lengthlist_before = len(self.master_list.master_list)
        self.master_list.highest_priority()
        lengthlist_after = len(self.master_list.master_list)
        self.assertEqual(lengthlist_before,lengthlist_after)

# A seperate class is created to test methods for an empty array.
class TestPriorityQueue_EmptyQueue(unittest.TestCase):

    def setUp(self):
        self.master_list = PriorityQueue.PriorityQueue()

    def tearDown(self):
        pass

    # See if you can add a student object to an empty list successfully.
    def test_add_to_list(self):
        self.master_list.add_to_list("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.assertIsNotNone(self.master_list)

    # Since the master list is empty, using the remove method should not change the length list.
    # Additionally this list checks to see if any errors happen from using the method remove_from_queue 
    # on an empty list.
    def test_show_name(self):
        lengthlist_before_remove = len(self.master_list.master_list)
        self.master_list.remove_from_queue()
        lengthlist_after_remove = len(self.master_list.master_list)
        self.assertEqual(lengthlist_before_remove,lengthlist_after_remove)

    # The highest priority method should return 1 if the master list is empty.
    def test_highest_priority(self):
        self.assertEqual(self.master_list.highest_priority(),1)

# This test class checks if there is only one element in the priority queue, and how it handles it.
class TestPriorityQueue_OneElement(unittest.TestCase):

    def setUp(self):
        self.master_list = PriorityQueue.PriorityQueue()
        self.master_list.add_to_list("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)

    def tearDown(self):
        pass

    # The priority queue should be empty after removing a student.
    def test_show_name(self):
        lengthlist_before_remove = len(self.master_list.master_list)
        self.master_list.remove_from_queue()
        self.assertEqual(lengthlist_before_remove-1,0)

# Establish and run the test cases.
if __name__ == '__main__':
    unittest.main()