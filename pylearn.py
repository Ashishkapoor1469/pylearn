# name="Ashish";
# Height=5.9;
# student= True;
# text="Hello World";

# print(type(name))
# print(type(Height))
# print(type(student))

# name = input("Enter your name: ")
# Favorite_laguage = input("Enter your Favorite language: ")
# print("Hello, ", name, "your favorite programming language is", Favorite_laguage)


# age = 18;

# if age>=18:
#     print("you can vote");
# else:
#     print("You are too young to vote.");


# for i in range(1,11):
#     print(i)

# c = 1
# while c<=10:
#     print(c)
#     c += 1

# fruits = ["apple", "banana", "cherry"]

# print(fruits[0])  # apple
# print(fruits[1])  # banana
# print(fruits[-1]) # cherry (negative index means from the end)

# fruits.append("mango")   # add element
# fruits.remove("banana")  # remove element
# print(fruits)

# fruits.reverse()
# print(fruits)

# programming_languages = ["Python", "C", "C++", "JavaScript"];

# for language in programming_languages:
#     print("I love ",language)

# def square(n):
#     return n*n

# print(square(5))

# def calculate_area(length, width):
#     return length * width

# print(calculate_area(5,10))

# def power(base, exponent=2):
#     return base** exponent;

# print(power(5))
# print(power(2,3))

# text = "I am learning Python"

# print(text[0:4])
# print(text[-6:])
# print(text[5:13])

# text = "I am learning Python"
# words = text.split()  

# print(words)       # ['I', 'am', 'learning', 'Python']
# print(words[0])    # I
# print(words[1])    # am
# print(words[2])    # learning
# print(words[3])    # Python

# text = "I am learning Python"

# start = text.find("Python")
# print(start)               #14

# print(text[start:start+6])  # python

# quote = "Practice makes a man perfect"

# print(quote)
# new_text = quote.replace("man", "person")
# print(new_text)


# x = 10
# y = 3

# print(x + y)   # 13
# print(x - y)   # 7
# print(x * y)   # 30
# print(x / y)   # 3.333... (division)
# print(x // y)  # 3 (floor division, no decimals)
# print(x % y)   # 1 (remainder)
# print(x ** y)  # 1000 (10 to the power 3)

# import math

# print(math.sqrt(16))   # 4.0
# print(math.pow(2, 5))  # 32.0
# print(math.pi)         # 3.141592653589793



# a = 49
# power=3
# print(math.sqrt(a));
# print(a**power)

# a=1

# if a>0:
#     print("Positive")
# elif a<0:
#     print("Negative")
# else:
#     print("Zero")

# for i in range(1,21):
#       if i%3==0 and i%5==0:
#         print("FizzBuzz")
#       elif i%5==0:
#        print("Buzz")
#       elif i%3==0:
#          print("Fizz")
#       else:
#          print(i)



# student = {
#     "name": "Ashish",
#     "course": "BCA",
#     "college":"Dronacharya College",
#     "favorite_language":"JavaScript,Python,C++"
# }

# print(student["college"])    # Ashish
# student["hobby"]="Playing Chess"
# print(student)

# student = {"name": "Ashish", "course": "BCA", "college": "Dronacharya College","hobby" : "Playing Chess", "favorite_language":"JavaScript,Python,C++"}

# # Loop through keys
# for key in student:
#     print(key, ":", student[key])

# # Loop through items (key + value)
# for key, value in student.items():
#     print(f"{key} -> {value}")

# student = {"name": "Ashish", "course": "BCA", "college": "Dronacharya College","hobby" : "Playing Chess", "favorite_language":"JavaScript,Python,C++"}
# for key in student:
#     print(key,"->",student[key])


# Language = [
#     {"name": "Python","language":"an Interpreted"},
#     {"name": "JavaScript","language":"a Compiled"},
#     {"name": "C++", "language":"an Interpreted"}
# ]

# for n in Language:
#     print(n["name"], "is",n["language"], "language")


# def print_students(st):
#     for s in st:
#      print(s["name"], "is studying in", s["course"])

# students =[{"name":"Ashish","course":"BCA"},{"name":"Rahul","course":"B.tech"},{"name":"sneha","course":"MCA"}]
# print_students(students)

# Open file in write mode ("w")
# file = open("example.txt", "w")
# file.write("Hello, Ashish! Welcome to Python file handling.\n")
# file.write("This is your first file write in Python.")
# file.close()


