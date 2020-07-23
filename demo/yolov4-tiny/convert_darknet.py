import os
import sys 
import unique_util

sys.path.append('../../')
import compiler

# python convert_darknet.py --weight ../weights/yolov4-tiny.weights
if __name__ == "__main__":
    args        = unique_util.arg_parse()
    model_name  = args.model_name
    cfg_file    = args.cfg_file
    weight_file = args.weight_file

    # set up the neural network
    print('loading darknet network...')
    model_name = unique_util.get_model_name(model_name, cfg_file)
    model      = compiler.model.darknet2onnx(model_name, cfg_file, weight_file)

    # onnx_extension = model_name + '.onnx'
    # onnx.save(model, onnx_extension)

    print('onnx model save successfully')

