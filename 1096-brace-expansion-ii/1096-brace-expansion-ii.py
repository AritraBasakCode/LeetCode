class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        op = []
        stk = []

        def ope():
            l, r = len(stk) - 2, len(stk) - 1
            if op[-1] == "+":
                stk[l] |= stk[r]
            else:
                tmp = set()
                for left in stk[l]:
                    for right in stk[r]:
                        tmp.add(left + right)
                stk[l] = tmp
            op.pop()
            stk.pop()

        for i, ch in enumerate(expression):
            if ch == ",":
                while op and op[-1] == "*":
                    ope()
                op.append("+")
            elif ch == "{":
                if i > 0 and (
                    expression[i - 1] == "}" or expression[i - 1].isalpha()
                ):
                    op.append("*")
                op.append("{")
            elif ch == "}":
                while op and op[-1] != "{":
                    ope()
                op.pop()
            else:
                if i > 0 and (
                    expression[i - 1] == "}" or expression[i - 1].isalpha()
                ):
                    op.append("*")
                stk.append({ch})

        while op:
            ope()

        return sorted(stk[-1])