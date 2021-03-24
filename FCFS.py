class FCFS:
    def __init__(self, process, burst_time):
        self.process = process
        self.burst_time = burst_time
        self.average_turnaround_time = 0
        self.waiting_time = []
        self.average_waiting_time = 0

    def waiting_time_fn(self):
        for i in range(0, len(self.process)):
            if i == 0:
                self.waiting_time.append(0)
            else:
                self.waiting_time.append(self.waiting_time[i-1]+self.burst_time[i-1])
        return (self.waiting_time)

    def average_waiting_time_fn(self):
        self.waiting_time_fn()
        self.average_waiting_time = sum(self.waiting_time)/len(self.process)


    def average_turnaround_time_fn(self):
        self.average_turnaround_time = (sum(self.waiting_time)+sum(self.burst_time))/len(self.process)

    def display_results(self):
        self.average_waiting_time_fn()
        self.average_turnaround_time_fn()
        print("Processes   Burst time  Waiting Time") 
        for i in range(0, len(self.process)):
            print(f"{self.process[i]}            {self.burst_time[i]}            {self.waiting_time_fn()[i]}")
        print('\n')
        print(f"Average waiting time {self.average_waiting_time}")
        print('\n')
        print(f'Average turnaround time {self.average_turnaround_time}')

            

if __name__ == "__main__":
    process_list = []
    burst_time_list = []
    while (True):
        process = int(input("Enter process time->"))
        burst_time = int(input("Enter burst time->"))
        process_list.append(process)
        burst_time_list.append(burst_time)
        choice = input("Enter another?(y/n)")
        if choice.lower() == 'y':
            continue
        else:
            break 

    batch1 = FCFS(process_list, burst_time_list)

    batch1.display_results()
        