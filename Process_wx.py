# encoding: utf-8

import requests
import time
import random
from loguru import logger
from Questions import Questions
import urllib3
import traceback

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning)  # type:ignore

qb = Questions()
session = requests.Session()

cookies = {
    "__root_domain_v": ".lgb360.com",
    "_qddaz": "QD.759087014511847",
    "Hm_lvt_9306f0abcf8c8a8d1948a49bc50d7773": "1687014511,1687014720", "Hm_lpvt_9306f0abcf8c8a8d1948a49bc50d7773": "1687014720",
    "agid": "E1tV3ptMz_N8OM-kmh6rBv6HZg",
    "_qdda": "3-1.1t9t5",
    "_qddab": "3-9jmt8n.lj0923u6",
    "acw_tc": "ACW_TC_CHANGE_ME_HERE",
    "token": "TOKEN_CHANGE_ME_HERE",
    "memberId": "MEMBERID_CHANGE_ME_HERE"
}

headers = {
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"", "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Token": "TOKEN_CHANGE_ME_HERE",
    "Memberid": "MEMBERID_CHANGE_ME_HERE",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://aqy.lgb360.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "X-Forwarded-For": "127.0.0.1"
}


def login_with_wechat():
    '''

    成功返回：
    {"data":{"unionId":"XXXXXXXXXXXXXXXXXX","linkUrl":"https://aqy-app.lgb360.com/#/home?user=","uidtok":"XXXXXXXXXXXXXXXXX"},"message":"成功","status":20000}
    错误返回：
    {"result":{"code":6,"msg":"未获得到UnionId"}}
    '''

    wx_code = '0312smGa1PylvF0S0XIa1y57xB02smGp'  # 需要通过sdk获取
    url = "https://aqy.lgb360.com:443/aqy/wechat/accountLogin?code={wx_code}&type=3"
    cookies = {
        "__root_domain_v": ".lgb360.com",
        "_qddaz": "QD.759087014511847", "Hm_lvt_9306f0abcf8c8a8d1948a49bc50d7773": "1687014511,1687014720", "Hm_lpvt_9306f0abcf8c8a8d1948a49bc50d7773": "1687014720",
        "agid": "E1tV3ptMz_N8OM-kmh6rBv6HZg",
        "_qdda": "3-1.1t9t5",
        "_qddab": "3-9jmt8n.lj0923u6"
    }
    headers = {
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Accept": "application/json, text/plain, */*", "Sec-Ch-Ua-Mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Origin": "https://aqy.lgb360.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://aqy.lgb360.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "X-Forwarded-For": "127.0.0.1"
    }
    session.post(url, headers=headers, cookies=cookies)


def activity_competition():
    '''
    返回正常json:
    {"result":{"msg":"成功"},"data":{"isRegist":true,"userCode":22573225}}
    '''
    url = "https://aqy.lgb360.com:443/aqy/regist/activity?memberId=MEMBERID_CHANGE_ME_HERE"

    try:
        resp = session.get(url, headers=headers, cookies=cookies, verify=False)
        if 'json' in resp.headers.get('Content-Type') and resp.status_code == 200:
            logger.info(resp.text)
            return
        logger.warning(resp.text)
    except Exception as e:
        traceback.print_exc()
        logger.error(e)


def regist_competition():
    '''
    request method is 'GET'
    返回正常json:
    {"result":{"msg":"成功"},"data":{"companyId":"3ee7be80-fb94-11ed-85d4-0c42a1380d98","userCategory":1,"companyName":"国家电网有限公司","isAnswered":true,"userCode":22573225,"points":28}}
    '''
    url = 'https://aqy.lgb360.com/aqy/regist/competition'
    try:
        resp = session.get(url, headers=headers,
                           cookies=cookies, verify=False, proxies=proxies)
        if 'json' in resp.headers.get('Content-Type') and resp.status_code == 200:
            logger.info(resp.text)
            return
        logger.warning(resp.text)
    except Exception as e:
        traceback.print_exc()
        logger.error(e)


def start_competition() -> dict:
    '''

    返回json如下：
    {"result":{"msg":"成功"},"data":{"ques":{"quesNo":1,"options":["安全评估论证","事故风险辨识","事故风险评估","应急资源调查"],"quesTypeStr":"多选题","quesId":"DABaEtG8ueNjFAA8","content":"根据《生产安全事故应急预案管理办法》的规定，编制应急预案前，编制单位应当进行（ ）。","quesType":2},"remainder":150}}
    '''
    startComp_url = "https://aqy-app.lgb360.com/aqy/ques/startCompetition"

    try:
        resp = session.post(
            startComp_url, json={}, headers=headers, cookies=cookies, verify=False, timeout=15, proxies=proxies)
        if resp.status_code == 200:
            result_dict = resp.json()
            msg = result_dict.get("result").get("msg")
            code = result_dict.get("result").get("code")
            if msg != "成功" and code == 9:
                logger.info(msg)
                return {}
            logger.info(result_dict)
            return result_dict
        return {}
    except Exception as e:
        traceback.print_exc()
        logger.error(e)
        return {}


def search_answer(result_dict):
    '''
    从题库搜索答案
    '''
    quesNo = 1
    data = {"quesId": "", "answerOptions": ["对"]}
    try:
        data = result_dict.get("data")
        assert data and isinstance(data, dict)
        ques = data.get("ques")
        assert ques and isinstance(ques, dict)

        quesId = ques.get("quesId")
        answerOptions = ques.get("options")
        assert answerOptions and isinstance(answerOptions, list)

        quesNo = ques.get('quesNo')
        content = ques.get('content')
        quesTypeStr = ques.get('quesTypeStr')

        if rightAnswer := qb.getAnswer(content):
            data = {"quesId": quesId, "answerOptions": rightAnswer}
            logger.info("题目：{quesNo}, rightAnswer", data)
        else:
            '''
            题库未找到时，则默认选
            '''
            opts = answerOptions if quesTypeStr == '多选题' else answerOptions[0]
            data = {"quesId": quesId,
                    "answerOptions": opts}
            qb.write_unkown_ques(
                {"quesTypeStr": quesTypeStr, "content": content, "optinos": answerOptions})
            logger.info(f'[-]题库无该题:{quesTypeStr}，默认选择答案：{opts}')
    except Exception as e:
        traceback.print_exc()
        logger.error(e)
    finally:
        return quesNo, data


def answer_question(result_dict: dict):
    '''
    请求参数如下：
    {"quesId":"DABaEtG8ueNjFAA8","answerOptions":["安全评估论证","事故风险辨识","事故风险评估","应急资源调查"]}

    返回正常：
     {"result":{"msg":"成功"},"data":{"answeredOptions":["对"],"ques":{"quesNo":2,"options":["巡查","督查","统计"],"quesTypeStr":"单选题","quesId":"KBxS1jtKxvbkGCgA","content":"建立完善地方各级党委和政府安全生产（ ）工作制度，加强对下级党委和政府的安全生产巡查，推动安全生产责任措施落实。","quesType":1},"rightOptions":["错"],"remainder":150}}
    返回异常：
    {"result":{"code":6,"msg":"未开始答题"}}
    '''
    if not result_dict:
        return

    is_finished = False
    answerQues = "https://aqy-app.lgb360.com/aqy/ques/answerQues"
    start_time = time.time()
    logger.info(f"开始答题：{start_time}")
    quesNo = 1
    while not is_finished:
        try:
            quesNo, data = search_answer(result_dict)
            answer = session.post(answerQues, json=data, headers=headers,
                                  cookies=cookies, verify=False, timeout=15, proxies=proxies)
            logger.info(answer.text)
            if answer and 'json' in answer.headers.get('Content-Type'):
                result_dict = answer.json()
            else:
                result_dict = {'data': answer.text}
        except Exception as e:
            traceback.print_exc()
            logger.error(e)
        finally:
            # 保证在出错的情况下也能执行超时函数，防止死循环ss
            end_time = time.time()
            if end_time-start_time > 150 or quesNo == 5:  # 2分半钟
                is_finished = True
                logger.info(f"答题结束,用时：{end_time-start_time}, 最后一题：{quesNo}")
                break
            time.sleep(random.randint(6, 9))


# {'https': 'http://127.0.0.1:8080', 'http': 'http://127.0.0.1:8080'}
proxies = None


def process():
    # 1
    activity_competition()
    # 2
    regist_competition()
    # 3
    result_dict = start_competition()
    # 4
    answer_question(result_dict)


def test():
    result_dict = {"result": {"msg": "成功"}, "data": {"answeredOptions": ["对"], "ques": {"quesNo": 2, "options": [
        "巡查", "督查", "统计"], "quesTypeStr": "单选题", "quesId": "KBxS1jtKxvbkGCgA", "content": "建立完善地方各级党委和政府安全生产（ ）工作制度，加强对下级党委和政府的安全生产巡查，推动安全生产责任措施落实。", "quesType": 1}, "rightOptions": ["错"], "remainder": 150}}
    answer_question(result_dict)


if __name__ == '__main__':
    test()
