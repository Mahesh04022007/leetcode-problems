from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # [left, right, weight, original index]
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        arr.sort()

        starts = [x[0] for x in arr]

        # Find first interval with left > current right
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        @lru_cache(None)
        def dp(i, k):

            if i == n or k == 0:
                return (0, ())

            # Don't take current interval
            skip_score, skip_indices = dp(i + 1, k)

            # Take current interval
            take_score, take_indices = dp(nxt[i], k - 1)

            take_score += arr[i][2]

            # Add original index and keep indices sorted
            take_indices = tuple(
                sorted((arr[i][3],) + take_indices)
            )

            # Better score
            if take_score > skip_score:
                return take_score, take_indices

            if skip_score > take_score:
                return skip_score, skip_indices

            # Same score:
            # choose lexicographically smaller index array
            if take_indices < skip_indices:
                return take_score, take_indices
            else:
                return skip_score, skip_indices

        return list(dp(0, 4)[1])