# file = open("example.txt", "r")
# content = file.read()
# file.close()
# print(content)

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# file = open("example.txt","w");
# file.write("name: Ashish\n")
# file.write("Course: BCA\n")
# file.write("College: Dronacharya College")
# file.close()
# file = open("example.txt","r")
# re =file.read()
# print(re)

# languages=["JavaScript","Python","C++"]
# with open("language.txt","w") as language:
#        for l in languages:
#               language.write(l+"\n")


# try:
#     with open("not_exist.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found!")


# a = input("Enter a number");

# try:
#     num = int(a)
#     print("You entered:",num);
# except Exception as e:
#     print("That’s not a valid number!",e)


# import random;

# a = input("Enter a number ")
# try:
#  num =int(a)
# except Exception as e:
#  print("Enter variable in not a number")
#  exit()
# rand = random.randrange(1,100)
# if rand==num:
#  print("You guessed it!",rand)
# else:
#  print("Wrong! The number was",num,"right answer is ",rand)


# class Student:
#     def __init__(self,name,type):
#         self.name= name;
#         self.type = type;
#     def n(self):
#         print(self.name,"is an",self.type,"language");

# s1 =Student("Python","Interpreted")
# s2 =Student("C++","Compiled")
# s1.n();
# s2.n();



# class Language:
#     def __init__(self,name):
#         self.name= name;
#     def n(self):
#         print(self.name,"is a programing language");
# class ProgrammingLanguage(Language):
#    def __init__(self, name,type):
#        super().__init__(name)
#        self.type = type;
   
#    def lng(self):
#        print(self.name,"is an",self.type,"language");

# s1= Language("Python")
# s2 =ProgrammingLanguage("Python","Interpreted")
# s1.n();
# s2.lng()

# i1= Language("c++");
# i2= ProgrammingLanguage("C++","Compiled")
# i1.n();
# i2.lng();



# student = {"name":"Ashish","course":"BCA"};

# json_data=json.dumps(student);
# print(json_data)

# data = json.loads(json_data);
# print(data["name"])
# import json;

# profile ={"name":"Ashish", "college":"Dronacharya college rait", "course":"BCA", "favorite_language":"Python,Javascript,c++"};

# pro_json= json.dumps(profile,indent=4);
# print(pro_json)

# data = json.loads(pro_json);
# print(data["college"])

# print(profile["college"])


# import datetime;

# date = datetime.date.today()
# time = datetime.datetime.today()
# print(date)
# print(time)

# import requests

# response = requests.get("https://api.github.com")
# print("Status Code:", response.status_code)

# # Print some response content
# print("Response JSON:", response.json())


# import numpy as n

# arr = n.array([10, 20, 30, 40, 50])

# print("Array:", arr)
# print("Mean:", n.mean(arr))
# print("Max value:", n.max(arr))


# import pandas as p

# data = {
#     "Language": ["Python", "C++", "JavaScript"],
#     "Type": ["Interpreted", "Compiled", "Interpreted"]
# }

# df = p.DataFrame(data)
# print(df.iloc[2])
# print(df[df["Type"]=="Interpreted"])



# import pandas as p

# # Read the CSV file
# df = p.read_csv("students.csv")

# # Show the whole DataFrame
# print("All Students:\n", df)

# # Show only the 'Name' column
# print("\nNames:\n", df["Name"])

# # Filter: Students with Course = BCA
# print("\nOnly BCA students:\n", df[df["Course"] == "BCA"])



# import pandas as p

# # Create some data
# students = {
#     "Name": ["Ashish", "Rahul", "Sneha"],
#     "Course": ["BCA", "B.Tech", "MCA"],
#     "College": ["Dronacharya College", "ABC College", "XYZ University"]
# }

# # Convert dictionary → DataFrame
# df = p.DataFrame(students)

# # Save DataFrame into CSV
# df.to_csv("students_saved.csv", index=False)

# print("CSV file created successfully!")


# import pandas as p

# # Load CSV
# df = p.read_csv("students_saved.csv")
# print("Data:\n", df)

# # 1. Count total rows and columns
# print("\nShape (rows, columns):", df.shape)

# # 2. Show basic info
# print("\nInfo:")
# print(df.info())

# # 3. Show first 2 rows
# print("\nFirst 2 rows:\n", df.head(2))

# # 4. Show statistics (only for numeric columns)
# print("\nStatistics:\n", df.describe())

