/**
 * EduTrend Analytics - Web Application Engine
 * Academic Project: Student Performance Trend Analysis (Case Study 17)
 * Course: Problem Solving and Python Programming
 */

// Configuration Constants
const SUBJECTS = ["Mathematics", "Physics", "Chemistry", "Computer Science"];
const EXAM_NAMES = ["Exam 1 (Internal)", "Exam 2 (Mid-Term)", "Exam 3 (Final)"];
const PASSING_BENCHMARK = 50.0;

// Standard Sample Cohort
const SAMPLE_STUDENTS = [
    [
        "Alice Smith",
        [
            [82.0, 88.0, 79.0, 91.0], // Exam 1
            [85.0, 90.0, 84.0, 94.0], // Exam 2
            [89.0, 93.0, 88.0, 96.0]  // Exam 3
        ]
    ],
    [
        "Bob Jenkins",
        [
            [48.0, 52.0, 42.0, 58.0],
            [58.0, 64.0, 55.0, 67.0],
            [70.0, 76.0, 68.0, 80.0]
        ]
    ],
    [
        "Charlie Brown",
        [
            [78.0, 82.0, 74.0, 80.0],
            [68.0, 72.0, 62.0, 70.0],
            [55.0, 60.0, 50.0, 59.0]
        ]
    ],
    [
        "Diana Prince",
        [
            [62.0, 65.0, 60.0, 68.0],
            [64.0, 66.0, 61.0, 70.0],
            [63.0, 67.0, 62.0, 69.0]
        ]
    ],
    [
        "Evan Wright",
        [
            [40.0, 35.0, 44.0, 52.0],
            [38.0, 32.0, 41.0, 48.0],
            [35.0, 30.0, 38.0, 45.0]
        ]
    ]
];

// In-Memory & LocalStorage State
let studentRecords = [];
let cohortChartInstance = null;
let individualChartInstance = null;

// ================= INITIALIZATION =================
document.addEventListener("DOMContentLoaded", () => {
    initData();
    setupNavigation();
    setupEventListeners();
    renderAllViews();
});

function initData() {
    const saved = localStorage.getItem("eduTrend_student_data");
    if (saved) {
        try {
            studentRecords = JSON.parse(saved);
        } catch (e) {
            studentRecords = JSON.parse(JSON.stringify(SAMPLE_STUDENTS));
        }
    } else {
        studentRecords = JSON.parse(JSON.stringify(SAMPLE_STUDENTS));
        saveData();
    }
}

function saveData() {
    localStorage.setItem("eduTrend_student_data", JSON.stringify(studentRecords));
}

