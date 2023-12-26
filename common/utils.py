from pathlib import Path
import os

def get_file_name_parts(filename:str):  
    #返回"."的最大索引
    pos = filename.rfind('.')
    if pos == -1:
        return filename,''
    
    return filename[:pos],filename[pos+1:]

def get_save_filepath(file_path:Path):
    # save_file = file_path.joinpath(filename)
    # if not save_file.exists():
    #     return save_file
    
    # name,ext = get_file_name_parts(os.path.basename(file_path))
    with_out_suffix =  file_path.stem
    for i in range(1,100):
        if file_path.exists():
            new_file_name = f'{with_out_suffix}_{i}{file_path.suffix}'
            file_path = file_path.with_name(new_file_name)
    print(f"保存到{file_path}")
    return file_path

