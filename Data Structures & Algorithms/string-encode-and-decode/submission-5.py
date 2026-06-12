class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f'{len(s)}#{s}' for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = s[i:j]
            sizeInt = int(size)
            res.append(s[i+len(size)+1:i+len(size) + sizeInt + 1])
            i += len(size) + sizeInt + 1
        return res