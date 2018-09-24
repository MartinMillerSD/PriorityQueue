class PriorityQueue:
    """ Inteface / Abstract Class concept for readability. """

    def __init__(self):
        self.queue = []

    def printQueue(self):
        print(self.queue)

    #master_queue = []
    def find(self, image):
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, ImageFinder is supposed to be an interface / abstract class!')


    #def add(self, Student):
    #    master_queue.append(Student)

class Student(PriorityQueue):
    ''' Locates images in flickr'''

    def __init__(self, name, redID, email, address, GPA, units_taken):
        self.name = name
        self.redID = redID
        self.email = email
        self.address = address
        self.GPA = GPA
        self.units_taken = units_taken
        #self.rank = PriorityQueue.rank_calculator(self,GPA,units_taken)

    def find(self, image):
        # in reality, query Flickr API for image path
        return "Found image in Flickr: " + image



class Faculty(PriorityQueue):
    ''' Locates images in database. '''
    def find(self, image):
        #in reality, query database for image path
        return "Found image in database: " + image
    
    
    
if __name__ == "__main__" :

    the_queue = PriorityQueue()
    aStudent = Student("Marty", 817405999, "mfmiller@sdsu.edu", "123 Street", 3.5, 60.0)
    aFaculty = Faculty()
    #master_queue.add(aStudent)



  #  try:
        #this is going to blow up!
   #     print (master_queue.find('chickens'))
   # except NotImplementedError as e:
   #     print ("The following exception was expected:")
   #     print (e)
        

    #print (aStudent.find('chickens'))
    #print (aStudent.find('rabbits'))
    #print (aFaculty.find('dogs'))
    #print (aFaculty.find('cats') ) 