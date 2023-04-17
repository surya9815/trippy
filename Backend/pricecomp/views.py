from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework.views import APIView
import os
# Create your views here.

API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')

def index(request):

    return render(request,"newres.html",{})
    #return render(request, "/home/suryanshthakur/Django/tripy/tripy/templates/pricecomp/index.html")

def search_hotel(request):
    data=dict(request.POST)
    if(len(data.keys()) > 0):    
        city=data['inputCity'][0]
        # api_call(city)    #Calling above api call function 

        #----------API CALL---------------
        url="https://api.makcorps.com/auth"
        payload = json.dumps({"username": API_USERNAME, "password": API_PASSWORD})
        headers ={ "Content-Type" :'application/json'}

        response = requests.request("POST", url,headers=headers, data=payload)
        print (response.text)
        print (type(response.text))

        # print(response.json()["access_token"])
        url=f"https://api.makcorps.com/free/{city}"
        payload = {}
        headers = {
            "Authorization":'JWT'+' '+response.json()["access_token"]
        }
        response = requests.request("GET", url,headers=headers, data=payload)
        response_json=response.text
        response_json=json.loads(response_json)

        # print(type(response_json))
        # print(response_json)
        f = open("apicallresponsetype.txt", "w")

        f.write(f"{response_json}")

        f.close()


        #Now Make Final Dict
        hotel_rates_dict={}
        final_data_dict={}

        for i in response_json["Comparison"][:-1]:    #list with 2 items 0 index --> dict and 1 index --> list
        # i is list
            # hotelname = i[0]["hotelName"].strip()
            hotelname = i[0]["hotelName"]

            # hotelid = i[0]["hotelId"]
            price_vender_list=[]

            # price_vender_dict={}
            for j in i[1]:    #inner list of vendors
                #j is dict
                for k,v in j.items():
                    if k.startswith("price") and v!=None : #for null checks
                        price=int(v)
                        # print(price)
                        # tax=0
                        # vendor_name = ""
                    elif k.startswith("tax") and v!=None :  #for null checks
                        tax=int(v)
                        # print(tax)

                    elif k.startswith("vendor") and v!=None:#for null checks
                        vendor_name = str(v)
                        # print(vendor_name)
                final_price = price+tax
                price_vender_list.append((final_price,vendor_name))
                # price_vender_dict[vendor_name]=vendor_name
            sorted_price_vender_list=sorted(price_vender_list)[:3]
            hotel_rates_dict[hotelname]=sorted_price_vender_list

            # hotel_rates_dict[(hotelname,hotelid)]=sorted_price_vender_list
            final_data_dict["Comparison"]=hotel_rates_dict
        #------------------API Call End-------------------
        
        return render(request,"newres.html",final_data_dict)

    return render(request,"newres.html",{})

class GetDataView(APIView):
    def get(self,request,destination):
        url = "https://api.makcorps.com/auth"
        payload = json.dumps({"username": API_USERNAME,
    "password": API_PASSWORD})
        headers = {"Content-Type": 'application/json'}

        response = requests.request("POST", url, headers=headers, data=payload)
        url = f"https://api.makcorps.com/free/{destination}"
        payload = {}
        headers = {
            "Authorization": 'JWT'+' '+response.json()["access_token"]
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        # print(type(response))
        # print(url)  
        # # response_json=json.loads(response)
        return Response(response.json())



