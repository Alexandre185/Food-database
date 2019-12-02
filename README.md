# Food-database

The `Database` class (in the database.py file) is made of 4 attributes:
  - `nodes` : a list of all the nodes in the database. eg: ['Core', A, B, A1]
  - `parents` : a list of the parents of each node in the database. eg: [None, 'Core', 'Core', A]
  - `images_siblings` : a dictionnary of dictionnaries. Each primary key is an image ID, each secondary key is a label of this image and each value is the number (including itself) of "siblings" labels (nodes that share the same parent node) that has this label when the image is added to the database. eg: {img001:{B: 2, A1: 1}}
  - `images_status` : a dictionnary with each key is an image ID and each value is the corresponding status of the image: `valid`, `invalid`, `granularity_staged`, or `coverage_staged`. eg: {img001: 'valid'}
  
The `Database` class has to be initialized with the root name (the name of the first node, the ensemble of the elements).

- The `nodes` and `parents` attributes are updated with the method `add_nodes`.
- The `images_siblings` attribute is updated with the method `add_extract`.
- The `images_status` is updated with the method `add_extract` where the new images status are set to `valid` or `invalid` and with the method `get_extract_status` that return the status of each image at the moment it is called: either `valid`, `invalid`, `granularity_staged` or `coverage_staged`.

  
 
 The Database has been tested with the provided examples:
 
 Example 1:
 ```python
from database import Database

# Initial graph
build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
# Extract
extract = {"img001": ["A"], "img002": ["C1"]}
# Graph edits
edits = [("A1", "A"), ("A2", "A")]

# Get status (this is only an example, test your code as you please as long as it works)
status = {}
if len(build) > 0:
    # Build graph
    db = Database(build[0][0])
    if len(build) > 1:
    	db.add_nodes(build[1:])
    # Add extract
    db.add_extract(extract)
    # Graph edits
    db.add_nodes(edits)
    # Update status
    status = db.get_extract_status()
print(status)
```
It does return:
```python
{"img001": "granularity_staged", "img002": "valid"}
```

Example 2:
```python
from database import Database

# Initial graph
build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
# Extract
extract = {"img001": ["A", "B"], "img002": ["A", "C1"], "img003": ["B", "E"]}
# Graph edits
edits = [("A1", "A"), ("A2", "A"), ("C2", "C")]

# Get status (this is only an example, test your code as you please as long as it works)
status = {}
if len(build) > 0:
    # Build graph
    db = Database(build[0][0])
    if len(build) > 1:
    	db.add_nodes(build[1:])
    # Add extract
    db.add_extract(extract)
    # Graph edits
    db.add_nodes(edits)
    # Update status
    status = db.get_extract_status()
print(status)
```

It does return:
```python
{"img001": "granularity_staged", "img002": "coverage_staged", "img003": "invalid"}
```

Example 3: (With the data available in the release)
```python
from database import Database

import json

with open('expected_status.json') as json_file:
    expected_status = json.load(json_file)

with open('graph_build.json') as json_file:
    graph_build = json.load(json_file)

with open('graph_edits.json') as json_file:
    graph_edits = json.load(json_file)

with open('img_extract.json') as json_file:
    img_extract = json.load(json_file)

status = {}
db = Database(graph_build[0][0])
db.add_nodes(graph_build[1:])
# Add extract
db.add_extract(img_extract)
# Graph edits
db.add_nodes(graph_edits)
# Update status
status = db.get_extract_status()

status == expected_status
```
It does return:
```python
True
```
