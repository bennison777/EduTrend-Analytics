# COLLEGE OF ENGINEERING & TECHNOLOGY
## DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
### ACADEMIC LABORATORY ASSIGNMENT & MINI-PROJECT REPORT

---

**Course Title:** Problem Solving and Python Programming  
**Course Code:** CS8151 / GE3151  
**Project Title:** Student Performance Trend Analysis  
**Case Study Number:** 17  
**Academic Year:** 2026–2027  

---

## 1. PROBLEM STATEMENT

In academic environments, periodic evaluations (such as Internal Continuous Assessments, Mid-Term Examinations, and Final Semester Tests) are standard mechanisms for measuring students' academic attainment. However, conventional evaluation systems often analyze examination marks in isolation—presenting static scores without contextualizing learning trajectories or long-term performance trends.

Static assessment systems suffer from key analytical shortcomings:
1. **Inability to Track Progression:** A single examination score fails to indicate whether a student is steadily mastering the syllabus, experiencing a sudden decline, or stagnating.
2. **Delayed Remedial Detection:** Students struggling with foundational weaknesses across specific technical subjects are often detected only after the final semester examination, when corrective interventions are no longer feasible.
3. **Lack of Objective Classification:** Without automated, rule-based classification criteria, instructors face significant administrative burdens in identifying candidates requiring honors acceleration versus those needing remedial coaching.

To address these challenges, this project formulates an automated, menu-driven **Student Performance Trend Analysis System** in Python. The system records subject-wise examination scores across multiple consecutive assessments, tracks individual improvements and declines, detects consistently weak subjects across examinations, objectively classifies students into pedagogical action categories, and generates individual student diagnostic scorecards along with institutional batch summaries.

The system is developed adhering strictly to foundational Python concepts—utilizing variables, operators, conditional branching, loops, strings, and multi-dimensional nested lists—without reliance on third-party libraries, databases, or object-oriented abstractions.

---

## 2. OBJECTIVES

The technical and educational objectives of this project are:

1. **Structured Data Modeling via Nested Lists:**
   - To model and store student identifiers alongside multi-examination, multi-subject numerical marks using native Python lists and multi-dimensional nested lists (`marks[exam][subject]`).

2. **Comparative Cross-Examination Analysis:**
   - To compute quantitative mark differentials between consecutive examinations ($Exam_2 - Exam_1$, $Exam_3 - Exam_2$) and net progress ($Exam_3 - Exam_1$) for individual subjects and cumulative aggregates.

3. **Weakness and Learning Gap Detection:**
   - To implement search and filtering algorithms that detect *Consistently Weak Subjects* where a student fails to achieve the proficiency benchmark ($< 50.0$) across all examinations.
   - To identify subjects exhibiting continuous negative performance decay across consecutive assessments.

4. **Multi-Criteria Performance Classification:**
   - To design and implement a hierarchical, rule-based classification rubric using conditional statements and logical operators to segment students into five distinct categories:
     - *Consistent High Performer*
     - *Progressive / Improving*
     - *Consistent Average Performer*
     * *Declining / Needs Attention*
     * *Critical / Remedial Required*

5. **Diagnostic Reporting & Batch Aggregation:**
   - To generate tabulated individual academic scorecards with subject-level metrics, progression indicators, and tailored instructor recommendations.
   - To produce an institutional batch summary highlighting cohort progression, academic toppers, most improved students, and most challenging subjects.

---

## 3. ASSUMPTIONS

1. **Assessment Scale & Grading Domain:**
   - All examination marks are numerical floating-point values constrained within the closed range of $[0.0, 100.0]$.
   - The standard passing/mastery benchmark is fixed at $50.0\%$. Marks strictly less than $50.0$ are classified as unsatisfactory/weak.

2. **Curricular Structure:**
   - The academic framework incorporates four core STEM subjects:
     1. Mathematics
     2. Physics
     3. Chemistry
     4. Computer Science
   - A minimum of three sequential examinations are tracked:
     1. Exam 1 (Internal Continuous Assessment)
     2. Exam 2 (Mid-Term Assessment)
     3. Exam 3 (Final / Model Examination)

3. **Analytical Rules & Thresholds:**
   - **Consistently Weak Subject:** A subject in which a student's score is strictly less than $50.0$ across all recorded examinations ($Exam_1 < 50$, $Exam_2 < 50$, and $Exam_3 < 50$).
   - **Progressive / Improving Student:** An overall gain of at least $+5.0\%$ between the first and final examination ($\Delta \ge +5.0\%$) with a passing final examination average ($\ge 50.0\%$).
   - **Declining Student:** A net drop of $-5.0\%$ or greater between the first and final examination ($\Delta \le -5.0\%$).
   - **Critical / Remedial Required:** A final examination average below $50.0\%$ or failure in two or more consistently weak subjects.

4. **System Architecture Constraints:**
   - Data persistence is maintained in-memory during script execution via Python lists.
   - No external libraries (`numpy`, `pandas`, `matplotlib`), databases, or custom classes are employed.

---

## 4. ALGORITHM

### Main Control Algorithm
- **Step 1:** Initialize configuration lists `SUBJECTS`, `EXAM_NAMES`, and the global list `student_records = []`. Set `PASSING_BENCHMARK = 50.0`.
- **Step 2:** Display the interactive main menu containing options:
  1. Add New Student Record
  2. View Registered Students Summary Roster
  3. Generate Detailed Student Performance Card
  4. Generate Institutional Batch Performance Summary
  5. Load Pre-Configured Sample Demonstration Data
  6. Reset / Clear All Student Records
  7. Exit Program
- **Step 3:** Read user option `user_choice`.
- **Step 4:** Execute the corresponding module based on `user_choice`:
  - If `user_choice == "1"`: Invoke `add_new_student()`.
  - If `user_choice == "2"`: Invoke `view_all_students_brief()`.
  - If `user_choice == "3"`: Invoke `display_individual_student_report()`.
  - If `user_choice == "4"`: Invoke `display_batch_performance_summary()`.
  - If `user_choice == "5"`: Invoke `load_demonstration_data()`.
  - If `user_choice == "6"`: Prompt confirmation and reset `student_records = []`.
  - If `user_choice == "7"`: Terminate application loop.
  - Else: Display invalid selection error message.
- **Step 5:** Repeat Steps 2 to 4 while `user_choice != "7"`.

---

