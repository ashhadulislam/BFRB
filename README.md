# CMI – Detect Behavior with Sensor Data

**Competition link:** [Kaggle – CMI Detect Behavior with Sensor Data](https://www.kaggle.com/competitions/cmi-detect-behavior-with-sensor-data/overview)

---

## Overview

The goal of this competition is to **train machine-learning models** to classify **body-focused repetitive behaviors (BFRBs)** — such as hair-pulling or skin-picking — from wearable sensor data (motion, temperature, proximity) captured by a wrist-worn device.

Such detection has potential relevance in **clinical settings** to track, treat, and understand BFRBs.

---

## Data

Participants are provided with **time-series sensor recordings** collected while participants performed gestures.  
The dataset includes:

- **8 BFRB-like gestures** and **10 non-BFRB-like gestures**  
- **Data modalities:**  
  - IMU (Inertial Measurement Unit / motion)  
  - Thermal (temperature) sensor  
  - ToF (Time-of-Flight / proximity) sensor  
- **Wearable device:** “Helios” device developed by the **Child Mind Institute**

---

## Tasks & Evaluation

- **Primary task:** Gesture classification — given the sensor data, identify which gesture (BFRB-type or non-BFRB) was performed.  
- **Data challenges:** Multimodal, time-series data, possibly noisy or with missing sensor channels.  
- **Additional considerations:** Device orientation (left/right wrist, upside-down), and subject-specific variability.

---

## Why It Matters

- Enables **objective monitoring** of BFRBs outside the clinic.  
- Assists in **early intervention**, **treatment tracking**, and **behavioral-health research**.  
- Presents a **challenging multimodal time-series classification** problem with real-world variability.

---

# Gesture Details

Each participant performed **18 unique gestures**:
- 8 BFRB-like gestures (**Target Gestures**)
- 10 non-BFRB-like gestures (**Non-Target Gestures**)

These were performed in at least one of four body positions:
- Sitting  
- Sitting leaning forward with their non-dominant arm resting on their leg  
- Lying on their back  
- Lying on their side  

The tables below list each gesture and its corresponding video example position(s).

---

## BFRB-Like Gestures (Target Gestures)

| **Gesture** | **Video Example Position(s)** |
|--------------|-------------------------------|
| Above ear – Pull hair | Sitting |
| Forehead – Pull hairline | Sitting leaning forward |
| Forehead – Scratch | Sitting |
| Eyebrow – Pull hair | Sitting |
| Eyelash – Pull hair | Sitting |
| Neck – Pinch skin | Sitting |
| Neck – Scratch | Sitting |
| Cheek – Pinch skin | Sitting, Sitting leaning forward, Lying on back, Lying on side |

---

## Non-BFRB-Like Gestures (Non-Target Gestures)

| **Gesture** | **Video Example Position(s)** |
|--------------|-------------------------------|
| Drink from bottle/cup | Sitting |
| Glasses on/off | Sitting |
| Pull air toward your face | Sitting |
| Pinch knee/leg skin | Sitting leaning forward |
| Scratch knee/leg skin | Sitting leaning forward |
| Write name on leg | Sitting leaning forward |
| Text on phone | Sitting |
| Feel around in tray and pull out an object | Sitting |
| Write name in air | Sitting |
| Wave hello | Sitting |

---
