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
                if(self.pages[i] not in self.s):
                    self.s.add(pages[i])
                    self.page_faults += 1
                    self.indexes.put(pages[i])
            else:
                if (self.pages[i] not in self.s):
                    val = self.indexes.queue[0]
                    self.indexes.get()
                    self.s.remove(val)
                    self.s.add(pages[i])
                    self.indexes.put(pages[i])
                    self.page_faults += 1

        return self.page_faults
     
    def display_results(self):
        self.page_fault()
        print(f"{self.pages}")
        print(f"Page faults {self.page_faults}")
        print(f"Page hits {len(self.pages)-self.page_faults}")


if __name__ == '__main__':
    pages = []
    capacity = 4

    
    while(True):
        pages_in = int(input("Enter pages->"))
        choice = input("Add more pages?(y/n)->")
        pages.append(pages_in)
        if choice.lower()=='y':
            continue
        else:
            break

    page1 = FCFS_PR(pages, capacity)

    page1.display_results()
    