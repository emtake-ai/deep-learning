# Why ResNet Matters in CNN History

ResNet is the architecture that finally solved  
the **deep network training problem**.

---

## 1. The degradation problem

As networks became deeper, performance did not always improve.  
In many cases, deeper models performed worse than shallower ones.

This phenomenon was not caused by overfitting,  
but by the difficulty of training very deep networks —  
known as the *degradation problem*.

---

## 2. Residual learning

ResNet introduced the concept of **residual learning**.

Instead of learning a direct mapping,  
the network learns the *difference* between the input and the desired output.

This is implemented using skip connections:

> Output = F(x) + x

These shortcut paths allow gradients to flow directly through the network,  
making extremely deep CNNs trainable.

---

## 3. Why ResNet is historically important

ResNet proved that:

- Depth itself is not the problem  
- Optimization is the real bottleneck  
- With proper architectural design, CNNs can scale to hundreds of layers

Almost all modern CNNs contain residual or skip-connection ideas.

---

## 4. ResNet and Edge AI

On Edge AI hardware, skip connections introduce new challenges:

- Additional memory reads and writes  
- Increased DMA traffic  
- Reduced NPU utilization due to tensor merging

Therefore, ResNet is often simplified or fused when deployed on embedded systems.

---

## Summary

LeNet created CNN.  
AlexNet scaled CNN.  
VGG standardized CNN.  
GoogLeNet optimized CNN structure.  
**ResNet made very deep CNNs possible.**
