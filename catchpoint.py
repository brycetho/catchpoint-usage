#!/usr/bin/env python
import os
import requests
from bs4 import BeautifulSoup

base_url = "https://portal.catchpoint.com"
login_url = base_url + "/ui/Entry/Login.aspx"
activity_url = base_url + "/ui/Content/Administration/AccountActivity.aspx"
headers=({ "User-Agent":
                "Mozilla/5.0 (Windows NT 6.1) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/37.0.2062.120 Safari/537.36"
            })

s = requests.Session()
s.headers.update(headers)
r = s.get(login_url)
soup = BeautifulSoup(r.content, "html5lib")

# for auth
data = {
    "ctl00$ContentPlaceholder1$LogOnDisplay1$UserName" : os.environ['CPUSER'],
    "ctl00$ContentPlaceholder1$LogOnDisplay1$Password" : os.environ['CPPASS'],
    "__VIEWSTATE": soup.find(id="__VIEWSTATE")['value'],
    "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
    "ctl00$ContentPlaceholder1$LogOnDisplay1$LoginButton": "Log In"
}

# login
p = s.post(login_url, data=data)

# get account activity page after login
act = s.get(activity_url)
act_soup = BeautifulSoup(act.content, "html5lib")
print(round("points_used=" +
    act_soup.find(id='DetailContentPlaceholder_ContractInfo_UsedThisMonth_0').text))
print(round("contracted_monthly=" +
    act_soup.find(id="DetailContentPlaceholder_ContractInfo_ContractedMonthly_0").text))