// ================= ANALYTICS CORE LOGIC =================
function calculateStudentAnalytics(studentIndex) {
    const name = studentRecords[studentIndex][0];
    const marksMatrix = studentRecords[studentIndex][1];

    const numExams = EXAM_NAMES.length;
    const numSubjects = SUBJECTS.length;

    // 1. Totals & averages per examination
    const examTotals = [];
    const examAverages = [];

    for (let e = 0; e < numExams; e++) {
        let total = 0.0;
        for (let s = 0; s < numSubjects; s++) {
            total += marksMatrix[e][s];
        }
        examTotals.push(total);
        examAverages.push(total / numSubjects);
    }

    const cumulativeAvg = (examAverages[0] + examAverages[1] + examAverages[2]) / 3.0;
    const netGrowth = examAverages[numExams - 1] - examAverages[0];

    // 2. Subject-wise difference matrix [s] -> [diff1to2, diff2to3, netDiff]
    const diffMatrix = [];
    for (let s = 0; s < numSubjects; s++) {
        const d1 = marksMatrix[1][s] - marksMatrix[0][s];
        const d2 = marksMatrix[2][s] - marksMatrix[1][s];
        const dnet = marksMatrix[2][s] - marksMatrix[0][s];
        diffMatrix.push([d1, d2, dnet]);
    }

    // 3. Consistently Weak Subjects (< 50 in ALL exams)
    const consistentlyWeakSubjects = [];
    for (let s = 0; s < numSubjects; s++) {
        let weakInAll = true;
        for (let e = 0; e < numExams; e++) {
            if (marksMatrix[e][s] >= PASSING_BENCHMARK) {
                weakInAll = false;
                break;
            }
        }
        if (weakInAll) {
            consistentlyWeakSubjects.push(SUBJECTS[s]);
        }
    }

    // 4. Continuously Declining Subjects (E1 > E2 > E3)
    const continuouslyDecliningSubjects = [];
    for (let s = 0; s < numSubjects; s++) {
        if (marksMatrix[0][s] > marksMatrix[1][s] && marksMatrix[1][s] > marksMatrix[2][s]) {
            continuouslyDecliningSubjects.push(SUBJECTS[s]);
        }
    }

    // 5. Hierarchical Classification Rubric
    let classification = "";
    let remarks = "";
    let tierClass = "";

    if (examAverages[numExams - 1] < 50.0 || consistentlyWeakSubjects.length >= 2) {
        classification = "Critical / Remedial Required";
        remarks = "Severe learning deficiencies identified. Mandatory remedial coaching sessions required immediately.";
        tierClass = "tier-critical";
    } else if (cumulativeAvg >= 75.0 && netGrowth >= 0.0 && consistentlyWeakSubjects.length === 0) {
        classification = "Consistent High Performer";
        remarks = "Outstanding academic mastery maintained throughout. Recommended for honor recognition.";
        tierClass = "tier-high";
    } else if (netGrowth >= 5.0 && examAverages[numExams - 1] >= 50.0) {
        classification = "Progressive / Improving";
        remarks = "Commendable improvement trajectory observed across terms. Keep encouraging this upward momentum.";
        tierClass = "tier-improving";
    } else if (netGrowth <= -5.0) {
        classification = "Declining / Needs Attention";
        remarks = "Steep drop in academic performance detected. Student requires urgent diagnostic counselling.";
        tierClass = "tier-declining";
    } else {
        classification = "Consistent Average Performer";
        remarks = "Stable moderate performance. Student has potential; targeted mentoring needed for higher grades.";
        tierClass = "tier-average";
    }

    return {
        name,
        marksMatrix,
        examTotals,
        examAverages,
        cumulativeAvg,
        netGrowth,
        diffMatrix,
        consistentlyWeakSubjects,
        continuouslyDecliningSubjects,
        classification,
        remarks,
        tierClass
    };
}

// Format Difference with badge
function formatDiff(val) {
    if (val > 0) return `<span class="diff-tag pos">+${val.toFixed(1)}</span>`;
    if (val < 0) return `<span class="diff-tag neg">${val.toFixed(1)}</span>`;
    return `<span class="diff-tag zero">0.0</span>`;
}

// ================= VIEW RENDERING =================
function renderAllViews() {
    renderDashboard();
    populateStudentSelect();
    renderScorecard(0);
    renderRoster();
}

