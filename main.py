import json
import time
from urllib.parse import urlparse


with open('G:\\aparser\\results\\Дима\\articles\\auction-domains.txt') as res_file:
    lines = res_file.readlines()

dict_result = {}


for line in lines:
    line = line.rstrip('\n')
    line_json = json.loads(line)
    donor_domain = line_json['query']
    donor_domain_url = urlparse(donor_domain).netloc
    if 'www.' in donor_domain_url:
        donor_domain_url = donor_domain_url.replace('www.', '')

    ext_links = line_json['links_ext']
    for out_link in ext_links:
        out_domain = urlparse(out_link).netloc

        if 'www.' in out_domain:
            out_domain = out_domain.replace('www.', '')


        if dict_result.get(donor_domain_url) is None:
            dict_result[donor_domain_url] = {out_domain: 1}
        else:
            if dict_result.get(donor_domain_url).get(out_domain) is None:
                dict_result[donor_domain_url][out_domain] = 1
            else:
                qty = dict_result[donor_domain_url][out_domain] + 1
                dict_result[donor_domain_url][out_domain] = qty


file_result = 'res.txt'

final_money_site_check = {}

for pbn_domain in dict_result:
    # print(pbn_domain, dict_result[pbn_domain])
    for money_domain in dict_result[pbn_domain]:
        if final_money_site_check.get(money_domain) is None:
            final_money_site_check[money_domain] = {'qty': 1,
                                                    'pbn_domains': [pbn_domain]}
        else:
            qty = final_money_site_check[money_domain]['qty'] + 1
            final_money_site_check[money_domain]['qty'] = qty

            pbn_domains = final_money_site_check[money_domain]['pbn_domains']
            if pbn_domain not in final_money_site_check[money_domain]['pbn_domains']:
                final_money_site_check[money_domain]['pbn_domains'].append(pbn_domain)

# print(final_money_site_check)

for money_domain in final_money_site_check:
    if final_money_site_check[money_domain]['qty'] >= 2:
        print(money_domain, final_money_site_check[money_domain])
""""
{'domain': {'out_domain1': 1,
            'out_domain2': 2,
            'out_domain3': 3
            }
"""