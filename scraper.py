from bs4 import BeautifulSoup
import requests
import scrapy

# header just for chrome
header = {'User-Agent': 'Chrome/96.0.4664.110'}
s = requests.Session()


def htmlgetter(url): return BeautifulSoup(
    s.get(url1, headers=header).content, 'html.parser').prettify()
# return


url1 = "https://www.optosigma.com/eu_en/optics/lens/es/spherical-lenses/plano-convex-spherical-lenses/spherical-lens-bk7-plano-convex-uncoated-SLB-P.html"
# r1 = s.get(url1, headers=header)
# soup1 = BeautifulSoup(r1.text, 'html.parser')
# print(soup1.prettify())
print(htmlgetter(url1))

# url2 = "https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=112"
# r2 = s.get(url2, headers=header)
# soup2 = BeautifulSoup(r2.text, 'html.parser')
# print(soup2.prettify())


# r5 = requests.get('https://api.github.com/events')
# print(r5)
# r5.json()

# print(r5)


# iframe_src = soup2.find("iframe").attrs['src']
# print(iframe_src)

# # r3 = s.get("https:{iframe_src}")
# r3 = s.get("https:{'//claudialayrisse.com'}")

# soup3 = BeautifulSoup(r3.content, "html.parser")
# print(soup3.prettify())

# for row in soup.select(".history-tb tr"):
#     print("\t".join([e.text for e in row.select("th, td")]))

# iFrames=[] # qucik bs4 example
# for iframe in soup("iframe"):
#     iFrames.append(soup.iframe.extract())


# iFrames = []  # qucik bs4 example
# iframexx = soup2.find_all('iframe')
# # for iframe in iframexx:
# #     print iframe.find_all('html')

# for iframe in iframexx:
#     response = requests(iframe.attrs['src'])


#     iframe_soup2 = BeautifulSoup(response)
#     with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()

# print(iframe_soup2.prettify())

# {
#   'LA1116': {
#     'provider': 'Thorlabs',
#     'price': 19.39,
#     'diameter': 6.0,
#     'focal_length': 10.0,
#     'edge_thickness': 1.5
#   },
#   'SLB-20-40P': {
#     'provider': 'OptoSigma',
#     'price': 16.40,
#     'diameter': 20,
#     'focal_length': 40,
#     'edge_thickness': 2
#   }
# }
