from requests_html import HTMLSession
import datetime

def scrape_weworkremotely():
    url = 'https://weworkremotely.com/categories/remote-programming-jobs'
    session = HTMLSession()
    r = session.get(url)
    list = r.html.find('section.jobs', first=True)
    listings = [element for element in list.find('li')]
    relevant_jobs = []
    now = datetime.datetime.now()
    print(f'scraping on {now}')

    for element in listings:
        job = {}

        if element.find('span.title', first=True) and element.find('time', first=True) and element.find('time', first=True).attrs['datetime']:
            job_title = element.find('span.title', first=True).text
            time_str = element.find('time', first=True).attrs['datetime']
   
            job_time = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
            delta = now - job_time

            if delta < datetime.timedelta(7):
                if "Senior" not in job_title and "Lead" not in job_title and "Sr." not in job_title:
                    print(f'adding {job_title}')

                    job['posted'] = job_time
                    job['title'] = job_title
                    job['company'] = element.find('span.company', first=True).text
                    job['url'] = f'https://weworkremotely.com/{element.find("a", first=True).attrs["href"]}'
                    job['logo_url'] = element.search('background-image:url({})')[0] if element.search('background-image:url({})') else ''
                    job['source'] = 'weworkremotely.com'

                    relevant_jobs.append(job)
                else:
                    print(f'not adding {job_title}')
            else:
                print('greater than 7 days, done')
                break
    
    print(f'found {len(relevant_jobs)} jobs!')
    return relevant_jobs

def scrape_remoteok():
    url = 'https://remoteok.io/remote-dev-jobs'
    session = HTMLSession()
    r = session.get(url)
    list = r.html.find('table#jobsboard', first=True)
    listings = [element for element in list.find('tr.job')]
    relevant_jobs = []
    now = datetime.datetime.now()
    print(f'scraping on {now}')

    for element in listings:
        job = {}

        time_str = element.find('tr.job', first=True).attrs['data-epoch']
        job_time = datetime.datetime.fromtimestamp(int(time_str))
        delta = now - job_time

        job_title = element.find('h2', first=True).text

        

        
        
        if delta < datetime.timedelta(7):
            if "Senior" not in job_title and "Lead" not in job_title and "Sr." not in job_title:
                print(f'adding {job_title}')

                job['posted'] = job_time
                job['title'] = job_title
                job['company'] = element.find('h3', first=True).text
                job['url'] = f'https://remoteok.io/{element.find("a.preventLink", first=True).attrs["href"]}'
                print(element.find('img.logo', first=True).attrs.get('src', '') if element.find('img.logo', first=True) else '')
                job['logo_url'] = element.find('img.logo', first=True).attrs.get('src', '') if element.find('img.logo', first=True) else ''
                job['source'] = 'remoteok.io'

                relevant_jobs.append(job)
            else:
                print(f'not adding {job_title}')
        else:
            print('greater than 7 days, done')
            break

    print(f'found {len(relevant_jobs)} jobs!')
    return relevant_jobs