# # 5. Count how many students in each course
# print("\nCourse counts:\n", df["Course"].value_counts())

# # 6. Unique courses
# print("\nUnique courses:", df["Course"].unique())


# import pandas as p

# df = p.read_csv("students_saved.csv")
# print("Original Data:\n", df)

# # Sort by Name (A → Z)
# print("\nSorted by Name:\n", df.sort_values("Name"))

# # Sort by Course (Z → A)
# print("\nSorted by Course (descending):\n", df.sort_values("Course", ascending=False))



# # Group by Course
# grouped = df.groupby("Course")

# # Count students in each course
# print("\nCount by Course:\n", grouped.size())

# # Show names grouped by Course
# for course, group in grouped:
#     print(f"\nCourse: {course}")
#     print(group[["Name", "College"]])


# import pandas as p
# import matplotlib.pyplot as plt

# # Load CSV
# df = p.read_csv("students_saved.csv")

# # 1. Count students by course
# course_counts = df["Course"].value_counts()

# # 2. Bar Chart
# course_counts.plot(kind="bar", title="Students per Course")
# plt.xlabel("Course")
# plt.ylabel("Number of Students")
# plt.show()

# # 3. Pie Chart
# course_counts.plot(kind="pie", autopct="%1.1f%%", title="Course Distribution")
# plt.ylabel("")  # Remove y-label for clean pie chart
# plt.show()


# import matplotlib.pyplot as plt

# plt.plot([1,2,3,4], [10,20,25,30])
# plt.title("Test Plot")
# plt.show()


# import pandas as p
# import matplotlib.pyplot as plt

# # Sample Data
# data = {
#     "Name": ["Ashish", "Rahul", "Sneha", "Rohit", "Anjali"],
#     "Marks": [85, 70, 90, 60, 75],
#     "Age": [20, 21, 22, 20, 23]
# }

# df = p.DataFrame(data)

# # 📈 Line Chart - Students' Marks
# plt.plot(df["Name"], df["Marks"], marker="o", color="blue", label="Marks")
# plt.title("Students' Marks")
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.legend()
# # plt.savefig("line_chart_marks.png")   # ✅ Save as image
# plt.show()

# # 🔵 Scatter Plot - Age vs Marks
# plt.scatter(df["Age"], df["Marks"], color="red")
# plt.title("Age vs Marks")
# plt.xlabel("Age")
# plt.ylabel("Marks")
# # plt.savefig("scatter_age_marks.png")  # ✅ Save as image
# plt



# import pandas as p
# import matplotlib.pyplot as plt

# # Sample Data
# data = {
#     "Name": ["Ashish", "Rahul", "Sneha", "Rohit", "Anjali"],
#     "Marks": [85, 70, 90, 60, 75],
#     "Age": [20, 21, 22, 20, 23]
# }
# df = p.DataFrame(data)

# # Create a figure with 1 row, 3 columns
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# # 📈 Line Chart
# axes[0].plot(df["Name"], df["Marks"], marker="o", color="blue")
# axes[0].set_title("Line Chart - Marks")
# axes[0].set_xlabel("Name")
# axes[0].set_ylabel("Marks")

# # 🔵 Scatter Plot
# axes[1].scatter(df["Age"], df["Marks"], color="red")
# axes[1].set_title("Scatter Plot - Age vs Marks")
# axes[1].set_xlabel("Age")
# axes[1].set_ylabel("Marks")

# # 📊 Bar Chart
# axes[2].bar(df["Name"], df["Marks"], color="green")
# axes[2].set_title("Bar Chart - Marks")
# axes[2].set_xlabel("Name")
# axes[2].set_ylabel("Marks")

# # Adjust layout
# plt.tight_layout()
# # plt.savefig("multiple_charts.png")   # ✅ Save as image
# plt.show()


# import pandas as p
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Sample Data
# data = {
#     "Name": ["Ashish", "Rahul", "Sneha", "Rohit", "Anjali"],
#     "Marks": [85, 70, 90, 60, 75],
#     "Age": [20, 21, 22, 20, 23],
#     "Course": ["BCA", "MCA", "BCA", "M.Tech", "MCA"]
# }
# df = p.DataFrame(data)

# # 🎨 Bar Plot (Seaborn style)
# sns.barplot(x="Name", y="Marks", data=df, palette="coolwarm")
# plt.title("Students' Marks (Seaborn)")
# plt.show()

