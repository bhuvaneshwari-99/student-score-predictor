# 🎯 Student Score Predictor

A machine learning project using **Linear Regression** to predict a student's performance (final score) based on three key factors:

* 📚 **Hours Studied**
* 🎯 **Attendance Percentage**
* 🧪 **Number of Practice Tests Taken**

---

## 🧩 Problem Statement

Academic performance depends on many factors, and understanding which ones impact scores can help students plan better.

> This project aims to **predict the final score** of a student using simple yet impactful inputs and demonstrate how machine learning can be applied to educational planning.

---

## 🔧 Tech Stack / Tools Used

* 🐍 Python 3.x
* 🧪 Scikit-learn (Linear Regression)
* 📊 Pandas, NumPy
* 📈 Matplotlib, Seaborn (for visualization)
* 🧠 Jupyter Notebook / Google Colab
* 📁 Dataset: `student_scores.csv`

---

## 🧠 Approach / Algorithm

### 👉 Algorithm Used:

* **Multivariate Linear Regression**

### 💾 Features Used:

* Hours Studied
* Attendance Percentage
* Practice Tests Taken

### 📊 Evaluation Metrics:

* **Mean Squared Error (MSE)**
* **R² Score (Coefficient of Determination)**

The model was trained on a sample dataset to predict the final score based on the above features.

---

## 📦 How to Run

1⃣ **Clone the repository**

```bash
git clone https://github.com/yourusername/student-score-predictor.git
cd student-score-predictor
```

2⃣ **Install required dependencies**

```bash
pip install -r requirements.txt
```

3⃣ **Run the script**

```bash
python student_multi_scores.py
```

---

## ✅ Sample Output

### Input:

* Hours Studied: `7.5`
* Attendance: `85%`
* Practice Tests Taken: `4`

### Output:

* 🔮 **Predicted Final Score:** `78.26`
* ✅ **R² Score (Model Accuracy):** `0.94`
* 📉 **Mean Squared Error (MSE):** `9.12`

📈 Visualizations include:

* Actual vs Predicted graph
* Regression Line Plot

---

## 📚 What I Learned

* 📌 Handling and cleaning datasets using **Pandas**
* 📌 Applying **Multivariate Linear Regression** to real-world problems
* 📌 Evaluating model performance using **MSE** and **R² Score**
* 📌 Visualizing model predictions with **Matplotlib** and **Seaborn**
* 📌 Understanding how data-driven insights support academic planning

---

## 🚀 Future Improvements

* ➕ Add more features like:

  * Sleep Hours
  * Assignment Scores
  * Mental Well-being Rating
* 🔁 Try other ML models (Random Forest, XGBoost)
* 🌐 Deploy as a **web app** using **Streamlit** or **Flask**
* 🎛️ Add real-time, interactive user input

---

## 🔗 Credits

* 📊 Dataset created manually for academic purposes
* 💡 Inspired by common patterns in education-related data projects

