class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda pair: pair[0])
        rooms = [0] * n
        meetingCount = [0] * n

        for s,e in meetings:
            minRoom = 0
            found=False
            for i in range(n):
                if rooms[i]<=s:
                    found=True
                    meetingCount[i]+=1
                    rooms[i]=e
                    break
                
                if rooms[minRoom]>rooms[i]:
                    minRoom = i
            
            if found:
                continue
            meetingCount[minRoom] += 1
            rooms[minRoom] += e-s

        return meetingCount.index(max(meetingCount))
        