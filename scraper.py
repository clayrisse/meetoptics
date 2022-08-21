from bs4 import BeautifulSoup
import requests


# header just for chrome
header = {'User-Agent': 'Chrome/96.0.4664.110'}
s = requests.Session()

opto_url = "https://www.optosigma.com/eu_en/optics/lens/es/spherical-lenses/plano-convex-spherical-lenses/spherical-lens-bk7-plano-convex-uncoated-SLB-P.html"
thor_url = "https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=112"
url3 = "https://www.claudialayrisse.com/"

# r1 = requests.get(opto_url, headers=header)
# with open('file10.txt', 'w') as file1:
# file.write(r1.text)

# r2 = requests.get(thor_url)
# with open('file20.txt', 'w') as file2:
# file.write(r2.text)


with open('file2.1.txt', 'r') as thor_html:
    thor_content = thor_html.read()
    soup = BeautifulSoup(thor_content, 'lxml')
    # print(soup)

    list = soup.find_all('div', class_='SubGroup')
    qq = soup.find_all('div', id='SG-13372')
    print(qq)

    # for each in list:

    # xx = each.find_all('div', class_='SubGroup')
    # xx = each.find_all('div', class_='SubGroupHeader')
    # print(xx)


# def html_getter(url): return BeautifulSoup(requests.get(
#     url).text, 'html.parser').prettify()
#     s.get(url).text, 'html.parser')


# print(html_getter(url2))


# def obj_builder(model, provider, price, diameter, focal_length, center_thickness, edge_thickness, coading, radius_of_curvature):
#     return {
#         'model': model,
#         'provider': provider,
#         'price': price,
#         'diameter': diameter,
#         'focal_length': focal_length,
#         'center_thickness': center_thickness,
#         'edge_thickness': edge_thickness,
#         'coading': coading,
#         'radius_of_curvature': radius_of_curvature
#     }


# tags = html_getter(url1).find_all(
#     "div", class_='product-box grouped-container')
# print(tags)
# for title in tags:
#     print(title.text)

# print(tags)
# print(html_getter(url2).prettify())


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
