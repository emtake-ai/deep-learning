resnet directory structure
```text
resnet-project/
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
 │   └─ model/keras/resnet.py
 ├─ train_resnet.py
 └─ run_resnet.py
 """

Step 1. Download Dataset
Download the resnet dataset ZIP file from HuggingFace.
[HuggingFace resnet datasset 다운로드](https://huggingface.co/datasets/emtake-ai/resnet/resolve/main/resnet-dataset.zip)

After downloading, extract it into the dataset/ directory:
unzip resnet-dataset.zip -d ./dataset

Step 2. Train the resnet Model
Run the training script:
python3 train_resnet.py

After training is complete, the trained model file will be generated:
resnet.keras

Step 3. Download Pretrained Models (Optional)
If you prefer not to train from scratch, download the pretrained models directly:
[HuggingFace resnet.keras 다운로드](https://huggingface.co/emtake-ai/resnet/resolve/main/resnet.keras)
[HuggingFace resnet.lne 다운로드](https://huggingface.co/emtake-ai/resnet/resolve/main/resnet.lne)

Step 4. Convert Model to NPU Format (LNE)
Convert resnet.keras into resnet.lne using Synabro.
[guide](model-conversion-to-npu/readme.md)

Step 5. Transfer Model to Eagleboard
After conversion, transfer the model to the Eagleboard:
[transfer](www.github.com/emtake-ai/eagleboard/transfer.md)

Step 6. Run resnet on Eagleboard
Log in to the Eagleboard and run:
python3 run_resnet.py


 

