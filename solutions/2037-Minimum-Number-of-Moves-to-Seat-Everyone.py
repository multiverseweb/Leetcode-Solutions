class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        m=0
        for i in range(len(seats)):
            m+=abs(seats[i]-students[i])
        return m