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

        return result

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().countAndSay(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
