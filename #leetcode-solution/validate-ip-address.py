class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def ipv4(string):
            string = string.split(".")
            if len(string) != 4:
                return False
            for s in string:
                if not s.isnumeric():
                    return False
                if not (0 <= int(s) <=255):
                    return False
                if len(s) > 1 and s[0] == "0":
                    return False
            return True
        def ipv6(string):
            string = string.split(":")
            if len(string) != 8:
                return False
            for s in string:
                # print(s)
                if not 0 < len(s) <= 4:
                    return False
                for i in s:
                    # print(i)
                    if not (i.isnumeric() or "a" <= i <= "f" or "A" <= i <= "F"):
                        return False
            return True
        if ipv4(queryIP):
            return "IPv4"
        elif ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
                    
                    
            