# Toward Fast, Flexible, and Robust Low-Light Image Enhancement
![visitors](https://visitor-badge.glitch.me/badge?page_id=vis-opt-group/SCI) 

[[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Ma_Toward_Fast_Flexible_and_Robust_Low-Light_Image_Enhancement_CVPR_2022_paper.html)] [[Online Demo](https://replicate.com/vis-opt-group/sci)]
## Self-Calibrated Illumination (SCI) Learning Framework
<img src="Figs/Flowchart.png" width="900px"/> 
*The architecture of the proposed Swin-Conv-UNet (SCUNet) denoising network. SCUNet exploits the swin-conv (SC) block as
the main building block of a UNet backbone. In each SC block, the input is first passed through a 1×1 convolution, and subsequently is
split evenly into two feature map groups, each of which is then fed into a swin transformer (SwinT) block and residual 3×3 convolutional
(RConv) block, respectively; after that, the outputs of SwinT block and RConv block are concatenated and then passed through a 1×1
convolution to produce the residual of the input. “SConv” and “TConv” denote 2×2 strided convolution with stride 2 and 2×2 transposed
convolution with stride 2, respectively.*

## Requirements
* python3.7
* pytorch==1.8.0
* cuda11.1

## Test steps
* Prepare the data and put it in the specified folder
* Select specific model (difficult.pt medium.pt easy.pt)
* run "test.py"