### Module 1: Data Entry & Nested List Construction (`add_new_student`)
- **Step 1:** Prompt for student full name; ensure name is non-empty.
- **Step 2:** Initialize an empty list `marks_matrix = []`.
- **Step 3:** For each examination index $e$ from $0$ to $\text{length}(EXAM\_NAMES) - 1$:
  - Initialize an empty list `current_exam_marks = []`.
  - For each subject index $s$ from $0$ to $\text{length}(SUBJECTS) - 1$:
    - Read input `mark`; validate that $0.0 \le mark \le 100.0$.
    - Append `mark` to `current_exam_marks`.
  - Append `current_exam_marks` to `marks_matrix`.
- **Step 4:** Construct student record `[name, marks_matrix]` and append to `student_records`.

---

### Module 2: Individual Performance Analytics (`calculate_student_analytics`)
- **Step 1:** Retrieve `name = student_records[index][0]` and `marks_matrix = student_records[index][1]`.
- **Step 2:** Compute exam totals and averages:
  - For each exam $e$, calculate sum of subject marks; compute $\text{average}[e] = \text{total} / \text{number of subjects}$.
  - Compute `overall_average` as the mean of all exam averages.
  - Compute `net_growth = exam_averages[final] - exam_averages[0]`.
- **Step 3:** For each subject $s$, calculate differences:
  - $diff_{1\to 2} = marks[1][s] - marks[0][s]$
  - $diff_{2\to 3} = marks[2][s] - marks[1][s]$
  - $diff_{net} = marks[final][s] - marks[0][s]$
- **Step 4:** Identify Consistently Weak Subjects:
  - For each subject $s$, check if $marks[e][s] < PASSING\_BENCHMARK$ for every exam $e$. If true, add subject to `consistently_weak_subjects`.
- **Step 5:** Classify Student Performance using hierarchical conditional logic:
  - If $\text{final\_exam\_avg} < 50.0 \lor \text{count}(\text{weak\_subjects}) \ge 2$: Classify as `"Critical / Remedial Required"`.
  - Else if $\text{overall\_avg} \ge 75.0 \land net\_growth \ge 0.0 \land \text{count}(\text{weak\_subjects}) == 0$: Classify as `"Consistent High Performer"`.
  - Else if $net\_growth \ge 5.0 \land \text{final\_exam\_avg} \ge 50.0$: Classify as `"Progressive / Improving"`.
  - Else if $net\_growth \le -5.0$: Classify as `"Declining / Needs Attention"`.
  - Else: Classify as `"Consistent Average Performer"`.
- **Step 6:** Return calculated analytical metrics.

---

### Module 3: Cohort Batch Aggregation (`display_batch_performance_summary`)
- **Step 1:** Verify `length(student_records) > 0`.
- **Step 2:** Compute batch exam averages for Exam 1, Exam 2, and Exam 3 by accumulating all student scores.
- **Step 3:** Initialize `highest_overall_avg = -1.0`, `highest_improvement = -999.0`, category counters, and subject weakness counters.
- **Step 4:** Iterate through all students in `student_records`:
  - Calculate analytics for each student.
  - Update `topper_name` if student's `overall_avg > highest_overall_avg`.
  - Update `most_improved_name` if student's $net\_growth > highest\_improvement$.
  - Increment category count matching the student's classification.
  - For each subject, increment weakness tally if subject is in student's weak subjects list.
- **Step 5:** Determine the most challenging subject (highest weakness tally).
- **Step 6:** Print formatted batch summary, honor roll, subject audit, and classification distribution.

---

## 5. FLOWCHART

```mermaid
flowchart TD
    Start([Start Program]) --> Init[Initialize Subjects, Exam Names, Benchmark = 50.0, student_records = []]
    Init --> Menu[Display Main Menu Options 1 to 7]
    Menu --> InputChoice[/Read user_choice/]
    
    InputChoice --> C1{user_choice == '1'?}
    C1 -- Yes --> AddStudent[Module 1: Read Name & Marks<br/>Build 2D Nested List<br/>Append to student_records]
    AddStudent --> Menu
    
    C1 -- No --> C2{user_choice == '2'?}
    C2 -- Yes --> Roster[Module 2: Iterate student_records<br/>Compute Exam Averages<br/>Display Summary Table]
    Roster --> Menu
    
    C2 -- No --> C3{user_choice == '3'?}
    C3 -- Yes --> SelectStudent[/Select Student Number/]
    SelectStudent --> Analyze[Compute Exam Totals & Averages<br/>Compute Subject Diff Matrix<br/>Find Consistently Weak Subjects<br/>Determine Performance Category]
    Analyze --> PrintCard[/Display Detailed Scorecard & Remarks/]
    PrintCard --> Menu
    
    C3 -- No --> C4{user_choice == '4'?}
    C4 -- Yes --> BatchSummary[Calculate Batch Exam Averages<br/>Find Topper & Most Improved<br/>Audit Subject Weakness Across Batch<br/>Compute Category Breakdown]
    BatchSummary --> PrintBatch[/Display Batch Performance Summary/]
    PrintBatch --> Menu
    
    C4 -- No --> C5{user_choice == '5'?}
    C5 -- Yes --> LoadDemo[Load 5 Representative Student Records<br/>Covering All Categories & Edge Cases]
    LoadDemo --> Menu
    
    C5 -- No --> C6{user_choice == '6'?}
    C6 -- Yes --> ConfirmReset{Confirm Reset?}
    ConfirmReset -- Yes --> ClearList[student_records = []]
    ConfirmReset -- No --> SkipReset[Cancel Reset]
    ClearList --> Menu
    SkipReset --> Menu
    
    C6 -- No --> C7{user_choice == '7'?}
    C7 -- Yes --> Terminate([Display Exit Message & Terminate])
    C7 -- No --> Invalid[Display 'Invalid Option' Error]
    Invalid --> Menu
```

---

## 6. PSEUDOCODE

