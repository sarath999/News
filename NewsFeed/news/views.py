from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from bson.json_util import dumps
import datetime
from datetime import datetime
from models import *
from django.http import *

# --------------@ Start Add News Feed Service Class  Here@ --------------#

#Request URL
#http://127.0.0.1:8000/addNewsFeed?headline=api&content=testingggggg&news_type=success

class AddnewsFeed(View):
	
	#get method for adding news feed service	
	def get(self,request):
		try:
			if request.GET['headline']!='':
				if request.GET['content']!='':
					if request.GET['news_type']!='' :
						if request.GET['news_type'] in ['warning','success','information'] :
							return addNewsFeed(request.GET['headline'],request.GET['content'],request.GET['news_type'],request)
						else:
							return HttpResponse(dumps({"message":"news type must be warning(or)success(or)information", "status":"failed", "code":"200", "statustext":"ok"}))
					else:
						return HttpResponse(dumps({"message":"type of news must be filled", "status":"failed", "code":"200", "statustext":"ok"}))
				else:
					return HttpResponse(dumps({"message":"contnet must be filled", "status":"failed", "code":"200", "statustext":"ok"}))
			else:
				return HttpResponse(dumps({"message":"uheadline must be filled", "status":"failed", "code":"200", "statustext":"ok"}))
		except KeyError as e:
			return HttpResponse(dumps({"message":"parameter "+e.message.replace("'","")+" is missing", "status":"failed", "code":"400", "statustext":"bad request"}))
	
	#post method for adding news feed service	
	def post(self,request):
		try:
			if request.POST['headline']!='':
				if request.POST['content']!='':
					if request.POST['news_type']!='' :
						if request.POST['news_type'] in ['warning','success','information'] :
							return addNewsFeed(request.POST['headline'],request.POST['content'],request.POST['news_type'],request)
						else:
							return HttpResponse(dumps({"message":"news type must be warning(or)success(or)information", "status":"failed", "code":"200", "statustext":"ok"}))
					else:
						return HttpResponse(dumps({"message":"type of news must be filled", "status":"failed", "code":"200", "statustext":"ok"}))
				else:
					return HttpResponse(dumps({"message":"contnet must be filled", "status":"failed", "code":"200", "statustext":"ok"}))
			else:
				return HttpResponse(dumps({"message":"uheadline must be filled", "status":"failed", "code":"200", "statustext":"ok"}))
		except KeyError as e:
			return HttpResponse(dumps({"message":"parameter "+e.message.replace("'","")+" is missing", "status":"failed", "code":"400", "statustext":"bad request"}))
	
# --------------@ End Add News Feed Service Class  Here@ --------------#
	
#logic for adding news feed
def addNewsFeed(headline, content,type_of_news,request):
	try:
		if type_of_news=="warning":
			Warning(headLine=headline,news_content=content,publication_date=datetime.now().date()).save()
			result={"status":"success", "message":"news added in warnings successfully", "code":"200", "statustext":"ok"}
		elif type_of_news=="success":
			Succes(headLine=headline,news_content=content,publication_date=datetime.now().date()).save()
			result={"status":"success", "message":"news added in success successfully", "code":"200", "statustext":"ok"}
		elif type_of_news=="information":
			Information(headLine=headline,news_content=content,publication_date=datetime.now().date()).save()				
			result={"status":"success", "message":"news added in inforamtions successfully", "code":"200", "statustext":"ok"}	
			
		else:
			result={"status":"failed", "message":"news not added", "code":"200", "statustext":"ok"}
		return HttpResponse(dumps(result))		
	except Exception as e:
		
		return exceptionHandler(e)
		
#logic for exception handling.
def exceptionHandler(e):
	
	#To get exception information from sys package
	exc_type, exc_msg, exc_obj = sys.exc_info()
	#To get fname in which file rised exception 
	fileDetails = os.path.split(exc_obj.tb_frame.f_code.co_filename)
	fapp = fileDetails[0].split('/')[-1]
	fname = fileDetails[1]
	#To save response in log files
	
	return HttpResponse(dumps({"status":"failed", "message":"exception in "+str(exc_obj.tb_lineno)+"th line in "+fname+" file of "+fapp+" application", "exception type":e.message, "code":"400", "statustext":"bad request"}))
