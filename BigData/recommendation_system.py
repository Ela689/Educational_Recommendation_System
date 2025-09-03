import numpy as np
import joblib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

# Încarcă modelul antrenat
model = joblib.load('random_forest_model.pkl')


# Funcția pentru prezicerea scorului
def make_prediction(model, bac_score, exam_score):
    # Crează un DataFrame cu aceleași denumiri de coloane ca în timpul antrenării modelului
    input_data = pd.DataFrame([[bac_score, exam_score]], columns=["bac_score", "exam_score"])
    predicted_score = model.predict(input_data)[0]
    return predicted_score


# Crearea ferestrei principale
root = tk.Tk()
root.title("Educational Recommendation System")
root.geometry("800x600")

# Adaugă o imagine de fundal
background_image = Image.open("univ.jpg")  # Înlocuiește cu calea imaginii tale
background_image = background_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(background_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Frame transparent pentru conținut, cu fundal gri deschis și margini
frame = tk.Frame(root, bg="#d3d3d3", bd=2, relief="solid", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Etichete și câmpuri de text pentru input
label_font = ("Helvetica", 12, "bold")  # Font mai mare și îngroșat pentru etichete
entry_font = ("Helvetica", 12)  # Font mai mare pentru casetele de text

tk.Label(frame, text="Baccalaureate Score:", bg="#d3d3d3", font=label_font).grid(row=0, column=0, pady=10, sticky="w")
bac_score_entry = tk.Entry(frame, font=entry_font, width=20, bd=2, relief="solid")  # Margini adăugate
bac_score_entry.grid(row=0, column=1, pady=10)

tk.Label(frame, text="Admission Exam Score:", bg="#d3d3d3", font=label_font).grid(row=1, column=0, pady=10, sticky="w")
exam_score_entry = tk.Entry(frame, font=entry_font, width=20, bd=2, relief="solid")
exam_score_entry.grid(row=1, column=1, pady=10)

tk.Label(frame, text="Preferred City (Optional):", bg="#d3d3d3", font=label_font).grid(row=2, column=0, pady=10, sticky="w")
city_entry = tk.Entry(frame, font=entry_font, width=20, bd=2, relief="solid")
city_entry.grid(row=2, column=1, pady=10)

tk.Label(frame, text="Preferred Field of Study (Optional):", bg="#d3d3d3", font=label_font).grid(row=3, column=0, pady=10, sticky="w")
field_of_study_entry = tk.Entry(frame, font=entry_font, width=20, bd=2, relief="solid")
field_of_study_entry.grid(row=3, column=1, pady=10)

# Butonul pentru a calcula recomandarea - plasat sub casetele de input
def get_recommendation():
    try:
        bac_score = float(bac_score_entry.get())
        exam_score = float(exam_score_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")
        return

    # Predicție cu modelul RandomForest
    predicted_score = make_prediction(model, bac_score, exam_score)

    # Recomandare pe baza scorului prezis
    if predicted_score >= 9.0:
        recommended_university = "UMFCLUJ University"
        recommended_faculty = "General Medicine"
    elif predicted_score >= 8.0:
        recommended_university = "UMFCD University"
        recommended_faculty = "Dental Medicine"
    else:
        recommended_university = "UMF Craiova University"
        recommended_faculty = "Medical Assistance"

    # Afișarea rezultatelor
    messagebox.showinfo("Recommendation",
                        f"Predicted Score: {predicted_score:.2f}\nRecommendation: {recommended_university}, {recommended_faculty}")

    # Crearea graficului cu scorurile prezise pentru mai mulți studenți
    students_data = [
        [9.0, 8.5],
        [8.5, 7.8],
        [9.5, 8.9],
        [7.5, 6.5],
        [8.0, 7.5]
    ]

    predicted_scores = [make_prediction(model, bac, exam) for bac, exam in students_data]
    student_ids = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']

    # Crearea graficului
    plt.figure(figsize=(10, 6))
    plt.bar(student_ids, predicted_scores, color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.title('Predicted Admission Scores for Students')
    plt.xlabel('Students')
    plt.ylabel('Predicted Score')
    plt.tight_layout()
    plt.show()


# Butonul pentru a calcula recomandarea - plasat sub casetele de input
get_recommendation_button = tk.Button(frame, text="Get Recommendation", command=get_recommendation, font=("Helvetica", 12, "bold"), relief="solid", bd=2)
get_recommendation_button.grid(row=4, column=0, columnspan=2, pady=20)

# Lansează interfața
root.mainloop()
