class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks = blocks
        k = k
        a = blocks[:k]
        c = a.count('W')

        for i in range(len(blocks)-k):
            a = a[1:] + blocks[i+k]
            c = min(c,a.count('W'))
        return c
