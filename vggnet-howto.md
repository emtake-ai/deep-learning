vggnet directory structure
```text
vggnet-project/
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
 │   └─ model/keras/vggnet.py
 ├─ train_vggnet.py
 └─ run_vggnet.py
```

Step 1. Download Dataset

Download the vggnet dataset ZIP file from HuggingFace.

[HuggingFace vggnet datasset 다운로드](https://huggingface.co/datasets/emtake-ai/vggnet/resolve/main/vggnet-dataset.zip)

After downloading, extract it into the dataset/ directory:

unzip vggnet-dataset.zip -d ./dataset

Step 2. Train the vggnet Model

Run the training script:

python3 train_vggnet.py

After training is complete, the trained model file will be generated:

vggnet.keras

Step 3. Download Pretrained Models (Optional)

If you prefer not to train from scratch, download the pretrained models directly:

[HuggingFace vggnet.keras 다운로드](https://huggingface.co/emtake-ai/vggnet/resolve/main/vggnet.keras)

[HuggingFace vggnet.lne 다운로드](https://huggingface.co/emtake-ai/vggnet/resolve/main/vggnet.lne)

Step 4. Convert Model to NPU Format (LNE)

Convert vggnet.keras into vggnet.lne using Synabro.

[guide](model-conversion-to-npu/readme.md)

Step 5. Transfer Model to Eagleboard

After conversion, transfer the model to the Eagleboard:

[transfer](www.github.com/emtake-ai/eagleboard/transfer.md)

Step 6. Run vggnet on Eagleboard

Log in to the Eagleboard and run:

python3 run_vggnet.py


 

