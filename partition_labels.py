class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # compute start interval
        # compute end interval
        last = {c:i for i,c in enumerate(S)}
        # print("last: ", last)
        intervals = []
        processed = set()
        for i,c in enumerate(S):
            if c not in processed:
                intervals.append([i, last[c]])
                processed.add(c)
        # intervals is a list of lists
        # print("intervals: ", intervals)
        anchor = intervals[0][0]
        last_end_point = intervals[0][1]
        # print("anchor: ", anchor)
        # print("last_end_point: ", last_end_point)
        
        partition_sizes = []
        flag = True
        
        for l,r in intervals[1:]:
            # if l >= last_end_point, we can create a new segment
            if l > last_end_point:
                partition_sizes.append(last_end_point-anchor+1)
                # update
                anchor = l
                last_end_point = r
            # otherwise, extend last endpoint if needed
            if r > last_end_point:
                last_end_point = r
            # print("processed: l", l, " r: ", r)
            # print("anchor: ", anchor)
            # print("last_end_point: ", last_end_point)
        partition_sizes.append(last_end_point-anchor+1) # why do we need to do this?
        
        # base case, nothing happens in the loop,
        # we started by initializing anchor, last and we haven't processed it
        
        # if we hit the first case in the loop, we assign an new anchor, last that we haven't procssed
        # if we hit the second case, we still have an unprocessed anchor, last
        # other wise, our interval is contained in the current interval, which is unprocessed
        
        return partition_sizes
