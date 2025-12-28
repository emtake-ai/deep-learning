lenet directory structure

lenet-project/
 ├─ dataset : MNIST
 ├─ model-sample/
 │   └─ model/keras/lenet.py
 ├─ train_lenet.py
 └─ run_lenet.py

 You can see as above directory, you can download the dataset as mnist in code.
 after that, you can download the train_lenet.py, run as below command in cli of Ubuntu

### python3 train_lenet.py in PC

You can get the "lenet.keras" after completing the training.
You should run below command in synabro "docker container".

### synabro --net keras/lenet in PC
Please ask us on this for how to convert using synabro such as installing with docker and running the compiling.
afer this you can get the "lenet.lne".

or you can get directly these from below link
[HuggingFace lenet.keras 다운로드](https://huggingface.co/emtake-ai/lenet/resolve/main/lenet.keras)
[HuggingFace lenet.lne 다운로드](https://huggingface.co/emtake-ai/lenet/resolve/main/lenet.lne)

After downloading above two, using tftp or scp, you can tranfer lne file to the eagleboard.
you can run the run_lenet.py in eaglebaord, using below commmand in cli
python3 run_lenet.py




 



