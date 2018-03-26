import random


class Schedule:
    PEOPLE_NUM = 10
    workers = []

    def __init__(self):
        # generate worker list
        for i in range(0, self.PEOPLE_NUM):
            name = i+1
            self.workers.append(name)

    def generate_week_schedule(self):
        schedule = []
        non_selected_workers = list(self.workers)

        # much quicker to get a new random number
        # than to create a new list of eligible workers
        for i in range(0, 10):  # 10 slots in weekly schedule

            pos = random.randint(0, len(non_selected_workers)-1)
            selected_worker = non_selected_workers[pos]
            non_selected_workers.remove(selected_worker)
            schedule.append(selected_worker)

        return schedule
