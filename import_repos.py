import os, subprocess, shutil
import glob

import config
import summary_writer

summary=summary_writer.Summary("SUMMARY.md")

def create_main_sidebar(md_dirs,sidebar_file):
    '''
    Recurse and add to the sidebar file
    '''
    sidebar='''* [Home](README.md) \n'''

    for dir in md_dirs:
        for root, dirs, files in os.walk(dir, topdown=True):
            for name in files:
                # Skip non markdown
                if name[-2:]!="md":
                    continue

                if root==dir and name=="README.md":
                    sidebar+='''* [{}]({}) \n'''.format(dir,dir+"/README.md")

    with open(sidebar_file,"w") as f:
        f.write(sidebar)

def append_to_sidebar(md_dirs,sidebar_file):
    '''
    Recurse and add to the sidebar file
    '''
    sidebar='''* [Home](README.md) \n'''

    for dir in md_dirs:
        for root, dirs, files in os.walk(dir, topdown=True):
            for name in files:
                # Skip non markdown
                if name[-2:]!="md":
                    continue

                if root==dir and name=="README.md":
                    sidebar+='''* [{}]({}) \n'''.format(dir,dir+"/README.md")

                elif root=="/".join([dir,"g3docs"]):

                    sidebar+='''\t* [{}]({}) \n'''.format(name[:-3],os.path.join(root,name))

                elif "/".join([dir,"g3docs"]) in root:
                    count=0
                    if not count:
                        sidebar+="\t* "+root.split("/")[-1]
                    else:
                        count+=1
                    sidebar+='''\t\t* [{}]({}) \n'''.format(name[:-3],os.path.join(root,name))

    with open(sidebar_file,"w") as f:
        f.write(sidebar)

def remove_all_except(dir,dirs,files):
    '''
    Removes all files and dir's except dirs

    Args:
    * dir: root dir
    * dirs: dirs to keep
    * files : files to keep

    Example: remove_all_except(attendance-system,)
    '''

    files_dirs_to_remove=os.listdir(dir)

    # Find files and dirs to remove
    files_to_remove=[f for f in files_dirs_to_remove if os.path.isfile(os.path.join(dir, f)) and f not in files]
    dirs_to_remove=[f for f in files_dirs_to_remove if not os.path.isfile(os.path.join(dir, f)) and f not in dirs]

    for file in files_to_remove:
        os.remove(os.path.join(dir,file))

    for dirs in dirs_to_remove:
        shutil.rmtree(os.path.join(dir,dirs))

def main():
    count=1
    for name in config.REPOS.keys():
        
        link=config.REPOS[name]['link']
        refresh=config.REPOS[name]['refresh']

        print ("Count {} \t | Repo {} \t | Refresh {} \t | Link {} ".format(count,name,refresh,link))
        if refresh:
            if os.path.exists(name):
                shutil.rmtree(name)
        elif os.path.exists(name):
            continue

        cmd = " ".join(["git clone ",link,name])
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output = ps.communicate()[0]

        # Remove Dirs
        remove_all_except(name,"g3docs","README.md")

        if os.path.exists(os.path.join(dir,"g3docs")):
            create_folder_sidebar()

    create_main_sidebar(config.REPOS.keys(),"_sidebar.md")

if __name__=='__main__':
    main()