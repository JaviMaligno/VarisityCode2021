class Solution:

    def billion_switches(self, switch):
        # Your code goes here
        if not switch:
            return 0

        switch = sorted(switch)

        return self.recursion(switch)

    def recursion(self, switch):
        l = len(switch)
        if l == 1:
            return switch[0]

        first = switch[0]
        switch = list(map(lambda x: x - first, switch[1:]))
        if l % 2 == 0:
            return self.recursion(switch)
        else:
            return first + self.recursion(switch)
