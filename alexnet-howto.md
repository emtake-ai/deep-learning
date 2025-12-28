alexnet directory structure

```text
alexnet-project/
 ├─ dataset/
 │   ├─ train/
 │   │   ├─ class0/
 │   │   ├─ class1/
 │   │   └─ ...
 │   └─ val/
 │       ├─ class0/
 │       ├─ class1/
 │       └─ ...
 ├─ model-sample/
 │   └─ model/keras/alexnet.py
 ├─ train_alexnet.py
 └─ run_alexnet.py
```
Step 1. Download Dataset

Download the AlexNet dataset ZIP file from HuggingFace.

[HuggingFace alexnet datasset download](https://huggingface.co/datasets/emtake-ai/alexnet/resolve/main/alexnet-dataset.zip)

After downloading, extract it into the dataset/ directory:

unzip alexnet-dataset.zip -d ./dataset

Step 2. Train the AlexNet Model

Run the training script:

python3 train_alexnet.py

After training is complete, the trained model file will be generated:

alexnet.keras

Step 3. Download Pretrained Models (Optional)

If you prefer not to train from scratch, download the pretrained models directly:

[HuggingFace alexnet.keras download](https://huggingface.co/emtake-ai/alexnet/resolve/main/alexnet.keras)

[HuggingFace alexnet.lne download](https://huggingface.co/emtake-ai/alexnet/resolve/main/alexnet.lne)

Step 4. Convert Model to NPU Format (LNE)

Convert alexnet.keras into alexnet.lne using Synabro.

[guide](model-conversion-to-npu/readme.md)

Step 5. Transfer Model to Eagleboard

After conversion, transfer the model to the Eagleboard:

[transfer](www.github.com/emtake-ai/eagleboard/transfer.md)

Step 6. Run AlexNet on Eagleboard

Log in to the Eagleboard and run:

python3 run_alexnet.py


 

