# 🎓 Educational Recommendation System

An intelligent system that recommends universities and study programs for students, based on their **location, admission scores, and preferences**.  
Developed in **Python** with **Jupyter Notebook**, using **machine learning models** and **data analysis**.

---

## 📖 Project Description
This project analyzes admission data of Romanian students and builds a **recommendation model** that helps future students:  
- Find the **most suitable universities** nearby.  
- Understand their chances of admission based on **Baccalaureate and exam scores**.  
- Receive suggestions tailored to their **field of interest**.  

---

## ⚙️ Workflow

### 🔹 Data Processing Pipeline
The system follows a multi-step pipeline for data preparation, training, and recommendation generation:

![Workflow](images/Screenshot%202025-09-03%20173704.png)

---

### 🔹 Dataset Before Preprocessing
Raw dataset structure with student information, universities, faculties, admission type, and scores:

![Before Preprocessing](images/Screenshot%202025-09-03%20173816.png)

---

### 🔹 Random Forest Model
A simplified view of the **Random Forest** algorithm used for prediction:

![Random Forest](images/Screenshot%202025-09-03%20173841.png)

---

### 🔹 Dataset After Preprocessing
The transformed dataset after feature encoding and cleaning:

![After Preprocessing](images/Screenshot%202025-09-03%201738412.png)

---

### 🔹 Clustering Students
Students were grouped into clusters based on similarities in admission profiles:

![Clustering](images/Screenshot%202025-09-03%20174136.png)

---

### 🔹 Geographical Mapping
Students and universities visualized on a map, showing distances and nearest institutions:

![Map](images/Screenshot%202025-09-03%20174208.png)

---

### 🔹 Model Evaluation & Prediction
Evaluation of the Random Forest model using **Mean Squared Error (MSE)** and predicted admission scores:

![MSE Results](images/Screenshot%202025-09-03%20174303.png)

---

### 🔹 GUI for Recommendations
A simple graphical interface where students can input their scores and preferences to receive personalized recommendations:

![GUI](images/Screenshot%202025-09-03%20174407.png)

---

## ⚙️ Technologies Used
- **Python** (pandas, scikit-learn, matplotlib, seaborn)  
- **Jupyter Notebook**  
- **Machine Learning**:  
  - Random Forest Regressor  
  - OneHot Encoding  
  - Clustering (K-Means, hierarchical methods)  
  - Collaborative Filtering  
- **Data Visualization**: Matplotlib & Seaborn  

---

## 📂 Repository Structure
- `Educational_Recommendation_System.ipynb` – Main Jupyter Notebook with all code, analysis, and results.  
- `data/` – Educational datasets used for training and evaluation.  
- `images/` – Figures and charts included in the presentation.  
- `README.md` – Project documentation (this file).  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Ela689/Educational_Recommendation_System.git
   cd Educational_Recommendation_System
