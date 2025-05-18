# **Solar Challenge - Week 0**  
**Cross-Country Solar Farm Analysis**  

## **📌 Project Overview**  
This project analyzes solar radiation data from Benin, Sierra Leone, and Togo to identify high-potential regions for solar energy investments.  

---

## **🚀 Setup & Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/TigistW/solar-challenge-week1.git
cd solar-challenge-week1
```

### **2. Set Up Python Virtual Environment**  
#### **Windows (PowerShell)**  
```
# Create and activate the virtual environment
python -m venv venv
.\venv\Scripts\Activate
```

#### **Linux/macOS**  
```bash
python -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```
---

## **📂 Project Structure**  
```
solar-challenge-week1/
├── .github/workflows/ci.yml    # GitHub Actions CI
├── data/                       # Raw/cleaned data (ignored by Git)
├── notebooks/                  # Jupyter notebooks for EDA
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   └── togo_eda.ipynb
├── app/                        # Streamlit dashboard
│   ├── main.py
│   └── utils.py
├── tests/                      # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
```


## **⚙️ CI/CD Pipeline**  
- GitHub Actions automates testing on push (`ci.yml`).  
- Ensures dependencies install correctly.  

---


