# mxnet

* https://mxnet.incubator.apache.org/

書籍 -- https://github.com/d2l-ai/d2l-zh


Ecosystem -- https://mxnet.incubator.apache.org/ecosystem

JavaScript 版 -- https://github.com/dmlc/mxnet.js/

## Ecosystem


GluonCV : GluonCV is a computer vision toolkit with rich model zoo. From object detection to pose estimation.

GluonNLP : GluonNLP provides state-of-the-art deep learning models in NLP. For engineers and researchers to fast prototype research ideas and products.

GluonTS : (安裝失敗) Gluon Time Series (GluonTS) is the Gluon toolkit for probabilistic time series modeling, focusing on deep learning-based models.

Coach RL : Coach is a python reinforcement learning framework containing implementation of many state-of-the-art algorithms, it supports MXNet as a back-end

Deep Graph Library : DGL is a Python package dedicated to deep learning on graphs supporting MXNet as a backend.

GluonFR : Community-driven toolkit for Face Recognition and Face Detection

InsightFace : State-of-the-art face detection and face recognition repository, including ArcFace loss and RetinaFace implementation

Keras-MXNet : Keras-MXNet provides a backend support for the widely used high level API Keras.

MXBoard : MXBoard provides a set of APIs for logging MXNet data for visualization in TensorBoard.

MXFusion : MXFusion is a modular deep probabilistic programming library. It lets you use state-of-the-art inference techniques for specialized probabilistic models.

MXNet Model Server: Model Server for Apache MXNet (MMS) is a flexible and easy to use tool for serving deep learning models exported from MXNet or the Open Neural Network Exchange (ONNX).

Sockeye
Sockeye is a sequence-to-sequence framework for Neural Machine Translation based on Apache MXNet Incubating. It implements state-of-the-art encoder-decoder architectures.

TensorLy : TensorLy is a high level API for tensor methods and deep tensorized neural networks in Python that aims to make tensor learning simple.

TVM : TVM is an open deep learning compiler stack for CPUs, GPUs, and specialized accelerators. It supports a number of framework including MXNet.


## mlpGluon1.py

```
PS D:\ccc\course\ai\python\10-deepLearning\mxnet> python mlpGluon1.py
epoch 1, loss 0.7854, train acc 0.706, test acc 0.830
epoch 2, loss 0.4908, train acc 0.819, test acc 0.848
epoch 3, loss 0.4308, train acc 0.840, test acc 0.863
epoch 4, loss 0.3945, train acc 0.853, test acc 0.867
epoch 5, loss 0.3689, train acc 0.862, test acc 0.868
```

## lenet1.py

```
PS D:\ccc\course\ai\python\10-deepLearning\mxnet> python lenet1.py
conv0 output shape:      (1, 6, 24, 24)
pool0 output shape:      (1, 6, 12, 12)
conv1 output shape:      (1, 16, 8, 8)
pool1 output shape:      (1, 16, 4, 4)
dense0 output shape:     (1, 120)
dense1 output shape:     (1, 84)
dense2 output shape:     (1, 10)
[18:05:36] c:\jenkins\workspace\mxnet-tag\mxnet\src\imperative\./imperative_utils.h:91: GPU support is disabled. Compile MXNet with USE_CUDA=1 to enable GPU support.
training on cpu(0)
epoch 1, loss 2.3199, train acc 0.103, test acc 0.100, time 151.1 sec
epoch 2, loss 1.8678, train acc 0.281, test acc 0.574, time 144.8 sec
epoch 3, loss 0.9355, train acc 0.633, test acc 0.702, time 144.9 sec
epoch 4, loss 0.7461, train acc 0.709, test acc 0.735, time 144.8 sec
epoch 5, loss 0.6694, train acc 0.736, test acc 0.757, time 144.9 sec
```