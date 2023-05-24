# FDA AI/ML-Enabled Medical Devices Dashboard

“**Artificial Intelligence (AI)** is the science and engineering of making intelligent machines, especially intelligent computer programs.” ([McCarthy, 2007]( http://jmc.stanford.edu/articles/whatisai/whatisai.pdf)).

AI has the potential to transform healthcare completely by accelerating and enhancing the accuracy of diagnoses, spotting possible health issues before they become serious, creating patient-centered treatment plans for patients, and many other applications.

### The FDA has updated the dataset of AI/ML-enabled medical devices (till 05-October-2022). 

#### Some of the important indicators that we can notice from the dashboard:
-	The number of Medical Devices that the FDA enabled is **521 in total**.
-	**Radiology** has the majority of AI/ML-enabled devices (392 devices).
-	**GE Healthcare** is the top applicant (42 AI/ML-enabled devices).

Refer to the link below to interactively answer your questions.

[![**Open in Streamlit**](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://omar-alkousa-fda-ai-ml-enabled-medical-devices-dash-board.streamlit.app/)

https://github.com/OmarAlkousa/FDA-AI-ML-Enabled-Medical-Devices-Dashboard/assets/64659365/7cbd9d26-04fc-46eb-bea7-4434279d9c6b

## About the Dataset:
The data is available by the FDA following the [link](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices). There are 521 rows and 6 columns, but we used only the following five columns:
- Date of Final Decision: (format mm/dd/yyyy)
- Submission Number: each device has a specific number given by the FDA. This number is useful for searching the device in other FDAs' datasets.
- Device: The name of the medical device that uses AI/ML and is enabled by the FDA.
- Company: the name of the applicant (this column is edited, read the notes below).
- Panel (Lead): the medical field (Radiology, Hematology, etc.)

## Notes:
- This list is not meant to be an exhaustive or comprehensive resource of AI/ML-enabled medical devices. Rather, it is a list of AI/ML-enabled devices across medical disciplines, based on publicly available information.
- A customized column is added "Applicant" based on the original column "Company". The latter contains the names of the companies but you may find different names for the same company, which is bad for grouping the data based on the company name.
