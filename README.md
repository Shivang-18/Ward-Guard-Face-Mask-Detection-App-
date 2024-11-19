# Ward-Guard: Precise Mask Detection for Optimal Infection Control

Ward-Guard is a real-time face mask detection system designed to enhance infection control in healthcare settings such as hospital wards, clinics, and nursing homes. By leveraging computer vision and deep learning, the system identifies whether individuals are wearing face masks and notifies hospital authorities of non-compliance, ensuring the safety of patients with weakened immunity.

## Objectives:

-> Detect whether individuals entering critical hospital areas are wearing face masks.

-> Automate the enforcement of mask-wearing policies through real-time alerts to hospital staff.

-> Provide visual feedback via bounding boxes and probabilities on detected faces.


## Key Features:

-> Deep Learning Models: Trained MobileNetV2 and ResNet-50 architectures, with MobileNetV2 achieving 98.68% accuracy.

-> Real-time Alerts: Integrated with the Twilio API to send immediate notifications to ward staff.

-> Data Visualization: Overlay bounding boxes and detection probabilities on live video streams.


## Methodology:

#### 1. Data Collection:

-> Utilized Covid-19-PIS and Kaggle datasets containing thousands of images labeled as "with_mask" and "without_mask."

-> Augmented data with operations such as rotation, flipping, and zooming to enhance diversity.

#### 2. Model Training:

-> Preprocessed images (resized to 224x224 pixels and normalized).

-> Trained on MobileNetV2 with parameters optimized for low loss and high accuracy.

#### 3. Deployment:

-> Integrated the model with OpenCV for real-time detection.

-> Implemented Twilio-based alert notifications for non-compliance.


## Outcomes:

-> MobileNetV2 outperformed ResNet-50, demonstrating superior accuracy and efficiency.

-> Real-time alerts and visual feedback systems proved effective in ensuring mask compliance.

-> Insights into data augmentation and preprocessing were gained, highlighting their impact on model performance.


## Future Enhancements:

-> Integration with access control systems for automated entry management.

-> Biometric authentication for hospital personnel.

-> Intelligent mask dispensing systems for improved compliance and hygiene.
