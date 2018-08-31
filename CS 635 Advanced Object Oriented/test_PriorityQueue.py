import unittest
import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_add_to_list(self):

        def compare_list_rank():
            comparison_rank = 0
            for x in List.master_list:
                self.assertGreaterEqual(x.rank,comparison_rank)
                comparison_rank = x.rank
            return

        List = PriorityQueue.PriorityQueue()
        List.add_to_list("Aaron",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        List.add_to_list("Issac",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0)
        List.add_to_list("Derek",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
        List.add_to_list("David",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        self.assertEqual(len(List.master_list),4)
        compare_list_rank()

        List.pop()
        compare_list_rank()

        List.add_to_list("David",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
        List.add_to_list("Jack",123456789, "email@sdsu.edu","123 Fake St",40.0,40.0)
        compare_list_rank()


    def test_rank_calculator(self):
        result = PriorityQueue.PriorityQueue.rank_calculator(self,2.0,30)
        self.assertEqual(result,.29)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,0.0,120)
        self.assertEqual(result,.56)
        result = PriorityQueue.PriorityQueue.rank_calculator(self,2.0,0)
        self.assertEqual(result,.15)

    def test_show_name(self):
        List = PriorityQueue.PriorityQueue()
        List.add_to_list("Brad",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        self.assertEqual(List.master_list[0].name,"Brad")
        List.add_to_list("Tom",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        self.assertEqual(List.master_list[1].name,"Tom")

    def test_pop(self):
        List = PriorityQueue.PriorityQueue()
        List.add_to_list("Brad",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        List.add_to_list("Tom",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
        lengthlist_before_pop = len(List.master_list)
        List.pop()
        lengthlist_after_pop = len(List.master_list)
        self.assertGreater(lengthlist_before_pop,lengthlist_after_pop)

    def test_highest_priority(self):
        List = PriorityQueue.PriorityQueue()
        List.add_to_list("Stephanie",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0)
        List.add_to_list("Greg",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0)
        List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
        List.add_to_list("Britany",123456789, "email@sdsu.edu","123 Fake St",4.0,150.0)
        List.add_to_list("Garrett",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
        self.assertEqual(List.highest_priority().name,"Britany")
        self.assertEqual(List.master_list[-1].name,"Britany")

if __name__ == '__main__':
    unittest.main()