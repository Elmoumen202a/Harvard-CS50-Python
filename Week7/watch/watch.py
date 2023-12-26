import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r'src=[\'"]([^\'"]+)', s):
        link = re.search(r'src=[\'"]([^\'"]+)', s).group(1)
        if re.search(r'(youtube)', link):
            urlSplit = re.sub(r"^(https?://)?(www\.)?youtube\.com/([a-z0-9_]+)", "", link)
            return f"https://youtu.be{urlSplit}"


if __name__ == "__main__":
    main()