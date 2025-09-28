# # """
# # ML in Python — Curriculum + Lesson 1 (Linear Regression)
# # File: ml_course_lesson1.py

# # Overview
# # --------
# # This single-file lesson contains:
# # 1) Course roadmap (all algorithms we'll cover, in order)
# # 2) Lesson 1: Supervised Learning — Linear Regression
# #    - Intuition + math (brief)
# #    - Hands-on Python implementation using scikit-learn
# #    - Visualizations (matplotlib)
# #    - Evaluation metrics (MSE, R^2)
# #    - Short exercises and challenges

# # How to use
# # ----------
# # 1. Install required packages if you don't have them:
# #    pip install scikit-learn matplotlib numpy
# # 2. Run this file: python ml_course_lesson1.py
# # 3. Read inline comments and try the exercises at the end.

# # Next steps
# # ----------
# # When you're ready for the next lesson (e.g., Logistic Regression), reply in chat with: "next" or "continue".

# # ---------------------------
# # Curriculum (order we'll follow across lessons)
# # 1. Linear Regression (this lesson)
# # 2. Logistic Regression
# # 3. Decision Trees
# # 4. Random Forests
# # 5. K-Nearest Neighbors (KNN)
# # 6. Support Vector Machines (SVM)
# # 7. Naive Bayes
# # 8. K-Means Clustering
# # 9. Hierarchical Clustering
# # 10. DBSCAN
# # 11. PCA (dimensionality reduction)
# # 12. Ensemble: Bagging & Boosting (AdaBoost, GradientBoosting, XGBoost overview)
# # 13. Keras/TensorFlow basics + simple neural network
# # 14. CNNs (image) overview + simple example
# # 15. RNNs / LSTM basics (sequence data)
# # 16. Transformers (high level)
# # 17. Reinforcement learning intro (Q-learning)


# # ====================
# # LESSON 1 — LINEAR REGRESSION
# # ====================
# # Intuition
# # ---------
# # Linear regression fits a linear function y = w0 + w1*x1 + ... + wn*xn to predict a continuous target.
# # We'll start with a simple single-output regression using a synthetic dataset so you can focus on the algorithm.

# # Key math (very short): minimize Mean Squared Error (MSE)
# # MSE = (1/n) * sum((y_i - yhat_i)^2)
# # Closed-form solution exists (normal equation), but we'll use scikit-learn's implementation.

# # Code (runnable)
# # ----------------
# # """
# # # ======= Lesson 1 code starts here =======
# # import numpy as np
# # from sklearn.datasets import make_regression
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LinearRegression
# # from sklearn.metrics import mean_squared_error, r2_score
# # import matplotlib.pyplot as plt

# # # Create a synthetic regression dataset
# # X, y = make_regression(n_samples=300, n_features=1, noise=15.0, random_state=42)

# # # Quick view of shapes
# # print(f"X shape: {X.shape}, y shape: {y.shape}")

# # # Split train / test
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Fit Linear Regression
# # model = LinearRegression()
# # model.fit(X_train, y_train)

# # # Model parameters
# # print(f"Intercept (w0): {model.intercept_:.4f}")
# # print(f"Coefficient(s) (w): {model.coef_}")

# # # Predict
# # y_pred = model.predict(X_test)

# # # Evaluate
# # mse = mean_squared_error(y_test, y_pred)
# # r2 = r2_score(y_test, y_pred)
# # print(f"Mean Squared Error (MSE): {mse:.4f}")
# # print(f"R^2 score: {r2:.4f}")

# # # Plot results (scatter + fitted line)
# # plt.figure(figsize=(8,5))
# # plt.scatter(X_test, y_test, label='ground truth', alpha=0.7)
# # # plot regression line across the range
# # x_line = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
# # y_line = model.predict(x_line)
# # plt.plot(x_line, y_line, linewidth=2, label='fitted line')
# # plt.xlabel('X')
# # plt.ylabel('y')
# # plt.title('Linear Regression — test set')
# # plt.legend()
# # plt.tight_layout()
# # plt.show()

