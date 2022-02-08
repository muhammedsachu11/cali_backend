
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.views import APIView
from .models import AuthUser, \
    Slotdetails, SlotAsscTime
from .serializers import Slotdetailsserializer, \
    SlotAsscTimeSerializer

from django.utils.timezone import datetime
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import models

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from django.contrib.auth.models import User
import json



class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slotdetails.objects.all()
    serializer_class = Slotdetailsserializer

    @action(detail=False, methods=["GET"])
    def mealplanselection(self, request, mp_id=None):

        lst = []
        slotdata = Slotdetails.objects.all().order_by('slot_id')
        for val in slotdata:
            dict = {}
            dict['slot_id'] = val.slot_id
            dict['candidate_name'] = val.candidate_name
            dict['date'] = val.slot_item_date.strftime('%m/%d/%Y')
            dict['slot_timing'] = val.slot_timing
            dict['slot_type'] = val.slot_type
            dict['recruiter_name'] = val.recruiter_name
            dict['slot_active'] = val.slot_active
            lst.append(dict)
        return Response(lst, status=200)



    @action(methods=["POST"], detail=False)
    def addtoclick(self, request):
        # import pdb; pdb.set_trace()
        user = request.user
        slot_id = request.data['slotid']
        candidate_name = request.data['candidate_name']
        if slot_id == 'None':
            slot_id == 1
        else: 
            slot_id == slot_id


        mealplan = Slotdetails.objects.get(slot_id=slot_id)
        if mealplan.slot_active == None:
            clicked_data = Slotdetails.objects.filter(
                slot_id=slot_id).update(slot_active=1, candidate_name= candidate_name)
        elif mealplan.slot_active == 1:
            clicked_data = Slotdetails.objects.filter(
                slot_id=slot_id).update(slot_active=0, candidate_name= '')
        else:
            clicked_data = Slotdetails.objects.filter(
                slot_id=slot_id).update(slot_active=1, candidate_name= candidate_name)

        return Response(clicked_data, status=200)



    @action(detail=False, methods=["POST"])
    def addyour_recipetocalendar(self, request):
        # import pdb; pdb.set_trace()
        slot_item_date = request.data['slot_item_date']
        slot_type = request.data['slot_type']
        recruiter_name = request.data['recruiter_name']
        checkedSlots = request.data['checkedNames']

        recruiter_id = request.data['recruiter_id']
        

        for slots in zip(checkedSlots):
            slots = " ".join(str(x) for x in slots)
            
            slot_id = Slotdetails.objects.all().order_by('-slot_id').first()
            
            
            if slot_id == None:
                slot_id = 1

            else:
                slot_id = slot_id.slot_id
                slot_id = int(slot_id) + 1
            add_mp = Slotdetails.objects.create(slot_id = slot_id,recruiter_name = recruiter_name,recruiter_id = recruiter_id
            ,slot_timing = slots,slot_item_date = slot_item_date,slot_type = slot_type)
        return Response(status=200)

    @action(detail=False, methods=["GET"])
    def getuser_timings(self, request):
        lst = []
        timings = SlotAsscTime.objects.all().order_by('-user_assc_id')
        for val in timings:
            dict = {}
            dict['slot'] = val.slot_timing
            lst.append(dict)
        return Response(lst, status=200)

   

    @action(detail=False, methods=["GET"])
    def getcurrentdates(self, request):
        from datetime import date
        today = date.today().strftime("%b %d, %Y")
        return Response(today, status=200)

    @action(detail=False, methods=["GET"])
    def getweekplans(self, request):
        from datetime import date
        from datetime import datetime
        import datetime
        lst = []
        dt = date.today() - timedelta(5)
        my_date = date.today()
        end = dt
        plan = Slotdetails.objects.all()

        for val in plan:
            dict = {}
            date =val.slot_item_date.strftime("%d")
            day = val.slot_item_date.strftime("%a")
            weekday = date + '-' + day

            dict['slot_id'] = val.slot_id
            dict['candidate_name'] = val.candidate_name
            dict['date'] = val.slot_item_date.strftime('%m/%d/%Y')
            dict['slot_timing'] = val.slot_timing
            dict['slot_type'] = val.slot_type
            dict['created_date'] = weekday
            dict['recruiter_name'] = val.recruiter_name
           
            lst.append(dict)
        sortedArray = sorted(
            lst,
            key=lambda x: datetime.datetime.strptime(x['date'], '%m/%d/%Y'), reverse=False
        )

        return Response(sortedArray, status=200)

   

 


 