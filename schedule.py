import random


class Schedule:
    WORKERS_AMOUNT = 10
    SLOTS_IN_WEEK = 10  # 10 slots in weekly schedule

    def generate_schedule(self, weeks=1):
        schedules = []
        for x in range(weeks):
            schedules.append(self.generate_week_schedule())
        return schedules


    def generate_week_schedule(self):
        schedule = []
        items = list(range(1, self.WORKERS_AMOUNT + 1))
        for x in range(0, self.SLOTS_IN_WEEK):
            pos = random.randint(0, len(items)-1)
            selected_item = items.pop(pos)
            schedule.append(selected_item)

        return schedule
