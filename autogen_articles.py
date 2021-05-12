import requests
import yaml
from os import walk, listdir
import sys

gh_dr = sys.argv[1]

def get_yml(inp):
    with open(inp) as file:
        documents = yaml.full_load(file)
        pub = {}
        for item, doc in documents.items():
            pub[item] = doc
    return pub

def get_list(path):
    out = []
    for file in listdir(path):
        if file.endswith(".yml"):
            out.append(file)
    return out

yaml_user = get_list(gh_dr + '/data/research_edit')
yaml_exists = get_list(gh_dr + '/data/research_autogen')
to_proc = list(set(yaml_user) - set(yaml_exists))

if not(to_proc):
    print('MRpub >>>>> Already up-to-date, nothing to process.')

for cur_yml in to_proc:
    print('MRpub >>>>> Creating website data for: ' + cur_yml)
    pub = get_yml(gh_dr + '/data/research_edit/' + cur_yml)
    response = requests.get('https://api.semanticscholar.org/v1/paper/' + pub['doi']) # Abstract 
    response2 = requests.get('http://api.crossref.org/works/' + pub['doi']) # Affiliations 
    if response.status_code == 200 and response2.status_code == 200:
        response = response.json()
        response2 = response2.json()
        response2 = response2['message']
        pub['authors'] = response2['author']
        for ii in range(len(pub['authors'])):
            pub['authors'][ii]['affiliation'] = pub['authors'][ii]['affiliation'][0]['name']
        pub['article_url'] = 'https://doi.org/' + pub['doi']
        pub['title'] = response['title']
        pub['abstract'] = response['abstract']
        with open('data/research_autogen/' + cur_yml, 'w') as outfile:
            yaml.dump(pub, outfile, default_flow_style=False)
    else: 
        print('MRpub >>>>> Cannot find semanticscholar entry for: ' + pub['doi'] + cur_yml) 