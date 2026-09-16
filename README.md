# project-make
a bash script to automatically generate structured project directories with .env ,.gitignore ,git initialization 

## features 
-Name for folder name, main file name and file extension
-creates .env and adds it to .gitignore.
-Initializes git
-generates package.json and installs TypeScript types.This is only if the extension is js or ts


-Linux (or Git bash / WSL on Windows)
-git
-node and npm (for js and ts)

## installation and usage
1.Clone the repo
```bash
git clone [https://github.com/migz-0day/project-make.git](https://github.com/migz-0day/project-make.git)
cd project-make
```

2.make it exaecutable
```bash
chmod +x create-project.sh
```
3.Run the script
```bash
./create-project.sh
```
4.to make it accessible globally on your system
```bash
sudo cp create-project.sh /usr/local/bin/create-project
```





