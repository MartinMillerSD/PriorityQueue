



class PriorityQueue:

    master_list = []
    #list_length = 0.0

    def __init__(self):
        #self.master_list = position
        return

    def add_to_list(self, name, redID, email, address, GPA, numberOfUnitsTaken):
        if GPA > 4.0 or GPA < 0.0 or numberOfUnitsTaken > 150 or numberOfUnitsTaken < 0.0:
            print("faill!")
            return

        #self.list_length = len(self.master_list)
        #self.list_length = self.list_length()
        #self.number = 0
        self.number = self.binary_search(0,self.list_length(),GPA,numberOfUnitsTaken)
        #print("this is the number " + str(self.number))
        self.master_list.insert(self.number,Students(name, redID, email, address, GPA, numberOfUnitsTaken))
        return

    def rank_calculator(self,GPA, numberOfUnitsTaken):
        return (GPA/4.0)*.3 + (numberOfUnitsTaken/150.0)*.7

    def binary_search(self,start,end,GPA,numberOfUnitsTaken):

        score = self.rank_calculator(GPA,numberOfUnitsTaken)
        #print(score)

        if not self.master_list:
            #print("should only happen once")
            return 0

        if (start+1) == end:
            if (self.rank_calculator(self.master_list[start].GPA,self.master_list[start].numberOfUnitsTaken)) > score:
                #print("1 was used")
                return start
            else:
                #print("2 was used")
                return start+1

        median = (end+start)/2
        if median%1 != 0:
            median = median-.5
        median = int(median)
        #print("start " + str(start) +" this is median " +str(median) + " and this is end " +str(end))

        if (self.rank_calculator(self.master_list[median].GPA,self.master_list[median].numberOfUnitsTaken)) < score:
            #print("recurse 1 was taken")
            inner = self.binary_search(median,end,GPA,numberOfUnitsTaken)  
            return inner
        elif (self.rank_calculator(self.master_list[median].GPA,self.master_list[median].numberOfUnitsTaken)) > score:
            #print("recurse 2 was taken")
            inner = self.binary_search(start,median,GPA,numberOfUnitsTaken)
            return inner
        else:
            #print("this was used")
            return median


    def show_name(self):
        #print(self.master_list)
        for x in self.master_list:
            print(x.name)

    def show_name_redID(self):
        for x in self.master_list:
            print("Name: " + str(x.name.ljust(20)) + "\t\tRedID: " + str(x.redID))

    def remove(self):
        self.master_list.remove()
        return

    def list_length(self):
        print(len(self.master_list))
        return len(self.master_list)

class Students:

    def __init__(self, name, redID, email, address, GPA, numberOfUnitsTaken):
        self.name = name
        self.redID = redID
        self.email = email
        self.address = address
        self.GPA = GPA
        self.numberOfUnitsTaken = numberOfUnitsTaken
        #self.rank = 0

List = PriorityQueue()
List.add_to_list("Delta",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)
List.add_to_list("Echo",123456789, "email@sdsu.edu","123 Fake St",1.2,50.0)
List.add_to_list("Indigo",123456789, "email@sdsu.edu","123 Fake St",3.2,80.0)
List.add_to_list("Helo",123456789, "email@sdsu.edu","123 Fake St",3.0,70.0)
List.add_to_list("SuperAlpha",123456789, "email@sdsu.edu","123 Fake St",0.8,00.0)
List.add_to_list("Gamma",123456789, "email@sdsu.edu","123 Fake St",3.8,50.0)
List.add_to_list("Charlie",123456789, "email@sdsu.edu","123 Fake St",1.6,30.0)
List.add_to_list("Bravo",123456789, "email@sdsu.edu","123 Fake St",1.8,20.0)
List.add_to_list("Gamma2",123456789, "email@sdsu.edu","123 Fake St",3.1,60.0)
List.add_to_list("SuperIndigo",123456789, "email@sdsu.edu","123 Fake St",3.1,150.0)
List.add_to_list("Fox",123456789, "email@sdsu.edu","123 Fake St",3.6,50.0)
List.add_to_list("Alpha",123456789, "email@sdsu.edu","123 Fake St",1.7,10.0)
List.add_to_list("Indigo",123456789, "email@sdsu.edu","123 Fake St",2.9,80.0)
List.add_to_list("Delta2",123456789, "email@sdsu.edu","123 Fake St",1.2,40.0)
List.add_to_list("Delta3",123456789, "email@sdsu.edu","123 Fake St",1.0,40.0)


#List.remove()
List.remove()
List.remove()
List.show_name_redID()


print("------------- done -------------")