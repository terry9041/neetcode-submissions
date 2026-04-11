class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        max_count = 0
        total_count = 0
        for char in counts:
            count = counts[char]
            total_count += count
            max_count = max(max_count, count)
        n_max = 0
        for char in counts:
            count = counts[char]
            if count == max_count:
                n_max += 1
        return max(total_count, (n+1)*(max_count-1)+n_max)