# # 🎨 Scatter Plot
# sns.scatterplot(x="Age", y="Marks", hue="Course", data=df, s=100)
# plt.title("Age vs Marks (by Course)")
# plt.show()

# # 🎨 Box Plot (Marks Distribution by Course)
# sns.boxplot(x="Course", y="Marks", data=df, palette="pastel")
# plt.title("Marks Distribution by Course")
# plt.show()

# import pandas as p
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Sample Data
# data = {
#     "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     "Marks": [20, 35, 40, 55, 60, 70, 75, 85, 95]
# }
# df = p.DataFrame(data)

# # 📊 Visualize Data
# plt.scatter(df["Hours"], df["Marks"], color="blue")
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.title("Study Hours vs Marks")
# plt.show()

# # 🧠 Train Model
# X = df[["Hours"]]   # Features (input)
# y = df["Marks"]     # Target (output)

# model = LinearRegression()
# model.fit(X, y)

# # ✅ Predict marks for 7.5 hours of study
# predicted = model.predict([[7.5]])
# print("Predicted Marks for 7.5 hours study:", predicted[0])

# # print("Predicted Marks for 2 hours:", model.predict([[2]])[0])
# # print("Predicted Marks for 5 hours:", model.predict([[5]])[0])
# # print("Predicted Marks for 9 hours:", model.predict([[9]])[0])



# import pandas as p
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Dataset
# data = {
#     "Size": [800, 1000, 1200, 1500, 1800, 2000],
#     "Price": [75, 100, 120, 150, 180, 210]
# }

# df = p.DataFrame(data)

# # Plot original data
# plt.scatter(df["Size"], df["Price"], color="blue", marker="o", label="Data Points")
# plt.xlabel("Size (sq. ft.)")
# plt.ylabel("Price (Lakhs)")
# plt.title("Predict House Prices")

# # Train model
# X = df[["Size"]]
# y = df["Price"]

# model = LinearRegression()
# model.fit(X, y)

# # Predictions for given sizes
# sizes = [[1000], [1500], [2500]]
# predictions = model.predict(sizes)

# for s, p_val in zip(sizes, predictions):
#     print(f"Predicted price for {s[0]} sq. ft. = {p_val:.2f} Lakhs")

# # Pl






# import pandas as p
# import matplotlib.pyplot as plt
# # import seaborn as sns
# from sklearn.linear_model import LinearRegression
# data ={
#     "Size":[800,1000,1200,1500,1800,2000],
#     "Price":[75,100,120,150,180,210]
# }

# df = p.DataFrame(data);

# plt.scatter(df["Size"],df["Price"],marker="o")



# plt.xlabel("Size (sq. ft.)")
# plt.ylabel("Price (Lakhs)")
# plt.title("Predict House Prices")
# # plt.show()

# X= df[["Size"]]
# y = df["Price"]

# model = LinearRegression()
# model.fit(X,y)

# size=[[1000],[1400],[2000]]

# pr = model.predict(size)
# for r, f in zip(size,pr):
#  print(f"price pridict for {r[0]}: {f:.2f} lakhs")


# import pandas as p
# import matplotlib as pt
# from sklearn.linear_model import LogisticRegression


# # Sample Dataset
# data = {
#     "Marks": [35, 40, 50, 60, 70, 80],
#     "Pass": [0, 0, 0, 1, 1, 1]  # 0 = Fail, 1 = Pass
# }


# df = p.DataFrame(data)

# X= df[["Marks"]]
# y=df["Pass"]

# model = LogisticRegression()
# model.fit(X,y)

# mask_test= [[45],[55],[75]]
# pr = model.predict(mask_test)

# for m, p_val in zip(mask_test,pr):
#     result="Pass" if p_val==1 else "fail"
#     print(f"Marks {m[0]} -- pridiction {result}")



# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# import matplotlib.pyplot as plt

# # Sample Dataset
# data = {
#     "Marks": [35, 40, 50, 60, 70, 80],
#     "Attendance": [60, 65, 70, 80, 90, 95],  # percentage attendance
#     "Pass": [0, 0, 0, 1, 1, 1]  # 0 = Fail, 1 = Pass
# }

# df = pd.DataFrame(data)

# # Features and target
# X = df[["Marks", "Attendance"]]
# y = df["Pass"]

# # Train Decision Tree Classifier
# model = DecisionTreeClassifier()
# model.fit(X, y)

