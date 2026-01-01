# Model Samples – CNN Architecture History for Embedded AI

This section introduces representative CNN architectures  
and reinterprets them from the perspective of **AI Module and Edge AI systems**.

Rather than listing deep learning theory, this documentation focuses on:

- Why each model was created  
- What architectural problem it solved  
- What it means when the model is deployed on embedded AI hardware

---

## CNN Evolution Path

CNN architecture started from LeNet,  
which established the core convolution concept.

AlexNet proved that deep CNNs can scale using GPUs.  
VGGNet standardized deep network design through depth-based architecture.  
GoogLeNet introduced architectural optimization through the Inception concept.  
ResNet solved the deep training problem with skip connections.

Finally, MobileNet and EfficientNet redefined CNN design  
for resource-constrained Edge AI environments.

---

## Model Index

| Model | Description |
|-------|-------------|
| LeNet | The first complete realization of CNN |
| AlexNet | The model that launched the deep learning era |
| VGGNet | The architecture that standardized deep CNN design |
| GoogLeNet | The structure-optimized Inception model |
| ResNet | The architecture that enabled very deep CNNs |
| MobileNet | The efficiency-driven CNN for embedded devices |
| EfficientNet | The systematic CNN scaling architecture |

---

## Read Each Model

- [LeNet](lenet.md)  
- [AlexNet](alexnet.md)  
- [VGGNet](vggnet.md)  
- [GoogLeNet](googlenet.md)  
- [ResNet](resnet.md)  
- [MobileNet](mobilenet.md)  
- [EfficientNet](efficientnet.md)  

---

## How to Use This Section

Each document explains not only the model structure but also:

- Why the model was created  
- What constraints appear when deploying it on AI modules  
- What ideas customers should adopt when designing their own models

By reading this section in order,  
you will understand both CNN history and Edge AI design philosophy.

## Test each model in eagleboard

- [LeNet](lenet-howto.md)
- [AlexNet](alexnet-howto.md)  
- [VGGNet](vggnet-howto.md)  
- [GoogLeNet](googlenet-howto.md)  
- [ResNet](resnet-howto.md)  
- [MobileNet](mobilenet-howto.md)  
- [EfficientNet](efficientnet.md)  

## you can check else in youtube 

- [how to annotate in yolo using labelimg](https://www.youtube.com/watch?v=nV26hK3CxNM)
- [how to download the git repos using git clone](https://www.youtube.com/watch?v=SGCvhjD3mtM)
- [how to download the model from huggingface](https://www.youtube.com/watch?v=JCcyCxori0M)
- [how to build keras, and how to convert it with lne](https://www.youtube.com/watch?v=BDnK0pujDvg)
- [how to install synabro with docker](https://www.youtube.com/watch?v=fNOcj9eNf_M)