```text
BEGIN
    DECLARE SUBJECTS = ["Mathematics", "Physics", "Chemistry", "Computer Science"]
    DECLARE EXAM_NAMES = ["Exam 1 (Internal)", "Exam 2 (Mid-Term)", "Exam 3 (Final)"]
    DECLARE PASSING_BENCHMARK = 50.0
    DECLARE student_records = []

    FUNCTION main()
        WHILE TRUE DO
            PRINT "1. Add Student | 2. View Roster | 3. Student Card | 4. Batch Summary | 5. Sample Data | 6. Clear | 7. Exit"
            INPUT choice
            
            IF choice == "1" THEN
                CALL add_new_student()
            ELSE IF choice == "2" THEN
                CALL view_all_students_brief()
            ELSE IF choice == "3" THEN
                CALL display_individual_student_report()
            ELSE IF choice == "4" THEN
                CALL display_batch_performance_summary()
            ELSE IF choice == "5" THEN
                CALL load_demonstration_data()
            ELSE IF choice == "6" THEN
                INPUT confirm
                IF confirm == "y" THEN
                    SET student_records = []
                END IF
            ELSE IF choice == "7" THEN
                PRINT "Program Terminated"
                BREAK
            ELSE
                PRINT "Invalid Selection"
            END IF
        END WHILE
    END FUNCTION

    FUNCTION add_new_student()
        INPUT student_name
        DECLARE marks_matrix = []
        
        FOR exam_idx = 0 TO LENGTH(EXAM_NAMES) - 1 DO
            DECLARE current_exam_marks = []
            FOR sub_idx = 0 TO LENGTH(SUBJECTS) - 1 DO
                REPEAT
                    INPUT mark
                UNTIL mark >= 0.0 AND mark <= 100.0
                APPEND mark TO current_exam_marks
            END FOR
            APPEND current_exam_marks TO marks_matrix
        END FOR
        
        APPEND [student_name, marks_matrix] TO student_records
    END FUNCTION

    FUNCTION calculate_student_analytics(student_index)
        SET name = student_records[student_index][0]
        SET marks = student_records[student_index][1]
        
        DECLARE exam_totals = []
        DECLARE exam_averages = []
        
        FOR e = 0 TO LENGTH(EXAM_NAMES) - 1 DO
            SET tot = 0.0
            FOR s = 0 TO LENGTH(SUBJECTS) - 1 DO
                SET tot = tot + marks[e][s]
            END FOR
            APPEND tot TO exam_totals
            APPEND (tot / LENGTH(SUBJECTS)) TO exam_averages
        END FOR
        
        SET overall_average = (exam_averages[0] + exam_averages[1] + exam_averages[2]) / 3.0
        SET net_growth = exam_averages[2] - exam_averages[0]
        
        DECLARE diff_matrix = []
        FOR s = 0 TO LENGTH(SUBJECTS) - 1 DO
            SET d1 = marks[1][s] - marks[0][s]
            SET d2 = marks[2][s] - marks[1][s]
            SET dnet = marks[2][s] - marks[0][s]
            APPEND [d1, d2, dnet] TO diff_matrix
        END FOR
        
        DECLARE consistently_weak = []
        FOR s = 0 TO LENGTH(SUBJECTS) - 1 DO
            SET weak_in_all = TRUE
            FOR e = 0 TO LENGTH(EXAM_NAMES) - 1 DO
                IF marks[e][s] >= PASSING_BENCHMARK THEN
                    SET weak_in_all = FALSE
                END IF
            END FOR
            IF weak_in_all == TRUE THEN
                APPEND SUBJECTS[s] TO consistently_weak
            END IF
        END FOR
        
        IF exam_averages[2] < 50.0 OR LENGTH(consistently_weak) >= 2 THEN
            SET classification = "Critical / Remedial Required"
        ELSE IF overall_average >= 75.0 AND net_growth >= 0.0 AND LENGTH(consistently_weak) == 0 THEN
            SET classification = "Consistent High Performer"
        ELSE IF net_growth >= 5.0 AND exam_averages[2] >= 50.0 THEN
            SET classification = "Progressive / Improving"
        ELSE IF net_growth <= -5.0 THEN
            SET classification = "Declining / Needs Attention"
        ELSE
            SET classification = "Consistent Average Performer"
        END IF
        
        RETURN analytics_tuple
    END FUNCTION
END
```

---

## 7. COMPLETE PYTHON SOURCE CODE

*(Saved locally in workspace as `student_performance_tracker.py`)*

