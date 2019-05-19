# numbers os rooms = max( intersections at same time)
# 0(N²)
def how_many_rooms(time):
    result = 0
    for x in time:
        count_rooms = -1  # x always intersect with himself
        for y in time:
            if check_intersection(x, y):
                count_rooms +=1
        if count_rooms > result:
            result = count_rooms
    return result


def check_intersection(x, y):
    if x[1] > y[0] and x[0] < y[1]:
        return True


# O (N*log N)
def how_many_rooms2(time_intervals):
    starts = []
    ends = []
    for class_time in time_intervals:
        starts.append(class_time[0])
        ends.append(class_time[1])

    starts.sort()
    ends.sort()
    
    index_start = 0
    index_end = 0
    current_rooms = 0
    max_rooms_used_at_same_time = 0
    while index_start < len(time_intervals) and index_end < len(time_intervals):
        if starts[index_start] < ends[index_end]:
            current_rooms += 1
            index_start += 1
        else:
            current_rooms -= 1
            index_end += 1
        max_rooms_used_at_same_time = max(max_rooms_used_at_same_time, current_rooms)
    return max_rooms_used_at_same_time


time_intervals = [(30, 75), (0, 50), (60, 150), (40, 70)]
print(how_many_rooms(time_intervals))
print(how_many_rooms2(time_intervals))