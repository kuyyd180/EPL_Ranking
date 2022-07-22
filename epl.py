# 작성자: 김달현
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

def fn_write_txt(text):
    f = open('epl.txt', 'a')
    f.write(text)
    f.writelines('\n')
    f.close()

url = 'https://sports.news.naver.com/wfootball/record/index'
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get(url)

page = driver.page_source
premi_team_rank_list = BeautifulSoup(page, "html.parser")
team_rank_list = premi_team_rank_list.select('#wfootballTeamRecordBody>table>tbody>tr')

for team in team_rank_list:
    num = team.select('.num > div.inner > strong')[0].text
    name = team.select('.name')[0].text
    point = team.select('.selected')[0].text.strip()
    last = num + "위 : " + name + "\t\t*승점 : " + point + "\n"
    print(last)
    fn_write_txt(last)


