class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            # Sum days of previous months + current day
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all four dates into day-of-the-year integers
        alice_arrive = date_to_day_of_year(arriveAlice)
        alice_leave = date_to_day_of_year(leaveAlice)
        bob_arrive = date_to_day_of_year(arriveBob)
        bob_leave = date_to_day_of_year(leaveBob)
        
        # Find the overlap interval
        latest_arrival = max(alice_arrive, bob_arrive)
        earliest_leave = min(alice_leave, bob_leave)
        
        # Calculate overlapping days
        if latest_arrival <= earliest_leave:
            return earliest_leave - latest_arrival + 1
        
        return 0