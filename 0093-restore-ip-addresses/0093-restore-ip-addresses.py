class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []

        def createIP(idx, expr, dots):
            if dots > 4:
                return
            if idx == n:
                if dots == 4:
                    ans.append(expr)
                return

            for i in range(idx, min(idx + 3, n)):
                curr = s[idx:i + 1]
                if len(curr) > 1 and curr[0] == "0":
                    break
                if int(curr) <= 255:
                    if idx == 0:
                        createIP(i + 1, curr, dots + 1)
                    else:
                        createIP(i + 1, expr + "." + curr, dots + 1)
                else:
                    break

        createIP(0, "", 0)
        return ans