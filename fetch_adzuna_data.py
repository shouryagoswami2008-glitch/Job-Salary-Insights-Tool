import requests
import pandas as pd
import os

# Note: In a real scenario, you would use your own API credentials.
# For this project, we'll simulate the API call or use a mock response
# if credentials are not available, to demonstrate the workflow.

ADZUNA_APP_ID = ""
ADZUNA_APP_KEY = ""

def fetch_jobs_adzuna(job_title, country='us', results_per_page=50):
    url = f"http://api.adzuna.com/v1/api/jobs/{country}/search/1"
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": results_per_page,
        "what": job_title,
        "content-type": "application/json"
    }
    
    try:
        # Check if credentials are set, otherwise use mock data for demonstration
        if ADZUNA_APP_ID == "cf0fe6d6":
            print("API credentials not set. Using mock data for demonstration.")
            return get_mock_adzuna_data()
            
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        results = data.get('results', [])
        job_list = []
        for job in results:
            job_list.append({
                "Title": job.get('title'),
                "Company": job.get('company', {}).get('display_name'),
                "Location": job.get('location', {}).get('display_name'),
                "Salary Min": job.get('salary_min'),
                "Salary Max": job.get('salary_max'),
                "Contract Type": job.get('contract_type'),
                "Created": job.get('created')
            })
        
        return pd.DataFrame(job_list)
        
    except Exception as e:
        print(f"Error fetching data from Adzuna: {e}")
        return get_mock_adzuna_data()

def get_mock_adzuna_data():
    # Mock data structured like Adzuna API response
    mock_data = [
        {"Title": "Data Scientist", "Company": "TechCorp", "Location": "San Francisco, CA", "Salary Min": 130000, "Salary Max": 180000, "Contract Type": "permanent", "Created": "2024-05-20T12:00:00Z"},
        {"Title": "Senior Data Scientist", "Company": "DataViz Inc", "Location": "New York, NY", "Salary Min": 160000, "Salary Max": 220000, "Contract Type": "permanent", "Created": "2024-05-21T09:00:00Z"},
        {"Title": "Junior Data Analyst", "Company": "RetailFlow", "Location": "Austin, TX", "Salary Min": 70000, "Salary Max": 95000, "Contract Type": "permanent", "Created": "2024-05-22T14:30:00Z"},
        {"Title": "Machine Learning Engineer", "Company": "AI Solutions", "Location": "Seattle, WA", "Salary Min": 140000, "Salary Max": 200000, "Contract Type": "permanent", "Created": "2024-05-23T11:15:00Z"},
        {"Title": "Data Scientist", "Company": "HealthTech", "Location": "Boston, MA", "Salary Min": 125000, "Salary Max": 170000, "Contract Type": "permanent", "Created": "2024-05-24T16:45:00Z"},
        {"Title": "Lead Data Scientist", "Company": "FinData", "Location": "Chicago, IL", "Salary Min": 180000, "Salary Max": 250000, "Contract Type": "permanent", "Created": "2024-05-25T10:00:00Z"},
        {"Title": "Data Analyst", "Company": "MarketInsights", "Location": "Denver, CO", "Salary Min": 85000, "Salary Max": 110000, "Contract Type": "permanent", "Created": "2024-05-26T13:20:00Z"},
        {"Title": "Data Scientist", "Company": "AutoAI", "Location": "Detroit, MI", "Salary Min": 110000, "Salary Max": 150000, "Contract Type": "permanent", "Created": "2024-05-27T08:50:00Z"},
        {"Title": "Principal Data Scientist", "Company": "CloudScale", "Location": "Remote", "Salary Min": 200000, "Salary Max": 280000, "Contract Type": "permanent", "Created": "2024-05-28T15:10:00Z"},
        {"Title": "Data Analyst", "Company": "LogiTrack", "Location": "Atlanta, GA", "Salary Min": 80000, "Salary Max": 105000, "Contract Type": "permanent", "Created": "2024-05-29T12:35:00Z"}
    ]
    return pd.DataFrame(mock_data)

if __name__ == "__main__":
    df = fetch_jobs_adzuna("Data Scientist")
    print(df.head())
    df.to_csv("adzuna_salaries.csv", index=False)
