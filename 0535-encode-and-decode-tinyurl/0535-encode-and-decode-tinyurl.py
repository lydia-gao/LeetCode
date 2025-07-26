class Codec:
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.base = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        if longUrl in self.url2code:
            return self.base + self.url2code[longUrl]
        code = str(self.counter)
        self.url2code[longUrl] = code
        self.code2url[code] = longUrl
        self.counter += 1
        return self.base + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.replace(self.base, "")
        return self.code2url[code]
