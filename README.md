# CrewAI Assignment: AI Research Assistant

## Overview
Welcome to the CrewAI Assignment! In this project, you will build an AI-powered research assistant using **CrewAI**. The goal is to develop two AI agents:
1. **Researcher Agent** – Collects research data on a given topic.
2. **Writer Agent** – Summarizes the research findings into a readable format.

This assignment will help you understand **multi-agent workflows, automation, and AI-driven text generation**. You will also learn how to use GitHub for version control and automated testing.

---

## 📝 Assignment Details

### 📌 Your Task
- Implement the **Researcher** agent to fetch relevant data.
- Implement the **Writer** agent to summarize the collected data.
- Ensure that your code passes all test cases.
- Push your final code to your assigned GitHub repository.

### 📂 Repository Structure

Your repository should follow this structure:
```
crewai_assignment/
│── agents/
│   ├── researcher.py  # Researcher agent implementation
│   ├── writer.py  # Writer agent implementation
│── tasks/
│   ├── research_task.py  # Research task logic
│   ├── writing_task.py  # Writing task logic
│── tests/
│   ├── test_agents.py  # Unit tests for agents
│   ├── test_tasks.py  # Unit tests for tasks
│── main.py  # Entry point of the project
│── README.md  # Assignment details
│── requirements.txt  # Dependencies
│── .github/
│   ├── workflows/
│       ├── autograding.yml  # Auto-grading setup
```

### 🔹 Functionality Requirements
- The **Researcher** agent should return at least **two key points** about the given topic.
- The **Writer** agent should generate a summary that includes at least **one reference to AI**.
- The code should be modular and follow clean coding practices.

---

## 🏗️ Setup Instructions

### **Step 1: Clone the Repository**
Once you accept the GitHub Classroom assignment link, a repository will be created for you. Clone it to your local machine:
```bash
git clone <your-repository-url>
cd crewai_assignment
```

### **Step 2: Install Dependencies**
Make sure you have Python installed (>=3.10). Install dependencies using:
```bash
pip install -r requirements.txt
```

### **Step 3: Implement Your Code**
Modify the following files:
- `agents/researcher.py` – Implement the **fetch_data()** method.
- `agents/writer.py` – Implement the **summarize()** method.

### **Step 4: Run Your Code**
Test your implementation by running:
```bash
python main.py
```

### **Step 5: Run Test Cases**
Before submitting, ensure all tests pass by running:
```bash
python -m unittest discover tests
```

If all tests pass, you will see:
```
OK (2 tests passed)
```

---

## 🚀 Submission Guidelines

### ✅ **Rules for Submission**
1. **All test cases must pass** before submission.
2. **Commit frequently** to track your progress.
3. **Do not modify test cases** (`tests/test_agents.py`, `tests/test_tasks.py`).
4. **Push your code to GitHub** before the deadline:
   ```bash
   git add .
   git commit -m "Final submission"
   git push origin main
   ```

### 🔹 **How to Check Submission Status?**
1. Go to your GitHub repository.
2. Click on **Actions** → You will see the **Auto-Grading Results**.
3. If all checks pass (✅), your submission is correct.
4. If there are errors (❌), fix them and push again.

### ❗ **Deadline**
All submissions must be pushed to GitHub before **the deadline provided by the instructor**. Late submissions may not be considered.

---

## 📢 Grading Criteria
Your assignment will be evaluated based on:
| Criteria            | Weightage |
|--------------------|-----------|
| Code correctness (passes tests) | 40% |
| Code quality & modularity  | 20% |
| Proper use of Git & version control  | 20% |
| Documentation (comments, README updates) | 10% |
| On-time submission | 10% |

---

## 💡 Tips for Success
- **Read the test cases** before coding to understand expected outputs.
- **Commit your progress regularly** to avoid losing work.
- **Use GitHub Actions logs** to debug failing tests.
- **Ask for help if stuck** – use classroom discussions or instructor guidance.

---


Happy Coding! 🚀