// 1. Dashboard View
function renderDashboard() {
    const totalStudents = studentRecords.length;
    document.getElementById("valTotalStudents").textContent = totalStudents;

    if (totalStudents === 0) {
        document.getElementById("valTopperName").textContent = "N/A";
        document.getElementById("valTopperScore").textContent = "0.0%";
        document.getElementById("valImprovedName").textContent = "N/A";
        document.getElementById("valImprovedScore").textContent = "0.0%";
        document.getElementById("valChallengingSub").textContent = "N/A";
        document.getElementById("valChallengingCount").textContent = "0 Students";
        return;
    }

    // Batch Exam Trajectory
    const batchExamTotals = [0, 0, 0];
    for (let i = 0; i < totalStudents; i++) {
        for (let e = 0; e < 3; e++) {
            for (let s = 0; s < 4; s++) {
                batchExamTotals[e] += studentRecords[i][1][e][s];
            }
        }
    }

    const totalMarksPossiblePerExam = totalStudents * 4;
    const batchExamAvgs = [
        batchExamTotals[0] / totalMarksPossiblePerExam,
        batchExamTotals[1] / totalMarksPossiblePerExam,
        batchExamTotals[2] / totalMarksPossiblePerExam
    ];

    document.getElementById("exam1MeanVal").textContent = `${batchExamAvgs[0].toFixed(2)}%`;
    document.getElementById("exam2MeanVal").textContent = `${batchExamAvgs[1].toFixed(2)}%`;
    document.getElementById("exam3MeanVal").textContent = `${batchExamAvgs[2].toFixed(2)}%`;

    const batchDelta = batchExamAvgs[2] - batchExamAvgs[0];
    const trendText = batchDelta >= 0 ? `+${batchDelta.toFixed(1)}% Overall Net` : `${batchDelta.toFixed(1)}% Overall Net`;
    document.getElementById("batchNetTrendBadge").textContent = trendText;

    // Topper & Most Improved & Category Tallies
    let topperName = "";
    let highestOverall = -1;
    let mostImprovedName = "";
    let highestGain = -999;

    const categoryNames = [
        "Consistent High Performer",
        "Progressive / Improving",
        "Consistent Average Performer",
        "Declining / Needs Attention",
        "Critical / Remedial Required"
    ];
    const categoryClasses = ["cat-fill-high", "cat-fill-improving", "cat-fill-average", "cat-fill-declining", "cat-fill-critical"];
    const categoryCounts = [0, 0, 0, 0, 0];
    const subjectWeakCounts = [0, 0, 0, 0];

    for (let i = 0; i < totalStudents; i++) {
        const a = calculateStudentAnalytics(i);

        if (a.cumulativeAvg > highestOverall) {
            highestOverall = a.cumulativeAvg;
            topperName = a.name;
        }

        if (a.netGrowth > highestGain) {
            highestGain = a.netGrowth;
            mostImprovedName = a.name;
        }

        const catIdx = categoryNames.indexOf(a.classification);
        if (catIdx !== -1) categoryCounts[catIdx]++;

        for (let s = 0; s < 4; s++) {
            if (a.consistentlyWeakSubjects.includes(SUBJECTS[s])) {
                subjectWeakCounts[s]++;
            }
        }
    }

    // Update KPI Card values
    document.getElementById("valTopperName").textContent = topperName;
    document.getElementById("valTopperScore").textContent = `${highestOverall.toFixed(2)}% Cumulative Mean`;

    document.getElementById("valImprovedName").textContent = highestGain > 0 ? mostImprovedName : "None";
    document.getElementById("valImprovedScore").textContent = highestGain > 0 ? `+${highestGain.toFixed(1)}% Net Growth` : "No positive jump";

    let maxWeak = -1;
    let challengingSub = SUBJECTS[0];
    for (let s = 0; s < 4; s++) {
        if (subjectWeakCounts[s] > maxWeak) {
            maxWeak = subjectWeakCounts[s];
            challengingSub = SUBJECTS[s];
        }
    }
    document.getElementById("valChallengingSub").textContent = challengingSub;
    document.getElementById("valChallengingCount").textContent = `${maxWeak} Student(s) affected`;

    // Render Category Distribution Bars
    const catBarsContainer = document.getElementById("categoryBarsList");
    catBarsContainer.innerHTML = "";
    for (let c = 0; c < categoryNames.length; c++) {
        const count = categoryCounts[c];
        const pct = ((count / totalStudents) * 100).toFixed(1);
        const item = document.createElement("div");
        item.className = "cat-bar-item";
        item.innerHTML = `
            <div class="cat-bar-label-row">
                <span>${categoryNames[c]}</span>
                <span>${count} students (${pct}%)</span>
            </div>
            <div class="cat-bar-track">
                <div class="cat-bar-fill ${categoryClasses[c]}" style="width: ${pct}%"></div>
            </div>
        `;
        catBarsContainer.appendChild(item);
    }

    // Render Subject Audit Grid
    const auditGrid = document.getElementById("subjectAuditGrid");
    auditGrid.innerHTML = "";
    for (let s = 0; s < 4; s++) {
        const cnt = subjectWeakCounts[s];
        const pct = ((cnt / totalStudents) * 100).toFixed(1);
        const card = document.createElement("div");
        card.className = "subject-audit-card";
        const badgeClass = cnt > 0 ? "badge-pill danger" : "badge-pill success";
        card.innerHTML = `
            <div>
                <h4 class="sub-audit-title">${SUBJECTS[s]}</h4>
                <span class="sub-audit-stat">${cnt} of ${totalStudents} students consistently failing</span>
            </div>
            <span class="${badgeClass}">${pct}% Failure</span>
        `;
        auditGrid.appendChild(card);
    }

    // Render Cohort Chart
    renderCohortChart(batchExamAvgs);
}

