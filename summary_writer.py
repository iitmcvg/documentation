'''
Handles 

writting the SUMMARY.md

'''

import os, sys

class Summary(object):
    def __init__(self,filepath):
        self.summary={}
        self.filepath=filepath
        self._init_from_file(self.filepath)

    def _init_from_file(self,filepath):
        '''
        Read summary and split into dictionary
        '''
        with open(filepath,"r") as f:
            lines=f.read().splitlines()

        data=[]
        key=None
        for line in lines:
            if not line:
                continue
            if line.startswith("# "):
                if data and key:
                    self.summary[key]=data
                data=[]
                key=line.lstrip("# ")
                self.summary[key]=data
            
            elif line.startswith("## "):
                data=[]
                key=line.lstrip("## ")
                self.summary[key]=data
            else:
                data.append(line)

    def update_files(self,header,files_list,files_link_list):
        '''
        Updates a list of files for gitbooks.
        '''
        assert (len(files_list)==len(files_link_list), "Links must match for each new file")

        if header not in list(self.summary.keys()):
            self.summary[header]=["["+x+"]"+"("+y+")" for x,y in zip(files_list,files_link_list)]

    def write_update(self,filepath):
        dump=[]
        dump.append("# Table of contents")
        for line in self.summary["Table of contents"]:
            dump.append(line)
    
        keys=list(self.summary.keys())
        keys.sort()
        for key in keys:
            if key =="Table of contents":
                continue
            else:
                dump.append("## "+ key)
                for line in self.summary[key]:
                    dump.append(line)

            with open(filepath,"w") as f:
                f.write("\n".join(dump))
            
