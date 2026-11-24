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
                exam_total += mark
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
    
    Returns a dictionary-like structured tuple of results using standard data types.
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
                batch_exam_totals[e] += student_records[i][1][e][s]
                
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
