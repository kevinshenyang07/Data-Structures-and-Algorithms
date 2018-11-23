import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, TimeoutError, as_completed

# give N very large files (numbers inside), and unlimited machines
# and an API int computeSum(fileID, machineID), which compute the sum of numbers in that file
# get the overall sum
# followup1: sometimes a machine will be blocked for issues, and the result has an additional field
#            'status' to indicate, write a wrapper to timeout that call and recompute
# followup2: there's p probability that computeSum will give a wrong subtotal, find a way to
#            make the overall probability of wrong result less than p

class Aggregator(object):
    # assume there's a resource manager with an API next_machine_id()
    def __init__(self, file_ids, agg_func):
        self.file_ids = collections.deque(file_ids)
        self.result = 0
        self.agg_func = agg_func

        self.executor = ThreadPoolExecutor(max_workers=50)
        self.mgr = ResourceManager()

    def process(self):
        future_to_file_id = self.submit_tasks()
        # if possible, yield futures that are completed
        for future in as_completed(future_to_file_id):
            file_id = future_to_file_id[future]
            try:
                sub_result = future.result(timeout=3600)
                self.result += sub_result  # no need for lock
            except TimeoutError:
                self.submit_task(file_id)

    def submit_tasks(self):
        return { self.submit_task(file_id): file_id for file_id in self.file_ids}

    def submit_task(self, file_id):
        machine_id = self.mgr.next_machine_id()
        return self.executor.submit(self.aggregate, file_id, machine_id)

    def aggregate(self, file_id, machine_id):
        while True:
            sub_result, status = self.agg_func(file_id, machine_id))
            if status == 0:
                return sub_result
            # else:
            #     handle errors by status
