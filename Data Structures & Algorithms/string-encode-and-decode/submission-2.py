class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeTmp = []
        encoded = ""
        for i in range(len(strs)):
            length = len(strs[i])
            encodeTmp.append(f'{length}#{strs[i]}')
        encoded = ''.join(encodeTmp)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        j = 0
        length = len(s)

        while j < length:
            while s[j] != "#":
                j += 1
            number = int(s[i:j])
            i = j + 1
            j = i + number
            if j >= length:
                decoded.append(s[i:])
                return decoded
            decoded.append(s[i:j])
            i = j

        return decoded