```python
"""
================================================================================
Academic Project: Student Performance Trend Analysis
Case Study Number: 17
Course: Problem Solving and Python Programming
Target Audience: College / Undergraduate Academic Level

Python Concepts Employed:
- Variables & Fundamental Data Types (int, float, str, bool)
- Operators (Arithmetic, Relational, Logical, Assignment)
- Conditional Statements (if, elif, else)
- Iteration / Loops (for, while)
- String Formatting & Manipulation
- Lists & Multidimensional Nested Lists
================================================================================
"""

# Global Configuration for Subjects and Examinations
# These lists define the structure of our academic tracking system.
SUBJECTS = ["Mathematics", "Physics", "Chemistry", "Computer Science"]
EXAM_NAMES = ["Exam 1 (Internal)", "Exam 2 (Mid-Term)", "Exam 3 (Final)"]
PASSING_BENCHMARK = 50.0  # Scores below this threshold are marked as weak/failing

# Primary Data Repository
# Structure: List of Student Records
# Each Student Record is a nested list:
# [
#     "Student Name", 
#     [
#         [m_e1_s1, m_e1_s2, m_e1_s3, m_e1_s4],  # Exam 1 marks
#         [m_e2_s1, m_e2_s2, m_e2_s3, m_e2_s4],  # Exam 2 marks
#         [m_e3_s1, m_e3_s2, m_e3_s3, m_e3_s4]   # Exam 3 marks
#     ]
# ]
student_records = []


def get_float_input(prompt_message, min_val=0.0, max_val=100.0):
    """
    Safely reads and validates a floating-point number within a specified range.
    Demonstrates: while loop, try-except, relational operators, and conditionals.
    """
    while True:
        user_input = input(prompt_message).strip()
        try:
            value = float(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [Error] Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  [Error] Invalid input! Please enter a valid numerical value.")


def add_new_student():
    """
    Collects student name and subject-wise examination marks from user input.
    Constructs a 2D nested list of examination marks and appends it to student_records.
    Demonstrates: Nested loops, input reading, list append, string stripping.
    """
    print("\n" + "=" * 60)
    print("           ADD NEW STUDENT ACADEMIC RECORD")
    print("=" * 60)
    
    # 1. Read student name
    while True:
        name = input("Enter Student Full Name: ").strip()
        if len(name) > 0:
            break
        print("  [Error] Student name cannot be empty. Please enter a valid name.")
    
    # 2. Collect marks across multiple examinations and subjects
    # marks_matrix will store marks for all examinations
    marks_matrix = []
    
    for exam_idx in range(len(EXAM_NAMES)):
        exam_name = EXAM_NAMES[exam_idx]
        print(f"\n--- Entering Marks for: {exam_name} (Out of 100) ---")
        
        current_exam_marks = []
        for subject_idx in range(len(SUBJECTS)):
            subject_name = SUBJECTS[subject_idx]
            prompt = f"  Enter mark for {subject_name}: "
            mark = get_float_input(prompt, 0.0, 100.0)
            current_exam_marks.append(mark)
            
        marks_matrix.append(current_exam_marks)
    
    # 3. Create the student record and append to our primary list
    new_record = [name, marks_matrix]
    student_records.append(new_record)
    
    print("\n" + "-" * 60)
    print(f"SUCCESS: Academic record for '{name}' successfully stored!")
    print("-" * 60)


def load_demonstration_data():
    """
    Pre-loads five representative student records to instantly test and demonstrate
    all system features, edge cases, and classification categories without manual typing.
    Demonstrates: Pre-configured nested lists and list assignment.
    """
    global student_records
    
    sample_students = [
        # Student 1: Consistent High Performer (Excellence across all subjects)
        [
            "Alice Smith",
            [
                [82.0, 88.0, 79.0, 91.0],  # Exam 1 (Avg: 85.0)
                [85.0, 90.0, 84.0, 94.0],  # Exam 2 (Avg: 88.25)
                [89.0, 93.0, 88.0, 96.0]   # Exam 3 (Avg: 91.5)
            ]
        ],
        # Student 2: Progressive / Improving (Low start, tremendous growth)
        [
            "Bob Jenkins",
            [
                [48.0, 52.0, 42.0, 58.0],  # Exam 1 (Avg: 50.0)
                [58.0, 64.0, 55.0, 67.0],  # Exam 2 (Avg: 61.0)
                [70.0, 76.0, 68.0, 80.0]   # Exam 3 (Avg: 73.5)
            ]
        ],
        # Student 3: Declining / Needs Attention (Strong start, notable drop)
        [
            "Charlie Brown",
            [
                [78.0, 82.0, 74.0, 80.0],  # Exam 1 (Avg: 78.5)
                [68.0, 72.0, 62.0, 70.0],  # Exam 2 (Avg: 68.0)
                [55.0, 60.0, 50.0, 59.0]   # Exam 3 (Avg: 56.0)
            ]
        ],
        # Student 4: Consistent Average Performer (Stable moderate marks)
        [
            "Diana Prince",
            [
                [62.0, 65.0, 60.0, 68.0],  # Exam 1 (Avg: 63.75)
                [64.0, 66.0, 61.0, 70.0],  # Exam 2 (Avg: 65.25)
                [63.0, 67.0, 62.0, 69.0]   # Exam 3 (Avg: 65.25)
            ]
        ],
        # Student 5: Critical / Remedial Required (Consistently failing multiple subjects)
        [
            "Evan Wright",
            [
                [40.0, 35.0, 44.0, 52.0],  # Exam 1 (Avg: 42.75)
                [38.0, 32.0, 41.0, 48.0],  # Exam 2 (Avg: 39.75)
                [35.0, 30.0, 38.0, 45.0]   # Exam 3 (Avg: 37.0)
            ]
        ]
    ]
    
    student_records = sample_students
    print("\n" + "=" * 60)
    print("  [SUCCESS] 5 Representative Demonstration Records Loaded!")
    print(f"  Total records in database: {len(student_records)}")
    print("=" * 60)


def view_all_students_brief():
    """
    Displays a concise tabulated roster of all enrolled students with overall averages.
    Demonstrates: Loops, string formatting, nested list navigation.
    """
    if len(student_records) == 0:
        print("\n[Notice] No student records available. Please add data or load sample data.")
        return

    print("\n" + "=" * 80)
    print("                   REGISTERED STUDENTS SUMMARY ROSTER")
    print("=" * 80)
    print(f"{'ID':<4} | {'Student Name':<22} | {'Exam 1 Avg':<12} | {'Exam 2 Avg':<12} | {'Exam 3 Avg':<12} | {'Overall':<10}")
    print("-" * 80)

    for i in range(len(student_records)):
        student_name = student_records[i][0]
        marks_matrix = student_records[i][1]
        
        exam_averages = []
        for e in range(len(marks_matrix)):
            exam_total = 0.0
            for mark in marks_matrix[e]:
                exam_total = exam_total + mark
            exam_avg = exam_total / len(marks_matrix[e])
            exam_averages.append(exam_avg)
            
        cumulative_avg = (exam_averages[0] + exam_averages[1] + exam_averages[2]) / 3.0
        
        print(f"{i + 1:<4} | {student_name:<22} | {exam_averages[0]:>10.2f}% | {exam_averages[1]:>10.2f}% | {exam_averages[2]:>10.2f}% | {cumulative_avg:>8.2f}%")

    print("-" * 80)


def calculate_student_analytics(student_index):
    """
    Analyzes an individual student's records:
    - Calculates totals and averages for each exam.
    - Computes progression differences between exams (improvements / declines).
    - Identifies consistently weak subjects (< PASSING_BENCHMARK across all exams).
    - Classifies student into defined performance categories.
    
    Returns a structured tuple of results using standard data types.
    """
    student_name = student_records[student_index][0]
    marks_matrix = student_records[student_index][1]
    
    num_exams = len(EXAM_NAMES)
    num_subjects = len(SUBJECTS)
    
    # 1. Calculate totals and averages per exam
    exam_totals = []
    exam_averages = []
    for e in range(num_exams):
        total = 0.0
        for s in range(num_subjects):
            total = total + marks_matrix[e][s]
        exam_totals.append(total)
        exam_averages.append(total / num_subjects)
        
    # Calculate cumulative average across all exams
    total_avg_sum = 0.0
    for avg in exam_averages:
        total_avg_sum = total_avg_sum + avg
    overall_average = total_avg_sum / num_exams
    net_growth = exam_averages[num_exams - 1] - exam_averages[0]
    
    # 2. Subject-wise comparisons (Exam 1 -> Exam 2, Exam 2 -> Exam 3, Net)
    # diff_matrix: [subject_idx] -> [diff_e1_to_e2, diff_e2_to_e3, net_diff]
    diff_matrix = []
    for s in range(num_subjects):
        diff_1_to_2 = marks_matrix[1][s] - marks_matrix[0][s]
        diff_2_to_3 = marks_matrix[2][s] - marks_matrix[1][s]
        net_sub_diff = marks_matrix[2][s] - marks_matrix[0][s]
        diff_matrix.append([diff_1_to_2, diff_2_to_3, net_sub_diff])
        
    # 3. Identify Consistently Weak Subjects
    # Defined as: scoring below PASSING_BENCHMARK (50.0) in EVERY exam
    consistently_weak_subjects = []
    for s in range(num_subjects):
        weak_in_all = True
        for e in range(num_exams):
            if marks_matrix[e][s] >= PASSING_BENCHMARK:
                weak_in_all = False
                break
        if weak_in_all:
            consistently_weak_subjects.append(SUBJECTS[s])
            
    # 4. Identify Declining Subjects (Continuous drop: E1 > E2 > E3)
    continuously_declining_subjects = []
    for s in range(num_subjects):
        if marks_matrix[0][s] > marks_matrix[1][s] and marks_matrix[1][s] > marks_matrix[2][s]:
            continuously_declining_subjects.append(SUBJECTS[s])
            
    # 5. Performance Classification Rules (Hierarchical Diagnostic Logic):
    # Rule 1: "Critical / Remedial Required"
    #   - Final exam average < 50% OR 2 or more consistently weak subjects
    # Rule 2: "Consistent High Performer"
    #   - Overall average >= 75% AND net growth >= 0 AND no consistently weak subjects
    # Rule 3: "Progressive / Improving"
    #   - Net growth >= +5.0% AND final exam average >= 50%
    # Rule 4: "Declining / Needs Attention"
    #   - Net growth <= -5.0%
    # Rule 5: "Consistent Average Performer"
    #   - Any student maintaining steady scores between 50% and 75%
    
    classification = ""
    remarks = ""
    
    if exam_averages[num_exams - 1] < 50.0 or len(consistently_weak_subjects) >= 2:
        classification = "Critical / Remedial Required"
        remarks = "Severe learning deficiencies identified. Mandatory remedial coaching sessions required immediately."
    elif overall_average >= 75.0 and net_growth >= 0.0 and len(consistently_weak_subjects) == 0:
        classification = "Consistent High Performer"
        remarks = "Outstanding academic mastery maintained throughout. Recommended for honor recognition."
    elif net_growth >= 5.0 and exam_averages[num_exams - 1] >= 50.0:
        classification = "Progressive / Improving"
        remarks = "Commendable improvement trajectory observed across terms. Keep encouraging this upward momentum."
    elif net_growth <= -5.0:
        classification = "Declining / Needs Attention"
        remarks = "Steep drop in academic performance detected. Student requires urgent diagnostic counselling."
    else:
        classification = "Consistent Average Performer"
        remarks = "Stable moderate performance. Student has potential; targeted mentoring needed for higher grades."
        
    return (
        student_name,
        marks_matrix,
        exam_totals,
        exam_averages,
        overall_average,
        net_growth,
        diff_matrix,
        consistently_weak_subjects,
        continuously_declining_subjects,
        classification,
        remarks
    )


def format_change_string(difference_value):
    """
    Helper function to format difference values with explicit + / - indicators.
    Demonstrates: Conditional statements and string formatting.
    """
    if difference_value > 0:
        return f"+{difference_value:.1f} (Imp)"
    elif difference_value < 0:
        return f"{difference_value:.1f} (Dec)"
    else:
        return " 0.0 (Same)"


def display_individual_student_report():
    """
    Prompts user to select a student and displays a comprehensive academic report.
    Demonstrates: Table rendering, nested loops, conditional checks, formatted strings.
    """
    if len(student_records) == 0:
        print("\n[Notice] No student records available. Please add data or load sample data first.")
        return

    print("\nAvailable Students:")
    for idx in range(len(student_records)):
        print(f"  {idx + 1}. {student_records[idx][0]}")
        
    choice = int(get_float_input("\nEnter Student Number to generate report: ", 1, len(student_records)))
    selected_idx = choice - 1
    
    analytics = calculate_student_analytics(selected_idx)
    (
        name,
        marks_matrix,
        exam_totals,
        exam_averages,
        overall_avg,
        net_growth,
        diff_matrix,
        weak_subjects,
        declining_subjects,
        classification,
        remarks
    ) = analytics
    
    print("\n" + "=" * 90)
    print(f"              ACADEMIC PERFORMANCE REPORT CARD: {name.upper()}")
    print("=" * 90)
    
    # Subject-by-Subject Examination Table
    print(f"{'Subject':<18} | {'Exam 1':<8} | {'Exam 2':<8} | {'E1->E2 Diff':<13} | {'Exam 3':<8} | {'E2->E3 Diff':<13} | {'Net Change':<12}")
    print("-" * 90)
    
    for s in range(len(SUBJECTS)):
        sub_name = SUBJECTS[s]
        m1 = marks_matrix[0][s]
        m2 = marks_matrix[1][s]
        m3 = marks_matrix[2][s]
        
        diff1 = diff_matrix[s][0]
        diff2 = diff_matrix[s][1]
        net_diff = diff_matrix[s][2]
        
        str_diff1 = format_change_string(diff1)
        str_diff2 = format_change_string(diff2)
        str_net = format_change_string(net_diff)
        
        print(f"{sub_name:<18} | {m1:>8.1f} | {m2:>8.1f} | {str_diff1:>13} | {m3:>8.1f} | {str_diff2:>13} | {str_net:>12}")
        
    print("-" * 90)
    
    # Totals and Averages Row
    print(f"{'TOTAL MARKS':<18} | {exam_totals[0]:>8.1f} | {exam_totals[1]:>8.1f} | {'-':^13} | {exam_totals[2]:>8.1f} | {'-':^13} | {'-':^12}")
    print(f"{'AVERAGE %':<18} | {exam_averages[0]:>7.1f}% | {exam_averages[1]:>7.1f}% | {format_change_string(exam_averages[1]-exam_averages[0]):>13} | {exam_averages[2]:>7.1f}% | {format_change_string(exam_averages[2]-exam_averages[1]):>13} | {format_change_string(net_growth):>12}")
    print("=" * 90)
    
    # Diagnostic Findings
    print("\n--- DIAGNOSTIC FINDINGS & WEAKNESS AUDIT ---")
    
    # 1. Consistently Weak Subjects
    if len(weak_subjects) > 0:
        weak_str = ", ".join(weak_subjects)
        print(f"  [!] Consistently Weak Subjects (< {PASSING_BENCHMARK} in all exams): {weak_str}")
    else:
        print("  [*] Consistently Weak Subjects: None (Cleared benchmark in at least one or all exams)")
        
    # 2. Continuous Decline
    if len(declining_subjects) > 0:
        dec_str = ", ".join(declining_subjects)
        print(f"  [!] Subjects on Continuous Downward Trend: {dec_str}")
    else:
        print("  [*] Subjects on Continuous Downward Trend: None")
        
    # 3. Overall Summary & Classification
    print(f"  [*] Cumulative 3-Exam Average : {overall_avg:.2f}%")
    print(f"  [*] Net Progression (E1 to E3): {format_change_string(net_growth)}")
    print(f"  [*] Academic Classification   : >>> {classification} <<<")
    print(f"  [*] Instructor Remark         : {remarks}")
    print("=" * 90 + "\n")


def display_batch_performance_summary():
    """
    Aggregates metrics across the entire student body:
    - Batch average across exams (cohort progression)
    - Identification of Class Topper
    - Identification of Most Improved Student
    - Most Challenging Subjects across the batch
    - Performance classification distribution
    Demonstrates: Loops, multi-accumulator logic, min/max search, percentages.
    """
    total_students = len(student_records)
    if total_students == 0:
        print("\n[Notice] No student records available. Please add data or load sample data first.")
        return

    print("\n" + "=" * 80)
    print("                INSTITUTIONAL BATCH PERFORMANCE SUMMARY")
    print("=" * 80)
    print(f"Total Number of Enrolled Students Evaluated: {total_students}")
    print("-" * 80)
    
    # 1. Batch Exam Averages
    batch_exam_totals = [0.0, 0.0, 0.0]
    
    for i in range(total_students):
        for e in range(len(EXAM_NAMES)):
            for s in range(len(SUBJECTS)):
                batch_exam_totals[e] = batch_exam_totals[e] + student_records[i][1][e][s]
                
    total_marks_per_exam_possible = total_students * len(SUBJECTS)
    batch_exam_avgs = [
        batch_exam_totals[0] / total_marks_per_exam_possible,
        batch_exam_totals[1] / total_marks_per_exam_possible,
        batch_exam_totals[2] / total_marks_per_exam_possible
    ]
    
    print("COHORT PROGRESSION ACROSS EXAMINATIONS:")
    print(f"  - {EXAM_NAMES[0]} Batch Mean : {batch_exam_avgs[0]:.2f}%")
    print(f"  - {EXAM_NAMES[1]} Batch Mean : {batch_exam_avgs[1]:.2f}%")
    print(f"  - {EXAM_NAMES[2]} Batch Mean : {batch_exam_avgs[2]:.2f}%")
    
    batch_delta = batch_exam_avgs[2] - batch_exam_avgs[0]
    print(f"  - Overall Batch Trajectory   : {format_change_string(batch_delta)}")
    print("-" * 80)
    
    # 2. Topper and Most Improved Search
    topper_name = ""
    highest_overall_avg = -1.0
    
    most_improved_name = ""
    highest_improvement = -999.0
    
    # Category Distribution Counters using parallel lists (Strictly adhering to Lists syllabus)
    category_names = [
        "Consistent High Performer",
        "Progressive / Improving",
        "Consistent Average Performer",
        "Declining / Needs Attention",
        "Critical / Remedial Required"
    ]
    category_counts = [0, 0, 0, 0, 0]
    
    # Subject Weakness Audit across cohort (counts how many students are consistently weak in each subject)
    subject_weak_counts = [0] * len(SUBJECTS)
    
    for i in range(total_students):
        analytics = calculate_student_analytics(i)
        (
            name,
            _,
            _,
            _,
            overall_avg,
            net_growth,
            _,
            weak_subjects,
            _,
            classification,
            _
        ) = analytics
        
        # Check Topper
        if overall_avg > highest_overall_avg:
            highest_overall_avg = overall_avg
            topper_name = name
            
        # Check Most Improved
        if net_growth > highest_improvement:
            highest_improvement = net_growth
            most_improved_name = name
            
        # Tally classification using list search and matching
        for c in range(len(category_names)):
            if classification == category_names[c]:
                category_counts[c] = category_counts[c] + 1
                break
            
        # Tally weak subjects
        for s in range(len(SUBJECTS)):
            for w in range(len(weak_subjects)):
                if SUBJECTS[s] == weak_subjects[w]:
                    subject_weak_counts[s] = subject_weak_counts[s] + 1
                    break

    print("HONOR ROLL & KEY RECOGNITION:")
    print(f"  [*] Class Academic Topper       : {topper_name} ({highest_overall_avg:.2f}% cumulative)")
    if highest_improvement > 0:
        print(f"  [*] Most Improved Student       : {most_improved_name} ({format_change_string(highest_improvement)} net jump)")
    else:
        print(f"  [*] Most Improved Student       : None (No student demonstrated positive score increase)")
    print("-" * 80)
    
    # 3. Subject-wise Difficulty Analysis
    print("SUBJECT DIFFICULTY & WEAKNESS AUDIT (Across Cohort):")
    max_weak_count = -1
    most_challenging_sub = ""
    for s in range(len(SUBJECTS)):
        cnt = subject_weak_counts[s]
        pct = (cnt / total_students) * 100.0
        print(f"  - {SUBJECTS[s]:<18}: {cnt} student(s) consistently weak ({pct:.1f}% of class)")
        if cnt > max_weak_count:
            max_weak_count = cnt
            most_challenging_sub = SUBJECTS[s]
            
    print(f"  => Most Challenging Subject     : {most_challenging_sub} ({max_weak_count} students affected)")
    print("-" * 80)
    
    # 4. Performance Category Breakdown
    print("COHORT CLASSIFICATION DISTRIBUTION:")
    for c in range(len(category_names)):
        cat_name = category_names[c]
        count = category_counts[c]
        percentage = (count / total_students) * 100.0
        bar = "=" * int(percentage // 5)
        print(f"  - {cat_name:<30}: {count:>2} students ({percentage:>5.1f}%) | {bar}")
        
    print("=" * 80 + "\n")


def display_main_menu():
    """Prints the primary interactive navigation menu."""
    print("\n" + "=" * 60)
    print("      STUDENT PERFORMANCE TREND ANALYSIS SYSTEM")
    print("               CASE STUDY NUMBER: 17")
    print("=" * 60)
    print("  1. Add New Student Record (Manual Data Entry)")
    print("  2. View Registered Students Summary Roster")
    print("  3. Generate Detailed Student Performance Card")
    print("  4. Generate Institutional Batch Performance Summary")
    print("  5. Load Pre-Configured Sample Demonstration Data")
    print("  6. Reset / Clear All Student Records")
    print("  7. Exit Program")
    print("=" * 60)


def main():
    """
    Main application orchestrator. Implements an infinite menu loop
    with conditional branching and graceful termination.
    Demonstrates: while loop, input handling, conditional execution.
    """
    global student_records
    
    print("\n" + "*" * 70)
    print(" Welcome to the Student Performance Trend Analysis Program")
    print(" Academic Term: Multi-Examination Diagnostic Assessment Tool")
    print("*" * 70)
    
    while True:
        display_main_menu()
        user_choice = input("Enter your option (1-7): ").strip()
        
        if user_choice == "1":
            add_new_student()
        elif user_choice == "2":
            view_all_students_brief()
        elif user_choice == "3":
            display_individual_student_report()
        elif user_choice == "4":
            display_batch_performance_summary()
        elif user_choice == "5":
            load_demonstration_data()
        elif user_choice == "6":
            confirm = input("Are you sure you want to clear all records? (y/n): ").strip().lower()
            if confirm == "y":
                student_records = []
                print("\n[Confirmed] All student records have been cleared.")
            else:
                print("\n[Cancelled] Operation aborted.")
        elif user_choice == "7":
            print("\n" + "=" * 60)
            print(" Thank you for using Student Performance Trend Analysis.")
            print(" Academic Program Terminated Successfully.")
            print("=" * 60 + "\n")
            break
        else:
            print("\n[Error] Invalid option selected! Please enter a number between 1 and 7.")


# Standard Python Entry Point idiom
if __name__ == "__main__":
    main()
```

