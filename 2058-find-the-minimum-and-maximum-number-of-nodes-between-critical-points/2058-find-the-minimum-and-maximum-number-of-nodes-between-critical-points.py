class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next

        index = 1

        first = -1
        last = -1
        prev_critical = -1

        min_dist = float('inf')

        while curr.next:
            next_node = curr.next

            # Check whether curr is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = index
                else:
                    # Distance from previous critical point
                    min_dist = min(
                        min_dist,
                        index - prev_critical
                    )

                prev_critical = index
                last = index

            prev = curr
            curr = next_node
            index += 1

        # Need at least two critical points
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]