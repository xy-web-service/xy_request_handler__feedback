#-*- coding: UTF-8 -*-
__author__ = 'helios'
'''
	该类作为
'''
import os
import json
import tempfile
from xy_django_app_feedback.models import *
from xy_django_app_resource.models import *
from django.core.files import File  # you need this somewhere

from xy_request_handler_api.Api import Api

class Feedback(Api):
	def set_default_headers(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
	def get(self):
		self.operation()
	def post(self):
		self.operation()

	@property
	def username(self):
		username = ""
		try:
			username = self.get_argument("username")
		except:
			username = ""
		return username
	@property
	def mobile(self):
		mobile = ""
		try:
			mobile = self.get_argument("mobile")
		except:
			mobile = ""
		return mobile
	@property
	def email(self):
		email = ""
		try:
			email = self.get_argument("email")
		except:
			email = ""
		return email
	@property
	def text(self):
		text = ""
		try:
			text = self.get_argument("text")
		except:
			text = ""
		return text
	@property
	def qq(self):
		qq = ""
		try:
			qq = self.get_argument("qq")
		except:
			qq = ""
		return qq

	@property
	def wechat(self):
		wechat = ""
		try:
			wechat = self.get_argument("wechat")
		except:
			wechat = ""
		return wechat
	@property
	def weibo(self):
		weibo = ""
		try:
			weibo = self.get_argument("weibo")
		except:
			weibo = ""
		return weibo
	@property
	def dingding(self):
		dingding = ""
		try:
			dingding = self.get_argument("dingding")
		except:
			dingding = ""
		return dingding
	@property
	def facebook(self):
		facebook = ""
		try:
			facebook = self.get_argument("facebook")
		except:
			facebook = ""
		return facebook
	@property
	def google(self):
		google = ""
		try:
			google = self.get_argument("google")
		except:
			google = ""
		return google
	@property
	def twitter(self):
		twitter = ""
		try:
			twitter = self.get_argument("twitter")
		except:
			twitter = ""
		return twitter

	def operation(self):
		responseDict = {
					"data":{},
					"message":"发送成功",
					"code":0
				}
		try:
			image_files = []
			try:
				file_metas = self.request.files.get('file')  # 提取表单中‘name’为‘file’的文件元数据
				if self.request.files != None:
					for file_key in self.request.files:
						file_meta = self.request.files.get(file_key)[0]
						filename = file_meta.get('filename')
						body = file_meta.get('body')
						suffix = os.path.splitext(filename)[-1]
						temp_file = tempfile.mkdtemp()
						temp = tempfile.NamedTemporaryFile(suffix=suffix, prefix=None, dir=temp_file, delete=True)
						temp.write(body)
						image_files.append(temp)
			except:
				image_files = []
			if self.text != None and len(str(self.text)) != "":
				feedback = Feedback.objects.create()
				feedback.username = self.username
				feedback.email = self.email
				feedback.mobile = self.mobile
				feedback.wechat = self.wechat
				feedback.qq = self.qq
				feedback.facebook = self.facebook
				feedback.twitter = self.twitter
				feedback.google = self.google
				feedback.weibo = self.weibo
				feedback.text = self.text
				if len(image_files) > 0:
					for image_file in image_files:
						image = Image.objects.create()
						image_file_File = File(image_file, os.path.split(image_file.name)[-1])
						image.image = image_file_File
						image.save()
						image_file.close()
						feedback.images.add(image)
				feedback.save()
		except:
			responseDict["code"] = "1"
			responseDict["message"] = "发送失败"

		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
		return self.write(json.dumps(responseDict))