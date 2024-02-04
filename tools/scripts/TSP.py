import math


class IncPoint:
    # The class of point with integer coordinates.
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class TSP:
    INF = float('inf')

    # The class of Traveling Salesman Problem.
    def __init__(self):
        self.n = 0

    # Calculate the distance between two points.
    def calculate_distance(self, p1, p2):
        distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
        return distance

    # Initialize the number of points and the distance between points.
    def intialization(self):
        # The number of points.
        self.n = len(self.points)
        self.points.append(self.start)
        # If the number of points is less than 1, return the points.
        if self.n <= 1:
            return self.points
        # dist[i][j]: the distance between point i and point j.
        self.dist = [[self.INF] * (self.n + 1) for _ in range(self.n + 1)]
        # dp[mask][i][0]: the shortest distance from start to point i with the mask.
        # dp[mask][i][1]: the previous point of point i with the mask.
        for i in range(self.n):
            for j in range(i + 1, self.n + 1):
                self.dist[i][j] = self.calculate_distance(
                    self.points[i], self.points[j])
                self.dist[j][i] = self.dist[i][j]

    # Using the greedy algorithm to find the shortest path (Traveling Salesman Problem).
    def tsp_gd(self):
        # Initialize section.

        self.intialization()
        points = self.points
        dist = self.INF
        min_idx = -1
        for i in range(self.n - 1):
            if self.calculate_distance(points[self.n], points[i]) < dist:
                dist = self.calculate_distance(points[self.n], points[i])
                min_idx = i
        path = [self.points[min_idx]]
        points.pop(min_idx)
        min_dist = dist

        # Greedy algorithm section.

        for i in range(self.n - 2):
            dist = self.INF
            min_idx = -1
            for j in range(self.n - i - 2):
                if self.calculate_distance(path[i], points[j]) < dist:
                    dist = self.calculate_distance(path[i], points[j])
                    min_idx = j
            path.append(points[min_idx])
            points.pop(min_idx)
            min_dist += dist

        # Return path section.

        return path, min_dist

    # Using the dynamic programming algorithm to find the shortest path (Traveling Salesman Problem).
    def tsp_dp(self):
        # Initialize section.

        self.intialization()
        # dp[mask][i][0]: the shortest distance from start to point i with the mask.
        # dp[mask][i][1]: the previous point of point i with the mask.
        dp = [[[self.INF, self.n]
               for _ in range(self.n)] for _ in range(1 << self.n)]
        for i in range(self.n):
            dp[1 << i][i][0] = self.dist[i][self.n]

        # Dynamic programming section.

        # mask: the mask of points.
        for mask in range(1 << self.n):
            # i: the index of the last point.
            for i in range(self.n):
                if not (mask & (1 << i)):
                    continue
                # j: the index of the next point.
                for j in range(self.n):
                    if mask & (1 << j):
                        continue
                    # new_mask: the mask of the next point.
                    new_mask = mask | (1 << j)
                    if dp[new_mask][j][0] > dp[mask][i][0] + self.dist[i][j]:
                        dp[new_mask][j][0] = dp[mask][i][0] + self.dist[i][j]
                        dp[new_mask][j][1] = i

        # Backtracking path section.

        # min_dist: the shortest distance.
        min_dist = self.INF
        # index: the index of the last point.
        index = -1
        for i in range(self.n):
            if dp[(1 << self.n) - 1][i][0] < min_dist:
                min_dist = dp[(1 << self.n) - 1][i][0]
                index = i
        # return_idx: the mask of the last point.
        return_idx = (1 << self.n) - 1 - (1 << index)
        # path: the shortest path.
        path = [self.points[index]]
        while return_idx > 0:
            index = dp[return_idx + (1 << index)][index][1]
            return_idx -= (1 << index)
            path.insert(0, self.points[index])

        return path, min_dist

    def flow(self):
        self.num = (
            input("Please input the number of points (input other characters to exit): "))
        try:
            num = int(self.num)
        except ValueError:
            print("Exit.")
            return False
        if num <= 0:
            print("Error: the number of points must be greater than 0.")
            return True
        if num > 20:
            print(
                "Warning: the number of points is greater than 20, it may take a long time to calculate.")
            if_continue = input("Do you want to continue? (y/[others]): ")
            if if_continue != 'y' and if_continue != 'Y' and if_continue != 'yes' and if_continue != 'Yes':
                print("Why not trust your computer?")
                return True
            else:
                print("Please wait patiently.")
        self.points = []
        for i in range(num):
            try:
                x, y = input("Please input the coordinates of point %d: " %
                             (i + 1)).split()
                self.points.append(IncPoint(int(x), int(y)))
            except ValueError:
                print("Error: illegal input.")
                return True
        self.start = IncPoint(0, 0)
        path_dp, min_dist_dp = self.tsp_dp()
        path_gd, min_dist_gd = self.tsp_gd()
        print("\nStarting from point (0, 0), the shortest path is:\nalgorithm:\t     greedy\t       dynamic programming")
        for i in range(len(path_dp)):
            print("%9d:\t|%5d%5d    |\t|%5d%5d    |" % (i + 1, path_gd[i].x, path_gd[i].y, path_dp[i].x, path_dp[i].y))
        print(" distance:\t|%10.4f    |\t|%10.4f    |" % (min_dist_gd, min_dist_dp))
        return True


def main():
    tsp=TSP()
    while tsp.flow():
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
