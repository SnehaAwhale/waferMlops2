import os

dirs=[
    'datagiven',
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    'notebook',
    'save models',
    'src'


]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_ , ".gitkeep"),"w") as f:
        pass

files=[
 "param.yaml",
    "dvc.yaml",
    "gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    try:
        os.makedirs(file_,exist_ok=True)
    except FileExistsError:
        print("FileExists already")
    try:
        with open(os.path.join(file_,".gitkeep"),"w") as f:
            pass
    except FileNotFoundError:
        pass

