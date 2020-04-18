from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Fuser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from django.contrib.auth import login
from django.contrib.auth import logout
import time
from .rec import *
# Create your views here.

@csrf_exempt
def fuser_add(request):
    """
    """
    data = JSONParser().parse(request)
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        # Fuser.objects.create_user(username=serializer['username'].value,
        #                     email=serializer['email'].value,
        #                     password=serializer['password'].value)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=400)


class FaceUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FaceSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def pswd_login(request):
    data = JSONParser().parse(request)
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        if len(Fuser.objects.filter(username=serializer['username'].value)) != 0:
            curr_user = Fuser.objects.get(username=serializer['username'].value)
            if curr_user.password == serializer['password'].value:
                login(request, curr_user)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'incorrect password'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'no such user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        username = request.POST['username']
        curr_user = Fuser.objects.get(username=username)
        logout(curr_user)
        return JsonResponse({'info': 'logout'}, status=status.HTTP_200_OK)


class FaceLoginView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        face_serializer = LoginWithFaceSerializer(data=request.data)
        if face_serializer.is_valid():
            imageInBase64 = request.data['face'].file
            t = time.time_ns()  # 生成照片唯一标示
            filename = './unknown/' + str(t) + '.png'
            with open(filename, 'wb') as f:
                f.write(imageInBase64.getbuffer())
                f.close()

            # 鉴别人脸
            username = identify(unknown_img=filename)
            os.remove(filename)   # 鉴定完毕后删除照片

            if username == "Unknown":
                return JsonResponse({'error': 'can not identify your face'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if len(Fuser.objects.filter(username=username)) != 0:
                    curr_user = Fuser.objects.get(username=username)
                    login(request, curr_user)
                    return JsonResponse({'info': 'login successful', 'username': username}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(face_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(face_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def userInfo(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = Fuser.objects.get(username=username)
        serializer = UserInfoSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
def updatInfo(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            curr_user = Fuser.objects.get(username=serializer['username'].value)
            serializer.update(curr_user, serializer.validated_data).save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            print('error')






