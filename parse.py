import markdown
import re
import translate
import pinyin
from deep_translator import GoogleTranslator

def parse_links(markdown_text):
    link_info = []

    # Parse the Markdown content
    html_content = markdown.markdown(markdown_text)

    # Use regular expressions to find links in the HTML content
    link_pattern = re.compile(r'<a\s+href=["\'](https?://.*?)(?:["\']|\s|>)\s*>(.*?)<\/a>')
    matches = link_pattern.findall(html_content)

    for url, title in matches:
        link_info.append({'url': url, 'title': title})

    return link_info

# Example usage
markdown_text = """
#### Web3 Daily News Feed
-（2023-11-03）

- Stories by melody on Medium
  - [第四阶段结束，标志着 Altitude 活动系列的结束](https://medium.com/@melody8848/%E7%AC%AC%E5%9B%9B%E9%98%B6%E6%AE%B5%E7%BB%93%E6%9D%9F-%E6%A0%87%E5%BF%97%E7%9D%80-altitude-%E6%B4%BB%E5%8A%A8%E7%B3%BB%E5%88%97%E7%9A%84%E7%BB%93%E6%9D%9F-b483d67d66e1?source=rss-bfc6f454c0f9------2)
- Longreads
  - [Cowgirls All the Way](https://longreads.com/2023/11/02/cowgirls-all-the-way/)
  - [‘I Remember The Silence Between The Falling Shells’: The Terror of Living Under Siege as a Child](https://longreads.com/2023/11/02/i-remember-the-silence-between-the-falling-shells-the-terror-of-living-under-siege-as-a-child/)
  - [The Club No School Principal Wants to Join](https://longreads.com/2023/11/02/the-club-no-school-principal-wants-to-join/)
  - [Children of War](https://longreads.com/2023/11/02/russia-ukraine-war-pregnant-women-atavist-magazine/)
- Matt Levine - Bloomberg Opinion Columnist
  - [The Banks Are Where the Money Isn’t](https://www.bloomberg.com/opinion/articles/2023-11-02/the-banks-are-where-the-money-isn-t)
- Ethereum Research - Latest posts
  - [The Influence of CeFi-DeFi Arbitrage on Order-Flow Auction Bid Profiles](https://ethresear.ch/t/the-influence-of-cefi-defi-arbitrage-on-order-flow-auction-bid-profiles/17258/3)
- FYI - For Your Innovation
  - [Bitcoin’s Most Under-Explored Use Cases](https://ark-invest.com/podcast/bitcoin-brainstorm-04-bitcoins-most-under-explored-use-cases/)
- Messari Crypto News Feed
  - [0x Q3 2023 Brief](https://messari.io/article/0x-q3-2023-brief)
  - [Spoiler Alert – Coinbase Q3 Revenue Estimates](https://messari.io/article/spoiler-alert-coinbase-q3-revenue-estimates)
  - [Fully Homomorphic Encryption, the Holy Grail of Computing](https://messari.io/article/fully-homomorphic-encryption-the-holy-grail-of-computing)
  - [State of Goldfinch Q3 2023](https://messari.io/article/state-of-goldfinch-q3-2023)
  - [State of Polygon Q3 2023](https://messari.io/article/state-of-polygon-q3-2023)
- I'm TualatriX
  - [谈谈定购 M3 Max 的 16 寸 MacBook Pro 后的一些想法](https://imtx.me/blog/thoughts-after-ordering-16-inch-m3-max-macbook-pro/)
- BanklessDAO - Medium
  - [How To Win A Hackathon](https://medium.com/bankless-dao/how-to-win-a-hackathon-ca7e3fca1dff?source=rss----2e8b6adb479c---4)
"""
# links = parse_links(markdown_text)

translated = GoogleTranslator(source='auto', target='english').translate(markdown_text)
print(markdown_text)

# for link in links:
    # print(f"URL: {link['url']}, Title: {link['title']}")
    # translated_title = translate(link['title'])
    # print(pinyin.get(link['title'], format="strip", delimiter=" "))

    