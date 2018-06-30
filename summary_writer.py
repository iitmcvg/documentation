'''
Handles 

writting the SUMMARY.md

'''

class Summary(object):
    def __init__(self,filepath):
        self.summary={}
        self._init_from_file(filepath)
    def _init_from_file(filepath):
        '''
        Read summary and split into dictionary
        '''
        with open(filepath,"r") as f:
            lines=f.read().splitlines()

    def update_files(self,header,files_list):
        '''
        Updates a list of files for gitbooks.
        '''
