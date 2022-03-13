from math import log
from collections import defaultdict

class TransmissionIntegrity:

    def fix_message(self, original):
        # Your code goes here
        b = self.hex_to_bin(original)
        l = len(b)
        parity_indices = [2 ** n for n in range(int(log(l, 2)))]
        #parity_bits = [b[i] for i in parity_indices]
        # parity_checks = dict(zip(parity_indices, [0] * len(parity_indices)))
        parity_checks = defaultdict(int)
        for i in parity_indices:
            parity_checks[i] = sum(int(b[j]) for j in range(1, l) if (j // i) % 2 == 1) % 2

        if all(parity_checks[i] == 0 for i in parity_indices):
            return original
        #brute force
        #flipped_bit = [j for j in range(1, l) if all((j // i) % 2 == parity_checks[i] for i in parity_indices)][0]
        #new_bit = str((int(b[flipped_bit]) + 1) % 2)
        #b = b[:flipped_bit] + new_bit + b[flipped_bit + 1:]

        #halving
        positions=list(range(l))
        # values=list(parity_checks.values()) apparently I cannot rely on this having the correct order
        values = list(parity_checks[i] for i in parity_indices)
        flipped_bit = self.halving(positions,values)
        new_bit = str((int(b[flipped_bit]) + 1) % 2)
        b = b[:flipped_bit] + new_bit + b[flipped_bit + 1:]
        return self.bin_to_hex(b)


    def hex_to_bin(self, original):
        binary = bin(int(original, 16))[2:]
        l = len(binary)
        n_bits = self.first_power(l)
        bin_array = binary.zfill(n_bits)
        return bin_array

    def bin_to_hex(self, binary):
        # hd = (len(binary) + 3) // 4
        # x = '%.*x' % (hd, int('0b' + binary, 0))
        x = '{:x}'.format(int(binary, 2))
        return x

    def first_power(self, l):
        x = 0
        while l > 2 ** x:
            x += 1
        n = 2 ** x
        return n

    def halving(self,positions,values):
        n=len(positions)
        if n == 1:
            return positions[0]
        elif values[-1] == 0:
            return self.halving(positions[:n//2],values[:-1])
        else:
            return self.halving(positions[n // 2:], values[:-1])


