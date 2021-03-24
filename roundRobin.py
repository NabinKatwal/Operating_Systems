class Round_robin:
    def __init__(self, burst_time, process, time_quantum):
        self.process = process
        self.burst_time = burst_time
        self.rem_burst_time = [burst_time[i] for i in range(len(process))]
        self.waiting_time = [0]*len(process)
        self.time = 0
        self.time_quantum = time_quantum
        self.turnaround_time = [0]*len(process)
    
    def calculate_waiting_time(self):
        while(1):
            done = True 
            for i in range(len(process)):
                if self.rem_burst_time[i]>0:
                    done = False
                    if self.rem_burst_time[i]>self.time_quantum:
                        self.time = self.time+self.time_quantum
                        self.rem_burst_time[i] -= self.time_quantum
                    else:
                        self.time = self.time + self.rem_burst_time[i]
                        self.waiting_time[i]=self.time - self.burst_time[i]
                        self.rem_burst_time[i] = 0
            if done == True:
                    break
        return self.waiting_time

    def turnaroundtime(self):
        for i in range(len(process)):
            self.turnaround_time[i] = self.burst_time[i]+self.waiting_time[i]

        return self.turnaround_time


    def display_results(self):
        self.calculate_waiting_time()
        self.turnaroundtime()
        average_wt = sum(self.waiting_time)/len(process)
        average_turnaround = (sum(self.waiting_time)+sum(self.burst_time))/len(self.process)
        print("Processes\t Burst Time\t Waiting Time\t Turn around time")
        for i in range(0, len(process)):
            print(f"{self.process[i]}\t\t {self.burst_time[i]}\t\t {self.waiting_time[i]}\t\t\t{self.turnaround_time[i]}")
        print('\n')
        print(f"Average waiting time: {average_wt}")
        print('\n')
        print(f"Average turnaround time: {average_turnaround}")
            
if __name__ == "__main__":
    process = []
    burst_time = []
    time_quantum = int(input("Enter time quantum->"))

    while(True):
        process_in = int(input("Enter process id->"))
        burst_time_in = int(input("Enter burst time->"))
        process.append(process_in)
        burst_time.append(burst_time_in)
        choice = input("Continue Input?(y/n)->")
        if choice.lower() == 'y':
            continue
        else:
            break

    round1 = Round_robin(burst_time, process, time_quantum)

    round1.display_results()
    