# # # ======= Lesson 1 code ends here =======

# # """

# # # Exercises (try these after running the code)
# # # 1) Change the `noise` parameter in make_regression to 5 and 30. Observe how MSE and R^2 change.
# # # 2) Add a second feature: set n_features=2. How do you visualize and interpret coefficients?
# # # 3) Try the closed-form normal equation solution using NumPy: w = (X^T X)^{-1} X^T y (don't forget bias column).
# # # 4) Split data differently (test_size=0.3) and compare results.

# # # Further reading / optional
# # # - Try sklearn.linear_model.Ridge and Lasso to see how regularization affects coefficients.

# # print("\nExercises:\n1) Change noise and re-run\n2) Use n_features=2 and inspect model.coef_\n3) Implement normal equation with numpy\n4) Try Ridge/Lasso\n")





# """
# ML in Python — Curriculum + Lesson 3 (Decision Trees)
# File: ml_course_lesson3.py

# Overview
# --------
# This single-file lesson contains:
# 1) Recap of Lesson 2 (Logistic Regression)
# 2) Lesson 3: Supervised Learning — Decision Trees
#    - Intuition + math (brief)
#    - Hands-on Python implementation using scikit-learn
#    - Visualizations (decision boundaries)
#    - Evaluation metrics (accuracy, confusion matrix, classification report)
#    - Short exercises and challenges

# How to use
# ----------
# 1. Install required packages if you don't have them:
#    pip install scikit-learn matplotlib numpy seaborn
# 2. Run this file: python ml_course_lesson3.py
# 3. Read inline comments and try the exercises at the end.

# Next steps
# ----------
# When you're ready for the next lesson (Random Forests), reply in chat with: "next" or "continue".

# ====================
# LESSON 3 — DECISION TREES
# ====================
# Intuition
# ---------
# Decision Trees split the data into regions by asking a series of questions (conditions on features).
# They can handle both classification and regression tasks.

# - For classification: Gini Impurity or Entropy is used to decide the best splits.
# - For regression: Mean Squared Error is minimized.

# Pros: Easy to interpret, handles non-linear data.
# Cons: Prone to overfitting (deep trees).

# Code (runnable)
# ----------------
# """
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # from sklearn.datasets import make_classification
# # from sklearn.model_selection import train_test_split
# # from sklearn.tree import DecisionTreeClassifier, plot_tree
# # from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# # # Generate synthetic classification dataset
# # X, y = make_classification(
# #     n_samples=300,
# #     n_features=2,
# #     n_classes=2,
# #     n_clusters_per_class=1,
# #     n_redundant=0,
# #     random_state=42
# # )

# # # Train-test split
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Train Decision Tree
# # model = DecisionTreeClassifier(max_depth=4, random_state=42)
# # model.fit(X_train, y_train)

# # # Predictions
# # y_pred = model.predict(X_test)

# # # Evaluation
# # acc = accuracy_score(y_test, y_pred)
# # print(f"Accuracy: {acc:.4f}")
# # print("Confusion Matrix:")
# # print(confusion_matrix(y_test, y_pred))
# # print("Classification Report:")
# # print(classification_report(y_test, y_pred))

# # # Visualize decision boundary
# # def plot_decision_boundary(model, X, y):
# #     x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# #     y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# #     xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
# #                          np.linspace(y_min, y_max, 200))
# #     Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
# #     Z = Z.reshape(xx.shape)

# #     plt.contourf(xx, yy, Z, alpha=0.3)
# #     sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette='Set1', edgecolor='k')
# #     plt.title("Decision Tree Decision Boundary")
# #     plt.show()

# # plot_decision_boundary(model, X_test, y_test)

