class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path = [*path]
        point = [0, 0]
        points = [[0,0]]
        status = False
        for i in path:
            if i == "N":
                point[1] += 1
            elif i == "E":
                point[0] += 1
            elif i == "S":
                point[1] -= 1
            elif i == "W":
                point[0] -= 1
            if point in points:
                status = True
            else:
                points.append(point[:])
        return status
