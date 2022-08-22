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

    list = soup.find_all('div', class_='SubGroup')

    item_list = soup.find('div', id='sgContainer')

    megalist = {}
    print(megalist)
    for each in item_list.children:
        name = each.find('div', class_='SubGroupTitle').h2.text
        provider = 'Thorlabs'

        tbody = each.find(
            'div', class_='row SubGroupDescription').div.table.tbody

        print('==============================================')
        price_table = each.find('div', class_='partnumbers').form.table.tbody

        counter = 0
        for tr in tbody:
            print('...........')
            td = tr.text.split('\n')
            pr_sec1 = price_table.contents[counter].text.split('Uncoated')

            if len(td) > 2:
                pr_sec2 = pr_sec1[1].split(' €')
                model = td[1]
                megalist[model] = {
                    'provider': provider,
                    'name': name,
                    'diameter': td[2],
                    'focal_length': td[3],
                    'radius_of_curvature': td[5],
                    'center_thickness': td[6],
                    'edge_thickness': td[7],
                    'coading': "Uncoated",
                    'price': f"{pr_sec2[0]} €",
                    'availability': pr_sec2[1]
                }
                counter += 1

    print('--------')
    print(megalist)
