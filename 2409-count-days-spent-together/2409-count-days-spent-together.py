class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str):
            # Extract month and day from the "MM-DD" format
            month = int(date_str[:2])
            day = int(date_str[3:])
            
            # Sum the days from all preceding months, then add the current day
            return sum(days_in_month[:month - 1]) + day
            
        # Convert all 4 dates into an absolute day index (1 to 365)
        a_arrive = date_to_day_of_year(arriveAlice)
        a_leave = date_to_day_of_year(leaveAlice)
        b_arrive = date_to_day_of_year(arriveBob)
        b_leave = date_to_day_of_year(leaveBob)
        
        # The overlapping period starts at the maximum of the arrivals
        # and ends at the minimum of the departures
        overlap_arrive = max(a_arrive, b_arrive)
        overlap_leave = min(a_leave, b_leave)
        
        # If overlap_leave < overlap_arrive, they never overlapped (returns 0)
        return max(0, overlap_leave - overlap_arrive + 1)