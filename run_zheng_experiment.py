# add this LD_LIBRARY_PATH=/home/titans/anaconda3/envs/dreamfusion/lib 

import subprocess 
import glob 
import os 
from icecream import ic 
print = ic 

path = "zhenggang/data_DreamG/"

for folder in glob.glob(path+"*/"):
	out_name = folder.split('/')[-2]

	files_obj = glob.glob(f"logs/{out_name}/*.obj")
	# ic(files_obj)
	if f'logs/{out_name}/_mesh.obj' in files_obj:
		ic("continue")
		continue
	# raise()
	to_call1 = f"python main.py --config configs/image.yaml input={folder}/input_img.png save_path={out_name}/"
	to_call2 = f"python main2.py --config configs/image.yaml input={folder}/input_img.png save_path={out_name}/"
	subprocess.call(to_call1.split(" "))
	subprocess.call(to_call2.split(" "))
	# raise()