# Elastic Scroll

A minimal library for efficient elasticsearch queries

## Install

```bash
git clone https://github.com/departmentofdefense/elasticscroll
cd elasticscroll
pip3 install .
```

## Usage

```python
import elasticscroll

esm = elasticscroll.ElasticMinimal('https://your-es-endpoint')

lookup = {
    'query': {
        'term': {'id_resp_h': '192.83.203.129'}
    }
}

for res in esm.scroll_query('conn', lookup):
    print(res)
```