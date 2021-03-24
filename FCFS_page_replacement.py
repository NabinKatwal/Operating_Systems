from queue import Queue

class FCFS_PR:
    def __init__(self, pages, capacity):
        self.pages = pages
        self.n = len(self.pages)
        self.capacity = capacity 
        self.s = set()
        self.indexes = Queue()
        self.page_faults = 0

    def page_fault(self):
        for i in range(self.n):
            if len(self.s)<self.capacity:
                if(self.pages[i] not in s):
                    s.add(pages[i])
                    self.page_faults += 1
                    self.indexes.put(pages[i])
            else:
                if (self.pages[i] not in s):
                    val = self.indexes.queue[0]
                    self.indexes.get()
                    self.s.remove(val)
                    self.s.add(pages[i])
                    self.indexes.put(pages[i])
                    self.page_faults += 1

        return page_faults
    
    def display_results(self):
        pass


if __name__ == '__main__':
    pages = [1,3,0,3,5,6,3]
    capacity = 4

    
    # while(True):
    #     pages_in = int(input("Enter pages->"))
    #     choice = input("Add more pages?(y/n)->")
    #     if choice.lower()=='y':
    #         continue
    #     else:
    #         break

    page1 = FCFS_PR(pages, capacity)
    