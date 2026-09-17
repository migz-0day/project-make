import os
import subprocess
import sys

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

if FILE_EXT=="ts":
   print("installing typescript depende....")
   subprocess.run("npm install --save-dev typescript @types/node", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
   subprocess.run("npx tsc --init",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

subprocess.run("git init")

print("==========m====i====g====z===========")
print(f"project {FOLDER_NAME}created successfully")
print(f"main file {FILE_NAME}")
print("==========m====i====g====z===========")
if __name__=="__main__":
 main()


