import os
import argparse

def arg_parse():
    '''
    parse arguments for yolov4
    '''
    parser = argparse.ArgumentParser(description = 'pyann yolov4 detection moudle')
    parser.add_argument('--model_name', dest = 'model_name', help = 'the name of model', 
                        default = '', type = str)
    parser.add_argument('--cfg', dest = 'cfg_file', help = 'config file', 
                        default = '../../rersources/cfg/yolov4-tiny.cfg', type = str)
    parser.add_argument('--weight', dest = 'weight_file', help = 'weight file',
                        default = '', type = str)
    return parser.parse_args()
        
def get_model_name(default, cfg):
    if default == "":
        basename = os.path.basename(cfg)
        name = basename.split(".")[-2]
        return name
    else:
        return default