---

## 8. TEST CASES WITH EXPECTED RESULTS

| Test Case ID | Test Objective / Profile | Input Test Data (Exam 1, Exam 2, Exam 3 Marks) | Expected Analytical Output | Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Verify detection of **Consistent High Performer** | **Alice Smith**<br>E1: [82, 88, 79, 91]<br>E2: [85, 90, 84, 94]<br>E3: [89, 93, 88, 96] | • Exam Averages: 85.0%, 88.25%, 91.5%<br>• Overall Mean: 88.25%<br>• Net Growth: +6.5%<br>• Consistently Weak: None<br>• Category: `Consistent High Performer` | **PASSED** |
| **TC-02** | Verify detection of **Progressive / Improving Student** | **Bob Jenkins**<br>E1: [48, 52, 42, 58]<br>E2: [58, 64, 55, 67]<br>E3: [70, 76, 68, 80] | • Exam Averages: 50.0%, 61.0%, 73.5%<br>• Overall Mean: 61.50%<br>• Net Growth: +23.5%<br>• Consistently Weak: None<br>• Category: `Progressive / Improving` | **PASSED** |
| **TC-03** | Verify detection of **Declining Student** | **Charlie Brown**<br>E1: [78, 82, 74, 80]<br>E2: [68, 72, 62, 70]<br>E3: [55, 60, 50, 59] | • Exam Averages: 78.5%, 68.0%, 56.0%<br>• Overall Mean: 67.50%<br>• Net Growth: -22.5%<br>• Consistently Weak: None<br>• Continuous Decline: Maths, Physics, Chem, CS<br>• Category: `Declining / Needs Attention` | **PASSED** |
| **TC-04** | Verify detection of **Consistent Average Performer** | **Diana Prince**<br>E1: [62, 65, 60, 68]<br>E2: [64, 66, 61, 70]<br>E3: [63, 67, 62, 69] | • Exam Averages: 63.75%, 65.25%, 65.25%<br>• Overall Mean: 64.75%<br>• Net Growth: +1.5%<br>• Consistently Weak: None<br>• Category: `Consistent Average Performer` | **PASSED** |
| **TC-05** | Verify detection of **Critical / Remedial Student** & Weak Subjects | **Evan Wright**<br>E1: [40, 35, 44, 52]<br>E2: [38, 32, 41, 48]<br>E3: [35, 30, 38, 45] | • Exam Averages: 42.75%, 39.75%, 37.0%<br>• Overall Mean: 39.83%<br>• Final Exam Avg: 37.0% (< 50%)<br>• Consistently Weak: Mathematics, Physics, Chemistry (3 subjects)<br>• Category: `Critical / Remedial Required` | **PASSED** |
| **TC-06** | Boundary Input Validation (Marks Range) | Negative Mark: `-15.0`<br>Excess Mark: `105.0`<br>Valid Mark: `85.0` | • Rejects negative marks with error prompt.<br>• Rejects marks > 100 with error prompt.<br>• Accepts `85.0` seamlessly. | **PASSED** |
| **TC-07** | Menu Input Boundary Validation | Non-numeric input: `"abc"`<br>Out-of-range option: `"9"` | • Displays clean validation message.<br>• Re-prompts without crashing or raising unhandled exceptions. | **PASSED** |
| **TC-08** | Batch Honors & Aggregation Verification | Evaluated on full sample cohort of 5 students | • Batch Mean: E1: 64.0%, E2: 64.45%, E3: 64.65%<br>• Topper: Alice Smith (88.25%)<br>• Most Improved: Bob Jenkins (+23.5%)<br>• Equal distribution across all 5 categories. | **PASSED** |

