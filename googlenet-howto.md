googlenet directory structure
```text
googlenet-project/
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
 │   └─ model/keras/googlenet.py
 ├─ train_googlenet.py
 └─ run_googlenet.py
```

Step 1. Download Dataset

Download the googlenet dataset ZIP file from HuggingFace.

[HuggingFace googlenet datasset download](https://huggingface.co/datasets/emtake-ai/googlenet/resolve/main/googlenet-dataset.zip)

After downloading, extract it into the dataset/ directory:

unzip googlenet-dataset.zip -d ./dataset

Step 2. Train the googlenet Model

Run the training script:

python3 train_googlenet.py

After training is complete, the trained model file will be generated:

googlenet.keras

Step 3. Download Pretrained Models (Optional)

If you prefer not to train from scratch, download the pretrained models directly:

[HuggingFace googlenet.keras download](https://huggingface.co/emtake-ai/googlenet/resolve/main/googlenet.keras)

[HuggingFace googlenet.lne download](https://huggingface.co/emtake-ai/googlenet/resolve/main/googlenet.lne)

Step 4. Convert Model to NPU Format (LNE)

Convert googlenet.keras into googlenet.lne using Synabro.

[guide](model-conversion-to-npu/readme.md)

Step 5. Transfer Model to Eagleboard

After conversion, transfer the model to the Eagleboard:

[transfer](www.github.com/emtake-ai/eagleboard/transfer.md)

Step 6. Run googlenet on Eagleboard

Log in to the Eagleboard and run:

python3 run_googlenet.py


 

