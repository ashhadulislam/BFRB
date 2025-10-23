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

| **Gesture** |
|--------------|
| Above ear – Pull hair |
| Forehead – Pull hairline |
| Forehead – Scratch |
| Eyebrow – Pull hair |
| Eyelash – Pull hair |
| Neck – Pinch skin |
| Neck – Scratch |
| Cheek – Pinch skin |

---

## Non-BFRB-Like Gestures (Non-Target Gestures)

| **Gesture** |
|--------------|
| Drink from bottle/cup |
| Glasses on/off |
| Pull air toward your face |
| Pinch knee/leg skin |
| Scratch knee/leg skin |
| Write name on leg |
| Text on phone |
| Feel around in tray and pull out an object |
| Write name in air |
| Wave hello |

---
## Tasks & Evaluation

- **Primary task:** Gesture classification — given the sensor data, identify which gesture (BFRB-type or non-BFRB) was performed.  
- **Data challenges:** Multimodal, time-series data, possibly noisy or with missing sensor channels.  
- **Additional considerations:** Device orientation (left/right wrist, upside-down), and subject-specific variability.  

---

### Core Objective

To investigate **how self-supervised pretraining (e.g., CEBRA-Time/Behavior)** improves the **interpretability, structure, and generalization** of learned latent representations compared to purely supervised approaches.

---

### Aspect 1: Interpretability and Mapping

- Evaluate whether the **latent space** learned from sensor data produces **separable clusters** corresponding to known behaviors.  
- Examine if the **latent dimensions** exhibit **meaningful correlations** with raw physical phenomena such as **kinematics, thermal, and proximity** signals.  
- Explore whether the model can be **constrained via inductive biases** (e.g., in the loss function) to enforce interpretable, physically grounded embeddings.

---

### Aspect 2: Performance Under Scarcity and Modality Effects

- Analyze how **multimodal inputs** (IMU, thermal, proximity) and **self-supervised pretraining** contribute to **improved performance and robustness**, particularly when **labeled data are scarce**.  
- Quantify the trade-offs between model complexity, sensor modality inclusion, and data availability.

---

### Aspect 3: Generalization, Stability, and Model Choice

- Assess whether the learned latent representations are **stable over time** (minimal drift) and **generalizable across individuals**.  
- Compare **Transformer-based architectures** to **classical supervised models** in terms of **efficiency, scalability, and usability** for behavior classification and representation learning.

---
# Citation
Laura Newman, David LoBue, Arianna Zuanazzi, Florian Rupprecht, Luke Mears, Roxanne McAdams, Erin Brown, Yanyi Wang, Camilla Strauss, Arno Klein, Lauren Hendrix, Maki Koyama, Josh To, Curt White, Yuki Kotani, Michelle Freund, Michael Milham, Gregory Kiar, Martyna Plomecka, Sohier Dane, and Maggie Demkin. CMI - Detect Behavior with Sensor Data. https://kaggle.com/competitions/cmi-detect-behavior-with-sensor-data, 2025. Kaggle.