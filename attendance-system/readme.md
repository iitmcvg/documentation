---
description: An experimental setup for face detection and recognition.
---

# Face Recognition Setup

_Computer Vision and Intelligence Group, IIT Madras_

![](../.gitbook/assets/avatar.png)

We implement an experimental setup with face detection and recognition. This has been used for our purposes with the following aims:

* Swapping multiple detectors and feature extractors for facenet.
* Multi GPU and distributed support
* Frozen graph support with quantisation.

Primarily, we use this in two use cases:

* **High accuracy:** SSD or FRCNN detectors with Inception-Resnet feature extractors.
* **CPU optimised FPS**: SSDlite mobilenet with mobilenet V2 extractors \(this is covered in _getting started_\).

## Sample Results

![example](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/media/example.jpg)

## Contents

* [Getting Started](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/getting-started.md)
* [Model Zoo](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/model-zoo.md)
* [Installing Dependencies](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/installing_dependencies.md)

### Facenet Docs

* [David Sandberg's Implementation](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/facenet.md)
* [Retraining Facenet](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/facenet_train_pipeline.md)
* [Recognition with Facenet](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/facenet_recognition_pipeline.md)
* [Facenet Wiki](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/facenet/README.md)

### Object Detection Experimental Setup

* [Object Detection Pipeline](https://github.com/iitmcvg/documentation/tree/814e2c3699ebac10178530a84cf93e0ea5ab71ee/attendance-system/g3docs/object_detection_pipeline.md)

## To Do

* [ ] TF-Estimator based scalable train file.
* [x] SSDLite based detector
* [x] Mobilenet models for facenet
* [x] Angular, Focal and triplet losses.
* [ ] Inference on Singular Videos.
* [ ] DALI, Tensor RT for faster inference.
* [ ] S3D support for detection.
* [ ] Experiments with weight tying.
* [ ] Results Section

## Dependencies

* Python 3.4+
* Tensorflow 1.6+
* Opencv 3.3.1+

## Pipeline

Image -&gt; FaceDetection -&gt; CroppedFace -&gt; FaceRecognition -&gt; Descriptor\(128D\) -&gt; FaceClassifier -&gt; Name

## Credits

## FaceRecognition\(FaceNet\)

TensorFlow implementation of the face recognizer described in the paper "FaceNet: A Unified Embedding for Face Recognition and Clustering". Ref. [https://github.com/davidsandberg/facenet](https://github.com/davidsandberg/facenet)

