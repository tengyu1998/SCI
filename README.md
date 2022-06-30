# Toward Fast, Flexible, and Robust Low-Light Image Enhancement, CVPR 2022 (Oral)
![visitors](https://visitor-badge.glitch.me/badge?page_id=vis-opt-group/SCI) 

[[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Ma_Toward_Fast_Flexible_and_Robust_Low-Light_Image_Enhancement_CVPR_2022_paper.html)] [[Supplement Material](https://openaccess.thecvf.com/content/CVPR2022/supplemental/Ma_Toward_Fast_Flexible_CVPR_2022_supplemental.pdf)] [[Online Demo](https://replicate.com/vis-opt-group/sci)] [[Media Report (in Chinese)](https://mp.weixin.qq.com/s/sac_TOQA16rvpArNYEa7yA)]

<img src="Figs/Firstfig.png" width="900px"/> 
<p style="text-align:justify">Comparison among recent state-of-the-art methods and our method. KinD is a representative paired supervised method.  EnGAN considers the unpaired supervised learning. ZeroDCE [7] and RUAS [16] introduce unsupervised learning. Our method (just contains three convolutions with the size of 3 × 3) also belongs to unsupervised learning. As shown in the zoomed-in regions, these compared methods appear incorrect exposure, color distortion, and insufficient structure to degrade visual quality. In contrast, our result presents a vivid color and sharp outline. Further, we report the computational efficiency (SIZE, FLOPs, and TIME) in (b) and numerical scores for five types of measurement metrics among three tasks including enhancement (PSNR, SSIM, and EME), detection (mAP), and segmentation (mIoU) in (c), it can be easily observed that our method is remarkably superior to others.

## Self-Calibrated Illumination (SCI) Learning Framework
<img src="Figs/Flowchart.png" width="900px"/> 
<p style="text-align:justify">The entire framework of SCI. In the training phase, our SCI is composed of the illumination estimation and self-calibrated module. The self-calibrated module map is added to the original low-light input as the input of the illumination estimation at the next stage. Note that these two modules are respectively shared parameters in the whole training procedure. In the testing phase, we just utilize a single illumination estimation module.</p>

## Codes
### Requirements
* python3.7
* pytorch==1.8.0
* cuda11.1

### Introduce the trained model
Under the weights folder, there are three different models, the main difference is that the training data is different
* easy.pt mainly uses the MIT dataset for training
* medium.pt mainly uses the LOL and LSRW datasets for training
* difficult.pt mainly uses the darkface dataset for training

If you want to retrain a new model, you can write the path of the dataset to train.py and run "train.py", the final model will be saved to the weights folder, and the intermediate visualization results will be saved to the results folder

### Test steps
* Prepare the data and put it in the specified folder
* Choose a specific model as needed (difficult.pt medium.pt easy.pt)
* run "test.py"

## Results on Low-light Image Enhancement
<img src="Figs/LLIE_1.png" width="900px"/> 
<img src="Figs/LLIE_3.png" width="900px"/> 

## Results on High-level Vision Tasks
### Dark Face Detection
<img src="Figs/Det_1.png" width="900px"/> 

### Nighttime Semantic Segmentation
<img src="Figs/Seg_1.png" width="900px"/> 


## Citation
```bibtex
@inproceedings{ma2022toward,
  title={Toward Fast, Flexible, and Robust Low-Light Image Enhancement},
  author={Ma, Long and Ma, Tengyu and Liu, Risheng and Fan, Xin and Luo, Zhongxuan},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={5637--5646},
  year={2022}
}
```
