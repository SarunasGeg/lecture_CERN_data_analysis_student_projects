# Dormitory Reverb Analysis

This project analyzes room impulse responses (IRs) from different rooms in my dorm and uses them to add a reverb effect to dry sounds via convolution. It extracts standard room-acoustic features, visualizes them, and generates reverberated audio examples.

## Overview

1. **Dorm rooms analyzed**:
   - Corridor
   - Personal room
   - Kitchen
   - Shower
   - Toilet

3. **Feature Extraction** from impulse responses:
   - RT60 (reverberation time)
   - DRR (Direct-to-Reverberant Ratio)
   - C80 (Clarity index for music)
   - Spectral Centroid (power-based, OpenAE standard)

4. **Statistical Visualization**:
   - Boxplots of each acoustic feature grouped by room/location

5. **Reverb effect**:
   - Convolution of dry audio sources with measured impulse responses
   - Output of normalized, high-quality WAV files

## Features

### Acoustic Metrics

- **RT60**  
  Time (in seconds) for the impulse response to decay by 60 dB.

- **DRR (Direct-to-Reverberant Ratio)**  
  Energy ratio between the first 10 ms and the remaining response.

- **C80 (Clarity Index)**  
  Energy ratio between the first 80 ms and the remaining response, commonly used for music clarity evaluation.

- **Spectral Centroid**  
  Single-value power spectral centroid computed using the OpenAE standard.

## Setup
1. **Clone the repository:**
``` bash
git clone https://github.com/thymerrata/lecture_CERN_data_analysis_student_projects

cd lecture_CERN_data_analysis_student_projects/Jokubas_Genys
```
2. **Install requirements:**
``` bash
pip install -r requirements.txt
```
3. **Run src/main.py:**
``` bash
python src/main.py
```
Results should appear in a new *Results* directory.