# # Test Data
# test_data = [[45, 65], [55, 75], [75, 85]]
# predictions = model.predict(test_data)

# # Print Predictions
# for (m, att), p in zip(test_data, predictions):
#     result = "Pass ✅" if p == 1 else "Fail ❌"
#     print(f"Marks={m}, Attendance={att} → Prediction: {result}")

# # Visualize the Tree
# plt.figure(figsize=(8,6))
# plot_tree(model, feature_names=["Marks", "Attendance"], class_names=["Fail", "Pass"], filled=True)
# plt.show()




# import pandas as p
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# import matplotlib.pyplot as plt

# # Dataset
# data = {
#     "Marks": [35, 40, 50, 60, 70, 80],
#     "Pass": [0, 0, 0, 1, 1, 1]  # 0 = Fail, 1 = Pass
# }

# df = p.DataFrame(data)

# X = df[["Marks"]]
# y = df["Pass"]

# # Train Decision Tree
# model = DecisionTreeClassifier()
# model.fit(X, y)

# # Test predictions
# test_marks = [[45], [55], [75]]
# predictions = model.predict(test_marks)

# for m, p_val in zip(test_marks, predictions):
#     result = "Pass ✅" if p_val == 1 else "Fail ❌"
#     print(f"Marks {m[0]} → Prediction: {result}")

# # Visualize the tree
# plt.figure(figsize=(6,4))
# plot_tree(model, feature_names=["Marks"], class_names=["Fail","Pass"], filled=True)
# plt.show()



# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
# from sklearn.model_selection import cross_val_score
# import numpy as np
# import math
# # Dataset
# data = {
#     "Marks": [35, 40, 50, 55, 60, 65, 70, 75, 80, 85],
#     "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
#     "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# }

# df = pd.DataFrame(data)

# X = df[["Marks", "Attendance"]]
# y = df["Pass"]

# # Step 1: Split into train (70%) and test (30%)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1,stratify=y)

# # Step 2: Train model
# model = KNeighborsClassifier(n_neighbors=1)
# model.fit(X_train, y_train)
# # Step 3: Predict on test data
# y_pred = model.predict(X_test)

# # Step 4: Check accuracy
# # accuracy = accuracy_score(y_test, y_pred)
# # print("Predictions:", y_pred)
# # print("Actual:", y_test.values)
# # print("Accuracy:", accuracy)
# scores = cross_val_score(model, X, y, cv=3)  # 3-fold CV
# print("Cross-validation scores:", scores)
# print("Average accuracy:",math.floor(np.mean(scores*100)) ,"%")

# cm = confusion_matrix(y_test, y_pred,labels=[0,1])
# print("Confusion Matrix:\n", cm)

# cr= classification_report(y_test, y_pred,labels=[0,1],target_names=["Fail","Pass"],zero_division=0)
# print("Classification Report:\n",cr)


# import pandas as pd
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import confusion_matrix, classification_report
# import numpy as np
# import math
# import matplotlib.pyplot as plt

# # Dataset
# data = {
#     "Marks": [35, 40, 50, 55, 60, 65, 70, 75, 80, 85],
#     "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
#     "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# }

# df = pd.DataFrame(data)

# X = df[["Marks", "Attendance"]]
# y = df["Pass"]

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, random_state=1, stratify=y
# )

# # Model
# model = KNeighborsClassifier(n_neighbors=1)
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Cross-validation (5-fold this time for better view)
# scores = cross_val_score(model, X, y, cv=5)
# print("Cross-validation scores:", scores)
# print("Average accuracy:", math.floor(np.mean(scores * 100)), "%")

# # Confusion Matrix
# cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
# print("Confusion Matrix:\n", cm)

# # Classification Report
# cr = classification_report(
#     y_test, y_pred, labels=[0, 1], target_names=["Fail", "Pass"], zero_division=0
# )
# print("Classification Report:\n", cr)

# # 📊 Visualization
# plt.figure(figsize=(10,4))

# # Boxplot of scores
# plt.subplot(1, 2, 1)
# plt.boxplot(scores)
# plt.title("Cross-Validation Accuracy (Boxplot)")
# plt.ylabel("Accuracy")

# # Line plot of scores
# plt.subplot(1, 2, 2)
# plt.plot(range(1, len(scores)+1), scores, marker='o')
# plt.title("Cross-Validation Accuracy (per fold)")
# plt.xlabel("Fold")
# plt.ylabel("Accuracy")
# plt.ylim(0,1.1)

