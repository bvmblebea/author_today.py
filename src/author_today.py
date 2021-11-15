import requests
import json


class Client:
    def __init__(self):
        self.web_api = "https://author.today"
        self.api = "https://api.author.today"
        self.token = "Bearer guest"
        self.headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"}

    def auth(self, email: str, password: str):
        data = {"Login": email, "Password": password}
        request = requests.post(
            f"{self.api}/v1/account/login-by-password",
            json=data,
            headers=self.headers)
        json = request.json()
        self.token = json["token"]
        self.headers["Authorization"] = f"Bearer {self.token}"
        return json

    def get_current_user(self):
        request = requests.get(
            f"{self.api}/v1/account/current-user",
            headers=self.headers)
        return request.json()

    def register(self, nickname: str, email: str, password: str):
        data = {"FIO": nickname, "Email": email, "Password": password}
        request = requests.post(
            f"{self.api}/v1/account/register",
            json=data,
            headers=self.headers)
        return request.json()

    def refresh_token(self):
        request = requests.post(
            f"{self.api}/v1/account/refresh-token",
            headers=self.headers)
        json = request.json()
        self.token = json["token"]
        self.headers["Authorization"] = f"Bearer {self.token}"
        return json

    def recover_password(self, email: str):
        data = {"Email": email}
        request = requests.post(
            f"{self.api}/v1/account/password/recovery",
            headers=self.headers)
        return request.json()

    def check_notifications(self):
        request = requests.get(
            f"{self.web_api}/notification/check?",
            headers=self.headers)
        return request.json()

    def get_work_content(self, work_Id: int):
        request = requests.get(
            f"{self.api}/v1/work/{work_Id}/content",
            headers=self.headers)
        return request.json()

    def get_work_meta_info(self, work_Id: int):
        request = requests.get(
            f"{self.api}/v1/work/{work_Id}/meta-info",
            headers=self.headers)
        return request.json()

    def edit_profile(
            self,
            username: str = None,
            nickname: str = None,
            status: str = None,
            birthday_day: int = None,
            birthday_month: int = None,
            birthday_year: int = None,
            sex: int = -1):
        data = {}
        if username:
            data["UserName"] = username
        if nickname:
            data["FIO"] = nickname
        if status:
            data["Status"] = status
        if birthday_day:
            data["BirthdayDay"] = birthday_day
        if birthday_month:
            data["BirthdayMonth"] = birthday_month
        if birthday_year:
            data["BirthdayYear"] = birthday_year
        if sex:
            data["Sex"] = sex
        request = requests.post(
            f"{self.web_api}/account/main-info",
            data=data,
            headers=self.headers)
        return request.json()

    def get_disputed_works(self):
        request = requests.get(
            f"{self.web_api}/widget/disputedWorks",
            headers=self.headers)
        return request.json()

    def track_last_activity(self):
        request = requests.post(
            f"{self.web_api}/account/trackLastActivity",
            headers=self.headers)
        return request.json()

    def add_to_library(self, id: int, state: str):
        data = {"ids": [id], "state": state}
        request = requests.post(
            f"{self.web_api}/work/updateLibrary",
            data=data,
            headers=self.headers)
        return request.json()

    def send_report(
            self,
            category: str,
            comment: str,
            target_Id: int,
            target_type: str,
            url: str):
        data = {
            "TargetId": target_Id,
            "targetType": target_type,
            "Category": category,
            "Comment": comment,
            "Url": url}
        request = requests.post(
            f"{self.api}/v1/feedback/complaint",
            json=data,
            headers=self.headers)
        return request.json()

    def search(self, title: str):
        request = requests.get(
            f"{self.web_api}/search?q={title}",
            headers=self.headers)
        return request.json()

    def get_chapter(self, work_Id: int, chapter_Id: int):
        request = requests.get(
            f"{self.web_api}/reader/{work_Id}/chapter?id={chapter_Id}",
            headers=self.headers)
        return request.json()

    def send_message(self, message: str, chat_Id: int):
        data = {"chatId": chat_Id, "text": f"<p>{message}<p>"}
        request = requests.post(
            f"{self.web_api}/pm/sendMessage",
            data=data,
            headers=self.headers)
        return request.json()

    def mark_as_read(self, chat_Id: int):
        data = {"chatId": chat_Id}
        request = requests.post(
            f"{self.web_api}/pm/markAsRead",
            data=data,
            headers=self.headers)
        return request.json()

    def get_chat_messages(self, chat_Id: int):
        request = requests.get(
            f"{self.web_api}/pm/messages?id={chat_Id}",
            headers=self.headers)
        return request.json()

    def get_my_chats(self, page: int = 1):
        request = requests.get(
            f"{self.web_api}/pm/recentChats?page={page}&onlyUnread=false",
            headers=self.headers)
        return request.json()

    def follow_user(self, user_Id: str):
        data = {
            "subscribe": True,
            "toggleOnlyShowingUpdates": False,
            "userId": user_Id}
        request = requests.post(
            f"{self.web_api}/subscription/updateSubscription",
            data=data,
            headers=self.headers)
        return request.json()

    def add_user_to_ignorelist(self, user_Id: str):
        data = {"userId": user_Id}
        request = requests.post(
            f"{self.web_api}/ignoreList/add",
            data=data,
            headers=self.headers)
        return request.json()

    def like_work(self, work_Id: int, is_Liked: boolean = True):
        request = requests.post(
            f"{self.api}/v1/work/{work_Id}/like?isLiked={is_Liked}",
            headers=self.headers)
        return request.json()
