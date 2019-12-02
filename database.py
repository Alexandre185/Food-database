class Database(object):

	def __init__(self, root):

		self.nodes =  [] # List of the nodes
		self.nodes.append(root)
		self.parents =  [] # List of the corresponding parents nodes
		self.parents.append(None)
		self.images_siblings = {} # Dictionary of the images with their labels and the associated coverage (number of "siblings") when the image is added 
		self.status = {} # Dictionary of the images with their status

	def add_nodes(self, nodes):

		for node in nodes:
		    self.nodes.append(node[0]) # Update of the nodes list
		    self.parents.append(node[1]) # Update of the parents nodes list
      
	def add_extract(self, extract):

		for key in extract:

			# Count of the number of "siblings" that has each label of the image
		    self.images_siblings[key] = {}
		    for val in extract[key]:
		        if val in self.nodes:
		            self.images_siblings[key][val] = (self.parents.count(self.parents[self.nodes.index(val)]))
		        else:
		            self.images_siblings[key][val] = 0

		    self.status[key] = 'valid' # Setting by default the images status to 'valid'
			# Changing the status to 'invalid' if a label is not matched
		    for val in extract[key]: 
		        for i in range(len(self.nodes)):
		            if val not in self.nodes:
		                self.status[key] = 'invalid'

	def get_extract_status(self):

		# First check if the images with 'invalid' status are now valid
		for key in self.images_siblings:
		    if self.status[key] == 'invalid':
		        self.status[key] = 'valid' # Setting by default the status to 'valid'
				# Changing this status to 'invalid' if a label is not matched
		        for val in self.images_siblings[key]:
		            for i in range(len(self.nodes)):
		                if val not in self.nodes:
		                	self.status[key] = 'invalid'

		# For the images with 'valid' status, check the new status 'valid', 'coverage_staged', or 'granularity_staged'
		for key in self.images_siblings:
		    if self.status[key] == 'valid':
		        for val in self.images_siblings[key]:
					# if a label of the image is in the parents list, set status to 'granularity_staged'
		            if val in self.parents: 
		               self.status[key] = 'granularity_staged'
		        for val in self.images_siblings[key]:
					# if the coverage has changed sinced the image was added, set status to "coverage_staged"
		            if self.images_siblings[key][val] != self.parents.count(self.parents[self.nodes.index(val)]):
		                self.status[key] = 'coverage_staged'		
		return self.status