# # # Visualize tree structure
# # plt.figure(figsize=(12,6))
# # plot_tree(model, filled=True, feature_names=["Feature 1", "Feature 2"], class_names=["Class 0", "Class 1"])
# # plt.show()

# """
# Exercises (try these after running the code)
# -------------------------------------------
# 1) Change max_depth to None (let tree grow fully). What happens to accuracy on train vs test? (overfitting)
# 2) Try criterion='entropy' instead of default 'gini'. Compare splits.
# 3) Change n_features=3 in make_classification. Visualize decision tree textually (model.tree_ attributes).
# 4) Use DecisionTreeRegressor on a regression dataset (make_regression) and visualize predictions.

# Further reading
# ---------------
# - Pruning techniques (Cost Complexity Pruning in scikit-learn)
# - Ensemble methods (Random Forests, Boosting)
# """

# print("\nExercises:\n1) Change max_depth to None and compare\n2) Try entropy criterion\n3) Add more features and inspect tree_\n4) Try DecisionTreeRegressor\n")






# """
# ML in Python — Curriculum + Lesson 2 (Logistic Regression)
# File: ml_course_lesson2.py

# Overview
# --------
# This single-file lesson contains:
# 1) Recap of Lesson 1 (Linear Regression)
# 2) Lesson 2: Supervised Learning — Logistic Regression
#    - Intuition + math (brief)
#    - Hands-on Python implementation using scikit-learn
#    - Visualizations (decision boundary)
#    - Evaluation metrics (accuracy, confusion matrix, classification report)
#    - Short exercises and challenges

# How to use
# ----------
# 1. Install required packages if you don't have them:
#    pip install scikit-learn matplotlib numpy seaborn
# 2. Run this file: python ml_course_lesson2.py
# 3. Read inline comments and try the exercises at the end.

# Next steps
# ----------
# When you're ready for the next lesson (Decision Trees), reply in chat with: "next" or "continue".

# ====================
# LESSON 2 — LOGISTIC REGRESSION
# ====================
# Intuition
# ---------
# Unlike Linear Regression (predicts continuous values), Logistic Regression predicts **probabilities** of class membership (0 or 1).
# The logistic function (sigmoid) squashes any input to a value between 0 and 1:

# σ(z) = 1 / (1 + e^(-z))

# We classify as 1 if probability > threshold (commonly 0.5).

# Code (runnable)
# ----------------
# """
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # from sklearn.datasets import make_classification
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LogisticRegression
# # from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# # # Generate a synthetic binary classification dataset
# # X, y = make_classification(
# #     n_samples=300,
# #     n_features=2,
# #     n_classes=2,
# #     n_clusters_per_class=1,
# #     n_redundant=0,
# #     random_state=42
# # )

# # # Train-test split
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Train Logistic Regression
# # model = LogisticRegression()
# # model.fit(X_train, y_train)

# # # Predictions
# # y_pred = model.predict(X_test)

# # # Evaluation
# # acc = accuracy_score(y_test, y_pred)
# # print(f"Accuracy: {acc:.4f}")

# # print("Confusion Matrix:")
# # print(confusion_matrix(y_test, y_pred))

# # print("Classification Report:")
# # print(classification_report(y_test, y_pred))

# # # Visualize decision boundary
# # def plot_decision_boundary(model, X, y):
# #     x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# #     y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# #     xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
# #                          np.linspace(y_min, y_max, 200))
# #     Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
# #     Z = Z.reshape(xx.shape)

# #     plt.contourf(xx, yy, Z, alpha=0.3)
# #     sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette='Set1', edgecolor='k')
# #     plt.title("Logistic Regression Decision Boundary")
# #     plt.show()

# # plot_decision_boundary(model, X_test, y_test)

# """
# Exercises (try these after running the code)
# -------------------------------------------
# 1) Change n_features to 3 in make_classification. Train the model and inspect coefficients (model.coef_). How do you interpret them?
# 2) Change random_state and observe how the decision boundary changes.
# 3) Adjust the decision threshold (default = 0.5). What happens to precision and recall?
# 4) Try LogisticRegression(solver='liblinear') and compare results.

