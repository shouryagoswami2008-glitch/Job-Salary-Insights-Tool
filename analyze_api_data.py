import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_api_data(file_path):
    df = pd.read_csv(r"D:\User Data\Desktop\data analysis project\adzuna_salaries.csv")
    
    # Calculate average salary
    df['Average Salary'] = (df['Salary Min'] + df['Salary Max']) / 2
    
    # 1. Salary Distribution for Data Roles
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Average Salary'], bins=10, kde=True, color='purple')
    plt.title('Distribution of Average Salaries (API Data)')
    plt.xlabel('Salary (USD)')
    plt.ylabel('Frequency')
    plt.savefig('api_salary_distribution.png')
    
    # 2. Top Paying Companies from API
    plt.figure(figsize=(12, 8))
    top_companies = df.sort_values(by='Average Salary', ascending=False).head(10)
    sns.barplot(x='Average Salary', y='Company', data=top_companies, palette='magma')
    plt.title('Top 10 Paying Companies for Data Roles (API Data)')
    plt.xlabel('Average Salary (USD)')
    plt.savefig('api_top_paying_companies.png')
    
    # 3. Salary by Location
    plt.figure(figsize=(12, 6))
    sns.stripplot(x='Average Salary', y='Location', data=df, size=8, jitter=True, palette='coolwarm')
    plt.title('Salary by Location (API Data)')
    plt.xlabel('Average Salary (USD)')
    plt.savefig('api_salary_by_location.png')
    
    print("Visualizations saved: api_salary_distribution.png, api_top_paying_companies.png, api_salary_by_location.png")

if __name__ == "__main__":
    analyze_api_data('adzuna_salaries.csv')
