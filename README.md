# Nhận diện và đếm số lượng phương tiện giao thông trong các điều kiện thời tiết khắc nghiệt
# 🚦 Traffic Counting under Extreme Weather Conditions

This repository contains the official implementation of the traffic tracking and counting system for my engineering project. The model is built using **YOLO11** and **ByteTrack**, specifically fine-tuned to handle challenging weather conditions (heavy rain, snow, night, fog) using the TSBOW dataset.

## 🌟 Demo Results
*(Ghi chú: Bạn nhớ upload 4 file ảnh thực tế vào thư mục `assets` trên GitHub để ảnh hiển thị ở đây nhé)*

| Normal Condition | Heavy Snow |
| :---: | :---: |
| ![Sunny](assets/ket_qua_sun.jpg) | ![Snow](assets/ket_qua_snow.jpg) |
| **Heavy Rain** | **Night Time** |
| ![Rain](assets/ket_qua_rain.jpg) | ![Night](assets/ket_qua_night.jpg) |

## ✨ Key Features
- **YOLO11m Architecture:** Optimized for detecting small and highly occluded vehicles.
- **ByteTrack Integration:** Maintains consistent tracking IDs even when confidence drops due to extreme weather.
- **Virtual ID Suppression (Ghost-filtering):** A custom dynamic bounding-box logic to strictly prevent double-counting and ID-switching.

## 🛠️ Installation
```bash
# Install required packages
pip install -r requirements.txt
```

⚖️ License & Acknowledgments
1. Codebase License:
The source code (training scripts, object tracking, counting logic) developed in this repository is licensed under the MIT License.

2. Dataset License & Attribution:
This project utilizes the TSBOW (Traffic Surveillance Benchmark for Occluded Vehicles) dataset for training and evaluation.

Creators: Automation Lab, Department of Electrical and Computer Engineering, Sungkyunkwan University.

Paper: TSBOW: Traffic Surveillance Benchmark for Occluded Vehicles Under Various Weather Conditions (AAAI-26)

License: The TSBOW dataset is distributed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license.

Disclaimer: This repository does NOT distribute or host the TSBOW dataset or its derivative weights. To access the dataset, please visit the official Hugging Face repository provided by the authors. This project is strictly for non-commercial, academic research purposes.
