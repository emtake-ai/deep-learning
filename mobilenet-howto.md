mobilenet directory structure
```text
mobilenet-project/
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
 │   └─ model/keras/mobilenet.py
 ├─ train_mobilenet.py
 └─ run_mobilenet.py
```

Step 1. Download Dataset

Download the mobilenet dataset ZIP file from HuggingFace.

[HuggingFace mobilenet datasset download](https://huggingface.co/datasets/emtake-ai/mobilenet/resolve/main/mobilenet-dataset.zip)

After downloading, extract it into the dataset/ directory:

unzip mobilenet-dataset.zip -d ./dataset

Step 2. Train the mobilenet Model

Run the training script:

python3 train_mobilenet.py

After training is complete, the trained model file will be generated:

mobilenet.keras

Step 3. Download Pretrained Models (Optional)

If you prefer not to train from scratch, download the pretrained models directly:

[HuggingFace mobilenet.keras download](https://huggingface.co/emtake-ai/mobilenet/resolve/main/mobilenet.keras)

[HuggingFace mobilenet.lne download](https://huggingface.co/emtake-ai/mobilenet/resolve/main/mobilenet.lne)

Step 4. Convert Model to NPU Format (LNE)

Convert mobilenet.keras into mobilenet.lne using Synabro.

[guide](model-conversion-to-npu/readme.md)

Step 5. Transfer Model to Eagleboard

After conversion, transfer the model to the Eagleboard:

[transfer](www.github.com/emtake-ai/eagleboard/transfer.md)

Step 6. Run mobilenet on Eagleboard

Log in to the Eagleboard and run:

python3 run_mobilenet.py


 

