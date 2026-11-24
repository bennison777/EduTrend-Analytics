# Student Performance Trend Analysis
## Case Study Number: 17
**Course:** Problem Solving and Python Programming (Undergraduate Academic Lab)

---

## 📌 Project Overview
The **Student Performance Trend Analysis System** is an academic software project designed to track, evaluate, and analyze student examination performance across multiple successive assessments. Unlike conventional static grading tools, this system performs longitudinal comparative analysis: tracking score gains and drops across examinations, detecting consistently weak subjects, and categorizing students into targeted pedagogical action categories.

---

## 📁 Repository & Project Structure

| File Name | Description |
| :--- | :--- |
| [`student_performance_tracker.py`](file:///c:/Users/Bennison/OneDrive/Documents/Student%20Performance%20Trend%20Analysis/student_performance_tracker.py) | **Primary Executable Source Code.** Menu-driven, pure beginner-friendly Python using variables, operators, conditionals, loops, strings, and multi-dimensional nested lists. |
| [`PROJECT_REPORT.md`](file:///c:/Users/Bennison/OneDrive/Documents/Student%20Performance%20Trend%20Analysis/PROJECT_REPORT.md) | **Complete Academic Submission Report.** Includes Problem Statement, Objectives, Assumptions, Algorithm, Mermaid Flowchart, Pseudocode, Test Cases, Sample Terminal Transcripts, and Conclusion. |
| [`run_test_suite.py`](file:///c:/Users/Bennison/OneDrive/Documents/Student%20Performance%20Trend%20Analysis/run_test_suite.py) | **Automated Non-Interactive Test Suite.** Runs all verification test cases and outputs verification tables for instant faculty demonstration. |
| `README.md` | Quick-start guide and project overview. |

---

## 🎯 Syllabus & Python Concepts Map

This project strictly adheres to introductory academic Python constraints (avoiding external libraries, classes, databases, or complex functional concepts):

| Python Syllabus Concept | Project Implementation |
| :--- | :--- |
| **Variables & Primitive Types** | `int`, `float`, `str`, `bool` used for names, counters, sums, benchmarks, and flags. |
| **Operators** | Arithmetic (`+`, `-`, `*`, `/`), Relational (`<`, `>`, `<=`, `>=`, `==`, `!=`), Logical (`and`, `or`, `not`), and Assignment (`+=`, `=`). |
| **Conditional Statements** | Multi-branch `if`, `elif`, `else` blocks for range validation, difference classification, and performance categorization. |
| **Iteration & Loops** | `while` loops for interactive menus and validated input loops; nested `for` loops for navigating examination and subject matrices. |
| **Strings** | String methods (`.strip()`, `.upper()`), ASCII formatting, table column alignments (`:<18`, `:>8.1f`), and concatenation. |
| **Lists & Nested Lists** | Core data structure: 3-tier nested list `student_records[i][1][exam_idx][subject_idx]` modeling dynamic examination performance. |

---

## 🚀 How to Run the Program

### Prerequisites
- Python 3.8 or higher installed.
- Standard terminal / command prompt (PowerShell, Command Prompt, or Bash).
- No external packages needed (`pip install` is NOT required).

### Execution Commands

1. **Run the Interactive Menu-Driven System:**
   ```bash
   python student_performance_tracker.py
   ```
   **Quick Tip:** Once the program starts, select **Option 5** (`Load Pre-Configured Sample Demonstration Data`) to instantly load 5 representative student records covering all performance tiers and test cases.

2. **Run the Automated Test Suite:**
   ```bash
   python run_test_suite.py
   ```

---

## 📋 Menu Navigation Options
```text
============================================================
      STUDENT PERFORMANCE TREND ANALYSIS SYSTEM
               CASE STUDY NUMBER: 17
============================================================
  1. Add New Student Record (Manual Data Entry)
  2. View Registered Students Summary Roster
  3. Generate Detailed Student Performance Card
  4. Generate Institutional Batch Performance Summary
  5. Load Pre-Configured Sample Demonstration Data
  6. Reset / Clear All Student Records
  7. Exit Program
============================================================
```

---

## 📊 Performance Categories Defined

1. **Consistent High Performer:** Cumulative average $\ge 75.0\%$, non-negative net trajectory, zero weak subjects.
2. **Progressive / Improving:** Net growth between Exam 1 and Exam 3 $\ge +5.0\%$ with final average $\ge 50.0\%$.
3. **Consistent Average Performer:** Stable moderate scores ($50.0\% \le \text{Average} < 75.0\%$).
4. **Declining / Needs Attention:** Net decrease between Exam 1 and Exam 3 $\le -5.0\%$.
5. **Critical / Remedial Required:** Final exam average $< 50.0\%$ or $\ge 2$ consistently weak subjects ($< 50.0$ in all exams).
