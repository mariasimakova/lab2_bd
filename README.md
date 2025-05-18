# Lab 2: Document Stores with MongoDB

![BSE Logo](./LaTex/imgs/BSE%20Barcelona%20Graduate%20School%20of%20Economics.svg)

## Overview

This repository contains the solution for Lab 2 of the course 23D020: Big Data Management for Data Science. The lab explores different modeling alternatives in MongoDB, comparing performance across various query patterns.

**Course:** 23D020 Big Data Management for Data Science  
**Authors:** Maria Simakova (172708), Moritz Peist (254017)  
**Group:** L2-T05  
**Programme:** DSDM

## Assignment Description

In this lab, we explore three different modeling alternatives in MongoDB for a Person-Company relationship:

1. **Model 1 (M1):** Two types of documents, one for each class and referenced fields
2. **Model 2 (M2):** One document for "Person" with "Company" as embedded document
3. **Model 3 (M3):** One document for "Company" with "Person" as embedded documents

For each model, we implement and analyze the following queries:

- **Q1:** For each person, retrieve their full name and their company's name
- **Q2:** For each company, retrieve its name and the number of employees
- **Q3:** For each person born before 1988, update their age to "30"
- **Q4:** For each company, update its name to include the word "Company"

## Repository Structure

```bash
Lab2-Document-Stores/
├── Lab2-Assignment-Statement.pdf    # Original assignment description
├── README.md                        # This file
├── lab2.ipynb                       # Main Jupyter notebook with implementation
├── L2-T05.pdf                       # Final submission PDF
├── code/
│   └── archive.py                   # Helper code for verification
├── LaTex/                           # LaTeX files for report
│   ├── chapters/
│   │   └── part1.tex                # Analysis and results
│   ├── commands.tex                 # LaTeX commands
│   ├── packages.tex                 # LaTeX packages
│   └── ...
├── results/
│   └── model_comparison.tex         # Performance results in LaTeX format
└── .gitignore                       # Git ignore file
```

## Setup and Requirements

### Prerequisites

- Python 3.x
- MongoDB installed and running
- Python packages: pymongo, faker, pandas, tqdm, dotenv

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd Lab2-Document-Stores
   ```

2. Create a Python environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:

   ```bash
   pip install pymongo faker pandas tqdm python-dotenv jupyter
   ```

4. Set up MongoDB connection:
   Create a `.env` file in the root directory with the following content:

   ```
   CONNECTION_STRING=mongodb://localhost:27017/
   DB_NAME=lab2
   ```

   Replace the connection string and database name as needed.

## Running the Code

1. Start your MongoDB server
2. Open the Jupyter notebook:

   ```bash
   jupyter notebook lab2.ipynb
   ```

3. Execute the cells in the notebook sequentially to:
   - Generate test data for all three models
   - Run all queries and measure performance
   - See performance comparison results

## Key Findings

The performance analysis (from `results/model_comparison.tex`) shows:

| Model | Q1 (s) | Q2 (s) | Q3 (s) | Q4 (s) |
|-------|--------|--------|--------|--------|
| M1    | 114.76 | 5.55   | 19.06  | 1.01   |
| M2    | 9.26   | 2.65   | 20.98  | 50.67  |
| M3    | 6.21   | 0.62   | 9.43   | 8.78   |

Key observations:

- **Model 3** (embedding people in companies) performs best for read operations (Q1, Q2) and person-focused updates (Q3)
- **Model 1** (normalized model) performs best for company-focused updates (Q4)
- **Model 2** generally shows intermediate performance but performs worst for company updates

The results demonstrate that MongoDB's performance strongly depends on the chosen data model and the specific access patterns of applications.

As part of the DSDM program at Barcelona School of Economics.

## License

This project is part of an academic assignment and is not licensed for public use.
