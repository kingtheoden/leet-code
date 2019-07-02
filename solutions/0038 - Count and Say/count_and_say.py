class Solution:
    def countAndSay(self, n: int) -> str:

        def transmute_term(term_list):
            return [str(len(term_list)), term_list[0]]

        def get_next(last_string):
            collector = []
            result = []
            for char in last_string:
                if len(collector) == 0 or char == collector[0]:
                    collector.append(char)
                else:
                    result.extend(transmute_term(collector))
                    collector = [char]
            if len(collector) > 0:
                result.extend(transmute_term(collector))

            return ''.join(result)

        result = '1'

        for _ in range(n - 1):
            result = get_next(result)
            print(result)
        return result
                    
