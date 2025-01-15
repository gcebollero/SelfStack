from glob import glob
import yaml
import pandas

if __name__ == "__main__":
    _results = []
    for _file in glob('stacks/*.yml'):
        _f = yaml.safe_load(open(_file, 'r'))
        for _service in _f.get('services', []):
            for _ports in _f['services'][_service].get('ports', []):
                _results.append({'Container': _service, 'Host port': _ports.split(':')[0], 'Container port': _ports.split(':')[1]})
    df = pandas.DataFrame(_results)
    df['order'] = pandas.to_numeric(df['Host port'], errors='coerce')
    df = df.sort_values('order').drop('order', axis=1)
    with open('ports.md', 'w') as md:
        md.write(df.to_markdown())