import os
class DirectoryExplorer:
	def __init__(self,path):
		self.path = path
	
	def check_if_folder(self,filepath):
		return os.path.isdir(filepath)
			

	def list_dir_recursive(self,current_path):
		filepaths = []
		
		for filename in os.listdir(current_path):
			filepath = os.path.join(current_path,filename)
			if(self.check_if_folder(filepath)):
				filepaths = filepaths + self.list_dir_recursive(filepath)
			else:
				filepaths.append(filepath)

		return filepaths

	def list_dir(self):
		return self.list_dir_recursive(self.path)	
			
  
	
	

