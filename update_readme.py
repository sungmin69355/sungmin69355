import feedparser 
applepick_blog_rss_url = "https://applepick.tistory.com/rss" 
rss_feed = feedparser.parse(applepick_blog_rss_url)

MAX_POST_NUM = 10 
latest_blog_post_list = "" 
MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']): 
  if idx > MAX_POST_NUM: 
    break 
  feed_date = feed['published_parsed'] 
  latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n" 
  
markdown_text = """

<h3 align="center"><b>🛠 Tech Stack 🛠</b></h3>
</br>
<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></a> &nbsp
<img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=Node.js&logoColor=white"/></a> &nbsp
<!-- <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=Android&logoColor=white"/></a> &nbsp -->
<img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=MongoDB&logoColor=white"/></a> &nbsp 
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/></a> &nbsp 
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon%20AWS&logoColor=white"/></a> &nbsp </p>


![Sungmin's GitHub stats](https://github-readme-stats.vercel.app/api?username=sungmin69355&show_icons=true&theme=radical)
[![Sungmin's github stats](https://github-readme-stats.vercel.app/api/top-langs/?username=sungmin69355&show_icons=true&hide_border=true&title_color=004386&icon_color=004386&layout=compact)](https://github.com/sungmin69355)


😎 Latest Blog Post

"""

readme_text = f"{markdown_text}{latest_blog_post_list}" 
with open("README.md", 'w', encoding='utf-8') as f: 
  f.write(readme_text)
