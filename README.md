# Food-database

The Database class (in the database.py file), is made of 4 attributes:
  - nodes : a list of all the nodes in the database. eg: ['Core', A, B, A1]
  - parents : a list of the parents of each node in the database. eg: [None, 'Core', 'Core', A]
  - images_siblings : a dictionnary of dictionnaries. Each primary key is an image ID, each secondary key is a label of this image and each value is the number (including itself) of "siblings" labels (nodes that share the same parent node) that has this label when the image is added to the database. eg: {img001:{B:2, A1:1}}
  - images_status : a dictionnary with each key is an image ID and each value is the corresponding status of the image: 'valid', 'invalid', 'granularity_staged', or 'coverage_staged'. eg: {img001: 'valid'}
