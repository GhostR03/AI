def job_sequencing():
    n = int(input("Enter the number of jobs: "))

    job = []
    deadline = []
    profit = []

    for i in range(n):
        print("\nJob ",i+1)
        job.append(input("Enter job name: "))
        deadline.append(int(input("Enter deadline for job : ")))
        profit.append(int(input("Enter profit for job : ")))

    max_deadline = max(deadline)

    sorted_jobs = sorted(zip(job, deadline, profit), key=lambda x: x[2], reverse=True)

    schedule = [None] * max_deadline
    total_profit = 0

    for j in sorted_jobs:
        current_deadline = j[1]
        slot = current_deadline - 1

        while slot >= 0:
            if schedule[slot] is None:
                schedule[slot] = j[0]
                total_profit += j[2]
                break
            slot -= 1

    return schedule, total_profit

# Example usage
schedule, total_profit = job_sequencing()

print("Job Schedule:")
for i in range(len(schedule)):
    if schedule[i] is not None:
        print("Time Slot", i+1, ":", schedule[i])

print("Total Profit:", total_profit)
































#
# The `job_sequencing` function is used to solve a job sequencing problem where each job has a deadline and a profit associated with it. The goal is to maximize the total profit by scheduling jobs within their deadlines.
#
# Here's how the function works:
#
# 1. **Input Gathering:**
#    - The user is prompted to enter the number of jobs (`n`).
#    - For each job, the user provides the job name, deadline, and profit.
#
# 2. **Sorting:**
#    - The jobs are sorted in descending order of profit using `sorted` and `lambda` functions. This ensures that higher-profit jobs are considered first.
#
# 3. **Scheduling:**
#    - A schedule list is initialized with `None` values, with a length equal to the maximum deadline among the jobs.
#    - Each job is considered in the sorted order.
#    - For each job, starting from its deadline:
#      - If the time slot is empty (`None`), the job is scheduled in that slot, and its profit is added to the total profit.
#      - If the slot is already occupied, the algorithm looks for the previous available slot until an empty slot is found.
#
# 4. **Output:**
#    - The function returns the schedule (list of job names) and the total profit obtained.
#
# **Example Usage:**
# Suppose we have three jobs with the following details:
# - Job 1: Deadline = 2, Profit = 100
# - Job 2: Deadline = 1, Profit = 50
# - Job 3: Deadline = 2, Profit = 200
#
# The sorted order based on profit would be: Job 3, Job 1, Job 2.
#
# The schedule would be:
# - Time Slot 1: Job 3
# - Time Slot 2: Job 1
#
# Total Profit: 300
#
# This algorithm ensures that jobs are scheduled optimally to maximize profit while meeting their deadlines.
