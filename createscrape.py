import requests
import codecs
import datetime

def add_to_readme(date_str, data_pass):
    with open('README.md', 'a') as f:
        f.write(f'## {date_str}\n\n')
        f.write(f'{data_pass}\n\n')

def createAndScrape(language, filename, yearString, dateString, isToday=False):
    filename = '{date}.md'.format(date=dateString)

    # createMarkdown(dateString, filename)

    HEADERS = {
        'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'	: 'gzip,deflate,sdch',
        'Accept-Language'	: 'zh-CN,zh;q=0.8'
    }

    # f string https://raw.githubusercontent.com/dubuqingfeng/yarb-web3/main/archive/2023/2023-01-01.md

    if isToday:
        url = 'https://raw.githubusercontent.com/dubuqingfeng/yarb-web3/main/today.md'
    else:
        url = f'https://raw.githubusercontent.com/dubuqingfeng/yarb-web3/main/archive/{yearString}/{dateString}.md'

    # url = 'https://raw.githubusercontent.com/dubuqingfeng/yarb-web3/main/today.md'
    print(url)
    r = requests.get(url, headers=HEADERS)
    assert r.status_code == 200

    # print(r.content)
    
    # d = pq(r.content)
    # items = d('div.Box article.Box-row')

    with codecs.open(filename, "a", "utf-8") as f:
        f.write('#### {language}\n'.format(language=language))

        # strdate2 = datetime.datetime.now().strftime('%Y-%m-%d')
        # minus one day
        # strdate2 = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        # print(strdate2)
        # remove # 每日 web3 资讯（2023-11-02) line
        content = r.content.decode('utf-8')

        # use date string to replace date in # 每日 web3 资讯（2023-11-02) 
        datestring1 = '# 每日 web3 资讯'
        # content = content.replace(f'# 每日 web3 资讯（{dateString}) ', '')
        content = content.replace(datestring1, '-')

        translated_text = translate_chinese_to_english(content)
        print(translated_text)

        f.write(content)


    # add_to_readme(dateString, content)