// Cohort Progression Line Chart
function renderCohortChart(averages) {
    const ctx = document.getElementById("cohortTrajectoryChart");
    if (!ctx) return;

    if (window.Chart) {
        if (cohortChartInstance) cohortChartInstance.destroy();
        cohortChartInstance = new Chart(ctx, {
            type: "line",
            data: {
                labels: ["Exam 1 (Internal)", "Exam 2 (Mid-Term)", "Exam 3 (Final)"],
                datasets: [{
                    label: "Cohort Mean Score (%)",
                    data: [averages[0].toFixed(2), averages[1].toFixed(2), averages[2].toFixed(2)],
                    borderColor: "#4f46e5",
                    backgroundColor: "rgba(79, 70, 229, 0.08)",
                    borderWidth: 3,
                    fill: true,
                    tension: 0.35,
                    pointBackgroundColor: "#4f46e5",
                    pointRadius: 6,
                    pointHoverRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        min: 30,
                        max: 100,
                        ticks: { callback: v => v + "%" },
                        grid: { color: "#f1f5f9" }
                    },
                    x: { grid: { display: false } }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }
}

// 2. Individual Scorecard View
function populateStudentSelect() {
    const dropdown = document.getElementById("studentSelectDropdown");
    dropdown.innerHTML = "";
    for (let i = 0; i < studentRecords.length; i++) {
        const opt = document.createElement("option");
        opt.value = i;
        opt.textContent = `${i + 1}. ${studentRecords[i][0]}`;
        dropdown.appendChild(opt);
    }
}

function renderScorecard(studentIndex) {
    if (studentRecords.length === 0) return;
    const a = calculateStudentAnalytics(studentIndex);

    document.getElementById("cardStudentId").textContent = `Student ID: #${String(studentIndex + 1).padStart(3, "0")}`;
    document.getElementById("cardStudentName").textContent = a.name;
    document.getElementById("cardAvatarInitial").textContent = a.name.charAt(0).toUpperCase();

    const classBadge = document.getElementById("cardClassificationBadge");
    classBadge.textContent = a.classification;
    classBadge.className = `tier-badge ${a.tierClass}`;

    document.getElementById("cardCumulativeMean").textContent = `Cumulative 3-Exam Average: ${a.cumulativeAvg.toFixed(2)}%`;

    // Table Body
    const tbody = document.getElementById("studentMarksTableBody");
    tbody.innerHTML = "";

    for (let s = 0; s < 4; s++) {
        const subName = SUBJECTS[s];
        const m1 = a.marksMatrix[0][s];
        const m2 = a.marksMatrix[1][s];
        const m3 = a.marksMatrix[2][s];
        const diff1 = a.diffMatrix[s][0];
        const diff2 = a.diffMatrix[s][1];
        const netDiff = a.diffMatrix[s][2];

        const isWeak = a.consistentlyWeakSubjects.includes(subName);
        const statusBadge = isWeak ? `<span class="badge-pill danger">Consistently Weak</span>` : `<span class="badge-pill success">Proficient</span>`;

        const row = document.createElement("tr");
        row.innerHTML = `
            <td><strong>${subName}</strong></td>
            <td>${m1.toFixed(1)}</td>
            <td>${m2.toFixed(1)}</td>
            <td>${formatDiff(diff1)}</td>
            <td>${m3.toFixed(1)}</td>
            <td>${formatDiff(diff2)}</td>
            <td>${formatDiff(netDiff)}</td>
            <td>${statusBadge}</td>
        `;
        tbody.appendChild(row);
    }

    // Table Foot
    const tfoot = document.getElementById("studentMarksTableFoot");
    const e1Diff = a.examAverages[1] - a.examAverages[0];
    const e2Diff = a.examAverages[2] - a.examAverages[1];

    tfoot.innerHTML = `
        <tr>
            <td><strong>TOTAL MARKS</strong></td>
            <td><strong>${a.examTotals[0].toFixed(1)}</strong></td>
            <td><strong>${a.examTotals[1].toFixed(1)}</strong></td>
            <td>-</td>
            <td><strong>${a.examTotals[2].toFixed(1)}</strong></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td><strong>EXAM MEAN %</strong></td>
            <td><strong style="color:var(--primary)">${a.examAverages[0].toFixed(1)}%</strong></td>
            <td><strong style="color:var(--primary)">${a.examAverages[1].toFixed(1)}%</strong></td>
            <td>${formatDiff(e1Diff)}</td>
            <td><strong style="color:var(--primary)">${a.examAverages[2].toFixed(1)}%</strong></td>
            <td>${formatDiff(e2Diff)}</td>
            <td>${formatDiff(a.netGrowth)}</td>
            <td>-</td>
        </tr>
    `;

    // Diagnostic Findings
    const weakBox = document.getElementById("auditWeakSubjectsText");
    const weakIcon = document.getElementById("auditWeakIcon");
    if (a.consistentlyWeakSubjects.length > 0) {
        weakBox.innerHTML = `<strong style="color:var(--danger)">Alert:</strong> Consistently weak in: <strong>${a.consistentlyWeakSubjects.join(", ")}</strong>`;
        weakIcon.textContent = "🚨";
    } else {
        weakBox.textContent = "None — Cleared standard benchmark in one or more assessments.";
        weakIcon.textContent = "✅";
    }

    const decBox = document.getElementById("auditDecliningSubjectsText");
    if (a.continuouslyDecliningSubjects.length > 0) {
        decBox.innerHTML = `<strong style="color:var(--warning)">Warning:</strong> Continuous downward trend across: <strong>${a.continuouslyDecliningSubjects.join(", ")}</strong>`;
    } else {
        decBox.textContent = "None — No continuous decline detected across consecutive assessments.";
    }

    const growthLabel = a.netGrowth >= 0 ? `+${a.netGrowth.toFixed(1)}% Net Growth (Upward Trajectory)` : `${a.netGrowth.toFixed(1)}% Net Growth (Downward Trajectory)`;
    document.getElementById("auditNetVectorText").textContent = growthLabel;

    document.getElementById("cardInstructorRemarks").textContent = `"${a.remarks}"`;

    // Individual Progression Mini-Chart
    renderIndividualChart(a.examAverages);
}

function renderIndividualChart(examAverages) {
    const ctx = document.getElementById("individualProgressionChart");
    if (!ctx) return;

    if (window.Chart) {
        if (individualChartInstance) individualChartInstance.destroy();
        individualChartInstance = new Chart(ctx, {
            type: "line",
            data: {
                labels: ["Exam 1", "Exam 2", "Exam 3"],
                datasets: [{
                    label: "Average %",
                    data: [examAverages[0].toFixed(1), examAverages[1].toFixed(1), examAverages[2].toFixed(1)],
                    borderColor: "#10b981",
                    backgroundColor: "rgba(16, 185, 129, 0.1)",
                    borderWidth: 2.5,
                    fill: true,
                    tension: 0.3,
                    pointRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { min: 20, max: 100, ticks: { callback: v => v + "%" }, grid: { color: "#f8fafc" } },
                    x: { grid: { display: false } }
                },
                plugins: { legend: { display: false } }
            }
        });
    }
}

// 3. Roster View
function renderRoster() {
    const tbody = document.getElementById("rosterTableBody");
    tbody.innerHTML = "";

    for (let i = 0; i < studentRecords.length; i++) {
        const a = calculateStudentAnalytics(i);
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>#${i + 1}</td>
            <td><strong>${a.name}</strong></td>
            <td>${a.examAverages[0].toFixed(2)}%</td>
            <td>${a.examAverages[1].toFixed(2)}%</td>
            <td>${a.examAverages[2].toFixed(2)}%</td>
            <td><strong>${a.cumulativeAvg.toFixed(2)}%</strong></td>
            <td>${formatDiff(a.netGrowth)}</td>
            <td><span class="tier-pill ${a.tierClass}">${a.classification}</span></td>
            <td>
                <button class="btn btn-outline" style="padding:4px 10px; font-size:0.78rem" onclick="selectAndShowScorecard(${i})">
                    View Scorecard
                </button>
            </td>
        `;
        tbody.appendChild(row);
    }
}

// Quick action from Roster
window.selectAndShowScorecard = function(index) {
    document.querySelector('.nav-tab[data-tab="scorecards"]').click();
    document.getElementById("studentSelectDropdown").value = index;
    renderScorecard(index);
};

// ================= EVENT HANDLERS & NAVIGATION =================
function setupNavigation() {
    const tabs = document.querySelectorAll(".nav-tab");
    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            tabs.forEach(t => t.classList.remove("active"));
            document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));

            tab.classList.add("active");
            const targetTab = tab.getAttribute("data-tab");
            document.getElementById(`${targetTab}Tab`).classList.add("active");
        });
    });
}

function setupEventListeners() {
    // Select Student in Scorecard
    document.getElementById("studentSelectDropdown").addEventListener("change", (e) => {
        renderScorecard(parseInt(e.target.value));
    });

    // Print Button
    document.getElementById("printScorecardBtn").addEventListener("click", () => {
        window.print();
    });

    // Load Sample Cohort Button
    document.getElementById("loadDemoBtn").addEventListener("click", () => {
        studentRecords = JSON.parse(JSON.stringify(SAMPLE_STUDENTS));
        saveData();
        renderAllViews();
        alert("Sample cohort (Alice, Bob, Charlie, Diana, Evan) successfully loaded!");
    });

    // Clear Data Button
    document.getElementById("clearDataBtn").addEventListener("click", () => {
        if (confirm("Are you sure you want to clear all student records?")) {
            studentRecords = [];
            saveData();
            renderAllViews();
        }
    });

    // Add Student Modal Open/Close
    const modal = document.getElementById("addStudentModal");
    document.getElementById("openAddModalBtn").addEventListener("click", () => {
        modal.classList.add("active");
    });
    document.getElementById("closeAddModalBtn").addEventListener("click", () => {
        modal.classList.remove("active");
    });
    document.getElementById("cancelAddBtn").addEventListener("click", () => {
        modal.classList.remove("active");
    });

    // Form Submit
    document.getElementById("addStudentForm").addEventListener("submit", (e) => {
        e.preventDefault();

        const name = document.getElementById("newStudentName").value.trim();
        if (!name) return;

        const e1 = [
            parseFloat(document.getElementById("m_e1_math").value),
            parseFloat(document.getElementById("m_e1_phy").value),
            parseFloat(document.getElementById("m_e1_chem").value),
            parseFloat(document.getElementById("m_e1_cs").value)
        ];
        const e2 = [
            parseFloat(document.getElementById("m_e2_math").value),
            parseFloat(document.getElementById("m_e2_phy").value),
            parseFloat(document.getElementById("m_e2_chem").value),
            parseFloat(document.getElementById("m_e2_cs").value)
        ];
        const e3 = [
            parseFloat(document.getElementById("m_e3_math").value),
            parseFloat(document.getElementById("m_e3_phy").value),
            parseFloat(document.getElementById("m_e3_chem").value),
            parseFloat(document.getElementById("m_e3_cs").value)
        ];

        studentRecords.push([name, [e1, e2, e3]]);
        saveData();
        renderAllViews();

        document.getElementById("addStudentForm").reset();
        modal.classList.remove("active");

        // Navigate to newly created student's scorecard
        window.selectAndShowScorecard(studentRecords.length - 1);
    });
}
