import os

path = "C:\\Drill_Directory\\"
dir = os.listdir(path)

for file in dir:
        ext = os.path.splitext(file)[-1].lower()
        time = os.path.getmtime(dir,file)
        if ext == '.txt':
            print(os.path.join(file," is a txt file.",time))

        else:
            print(os.path.join(file," is not a txt file.",time))









