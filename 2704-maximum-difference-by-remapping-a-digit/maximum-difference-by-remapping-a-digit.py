class Solution:
    def minMaxDifference(self, num: int) -> int:
        mini = str(num)
        maxi = str(num)
        for ch in maxi:
            if ch != '9':
                maxi = maxi.replace(ch,'9')
                break
        for ch in mini:
            if ch != '0':
                mini = mini.replace(ch,'0')
                break

        return int(maxi) - int(mini)