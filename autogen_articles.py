import requests
import yaml
from os import walk

def get_yml(inp):
    with open(inp) as file:
        documents = yaml.full_load(file)
        pub = {}
        for item, doc in documents.items():
            pub[item] = doc
    return pub

_, _, yaml_user = next(walk('data/research_edit'))
_, _, yaml_exists = next(walk('data/research_autogen'))
yaml_user = [i for i in yaml_user if i.endswith('.yml')]
yaml_exists = [i for i in yaml_exists if i.endswith('.yml')]
to_proc = list(set(yaml_user) - set(yaml_exists))

if not(to_proc):
    print('Already up-to-date, nothing to process.')

for cur_yml in to_proc:
    print('Creating website data for: ' + cur_yml)
    pub = get_yml('data/research_edit/' + cur_yml)
    response = requests.get('https://api.semanticscholar.org/v1/paper/' + pub['doi'])
    if response.status_code == 200:
        response = response.json()
        pub['authors'] = response['authors']
        pub['title'] = response['title']
        pub['abstract'] = response['abstract']
        with open('data/research_autogen/' + cur_yml, 'w') as outfile:
            yaml.dump(pub, outfile, default_flow_style=False)
    else: 
        print('Cannot find semanticscholar entry for: ' + pub['doi'] + cur_yml) 