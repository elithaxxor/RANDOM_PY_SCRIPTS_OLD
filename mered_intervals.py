'''
merge intervals of arrays. index 0 and -1 are not considerd interval. only in the middle
the first value in the middle interval set and the last value in the middle interval set get merged in the middle

ie [1,2][3,5],[9,3][,4,4]
sample: [1,2] [3,5], [4,4]
'''
intervals = [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]

def mergeOverlappingIntervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0]) # sorts by first index of inner arrays
    merged_intervals = []
    current_interval = sorted_intervals[0]  ##  ARRAY RERFECNE FOR LOOP TO COMPARE
    merged_intervals.append(current_interval)  # RESULTS

    print('intervals [input array]:, ', intervals) ## INPUT
    print('sorted intervals [by x vals]:, ', sorted_intervals)
    print('current intervals [the current interval for iteration] :, ', current_interval)
    print('merged intervals: [appends the current interval IF ] ', merged_intervals) ## RESULTS

    for next_interval in sorted_intervals:
        curr_start, curr_end = current_interval ## modifies array defined above
        next_start, next_end = next_interval  ## compares elements in loop array
        print(curr_start, curr_end)
        print(next_start, next_end)

        if curr_end >= next_start:
            current_interval[0] = max(curr_start, next_end)
            print(current_interval[0])
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)


def main():
    results =  mergeOverlappingIntervals(intervals)
    print(results)

if __name__ == '__main__':
    main()

