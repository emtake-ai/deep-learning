# Why MobileNet Matters in CNN History

MobileNet is the architecture that brought CNNs  
from data centers to **real embedded devices**.

---

## 1. The efficiency crisis

After VGG and ResNet, CNN accuracy improved rapidly —  
but computation and power consumption exploded.

It became clear that these models could not be deployed on  
mobile phones, IoT devices, or edge AI modules.

MobileNet was created to solve this problem.

---

## 2. Depthwise separable convolution

MobileNet replaced standard convolution with  
**Depthwise Separable Convolution**:

- Depthwise convolution: one filter per input channel  
- Pointwise convolution: 1×1 convolution to mix channels  

This reduces computation by nearly **9×** with minimal accuracy loss.

---

## 3. Why MobileNet is historically important

MobileNet proved that:

- CNN performance can be traded for efficiency  
- Architecture must be designed specifically for hardware limits  
- Edge AI is not about shrinking big models —  
  it requires **new design philosophy**

---

## 4. MobileNet and Edge AI

MobileNet is naturally suited for Edge AI hardware:

- Simple layer structure  
- Regular memory access patterns  
- Quantization-friendly activations (ReLU6)

It became the backbone of almost every modern lightweight CNN.

---

## Summary

MobileNet did not just make CNNs smaller.  
It changed CNN design from  
**“how accurate can we be” to “how efficient can we be.”**
