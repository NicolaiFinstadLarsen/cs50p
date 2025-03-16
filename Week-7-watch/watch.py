import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    # [^>] is non gready, meaning we only capture everything until first instance of >
    # Same goes for the accutall URL: Everything up until the ' or "
    if match := re.search(r"<iframe[^>]+src=['\"](https?://[^'\"]+)['\"]", s, re.IGNORECASE):
        if "youtube." in match.group(1):
            # Using non capture group to find the embed text in URL
            # Extracting what is behind using \w atleast once.
            if match_2 := re.search(r"(?:embed/)([\w]+)", match.group(1)):
                # Cat the video id to the short form URL
                text_2 = "https://youtu.be/"+match_2.group(1)
                return text_2
    else:
        return None

if __name__ == "__main__":
    main()