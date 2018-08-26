'''
Imports repos to depth of 1.
Updates sidebars and navbar.
'''

import os, subprocess, shutil
import glob

import config

def _transform_string(string):
    '''
    Make strings more readable
    '''
    return string.replace("-"," ").capitalize()

def _reverse_transform(string):
    '''
    Undo transform string
    '''
    return string.replace(" ","-").lower()

def _unindent(lines):
    return "\n".join(["*"+line[2:] for line in lines.split("\n")[:-1]])

def _human_message(file_type):
    if file_type=="project":
        lines=["Here's the list of projects currently compiled by the documentation engine.",
        "Contact us to add your project to the auto-render."]
        return "\n".join(lines)

    elif file_type=="utils":
        lines=["Here's the list of utilities currently compiled by the documentation engine.",
        "Contact us to add your project to the auto-render."]
        return "\n".join(lines)

def create_main_sidebar(repos,sidebar_file,navbar_file):
    '''
    Recurse and add to the sidebar file

    * repos: dictionary config
    '''
    sidebar='''* [Home](README.md) \n'''

    md_dirs=repos.keys()

    # Side bar
    repo_side_bar={}
    repo_side_bar["home"]="* [Home](README.md) \n"

    # Nav bar
    repo_nav_bar="* [Home](README.md) \n* [Projects](projects.md) \n* [Utilities](utils.md) \n"

    # Project list
    project_bar=''

    # Utils list
    utils_bar=''

    for dir in md_dirs:
        dir_name=_transform_string(dir)
        for root, dirs, files in os.walk(dir, topdown=True):
            for name in files:
                # Skip non markdown
                if name[-2:]!="md":
                    continue

                if root==dir and name=="README.md":
                    sidebar+='''* [{}]({}) \n'''.format(dir_name,dir+"/README.md")

        repo_side_bar[dir_name]="* [{}]({}) \n".format(dir_name,dir+"/README.md")

    side_bar="* [Home](README.md) \n"
    side_bar+="\n* [Projects](projects.md) \n" 

    # Add projects to main sidebar
    for dir_name in sorted(repo_side_bar.keys()):
        if dir_name=="home":
            continue
        md_dir=_reverse_transform(dir_name)
        if repos[md_dir]['type']=='project':
            project_bar+="\t* [{}]({})\n".format(dir_name,md_dir+"/README.md")

    # Collect projects
    side_bar+=project_bar
    side_bar+="* [Utils](utils.md) \n"

    # Add utils to main sidebar
    for dir_name in sorted(repo_side_bar.keys()):
        if dir_name=="home":
            continue
        md_dir=_reverse_transform(dir_name)
        if repos[md_dir]['type']=='utils':
            utils_bar+="\t* [{}]({})\n".format(dir_name,md_dir+"/README.md")

    # Collect utils
    side_bar+=utils_bar

    # Write sidebar
    with open(sidebar_file,"w") as f:
        f.write(side_bar)

    # Project write ups
    with open("projects.md","w") as f:
        f.write(_human_message("project"))
        f.write("\n\nProjects : \n")
        f.write(_unindent(project_bar))

    # Utils write ups
    with open("utils.md","w") as f:
        f.write(_human_message("utils"))
        f.write("\n\nUtils : \n")
        f.write(_unindent(utils_bar))
    # navbar 
    with open("_navbar.md","w") as f:
        f.write(repo_nav_bar)

def create_folder_sidebar(dir,sidebar_file):
    '''
    Recurse and add to the  folder sidebar file
    '''
    sidebar='''* [{}]({}/README.md) \n'''.format(dir,dir)

    root_covered=[]
    for root, dirs, files in os.walk(dir, topdown=True):
        for name in sorted(files):
            # Skip non markdown
            if name[-2:]!="md" or name[0]=="_":
                continue

            elif root=="/".join([dir,"g3docs"]):

                sidebar+='''\t* [{}]({}) \n'''.format(name[:-3],os.path.join(root,name))

            elif "/".join([dir,"g3docs"]) in root:
                if root not in root_covered:
                    sidebar+="\t* "+root.split("/")[-1]+"\n"
                    root_covered.append(root)
                sidebar+='''\t\t* [{}]({}) \n'''.format(name[:-3],os.path.join(root,name))

    with open("/".join([dir,sidebar_file]),"w") as f:
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
        
            cmd = " ".join(["git clone --depth 1",link,name])
            ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            output = ps.communicate()[0]

            # Remove Dirs
            remove_all_except(name,"g3docs","README.md")

        if os.path.exists(os.path.join(name,"g3docs")):
            create_folder_sidebar(name,"_sidebar.md")
            print(os.path.join(name,"g3docs"))
        else:
            print(os.path.join(name,"g3docs"))

        count+=1

    create_main_sidebar(config.REPOS,"_sidebar.md","navbar.md")

if __name__=='__main__':
    main()