class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Fixed: Include all 12 months and match the variable name
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            return sum(days_in_months[:month - 1]) + day

        # Fixed: Unindented so they execute in the main method scope
        alice_arrive = date_to_day_of_year(arriveAlice)
        alice_leave = date_to_day_of_year(leaveAlice)
        bob_arrive = date_to_day_of_year(arriveBob)
        bob_leave = date_to_day_of_year(leaveBob)

        latest_arrival = max(alice_arrive, bob_arrive)
        earliest_leave = min(alice_leave, bob_leave)

        if latest_arrival <= earliest_leave:
            return earliest_leave - latest_arrival + 1

        return 0