import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

page=wikipedia.page("Machine Learning")
text= page.content

cloud = WordCloud().generate(text)
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(cloud, interpolation ="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
cloud.to_file("wordcloud.png")
