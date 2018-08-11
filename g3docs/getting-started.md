# Getting Started

## Basic Usage

These set of instructions are for running the trained models.

### Step 1:

Install all required dependencies by running \(does not include tensorflow, opencv3\): `pip install -r requirements.txt`

### Step 2:

Place subjects as seperate folders under `media/train_image_classifier`.

There needs to be a minimum of two subjects.

Download the following models from here:

* [SSDLite mobilenet](https://drive.google.com/open?id=1k6ZXrgo4f0tU18tqlMLjN5tTb_6mwnsS): Place under detection/model/ssdlite\_v2.pb \[This can be customised\].
* [Facenet Mobilenet](https://drive.google.com/open?id=1sBHIXC66tdKlj7pd9zxaEpxcGJmC5NA1): Place the frozen\_inference.pb under detection/model/mobilenet\_v2.pb \[This can be customised\].

### Step 3:

<<<<<<< HEAD:attendance-system/g3docs/getting-started.md
* [Facenet Inception_ Resnet_v1](https://drive.google.com/open?id=1S98bS1bQM9BuxXqmwJAGS6SNkMz_Rzj0): Place the frozen_inference.pb under detection/model/inception_resnet_v1.pb [This can be customised]. 

#### Step 3:

Run
`python train_face_classify.py` (mobilenet)

`python train_face_classify.py --recognition_model inception_resnet_v1`
=======
Run `python train_face_classify.py`
>>>>>>> a591e0012047811cf0d3e09ae28209995fbfdc49:g3docs/getting-started.md

For non-standard flags, run as:

```text
python train_face_classify.py [-h]
                              [--recognition_model {inception_resnet_v1,mobilenet_v2,inception_resnet_v2}]
                              [--detection_model {ssdlite_v2,ssd_mobilenet}]
                              [--trained_classifier TRAINED_CLASSIFIER]
                              [--classifier {SVM,KNN}]
                              [--embedding_size {128,512}]

optional arguments:
  -h, --help            show this help message and exit
  --recognition_model {inception_resnet_v1,mobilenet_v2,inception_resnet_v2}
  --detection_model {ssdlite_v2,ssd_mobilenet}
                        detection model to use
  --trained_classifier TRAINED_CLASSIFIER
                        trained classifier to use
  --classifier {SVM,KNN}
                        trained classifier to use
  --embedding_size {128,512}
                        Embedding Size
```

### Step 4:

Run

<<<<<<< HEAD:attendance-system/g3docs/getting-started.md
`python demo_face_recognition.py (mobilenet)`


`python train_face_classify.py --recognition_model inception_resnet_v1` (inception_resnet)
=======
```text
python demo_face_recognition.py
```

>>>>>>> a591e0012047811cf0d3e09ae28209995fbfdc49:g3docs/getting-started.md