class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = [False] * len(rooms)
        unlocked[0] = True
        def dfs(key: int):
            unlocked[key] = True
            for k in rooms[key]:
                if unlocked[k] == False:
                    dfs(k)
        dfs(0)
        return True if all(unlocked) else False
        