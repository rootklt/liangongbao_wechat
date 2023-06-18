import schedule
import time
import os

from Process_wx import process, activity_competition

every_day = os.environ.get('every_day')
run_start = os.environ.get('run_start')


def job():
    process()


def alive():
    '''
    保持会话
    '''
    activity_competition()


default_time = "00:05"  # 设置启动时间
default_every_day = every_day if every_day is not None else default_time

if run_start is None:
    process()

os.environ.setdefault('run_start', 'started')  # 配置环境变量

do_competition = schedule.every().day.at(default_every_day).do(job)
active_job = schedule.every(30).seconds.do(alive)  # 第30秒请求一次

while True:
    schedule.run_pending()
    time.sleep(1)
