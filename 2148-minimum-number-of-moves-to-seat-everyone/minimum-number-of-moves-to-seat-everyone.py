class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_val = 0
        for s in seats:
            if s > max_val: max_val = s
        for st in students:
            if st > max_val: max_val = st
            
        seat_count = [0] * (max_val + 1)
        student_count = [0] * (max_val + 1)
        
        for s in seats: seat_count[s] += 1
        for st in students: student_count[st] += 1
        
        sorted_seats = [0] * len(seats)
        idx = 0
        for val in range(len(seat_count)):
            for _ in range(seat_count[val]):
                sorted_seats[idx] = val
                idx += 1
                
        sorted_students = [0] * len(students)
        idx = 0
        for val in range(len(student_count)):
            for _ in range(student_count[val]):
                sorted_students[idx] = val
                idx += 1
                
        ans = 0
        for i in range(len(sorted_seats)):
            ans += abs(sorted_students[i] - sorted_seats[i])
        return ans