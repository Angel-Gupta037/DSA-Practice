from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(s):
            balance = 0
            for c in s:
                if c == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        def generate_all(curr, n, res):
            if len(curr) == 2 * n:
                if is_valid(curr):
                    res.append(curr)
                return
            generate_all(curr + '(', n, res)
            generate_all(curr + ')', n, res)

        
        res = []
        generate_all("", n, res)
        return res

        def main():
            result = generate_parenthesis(3)
            for s in result:
                print(s)

        if __name__ == "__main__":
            main()