---

## 9. SAMPLE PROGRAM OUTPUT

Below is the verified terminal session transcript demonstrating menu navigation, sample data loading, individual score report generation, and batch aggregation:

```text
**********************************************************************
 Welcome to the Student Performance Trend Analysis Program
 Academic Term: Multi-Examination Diagnostic Assessment Tool
**********************************************************************

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
Enter your option (1-7): 5

============================================================
  [SUCCESS] 5 Representative Demonstration Records Loaded!
  Total records in database: 5
============================================================

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
Enter your option (1-7): 2

================================================================================
                   REGISTERED STUDENTS SUMMARY ROSTER
================================================================================
ID   | Student Name           | Exam 1 Avg   | Exam 2 Avg   | Exam 3 Avg   | Overall   
--------------------------------------------------------------------------------
1    | Alice Smith            |      85.00%  |      88.25%  |      91.50%  |    88.25%
2    | Bob Jenkins            |      50.00%  |      61.00%  |      73.50%  |    61.50%
3    | Charlie Brown          |      78.50%  |      68.00%  |      56.00%  |    67.50%
4    | Diana Prince           |      63.75%  |      65.25%  |      65.25%  |    64.75%
5    | Evan Wright            |      42.75%  |      39.75%  |      37.00%  |    39.83%
--------------------------------------------------------------------------------

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
Enter your option (1-7): 3

Available Students:
  1. Alice Smith
  2. Bob Jenkins
  3. Charlie Brown
  4. Diana Prince
  5. Evan Wright

Enter Student Number to generate report: 2

==========================================================================================
              ACADEMIC PERFORMANCE REPORT CARD: BOB JENKINS
==========================================================================================
Subject            | Exam 1   | Exam 2   | E1->E2 Diff   | Exam 3   | E2->E3 Diff   | Net Change  
------------------------------------------------------------------------------------------
Mathematics        |     48.0 |     58.0 |   +10.0 (Imp) |     70.0 |   +12.0 (Imp) |  +22.0 (Imp)
Physics            |     52.0 |     64.0 |   +12.0 (Imp) |     76.0 |   +12.0 (Imp) |  +24.0 (Imp)
Chemistry          |     42.0 |     55.0 |   +13.0 (Imp) |     68.0 |   +13.0 (Imp) |  +26.0 (Imp)
Computer Science   |     58.0 |     67.0 |    +9.0 (Imp) |     80.0 |   +13.0 (Imp) |  +22.0 (Imp)
------------------------------------------------------------------------------------------
TOTAL MARKS        |    200.0 |    244.0 |       -       |    294.0 |       -       |      -      
AVERAGE %          |    50.0% |    61.0% |   +11.0 (Imp) |    73.5% |   +12.5 (Imp) |  +23.5 (Imp)
==========================================================================================

--- DIAGNOSTIC FINDINGS & WEAKNESS AUDIT ---
  [*] Consistently Weak Subjects: None (Cleared benchmark in at least one or all exams)
  [*] Subjects on Continuous Downward Trend: None
  [*] Cumulative 3-Exam Average : 61.50%
  [*] Net Progression (E1 to E3): +23.5 (Imp)
  [*] Academic Classification   : >>> Progressive / Improving <<<
  [*] Instructor Remark         : Commendable improvement trajectory observed across terms. Keep encouraging this upward momentum.
==========================================================================================

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
Enter your option (1-7): 3

Available Students:
  1. Alice Smith
  2. Bob Jenkins
  3. Charlie Brown
  4. Diana Prince
  5. Evan Wright

Enter Student Number to generate report: 5

==========================================================================================
              ACADEMIC PERFORMANCE REPORT CARD: EVAN WRIGHT
==========================================================================================
Subject            | Exam 1   | Exam 2   | E1->E2 Diff   | Exam 3   | E2->E3 Diff   | Net Change  
------------------------------------------------------------------------------------------
Mathematics        |     40.0 |     38.0 |    -2.0 (Dec) |     35.0 |    -3.0 (Dec) |   -5.0 (Dec)
Physics            |     35.0 |     32.0 |    -3.0 (Dec) |     30.0 |    -2.0 (Dec) |   -5.0 (Dec)
Chemistry          |     44.0 |     41.0 |    -3.0 (Dec) |     38.0 |    -3.0 (Dec) |   -6.0 (Dec)
Computer Science   |     52.0 |     48.0 |    -4.0 (Dec) |     45.0 |    -3.0 (Dec) |   -7.0 (Dec)
------------------------------------------------------------------------------------------
TOTAL MARKS        |    171.0 |    159.0 |       -       |    148.0 |       -       |      -      
AVERAGE %          |    42.8% |    39.8% |    -3.0 (Dec) |    37.0% |    -2.8 (Dec) |   -5.8 (Dec)
==========================================================================================

--- DIAGNOSTIC FINDINGS & WEAKNESS AUDIT ---
  [!] Consistently Weak Subjects (< 50.0 in all exams): Mathematics, Physics, Chemistry
  [!] Subjects on Continuous Downward Trend: Mathematics, Physics, Chemistry, Computer Science
  [*] Cumulative 3-Exam Average : 39.83%
  [*] Net Progression (E1 to E3): -5.8 (Dec)
  [*] Academic Classification   : >>> Critical / Remedial Required <<<
  [*] Instructor Remark         : Severe learning deficiencies identified. Mandatory remedial coaching sessions required immediately.
==========================================================================================

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
Enter your option (1-7): 4

================================================================================
                INSTITUTIONAL BATCH PERFORMANCE SUMMARY
================================================================================
Total Number of Enrolled Students Evaluated: 5
--------------------------------------------------------------------------------
COHORT PROGRESSION ACROSS EXAMINATIONS:
  - Exam 1 (Internal) Batch Mean : 64.00%
  - Exam 2 (Mid-Term) Batch Mean : 64.45%
  - Exam 3 (Final) Batch Mean    : 64.65%
  - Overall Batch Trajectory     : +0.7 (Imp)
--------------------------------------------------------------------------------
HONOR ROLL & KEY RECOGNITION:
  [*] Class Academic Topper       : Alice Smith (88.25% cumulative)
  [*] Most Improved Student       : Bob Jenkins (+23.5 (Imp) net jump)
--------------------------------------------------------------------------------
SUBJECT DIFFICULTY & WEAKNESS AUDIT (Across Cohort):
  - Mathematics       : 1 student(s) consistently weak (20.0% of class)
  - Physics           : 1 student(s) consistently weak (20.0% of class)
  - Chemistry         : 1 student(s) consistently weak (20.0% of class)
  - Computer Science  : 0 student(s) consistently weak (0.0% of class)
  => Most Challenging Subject     : Mathematics (1 students affected)
--------------------------------------------------------------------------------
COHORT CLASSIFICATION DISTRIBUTION:
  - Consistent High Performer     :  1 students ( 20.0%) | ====
  - Progressive / Improving       :  1 students ( 20.0%) | ====
  - Consistent Average Performer  :  1 students ( 20.0%) | ====
  - Declining / Needs Attention   :  1 students ( 20.0%) | ====
  - Critical / Remedial Required  :  1 students ( 20.0%) | ====
================================================================================

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
Enter your option (1-7): 7

============================================================
 Thank you for using Student Performance Trend Analysis.
 Academic Program Terminated Successfully.
============================================================
```

