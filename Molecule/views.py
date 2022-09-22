import base64
from email.policy import HTTP
from django.forms import ModelChoiceField
from django.http import JsonResponse, HttpResponse
from .models import Molecule
from .serializers import MoleculeSerialiser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.filters import SearchFilter
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

from rest_framework.parsers import BaseParser
import json

@api_view(['GET', 'POST','EXECUTE'])
def Molecule_list(request,*args,**kwargs):

    if request.method == 'GET':
        #molecule = Molecule.objects.all()
        #lsn_string = request.query_params.get('LSN', None)
        #LSNs = lsn_string.split('&LSN=')

        LSNs = request.GET.getlist('LSNs')

        molecule_list = []
        with open('C:/molecule2_master/Molecule/details.json', 'r') as f:
                    data4 = json.load(f)
                    molecule_list.append(data4)

        if LSNs:
            
            for lsn in LSNs:
                molecule=Molecule.objects.filter(id=lsn).values_list('LSN','id','sdf')
                serialized_data = json.dumps(list(molecule))
                molecule_list.append(serialized_data)
                
        return Response(molecule_list)
        
        '''molecules = Molecule.objects.all()
        serializer = MoleculeSerialiser(molecules, many=True)
        filter_backends = (filters.SearchFilter,)
        search_fields = ['LSN']
        return Response(serializer.data)'''                 
       
    '''if request.method == 'POST':
        if 'lsn_arr' in request.data.keys():
            response = {}
            lsn_list = request.data['lsn_arr']
            data = list(Molecule.objects.filter(id__in=lsn_list).values())
            with open('C:/Users/prash/Documents/p4/test_molecule/test_molecule/Molecule/details.json', 'r') as f:
                data3 = json.load(f)
                data3['rows'][0]['data'].append(data)
            if (Molecule.objects.filter(id__in=lsn_list).values()):
                response['returnValue'] = data3
                response['message'] = 'Molecules Fetched Successfully'
                return Response(response, status=status.HTTP_200_OK)
            else: 
                    return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            response = {}
            LSN_data = request.data['LSN']
            sdf_data = request.data['sdf']
            data2 = Molecule.objects.create(LSN = LSN_data, sdf = sdf_data)
            data2.save()
            response['data2'] = data2
            return redirect(reverse ('mol_view'))'''

def ntlm_auth(request):
    username = None
    response = None

    auth = request.META.get('HTTP_AUTHORIZATION')
    if not auth:
        response = HttpResponse(status=401)
        response['WWW-Authenticate'] = "NTLM"
    elif auth[:4] == "NTLM":
        msg = base64.b64decode(auth[4:])
        #  print repr(msg)
        ntlm_fmt = "<8sb" #string, length 8, 4 - op
        NLTM_SIG = "NTLMSSP\0"
        signature, op = struct.unpack(ntlm_fmt, msg[:9])
        if signature != NLTM_SIG:
            print ("error header not recognized")
        else:
            print ("recognized")
            # print signature, op
            # print repr(msg)
            if op == 1:
                out_msg_fmt = ntlm_fmt + "2I4B2Q2H"
                out_msg = struct.pack(out_msg_fmt,
                    NLTM_SIG, #Signature
                    2, #Op
                    0, #target name len
                    0, #target len off
                    1, 2, 0x81, 1, #flags
                    0, #challenge
                    0, #context
                    0, #target info len
                    0x30, #target info offset
                )

                response = HttpResponse(status=401)
                response['WWW-Authenticate'] = "NTLM " + base64.b64encode(out_msg).strip()
            elif op == 3:
                username = get_msg_str(msg, 36)

    return username, response

@api_view(['GET', 'PUT', 'DELETE'])
def Molecule_detail(request, id, format=None):
    try:
        molecules = Molecule.objects.get(pk=id)
    except Molecule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = MoleculeSerialiser(molecules)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        molecules.delete()
        return Response(status.HTTP_204_NO_CONTENT)
