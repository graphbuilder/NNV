import os 
import unique_util

#python convert_darknet.py --weight ../weights yolov4-tiny.weights
if __name__ == "__main__":
    args = unique_util.arg_parse()
    model_name  = args.model_name
    cfg_file    = args.cfg_file
    weight_file = args.weight_file

    # set up the neural network
    print('loading darknet network...')
    model_name = unique_util.get_model_name(model_name, cfg_file)
    print(model_name)

