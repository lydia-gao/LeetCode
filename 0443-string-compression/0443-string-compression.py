class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = ""
        chars.append(" ")
        count = 1
        pos = 1
        l = 1
        for i in range(len(chars)):
            if curr == "":
                curr = chars[i]
            elif (curr != chars[i]):
                if count != 1:
                    num = list(str(count))
                    chars[pos:pos+len(num)] = num
                    l += len(num) + 1
                else:
                    l += 1
                chars[pos - 1] = curr
                pos = l
                count = 1
                curr = chars[i]
                
            else:
                count += 1
                
        del chars[l - 1:]
        return l

