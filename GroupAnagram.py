#groupAnagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        HashMap = {}
        output = []

        for items in strs:
            sorted_items = "".join(sorted(items))

            if sorted_items not in HashMap.keys():
                HashMap[sorted_items] = [items]
            else:
                HashMap[sorted_items] == HashMap[sorted_items].append(items)

        for items in HashMap.keys():
            output.append(HashMap[items])

        return output

