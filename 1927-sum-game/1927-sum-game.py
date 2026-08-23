class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        def get(s: str) -> (int, int):
            n = q = 0
            for ch in s:
                if ch == "?":
                    q += 1
                else:
                    n += int(ch)
            return n, q

        n0, q0 = get(num[: n // 2])
        n1, q1 = get(num[n // 2 :])

        return (q0 + q1) % 2 == 1 or n0 - n1 != (q1 - q0) * 9 // 2
        