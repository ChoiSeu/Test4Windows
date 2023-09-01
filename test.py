#---------------------------------------------------------
# Information
#---------------------------------------------------------
__author__      = "biul"
__credits__    = ["none", "some"]
__maintainer__ = "biul"
__email__      = "qtrr9870@gmail.com"
__status__     = "Development"
__date__       = "2023.09.01"
__description__= "MLP model test for WiFi CSI data"

#---------------------------------------------------------
#import argparse
#import sys
import torch
import numpy as np
import time

# To use CSIKit, You should install csikit
# pip install csikit
# I will add the command in 'makefile'
from CSIKit.reader import get_reader
from CSIKit.util import csitools

#---------------------------------------------------------
def load_model():
    device = torch.device('cpu')
    model = torch.load('./models/0720_with_outlier_1.pth', map_location=device)
    print('\n**************Load Mdoel**************\n')
    print(model)
    print('*****************************************')
    return model

#---------------------------------------------------------
def load_sample( k ):
    if k < 4:
        output = "0831_blank"
    elif k < 7:
        output = "0831_left"
    elif k < 10:
        output = "0831_middle"
    else:
        output = "0831_right"

    my_reader = get_reader(f'./samples/0831/{output}%d.pcap'%k)
    csi_matrix = my_reader.read_file(f'./samples/0831/{output}%d.pcap'%k, scaled=True)
    csi_data, no_frames, no_subcarriers = csitools.get_CSI(csi_matrix, metric='amplitude')

    csi_matrix_first = csi_data[:,:,0,0]
    csi_matrix_squeezed = np.squeeze(csi_matrix_first)
    if csi_matrix_squeezed.ndim == 1:
        x_test = np.delete(csi_matrix_squeezed, (0,1,2,3,4,5,11,25,28,29,30,31,32,33,34,35,36,38,52,58,59,60,61,62,63))
    else:
        x_test = np.delete(csi_matrix_squeezed, (0,1,2,3,4,5,11,25,28,29,30,31,32,33,34,35,36,38,52,58,59,60,61,62,63), 1)
    x_test = np.where(x_test < -200, 0, x_test)
    x_test = np.floor(x_test.reshape(-1, 39) * (-1))
    print('Preprocessing for Outlier is Complete!\n')
    return x_test

#---------------------------------------------------------
def inferencing( x_test, model ):
    with torch.no_grad():
        device = torch.device('cpu')
        x_test = torch.tensor(x_test).float().to(device)
        
        output = model(x_test)

        labels = ['Blank', 'Left P', 'Left R', 'Mid P', 'Mid R', 'Right P', 'Right R']
        #prediction = labes[torch.argmax(output).item()]
        if output.size == 1:
            result = torch.argmax(output).item()
        else:
            prediction = torch.argmax(output, 1)
            values, counts = np.unique(prediction, return_counts=True)
            result = values[np.argmax(counts)]
        infer = labels[result]
        print('Prediction of this packet : ', infer)
    return infer
        #return will need for Application(I will use this result for keyboard interupt)
        #return prediction

#---------------------------------------------------------
def vote( result ):
    values, counts = np.unique(result, return_counts=True)
    winner = values[np.argmax(counts)]
    print('Final Prediction : ', winner)
    
#---------------------------------------------------------

if __name__ == '__main__':

    model = load_model()
    i = 0
    k = 1
    result = ['Blank', 'Blank', 'Blank']

    while True:
        
        start = time.time()
        x_test =  load_sample(k)
        infer = inferencing( x_test, model )
        result[i] = infer
        if i < 2:
            i += 1
        else:
            i = 0
        vote( result ) #나중에 return 추가해서 키보드 입력에 사용할 수 있게 변경
        end = time.time()
        if k < 12:
            k += 1
        else:
            break
        while (end - start) < 1 :
            end = time.time()
        print('*****************************************')
        print(f'All process is done in {end - start:.5f} sec!')
        print('*****************************************')