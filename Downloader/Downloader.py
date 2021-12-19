import mimetypes
import requests
import re
from bs4 import BeautifulSoup
import os, pdfkit


class Downloader:

    def __init__(self, email, password):
        self.app_data = {
            "login": email,
            "password": password,
            "url": "https://lms.eng.asu.edu.eg/login/index.php"
        }

        self.extension = mimetypes.types_map
        self.ex = {val: key for key, val in self.extension.items()}
        self.session = None
        self.session_key = None

        self.auth_moodle(self.app_data)
        self.Param = {'sesskey': f'{self.session_key}',
                 'info': 'core_course_get_enrolled_courses_by_timeline_classification'}

        self.dict_pay = '[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification",' \
                   '"args":{"offset":0,"limit":96,"classification":"all","sort":"fullname"}}]'
        self.re = self.session.get("https://lms.eng.asu.edu.eg/lib/ajax/service.php",
                        data=self.dict_pay, params=self.Param)

        self.data = self.re.json()
        self.subjects = {subject['fullname'].split()[0]: subject['viewurl'] for subject in self.data[0]['data']['courses']}


    def auth_moodle(self, data: dict) -> requests.Session():
        try:
            login, password, url_domain = data.values()
            s = requests.Session()
            r_1 = s.get(url=url_domain + "/login/index.php")
            pattern_auth = '<input type="hidden" name="logintoken" value="\w{32}">'
            token = re.findall(pattern_auth, r_1.text)
            token = re.findall("\w{32}", token[0])[0]
            payload = {'anchor': '', 'logintoken': token, 'username': login, 'password': password, 'rememberusername': 1}
            r_2 = s.post(url=url_domain + "/login/index.php", data=payload)
            sessionStr = re.findall('"sesskey":"\w*', r_2.text)
            print(sessionStr)
            print((re.split(':', sessionStr[0])))
            session_key = (re.split(':', sessionStr[0])[1])[1:]
            self.session = s
            self.session_key = session_key
        except requests.exceptions.SSLError:
            raise requests.exceptions.SSLError
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError

    def get_files(self, subjects):
        try:
            for subject_code in subjects:
                sub_link = self.subjects[subject_code]
                re = self.session.get(sub_link)
                res = BeautifulSoup(re.content, 'html.parser')
                re = res.select('.activity.assign.modtype_assign a')
                assign_links = {atag.getText():atag.get("href") for atag in re}
                for key1, ass in assign_links.items():
                    re = self.session.get(ass)
                    res = BeautifulSoup(re.content, 'html.parser')
                    link = res.select(".submissionstatustable .fileuploadsubmission a")
                    if bool(link):
                        path = None
                        name = link[0].getText()
                        if "LAB" in key1.upper():
                            path = subject_code + "/lab/" + name
                        elif "PROJECT" in key1.upper():
                            path = subject_code + "/project/" + name
                        elif "ASS" in key1.upper():
                            path = subject_code + "/ass/" + name
                        re = self.session.get(link[0].get("href"), allow_redirects=True)
                        self.save_file(path, re.content)
        except requests.exceptions.SSLError:
            raise requests.exceptions.SSLError
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError

    def save_file(self, filepath, content):
        filename = "Subjects/" + filepath
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            f.write(content)

    def get_quizzes(self, subjects):
        try:
            for subject_code in subjects:
                sub_link = self.subjects[subject_code]
                re = self.session.get(sub_link)
                res = BeautifulSoup(re.content, 'html.parser')
                re = res.select('.activity.quiz.modtype_quiz a')
                quiz_links = {atag.getText(): atag.get("href") for atag in re}
                for key, quiz in quiz_links.items():
                    re = self.session.get(quiz)
                    res = BeautifulSoup(re.content, 'html.parser')
                    body = res.select(".quizattemptsummary a")
                    if bool(body):
                        cookies = self.session.cookies.items()
                        option = {
                            'cookie': cookies,
                            'no-outline': None,
                            'page-size': 'A4',
                            'print-media-type': None,
                            'quiet': None
                        }
                        os.makedirs(os.path.dirname(f"Subjects/{subject_code}/quizzes/{key}.pdf"), exist_ok=True)
                        config = pdfkit.configuration(wkhtmltopdf="resources/wkhtmltopdf/bin/wkhtmltopdf.exe")
                        pdfkit.from_url(body[0].get("href"), f"Subjects/{subject_code}/quizzes/{key}.pdf",
                                        configuration=config, options=option)

        except requests.exceptions.SSLError:
            raise requests.exceptions.SSLError
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError

