from math import sqrt


class FraudAlert:

    def detect_outliers(self, data_points):
        # Your code goes here
        x_coordinates = data_points[::2]
        y_coordinates = data_points[1::2]
        points = list(zip(x_coordinates, y_coordinates))
        C = {}

        for p in points:
            C[p] = min((self.distance(p, q), q) for q in points if q != p)

        isolated = []
        for p in points:
            q = C[p][1]
            cq = C[q][0]
            if self.distance(p, q) > 3 * cq:
                isolated.append(p)

        isolated = sum(list(map(lambda x: list(x), isolated)), [])
        return isolated

    def distance(self, p, q):
        d = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        return sqrt(d)


if __name__ == '__main__':
    solution = FraudAlert()
    print(solution.detect_outliers(
        [10, 10, -10, -10, 11, 10, -13, -12, 15, 18, 9, 11, -12, -8, -13, -12, -15, -10, 0, -13]))
