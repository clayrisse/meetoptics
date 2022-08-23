from bs4 import BeautifulSoup
import requests

# header just for chrome
header = {'User-Agent': 'Chrome/96.0.4664.110'}
s = requests.Session()

# opto_url = "https://www.optosigma.com/eu_en/optics/lens/es/spherical-lenses/plano-convex-spherical-lenses/spherical-lens-bk7-plano-convex-uncoated-SLB-P.html"
opto_url = "https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/spherical-lens-bk7-plano-convex-uncoated-SLB-P.html"
thor_url = "https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=112"

# r_opto = requests.get(opto_url).text
# with open('html_optosigma1.txt', 'w', encoding='utf-8') as file1:
#     file1.write(r_opto)
# file1.close()

# r_thor = requests.get(thor_url).text
# with open('html_thorlab2.txt', 'w') as file2:
# file.write(r_thor)
# file2.close()

json_list = {}

# time to add THORLAB
with open('html_optosigma.txt', 'r') as thor_html:
    opto_content = thor_html.read()
    opto_soup = BeautifulSoup(opto_content, 'lxml')
    opto_tbody = opto_soup.find('tbody', class_='grouped-items-body')
    json_list = {}
    for tr in opto_tbody:
        model = ''

        counter = 0
        for td in tr:
            if counter == 1:
                # print(td)
                # print('------------------------------')
                model = td.find('span', class_='sku-cell').text.strip()
                name = td.find('a', class_='link').text.strip()
                # print(model)
                json_list[model] = {
                    'provider': 'Optosigma',
                    'name': name
                }

            if counter == 9:
                price = td.find('span', class_="price-wrapper")
                json_list[model]['price'] = f"{price['data-price-amount']} €"

            if counter == 15:
                specs = td.find_all('tr')

                count = 0
                for spec in specs:
                    arr_spec = spec.text.strip().split('\n')
                    if 'material' in arr_spec[0].lower():
                        json_list[model]['material'] = arr_spec[2].strip()
                    if 'diameter' in arr_spec[0].lower():
                        json_list[model]['diameter'] = arr_spec[2].strip()
                    if 'focal length f' in arr_spec[0].lower():
                        json_list[model]['focal_length'] = arr_spec[2].strip()
                    if 'edge thickness' in arr_spec[0].lower():
                        json_list[model]['edge_thickness'] = arr_spec[2].strip()
                    if 'radius of curvature' in arr_spec[0].lower():
                        json_list[model]['radius_of_curvature'] = arr_spec[2].strip()
                    if 'center thickness' in arr_spec[0].lower():
                        json_list[model]['center_thickness'] = arr_spec[2].strip()
                    if 'edge thickness' in arr_spec[0].lower():
                        json_list[model]['edge_thickness'] = arr_spec[2].strip()
                    if 'coading' in arr_spec[0].lower():
                        json_list[model]['coading'] = arr_spec[2].strip()
                    if 'availability' in arr_spec[0].lower():
                        json_list[model]['availability'] = arr_spec[2].strip()
                    count += 1

            counter += 1

    print(json_list['SLB-30-500P'])

# time to add THORLAB
with open('html_thorlab.txt', 'r') as thor_html:
    thor_content = thor_html.read()
    soup = BeautifulSoup(thor_content, 'lxml')
    list = soup.find_all('div', class_='SubGroup')
    item_list = soup.find('div', id='sgContainer')

    for each in item_list.children:
        name = each.find('div', class_='SubGroupTitle').h2.text
        provider = 'Thorlabs'

        thor_tbody = each.find(
            'div', class_='row SubGroupDescription').div.table.tbody
        price_table = each.find('div', class_='partnumbers').form.table.tbody

        counter = 0
        for tr in thor_tbody:
            td = tr.text.split('\n')
            price_sec1 = price_table.contents[counter].text.split('Uncoated')

            if len(td) > 2:
                price_sec2 = price_sec1[1].split(' €')
                model = td[1]
                json_list[model] = {
                    'provider': provider,
                    'name': name,
                    'diameter': td[2],
                    'focal_length': td[3],
                    'radius_of_curvature': td[5],
                    'center_thickness': td[6],
                    'edge_thickness': td[7],
                    'coading': "Uncoated",
                    'price': f"{price_sec2[0]} €",
                    'availability': price_sec2[1]
                }
                counter += 1

print(json_list)

with open('json_list.txt', 'w') as file3:
    file3.write(str(json_list))
    # file3.close()
