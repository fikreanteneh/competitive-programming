class Solution:
    def finalString(self, s: str) -> str:
        store = []
        for i in s:
            if i == "i":
                store.reverse()
            else:
                store.append(i)
        return "".join(store)