import os, subprocess
import glob

import summary_writer

summary=Summary("SUMMARY.md")
def main():
    with open("repo_list.txt") as f:
        repos=f.read().splitlines()

    for repo in repos:
        name,link=repo.split(" ")
        cmd = " ".join("git clone",link,name)
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output = ps.communicate()[0]
        print (output)