# plt.tight_layout()
# plt.show()



# import pandas as pd
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import classification_report, confusion_matrix

# # Dataset
# data = {
#     "Marks": [35, 40, 50, 55, 60, 65, 70, 75, 80, 85],
#     "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
#     "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# }

# df = pd.DataFrame(data)

# X = df[["Marks", "Attendance"]]
# y = df["Pass"]

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, random_state=1, stratify=y
# )

# # Define KNN model
# knn = KNeighborsClassifier()

# # Define parameter grid to search
# param_grid = {
#     "n_neighbors": range(1, 4),   # try k = 1 to 5
#     "weights": ["uniform", "distance"],  # try both
#     "p": [1, 2]   # 1 = Manhattan, 2 = Euclidean
# }



# # GridSearchCV
# grid = GridSearchCV(knn, param_grid, cv=3, scoring="accuracy")
# grid.fit(X_train, y_train)

# print("Best Parameters:", grid.best_params_)
# print("Best Cross-Validation Score:", grid.best_score_)

# # Test performance with best model
# best_model = grid.best_estimator_
# y_pred = best_model.predict(X_test)

# print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))


# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# import matplotlib.pyplot as plt

# # Dataset
# data = {
#     "Marks": [35, 40, 50, 55, 60, 65, 70, 75, 80, 85],
#     "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
#     "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# }
# df = pd.DataFrame(data)

# X = df[["Marks", "Attendance"]]
# y = df["Pass"]

# # Train Decision Tree
# model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=1)
# model.fit(X, y)

# # Plot tree
# plt.figure(figsize=(8,5))
# plot_tree(model, feature_names=["Marks","Attendance"], class_names=["Fail","Pass"], filled=True)
# plt.show()


# from sklearn.tree import DecisionTreeClassifier, plot_tree
# import matplotlib.pyplot as plt
# import pandas as pd

# # Example dataset
# data = {
#     'Marks': [50,70,90,40,65,30],
#     'Attendance': [60,80,85,55,70,50],
#     'Result': [0,1,1,0,1,0]
# }
# df = pd.DataFrame(data)

# X = df[['Marks','Attendance']]
# y = df['Result']

# # Train Decision Tree
# clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
# clf.fit(X, y)

# # Plot Tree
# plt.figure(figsize=(10,6))
# plot_tree(clf, feature_names=['Marks','Attendance'], class_names=['Fail','Pass'], filled=True)
# plt.show()


# from sklearn.tree import DecisionTreeClassifier
# import pandas as p
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score
# import numpy as np
# import math as m

# # Load dataset
# data = p.read_csv("vgsales.csv")

# # Drop useless columns
# data = data.drop(columns=["Rank", "Name"])  

# # Handle missing values
# data = data.dropna()

# # Convert categorical columns to numbers
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()

# # Encode Platform and Publisher
# data["Platform"] = le.fit_transform(data["Platform"])
# data["Publisher"] = le.fit_transform(data["Publisher"].astype(str))  # just in case NaN exists

# # Features and labels
# X = data.drop(columns=["Genre"])
# y = data["Genre"]

# # Encode target as well (Genre is categorical)
# y = le.fit_transform(y)

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42,stratify=y)

# # Model
# model = DecisionTreeClassifier(criterion="gini", max_depth=8, random_state=42)
# model.fit(X_train, y_train)
# # Prediction
# pred = model.predict(X_test)
# print("Predictions:", pred)
# # Accuracy
# score = accuracy_score(y_test, pred)
# print("Test set accuracy:", m.floor(score * 100), "%")


# import xgboost as xgb
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# # Load Iris dataset
# iris = load_iris()
# X = iris.data
# y = iris.target

# # Split dataset
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# # Create XGBoost model
# model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')

# # Train the model
# model.fit(X_train, y_train)

# # Make predictions
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy*100:.2f}%")

# # Predict for a new sample
# sample = [[5.0, 3.6, 1.4, 0.2]]
# prediction = model.predict(sample)
# print("Predicted class:", iris.target_names[prediction][0])


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Dataset
data = {
    "Marks": [35, 40, 50, 55, 60, 65, 70, 75, 80, 85],
    "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Marks", "Attendance"]]
y = df["Pass"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Predictions:", y_pred)
print("Actual:", y_test.values)
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))
