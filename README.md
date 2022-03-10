# [CVPR 2022] Toward Fast, Flexible, and Robust Low-Light Image Enhancement

## Environment Preparing
```
python 3.6
pytorch 1.8.0
```

### Testing Enhancement

We provide different models which are trained from different datasets, the models are saved in './weights/'.
*lol.pt* is trained from LOL dataset.
*mit.pt* is trained from MIT5K dataset.
*darkface.pt* is trained from DarkFace dataset.
Finally, run *test_enhancement.py*, the results will be saved in `./result/`
```
python test_enhancement.py 
--data_path           #The folder path of the picture you want to test
'./data/enhance_test_data/lol/test'
--model               #The checkpoint which you want use
'weights/lol.pt'
--save_path            #The save path of the picture processed
./result/
```
