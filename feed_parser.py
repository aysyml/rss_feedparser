import feedparser
import webbrowser

# Rss bulma = urlin sonuna rss.xml,rss,rss.html,siitemap.xml,robots.txt yaparak bulunur.
# Yukarıdaki işlemlerde kesin sonuç elde edilmeyebilir.Bazı haber sitelerinin rss lerini bulmak zor olabiliyor,bulunamayabiliyor.

feed = feedparser.parse("https://www.haberturk.com/rss/manset.xml")

title_al = feed['feed']['title']
entries_al = feed.entries

for entry in feed.entries:
    baslik = entry.title
    link = entry.link
    yayinlanma_tarihi = entry.published
    yayinlanma_tarihi_parse = entry.published_parsed

    print("Başlık :" + baslik, "Link :" + link)
    print("Yayınlanma Tarihi :", yayinlanma_tarihi)
