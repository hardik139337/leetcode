class LUPrefix:
    def __init__(self, n: int):
        self.longestData = 0

        self.setArr = [False] * (n + 1)

    def upload(self, video: int) -> None:
        if self.longestData + 1 == video:
            self.longestData += 1
        else:
            self.setArr[video] = True
            return

        while (self.longestData + 1) < len(self.setArr) and self.setArr[
            (self.longestData + 1)
        ]:
            self.longestData += 1

    def longest(self) -> int:
        return self.longestData