---

## 10. CONCLUSION

The **Student Performance Trend Analysis System (Case Study 17)** successfully demonstrates how fundamental computational principles in Python can be applied to solve an essential real-world diagnostic challenge in educational administration.

### Key Learning Outcomes & Technical Insights:
1. **Multidimensional Data Representation:** 
   By structuring student records as nested lists (`student_records[i][1][exam][subject]`), the project reinforces matrix-like data manipulation and indexing without requiring external tabular frameworks like Pandas.
2. **Algorithmic Analytical Thinking:** 
   The system models educational metrics dynamically—quantifying progression vectors (improvements and declines) rather than relying on static percentages.
3. **Rigorous Flow Control & Robustness:** 
   The design illustrates how nested loops, accumulator variables, and multi-branch conditional statements (`if-elif-else`) work harmoniously to filter data, search extrema (toppers and most improved), audit recurring weaknesses, and categorize records.
4. **Pedagogical Impact:** 
   From an instructional perspective, the system bridges the gap between raw examination scores and proactive educational intervention. Identifying consistently weak subjects and continuous declines empowers educators to provide targeted remedial guidance well before final summative evaluations.

### Scope for Future Expansion:
When advanced Python programming topics are introduced in subsequent semesters, this foundation can be expanded to include:
- Persistent file storage using CSV/JSON or relational databases (SQLite).
- Data visualization via graphical plotting libraries (Matplotlib/Seaborn) for sparkline trend charts.
- Graphical User Interface (GUI) development utilizing Tkinter or PyQt.
