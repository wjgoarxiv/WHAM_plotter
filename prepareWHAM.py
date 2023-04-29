import os
import time 
import sys

# Create a folder entitled `WHAM`. If it exists, delete it and create a new one. 
try:
    os.mkdir('./WHAM/')
    print('INFO: Created a folder entitled `WHAM`.')
except FileExistsError:
    os.system('rm -rf ./WHAM/')
    os.mkdir('./WHAM/')
    print('INFO: Deleted the existing `WHAM` folder and created a new one.')

# Move `.tpr` and `.xvg` files from `./window_folders/window_{}/` to `./WHAM/`

## Move on to the target folder and get the number of folders; the number of windows
dir_list = os.listdir('./window_folders/')
num_dirs = len([dir_name for dir_name in dir_list if os.path.isdir('./window_folders/' + dir_name)]) 

## Iteratively copy `.tpr` and `.xvg` files from `./window_folders/window_{}/` to `./WHAM/`
for i in range(num_dirs):
    os.system('cp ./window_folders/window_{}/umbrella_{}.tpr ./WHAM/'.format(i+1, i+1))
    os.system('cp ./window_folders/window_{}/umbrella_{}_pullx.xvg ./WHAM/'.format(i+1, i+1))
    os.system('cp ./window_folders/window_{}/umbrella_{}_pullf.xvg ./WHAM/'.format(i+1, i+1))
    print('INFO: Copied files from window_{} to WHAM'.format(i+1))
time.sleep(1)

## Make `pullf-files.dat`, `pullx-files.dat`, and `tpr-files.dat` in `./WHAM/`. Store the file names of `.tpr`, `.xvg` files in the corresponding `.dat` files.
## (This is required to run `gmx wham`.)
for i in range(num_dirs):
    os.system('touch ./WHAM/tpr-files.dat ./WHAM/pullx-files.dat ./WHAM/pullf-files.dat')
    os.system('echo umbrella_{}.tpr >> ./WHAM/tpr-files.dat'.format(i+1))
    os.system('echo umbrella_{}_pullx.xvg >> ./WHAM/pullx-files.dat'.format(i+1))
    os.system('echo umbrella_{}_pullf.xvg >> ./WHAM/pullf-files.dat'.format(i+1))

print('INFO: Created tpr-files.dat, pullx-files.dat, and pullf-files.dat in WHAM.')
time.sleep(1)

# Alert user that the preparation is complete.
print('INFO: Preparation for WHAM is complete.')
time.sleep(1)
sys.exit()