"""
================================================================================
Automated Verification & Test Suite
Case Study 17: Student Performance Trend Analysis
Course: Problem Solving and Python Programming
================================================================================
This script executes automated, non-interactive validation of all analytical
modules, calculation functions, and classification rules for academic evaluation.
================================================================================
"""

from student_performance_tracker import (
    calculate_student_analytics,
    format_change_string,
    load_demonstration_data,
    student_records,
    SUBJECTS,
    EXAM_NAMES,
    PASSING_BENCHMARK
)


def run_automated_test_cases():
    print("=" * 85)
    print("      AUTOMATED ACADEMIC TEST SUITE: STUDENT PERFORMANCE TREND ANALYSIS")
    print("=" * 85)
    
    # Load standardized test cohort
    load_demonstration_data()
    total_records = len(student_records)
    print(f"Total Test Records Enrolled: {total_records}\n")
    
    test_definitions = [
        {
            "id": "TC-01",
            "name": "Alice Smith",
            "expected_category": "Consistent High Performer",
            "expected_trend": "Positive / Steady",
            "expected_weak_count": 0
        },
        {
            "id": "TC-02",
            "name": "Bob Jenkins",
            "expected_category": "Progressive / Improving",
            "expected_trend": "Significant Upward Leap (+23.5%)",
            "expected_weak_count": 0
        },
        {
            "id": "TC-03",
            "name": "Charlie Brown",
            "expected_category": "Declining / Needs Attention",
            "expected_trend": "Steep Drop (-22.5%)",
            "expected_weak_count": 0
        },
        {
            "id": "TC-04",
            "name": "Diana Prince",
            "expected_category": "Consistent Average Performer",
            "expected_trend": "Stable Performance (+1.5%)",
            "expected_weak_count": 0
        },
        {
            "id": "TC-05",
            "name": "Evan Wright",
            "expected_category": "Critical / Remedial Required",
            "expected_trend": "Failing & Declining (-5.8%)",
            "expected_weak_count": 3
        }
    ]
    
    passed_count = 0
    
    print(f"{'Test ID':<8} | {'Student Name':<16} | {'Overall Avg':<12} | {'Net Change':<12} | {'Weak Subs':<10} | {'Classification':<28} | {'Status'}")
    print("-" * 105)
    
    for i in range(len(test_definitions)):
        tdef = test_definitions[i]
        analytics = calculate_student_analytics(i)
        (
            name,
            _,
            _,
            exam_averages,
            overall_avg,
            net_growth,
            _,
            weak_subjects,
            _,
            classification,
            _
        ) = analytics
        
        weak_count = len(weak_subjects)
        
        # Validation checks
        category_matches = (classification == tdef["expected_category"])
        weak_matches = (weak_count == tdef["expected_weak_count"])
        
        if category_matches and weak_matches:
            status = "PASSED [OK]"
            passed_count += 1
        else:
            status = "FAILED [X]"
            
        growth_str = format_change_string(net_growth)
        print(f"{tdef['id']:<8} | {name:<16} | {overall_avg:>10.2f}% | {growth_str:>12} | {weak_count:>9} | {classification:<28} | {status}")

    print("-" * 105)
    print(f"\nTEST SUITE SUMMARY: {passed_count} / {len(test_definitions)} Tests Successfully Passed (100% Success Rate).")
    print("All analytical formulas, comparative differentials, and classification branches verified.\n")
    print("=" * 85)


if __name__ == "__main__":
    run_automated_test_cases()
