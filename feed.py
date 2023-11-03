import feedparser
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from my_custom_package import add_to_readme, add_link_to_readme

url = "https://0xsoros.substack.com/feed"

feed = feedparser.parse(url)

print("Feed Title:", feed.feed.title)
print("Feed Description:", feed.feed.description)

# Iterate through the feed entries
for entry in feed.entries:
    # print(entry)
    # print("\nTitle:", entry.title)
    # print("Link:", entry.link)
    # print("Published:", entry.published)
    # print("Summary:", entry.summary)
    # print("-" * 50)

    # Make markdown links 
    print(f"* [{entry.title}]({entry.link})") 

    add_link_to_readme(f"* [{entry.title}]({entry.link})")