LeNet directory structure
```text
lenet-project/
 ├─ dataset : MNIST
 ├─ model-sample/
 │   └─ model/keras/lenet.py
 ├─ train_lenet.py
 └─ run_lenet.py
```

Step 1. Download Dataset

you can download MNIST. in code, there is code to download by code itselft.

Step 2. Train the LeNet Model

Run the training script:

python3 train_lenet.py

After training is complete, the trained model file will be generated:

lenet.keras

Step 3. Download Pretrained Models (Optional)

If you prefer not to train from scratch, download the pretrained models directly:

[HuggingFace lenet.keras download](https://huggingface.co/emtake-ai/lenet/resolve/main/lenet.keras)

[HuggingFace lenet.lne download](https://huggingface.co/emtake-ai/lenet/resolve/main/lenet.lne)

Step 4. Convert Model to NPU Format (LNE)

Convert lenet.keras into lenet.lne using Synabro.

[guide](model-conversion-to-npu/readme.md)
Step 5. Transfer Model to Eagleboard

After conversion, transfer the model to the Eagleboard:

[transfer](www.github.com/emtake-ai/eagleboard/transfer.md)

Step 6. Run LeNet on Eagleboard

Log in to the Eagleboard and run:

python3 run_lenet.py


 






 



