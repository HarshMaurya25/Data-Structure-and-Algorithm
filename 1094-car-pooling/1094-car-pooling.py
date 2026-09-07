class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for people, start, end in trips:
            events.append((start, people))
            events.append((end, -people))

        events.sort()

        passengers = 0

        for location, change in events:
            passengers += change

            if passengers > capacity:
                return False

        return True
