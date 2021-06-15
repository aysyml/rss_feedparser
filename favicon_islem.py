from newspaper import Article
#Farklı haber siteleri için denenmeli,bazı sonuçlar gelmeyecektir.
url = 'https://www.posta.com.tr/'
haber = Article(url)
print("Download :", haber.download())  # print yapmamıza gerek yok
print("HTML : ", haber.html)
print("PARSE :", haber.parse())
print("AUTHORS :", haber.authors)
print("PUBLISH DATE :", haber.publish_date)
print("TEXT :" , haber.text)
print("IMAGE :" ,haber.images)
print("TOP IMAGE : ", haber.top_image)
print("MOVIES :" ,haber.movies)
print("NLP :" , haber.nlp())
print("SUMMARY :", haber.summary)
print("KEYWORD :" ,haber.keywords)
