import requests

class AuthorToday:
	def __init__(self):
		self.api = "https://api.author.today"
		self.web_api = "https://author.today"
		self.token = "Bearer guest"
		self.headers = {
			"authorization": self.token,
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
			"x-requested-with": "XMLHttpRequest"
		}
	
	def login(self, login: str, password: str):
		data = {
			"login": login,
			"password": password
		}
		response = requests.post(
			f"{self.api}/v1/account/login-by-password",
			json=data,
			headers=self.headers).json()
		if "token" in response:
			self.token = response["token"]
			self.headers["authorization"] = f"Bearer {self.token}"
			self.user_id = self.get_account_info()["id"]
		return response 
	
	def login_with_token(self, token: str):
		self.token = token
		self.headers["authorization"] = f"Bearer {self.token}"
		response = self.get_account_info()
		if "id" in response:
			self.user_id = response["id"]
		return response

	def get_account_info(self):
		return requests.get(
			f"{self.api}/v1/account/current-user",
			headers=self.headers).json()
	
	def register(
			self,
			nickname: str,
			email: str,
			password: str):
		data = {
			"email": email,
			"fio": nickname,
			"password": password,
			"termsAgree": True
		}
		return requests.post(
			f"{self.api}/v1/account/register",
			json=data,
			headers=self.headers).json()

	def refresh_token(self):
		return requests.post(
			f"{self.api}/v1/account/refresh-token",
			headers=self.headers).json()

	def recover_password(self, email: str):
		data = {
			"email": email
		}
		return requests.post(
			f"{self.api}/v1/account/password/recovery",
			headers=self.headers).json()

	def check_notifications(self):
		return requests.get(
			f"{self.web_api}/notification/check",
			headers=self.headers).json()

	def get_work_content(self, work_id: int):
		return requests.get(
			f"{self.api}/v1/work/{work_id}/content",
			headers=self.headers).json()

	def get_work_meta_info(self, work_id: int):
		return requests.get(
			f"{self.api}/v1/work/{work_id}/meta-info",
			headers=self.headers).json()
	
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
		return requests.post(
			f"{self.web_api}/account/main-info",
			data=data,
			headers=self.headers).json()

	def get_disputed_works(self):
		return requests.get(
			f"{self.web_api}/widget/disputedWorks",
			headers=self.headers).json()

	def track_last_activity(self):
		return requests.post(
			f"{self.web_api}/account/trackLastActivity",
			headers=self.headers).json()

	def add_to_library(self, id: int, state: str):
		data = {
			"ids": [id],
			"state": state
		}
		return requests.post(
			f"{self.web_api}/work/updateLibrary",
			data=data,
			headers=self.headers).json()

	def send_report(
			self,
			category: str,
			comment: str,
			target_id: int,
			target_type: str,
			url: str):
		data = {
			"TargetId": target_id,
			"targetType": target_type,
			"Category": category,
			"Comment": comment,
			"Url": url
		}
		return requests.post(
			f"{self.api}/v1/feedback/complaint",
			json=data,
			headers=self.headers).json()

	def search(self, title: str):
		return requests.get(
			f"{self.web_api}/search?q={title}",
			headers=self.headers).json()

	def get_chapter(self, work_id: int, chapter_id: int):
		return requests.get(
			f"{self.web_api}/reader/{work_id}/chapter?id={chapter_id}",
			headers=self.headers).json()

	def send_message(self, message: str, chat_id: int):
		data = {
			"chatId": chat_id,
			"text": f"<p>{message}<p>"
		}
		return requests.post(
			f"{self.web_api}/pm/sendMessage",
			data=data,
			headers=self.headers).json()

	def mark_as_read(self, chat_id: int):
		data = {"chatId": chat_id}
		return requests.post(
			f"{self.web_api}/pm/markAsRead",
			data=data,
			headers=self.headers).json()

	def get_chat_messages(self, chat_id: int):
		return requests.get(
			f"{self.web_api}/pm/messages?id={chat_id}",
			headers=self.headers).json()

	def get_my_chats(self, page: int = 1):
		return requests.get(
			f"{self.web_api}/pm/recentChats?page={page}&onlyUnread=false",
			headers=self.headers).json()

	def follow_user(self, user_id: str):
		data = {
			"subscribe": True,
			"toggleOnlyShowingUpdates": False,
			"userId": user_id
		}
		return requests.post(
			f"{self.web_api}/subscription/updateSubscription",
			data=data,
			headers=self.headers).json()

	def add_user_to_ignore(self, user_id: str):
		data = {
			"userId": user_id
		}
		return requests.post(
			f"{self.web_api}/ignoreList/add",
			data=data,
			headers=self.headers).json()


	def like_work(
			self,
			work_id: int,
			is_liked: bool = True):
		return requests.post(
			f"{self.api}/v1/work/{work_id}/like?isLiked={is_liked}",
			headers=self.headers).json()

	def get_account_library(self):
		return requests.get(
			f"{self.api}/v1/account/user-library",
			headers=self.headers).json()

	def get_catalog(
			self,
			sorting: str,
			page: int = 1,
			ps: int = 40,
			genre: str = "all",
			form: str = "any",
			state: str = "any",
			series: str = "any",
			access: str = "any",
			dnl: str = "any",
			promo: str = "hide",
			upd: int = -1,
			pub: int = -1,
			length: str = "any",
			fnd: bool = False,
			rec: bool = False,
			exc: bool = False,
			disc: bool = False):
		return requests.get(
			f"{self.api}/v1/catalog/search?page={page}&ps={ps}&genre={genre}&sorting={sorting}&form={form}&state={state}&series={series}&access={access}&dnl={dnl}&promo={promo}&upd={upd}&pub={pub}&length={length}&fnd={fnd}&rec={rec}&exc={exc}&disc={disc}",
			headers=self.headers).json()

	def get_home_page(self, view: str = "all"):
		return requests.get(
			f"{self.api}/v1/home/home-page?View={view}",
			headers=self.headers).json()