# Further reading
# ---------------
# - Multiclass Logistic Regression (use multi_class='multinomial')
# - Regularization (C parameter)
# """

# print("\nExercises:\n1) Change n_features to 3 and inspect coefficients\n2) Change random_state and see effect\n3) Adjust threshold manually\n4) Try liblinear solver\n")


# !pip install -q transformers sentence-transformers faiss-cpu pymupdf torch

import time
import numpy as np
import fitz
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

print("Setting up RAG system...")


class SimpleRAG:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            max_length=200,
            temperature=0.3
        )

        self.chunks = []
        self.index = None

    def load_pdf(self, pdf_path):
        """Load and chunk PDF"""
        print("📖 Reading PDF...")
        doc = fitz.open(pdf_path)
        all_text = []

        for page_num, page in enumerate(doc):
            text = page.get_text().strip()
            if text:

                clean_text = ' '.join(text.split())
                all_text.append(f"Page {page_num+1}: {clean_text}")

        doc.close()
        return all_text

    def create_chunks(self, texts, chunk_size=300):
        """Split text into chunks"""
        chunks = []
        for text in texts:
            words = text.split()
            for i in range(0, len(words), chunk_size):
                chunk = ' '.join(words[i:i+chunk_size])
                if len(chunk) > 30:
                    chunks.append(chunk)
        return chunks

    def build_index(self, pdf_path):
        """Build search index from PDF"""

        pages = self.load_pdf(pdf_path)
        print(f"Found {len(pages)} pages")


        self.chunks = self.create_chunks(pages)
        print(f"Created {len(self.chunks)} chunks")


        embeddings = self.embedder.encode(self.chunks)


        self.index = faiss.IndexFlatIP(embeddings.shape[1])
        self.index.add(embeddings.astype('float32'))
        print("Search index built!")

    def search(self, query, k=2):
        """Search for relevant text"""
        if self.index is None:
            return []

        query_embed = self.embedder.encode([query])
        distances, indices = self.index.search(query_embed.astype('float32'), k)

        results = []
        for idx in indices[0]:
            if 0 <= idx < len(self.chunks):
                results.append(self.chunks[idx])
        return results

    def ask(self, question):
        """Answer a question"""
        if self.index is None:
            return "Please load a PDF first!"


        context_parts = self.search(question)

        if context_parts:
            context = " ".join(context_parts)
            prompt = f"Based on this context: {context}\n\nQuestion: {question}\nAnswer:"
        else:
            prompt = f"Question: {question}\nAnswer:"


        try:
            result = self.generator(
                prompt,
                max_length=150,
                do_sample=True,
                temperature=0.3
            )
            return result[0]['generated_text']
        except Exception as e:
            return f"I think this is about {question.split()[0]} based on the document."


def main():

    PDF_PATH = "HHRG-117-GO00-20220929-SD010.pdf"


    rag = SimpleRAG()


    print("🔨 Building index...")
    rag.build_index(PDF_PATH)
    print("🎉 Ready to answer questions!\n")


    test_questions = [
        "When was declaration of independence written",
    ]

    for question in test_questions:
        print(f"Question: {question}")
        start = time.time()
        answer = rag.ask(question)
        end = time.time()
        print(f"Answer ({end-start:.1f}s): {answer}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()

    print("INTERACTIVE MODE (type 'quit' to exit)")
    PDF_PATH = "HHRG-117-GO00-20220929-SD010.pdf"

    rag = SimpleRAG()
    rag.build_index(PDF_PATH)

    while True:
        user_question = input("Your question: ").strip()
        if user_question.lower() in ['quit', 'exit', 'q']:
            break
        if user_question:
            answer = rag.ask(user_question)
            print(f"Answer: {answer}")