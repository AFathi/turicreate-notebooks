# Turi Create Notebooks
This repository's main goal is to explain what [Turi Create](https://github.com/apple/turicreate) is, how to install it, and how to use it. Additionally, I'm providing a few [Jupyter Notebook](http://jupyter.org) examples that demonstrate different uses of the Python package.

Also, in this **README** file, I will explain how to setup `Python`, `pip`, and install the `turicreate` package on your machine.


| Table of Contents  |  Description       |
| ------------------ | ------------------ |
| [What is Turi Create?](#what-is-turi-create) |  Describes what **Turi Create** is and what developers can use it for.|
| [Why use Turi Create?](#why-use-turi-create) | Describes why **Turi Create** is useful for developers. |
| [Requirements](#requirements) | Describes the machine and software requirements needed to use **Turi Create** and run the **Jupyter Notebook** examples.|
| [Install & Setup](#install--setup) | Explains the installation and setup process in details. |
| [Contributions](#contributions) | Describes how you can contribute to this project. |
| [Turi Create Docs](https://apple.github.io/turicreate/docs/api) | Redirects you to the official **Turi Create** documentations. |
| [License](#license) | Describes the license of this project. |

## What is Turi Create?
In the [Turi Create](https://github.com/apple/turicreate) official repository, they describe it as a library that:
>simplifies the development of custom machine learning models. You don't have to be a machine learning expert to add recommendations, object detection, image classification, image similarity or activity classification to your app.

From a point of view of an iOS developer with some background in machine learning, I'd describe it as a library that does the complex mathematical computation for you, while you only worry about finding the right dataset for your machine learning model.

Some machine learning models created using **Turi Create** can easily be exported as a [Core ML](https://developer.apple.com/documentation/coreml) model and be implemented into iOS, macOS, tvOS or watchOS applications.

Models that easily allow **Core ML** exporting include:
- Image Classification models
- Object Detection models

## Why use Turi Create?
In the past few years, the use of machine learning approaches to solve problems and perform complex tasks have been increasing. Machine learning enable us to use big data to perform complex tasks, such as image classification.

Before **Turi Create**, it would be very challenging and time consuming for software developers to create a machine learning model and run it on mobile devices. In order to run a machine learning model on a mobile device, you would have to optimize your model and make it work on devices that doesn't have the hardware capabilities, such as the iPhone.

However, thanks to GraphLab and Apple, now we have both **Turi Create** and **CoreML** that enable us to easily create machine learning models for Apple devices. Turi Create provides us with essential machine learning algorithms, such as k-nearest neighbor, and advanced deep learning algorithms, such as Residual Networks (ResNet), in order to create a production-ready machine learning trained model.

In this repository, I will be demonstrating how to create useful machine learning models that may have many uses in your existing and future applications!

## Requirements
In order to install, setup and try out the example notebooks you will need the following:
- A computer with a 64-bit processor (**x86_64** architecture)
- Anaconda, Python 2.7 version: [Download here](https://www.anaconda.com/download/)

**Note**:- Currently, **Turi Create** only supports Python 2.7.
## Install & Setup
After making sure our machine has **x86_64** architecture we will do the following:

1. Download & install [Anaconda, Python 2.7 version](https://www.anaconda.com/download/)
2. After done installing Anaconda, go to your computer's terminal and create an environment to install **Turi Create**, by doing the following:
```
$ conda create -n turienv
```
3. Activate your new enviornment:
```
source activate turienv
```
4. Install **Turi Create**:
```
pip install -U turicreate
```
5. Restart _Anaconda-Navigator_ then launch Jupyter Notebook

6. Clone this repository and redirect to it through Jupyter Notebook!

## Contributions
If you have an idea for a new **Turi Create** example and want to add it to this repository, feel free to fork the project and create a pull request!

Also, feel free to create an issue if you have any suggestions or need any help ☺️

## License
This repository is published under the MIT license. Check [LICENSE](LICENSE) for more information.

Note:- **Turi Create** is under a BSD-3-Clause license. Check the official repository [LICENSE](https://github.com/apple/turicreate/blob/master/LICENSE.md) for more information.
