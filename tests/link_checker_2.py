import regex
body_markdown = "This is an [inline link](http://google.com). This is a [non inline link][4]\r\n\r\n  [1]: http://yahoo.com"

with open ("I:\\_dev_awake\\aceql-http-main\\Python\\aceql-http-client-python\\README.md", "r") as myfile:
    body_markdown=myfile.read()

rex = """(?|(?<txt>(?<url>(?:ht|f)tps?://\S+(?<=\P{P})))|\(([^)]+)\)\[(\g<url>)\])"""
pattern = regex.compile(rex)
matches = regex.findall(pattern, body_markdown, overlapped=True)
for m in matches:
    the_link:str = m[0]
    print(str)