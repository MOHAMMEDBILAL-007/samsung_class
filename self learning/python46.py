import os
print(os.getcwd())# returns the current working directory

if not os.path.exists("data46"):# this checks if the file is already exists
    os.mkdir("data46")# if the file doesent exist then creates the folder

#os.chdir("data46")# changes the current directory to the following directory

print(os.getcwd())

for i in range(1,20):# this allows us to make so many changes at a single time 
    os.mkdir(f"data46/day{i}")# creating a lot of folders at once
# above because we are using the required folder or else we need to put the path to specify like data46/day
print(os.listdir("data46"))# returns the list of directories in the path
ix=0
for i in os.listdir("data46"):
    ix+=1
    os.rename("data46/"+i,f"data46/tutorial{ix}")# renaming the large sum offolders at a time