class Solution:
    def reverse(self, x: int) -> int:
            hoge = str(x)
            print(hoge)
            if hoge[0] == '-':
                a = hoge[0]
                b = hoge[1:]
                c = b[::-1]
                d = a + c
                result = int(d)
                if result >= 2147483647 or result <= -2147483648:
                    return 0
                else:
                    return result
            else:
                hage = hoge[::-1]
                print(hage)
                result = int(hage)
                if result >= 2147483647 or result <= -2147483648:
                    return 0
                else:
                    return result
