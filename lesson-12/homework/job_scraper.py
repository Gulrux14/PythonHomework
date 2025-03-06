import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Veb-sahifani yuklab olish
url = 'https://realpython.github.io/fake-jobs'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# SQLite ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# 'jobs' jadvalini yaratish
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    job_title TEXT,
    company_name TEXT,
    location TEXT,
    job_description TEXT,
    application_link TEXT,
    UNIQUE(job_title, company_name, location)
)
''')

# E'lonlarni yig'ish
jobs = soup.find_all('div', class_='card-content')
for job in jobs:
    job_title = job.find('h2', class_='title').text.strip()
    company_name = job.find('h3', class_='subtitle').text.strip()
    location = job.find('p', class_='location').text.strip()
    job_description = job.find('div', class_='content').text.strip()
    application_link = job.find('a', text='Apply')['href']

    # Ma'lumotlarni qo'shish yoki yangilash
    cursor.execute('''
    INSERT OR IGNORE INTO jobs (job_title, company_name, location, job_description, application_link)
    VALUES (?, ?, ?, ?, ?)
    ''', (job_title, company_name, location, job_description, application_link))

    cursor.execute('''
    UPDATE jobs
    SET job_description = ?, application_link = ?
    WHERE job_title = ? AND company_name = ? AND location = ?
    ''', (job_description, application_link, job_title, company_name, location))

# O'zgarishlarni saqlash
conn.commit()

# Filtrlash funksiyasi
def filter_jobs(location=None, company_name=None):
    query = 'SELECT * FROM jobs WHERE 1=1'
    params = []
    if location:
        query += ' AND location = ?'
        params.append(location)
    if company_name:
        query += ' AND company_name = ?'
        params.append(company_name)
    cursor.execute(query, params)
    return cursor.fetchall()

# CSV eksport funksiyasi
def export_to_csv(jobs, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Job Title', 'Company Name', 'Location', 'Job Description', 'Application Link'])
        writer.writerows(jobs)

# Misol: 'Stewartbury, AA' joylashuvidagi e'lonlarni CSV fayliga eksport qilish
filtered_jobs = filter_jobs(location='Stewartbury, AA')
export_to_csv(filtered_jobs, 'filtered_jobs.csv')

# Ma'lumotlar bazasini yopish
conn.close()