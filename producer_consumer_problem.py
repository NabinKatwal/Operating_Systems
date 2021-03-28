from threading import Thread, Semaphore
import time
import random       

queue = []       
MAX_NUM = 10

sem = Semaphore()

class ProducerThread(Thread):
    def run(self):
        nums = range(5) 
        global queue
            
        while True:
            sem.acquire()
            if len(queue) == MAX_NUM:
                    
                print ("List is full, producer will wait")
                sem.release()  
                print ("Space in queue, Consumer notified the producer")

            num = random.choice(nums) 
            queue.append(num) 
            print ("Produced", num) 
            sem.release()

            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
            
        while True:
            sem.acquire()
            if not queue:
                print ("List is empty, consumer waiting")
                sem.release()
                print ("Producer added something to queue and notified the consumer")

            num = queue.pop(0)
                
            print ("Consumed", num)
            sem.release()

            time.sleep(random.random())

def main():
    ProducerThread().start()
    ConsumerThread().start()

if __name__ == '__main__':
    main()

