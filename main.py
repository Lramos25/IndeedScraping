import requests         
from bs4 import BeautifulSoup as bs 

# Tring out several methods to capture data from several pages when ran. So far the results have not been as expected. 

#for x in range(0,20,10): 
#job, title = data analyst, Denver

x = 0

while x <= 60:
    
    x = x+10
    
    #webpage=requests.get('https://www.indeed.com/jobs?q={}&l={}&start={}'.format(title,location,x))

    webpage=requests.get('https://www.indeed.com/jobs?q=data%20analyst&l=Denver%2C%20CO&start={}'.format(x))

    soup=bs(webpage.text,'html.parser')

    #print(soup) # check if working properly, response code needs to be 200

    for div in soup.find_all('div',{"class":"job_seen_beacon"}):
        tbody=div.find('tbody') # calling the table body to go inside of
        tr= tbody.find('tr') # going inside the table

        #Job
        for n in tr.find_all('h2',{'class':'jobTitle jobTitle-color-purple jobTitle-newJob'}):
            job_title=n.find_all('span')[1].get_text()# use the 1 to not include the 'new' posting text
            print(job_title)

        # Company
            div_class=tr.find('div',{'class':'heading6 company_location tapItem-gutter'})
            span_=div_class.find('span')
            company_=(span_.get_text())
            print(company_) 

        # Salary:
            sal = tr.find('div',{'class':'heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly'})
            if sal is not None:
                sal_text = sal.get_text()
                print(sal_text)
            else:
                print('None Listed')
                
        # Location:
            pre=div_class.find('pre')
            print(pre.find('div',{'class':'companyLocation'}).get_text())
            print('\n')
