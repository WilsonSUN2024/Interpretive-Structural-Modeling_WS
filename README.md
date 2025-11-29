# Interpretive-Structural-Modeling_WS
# ISM


## README – Interpretive Structural Modeling (ISM) Script


### 📌 Overview
This project implements **Interpretive Structural Modeling (ISM)**, a methodology used to identify and analyze relationships among system elements and derive a hierarchical structure. ISM is widely used in management science, engineering management, decision support, and systems analysis.


This script provides a complete ISM workflow, including:
- Loading an initial relationship (adjacency) matrix
- Computing the reachability matrix using the Warshall algorithm
- Performing level partitioning to determine hierarchical structure
- Exporting the results to CSV files


---


### 📁 Project Structure
```
├── ism_script.py # Main ISM implementation (your Python script)
├── reachability_matrix.csv # Auto-generated output
├── structure_levels.csv # Auto-generated output
└── README.md # This documentation
```


---


### 🚀 How to Use
1. Prepare an Excel file containing the **adjacency/relationship matrix**.
- No header rows
- Square matrix (e.g., 10×10)
- Values: 0 or 1


2. Run the script:
```bash
python ism_script.py
```


3. Enter the file path when prompted:
```
Enter the Excel file path: your_matrix.xlsx
```


4. The script will automatically:
- Compute the reachability matrix
- Perform level partitioning
- Export:
- `reachability_matrix.csv`
- `structure_levels.csv`


---


### 📊 Output Files
#### **1. reachability_matrix.csv**
A matrix showing full reachability between elements (direct + transitive).


#### **2. structure_levels.csv**
The hierarchical structure levels, e.g.:
```
Level,Nodes
1, 5, 7
2, 3
3, 1, 2, 4
```
Interpretation:
- Level 1 → top level (independent elements)
- Last level → foundational factors


---


### 🧠 ISM Methodology Summary
1. **Build relationship matrix** (base adjacency matrix)
2. **Compute reachability matrix** (transitive closure)
3. **Reachability set & antecedent set** computation
4. **Level identification**
5. **Construct hierarchical model (digraph)**


The script fully automates Steps 1–4.


---


### 🔧 Requirements
Ensure the following libraries are installed:
```bash
pip install pandas numpy openpyxl
```


---


### 📝 Notes
- Do not include text headers in your Excel matrix.
- Matrix must be square.
- Non-binary values will cause an error.


---


### 📬 Contact
If you want to:
- Add ISM diagrams
- Integrate FISM (Fuzzy ISM)
(Interpretive Structural Modeling) Implementation
