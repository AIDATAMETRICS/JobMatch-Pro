import tkinter as tk
from tkinter import filedialog, messagebox

class JobMatchApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JobMatch-Pro")
        self.root.geometry("500x400")

        # Upload CV Button
        self.cv_button = tk.Button(self.root, text="Upload CV", command=self.upload_cv)
        self.cv_button.pack(pady=10)

        # Upload Job Description Button
        self.jd_button = tk.Button(self.root, text="Upload Job Description", command=self.upload_jd)
        self.jd_button.pack(pady=10)

        # Display Result
        self.result_label = tk.Label(self.root, text="Score: N/A")
        self.result_label.pack(pady=20)

        # Score Button
        self.score_button = tk.Button(self.root, text="Calculate Score", command=self.calculate_score)
        self.score_button.pack(pady=10)

    def upload_cv(self):
        self.cv_path = filedialog.askopenfilename(title="Select CV File")
        messagebox.showinfo("Selected", f"CV uploaded: {self.cv_path}")

    def upload_jd(self):
        self.jd_path = filedialog.askopenfilename(title="Select Job Description")
        messagebox.showinfo("Selected", f"Job description uploaded: {self.jd_path}")

    def calculate_score(self):
        messagebox.showinfo("Result", "Scoring functionality to be implemented!")

    def run(self):
        self.root.mainloop()

