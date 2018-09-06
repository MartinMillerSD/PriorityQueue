import unittest
import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.List = PriorityQueue.PriorityQueue()
        self.List.add_to_list("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.List.add_to_list("Eric",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0)
        self.List.add_to_list("Indie",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0)
        self.List.add_to_list("Hank",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
        self.List.add_to_list("Aaron",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0)
        self.List.add_to_list("Gary",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0)
        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.List.add_to_list("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
        self.List.add_to_list("Geoff",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
        self.List.add_to_list("Issac",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
        self.List.add_to_list("Frank",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
        self.List.add_to_list("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        self.List.add_to_list("Ivan",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0)
        self.List.add_to_list("Derek",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
        self.List.add_to_list("Doug",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.List.add_to_list("Jeff",123456789, "email@sdsu.edu","123 Fake St",3.9,150.0)

        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)

        self.List.add_to_list("Diego",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        self.List.add_to_list("Brittany",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
        self.List.add_to_list("Alex",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        

    def tearDown(self):
        pass 


    def test_add_to_list(self):

        def compare_list_rank():
            comparison_rank = 0
            for x in self.List.master_list:
                self.assertGreaterEqual(x.rank,comparison_rank)
                comparison_rank = x.rank
            
        compare_list_rank()
        self.List.pop()
        compare_list_rank()

        with self.assertRaises(ValueError):
            self.List.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",40.0,40.0)

        with self.assertRaises(ValueError):
            self.List.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",-1.0,40.0)

        with self.assertRaises(ValueError):
            self.List.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",4.0,500)

        with self.assertRaises(ValueError):
            self.List.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",4.0,-12.9)

        with self.assertRaises(ValueError):
            self.List.add_to_list("Jack",123456789,"email@sdsu.edu","123 Fake St",4.0,-12.9)

    def test_rank_calculator(self):
        result = PriorityQueue.PriorityQueue.rank_calculator(self,2.0,30)
        self.assertEqual(result,.29)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,0.0,120)
        self.assertEqual(result,.56)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,2.0,0)
        self.assertEqual(result,.15)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,0,0)
        self.assertEqual(result,0.0)



    def test_show_name(self):
        for x in self.List.master_list:
            self.assertTrue(type(x.name) == type("string"))

        for x in self.List.master_list:
            self.assertTrue(type(x.redID) == int)

        
        #for x in self.List.master_list:
        #    self.List.add_to_list(2,123456789,"email@sdsu.edu","123 Fake St",4.0,10)
        #    self.assertFalse(type(int(x.name)) == type("string"))
        ###

    def test_pop(self):
        lengthlist_before_pop = len(self.List.master_list)
        self.List.pop()
        lengthlist_after_pop = len(self.List.master_list)
        self.assertGreater(lengthlist_before_pop,lengthlist_after_pop)
        

    def test_highest_priority(self):

        self.List.add_to_list("Zack",123456789, "email@sdsu.edu","123 Fake St",4.0,150.0)
        self.assertEqual(self.List.highest_priority().name,"Zack")
        self.assertEqual(self.List.master_list[-1].name,"Zack")
        pass


if __name__ == '__main__':
    unittest.main()