# Last updated: 11/14/2025, 10:09:24 AM
class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        counter = 0 
        for i in range(len(seats)):
            counter += abs(seats[i] - students[i])
        return counter

        