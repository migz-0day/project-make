import os
import subprocess
import sys

def run_cmd(command):
   subprocess.run(command,shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== make project instantly === ")
FOLDER_NAME=input("enter the project folder name : ")
FILE_NAME=input("enter file name without extension : ")
FILE_EXT=input("enter file extension (js,ts,py,go,rs) : ")

if not FOLDER_NAME or not FILE_NAME or not FILE_EXT:
    print(f"error all field required")
    sys.exit(1)

os.makedirs(FOLDER_NAME)
os.chdir(FOLDER_NAME)

with open(".env","w") as f:
    f.write("# enviroment variable\n")

with open(".gitignore","w") as f:
    f.write(".env\nnode_modules/\n__pycache__/\n*.exe\n")

FULL_FILE=f"{FILE_NAME}.{FILE_EXT}"
with open(FULL_FILE,"w") as f:
    if FILE_EXT=="py":
     f.write("# main entry point\nprint('hello world')\n")
    elif FILE_EXT in ["js","ts"]:
      f.write("// main entry point\nconsole.log('hello world');\n")

print(f"created{FULL_FILE}")

if FILE_EXT in ["js","ts"]:
 print("javascript/typescript found.initializing node project...")
 subprocess.run("npm init -y", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if FILE_EXT in ["ts","tsx"]:
   print("installing typescript depende....")
   subprocess.run("npm install --save-dev typescript @types/node", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
   subprocess.run("npx tsc --init",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if FILE_EXT in ["jsx","tsx"]:
   print("react......")
   run_cmd("npm install react react-dom")
   if FILE_EXT=="tsx":
        run_cmd("npm install --save-dev @types/react @types/react-dom")

with open(FULL_FILE,"w") as f:
 if FILE_EXT in ["jsx","tsx"]:
   f.write("import React from 'react'\nexport default function App(){\n return <h1>hello react</h1>;\n}\n") 
 else:
   f.write("// main entry\n console.log('hello world');\n") 
    
if FILE_EXT=="go":
   print("go detected.Go modules ....")
   run_cmd(f"go mod init {FOLDER_NAME}")
   with open(FULL_FILE,"w") as f:
      f.write("package main\n\nimport \"fmt\"\n\nfunc main() {\n\tfmt.println(\"hello world\")\n}\n")    


run_cmd("git init")

print("==========m====i====g====z===========")
print(f"project {FOLDER_NAME} created successfully")
print(f"main file {FILE_NAME}")
print("==========m====i====g====z===========")
if __name__=="__main__":
 main()


