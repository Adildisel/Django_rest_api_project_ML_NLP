from django.shortcuts import render

from .models import *

from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework import permissions

from django.contrib.auth.models import User

from .ml import MlHelper
import os
import pickle

dirname = os.path.dirname(__file__)

ml_helper = MlHelper()

# dest = os.path.join(dirname, 'movieclassifier', 'pkl_objects')

vect = ml_helper.vect
clf = pickle.load(open(os.path.join(
    dirname,
    'movieclassifier/pkl_objects/classifier.pkl'), 'rb'))




class ParserAPIView(APIView):

    # permission_classes = [permissions.AllowAny, ]
    
    def get(self, request):
        comments = ParserComments.objects.all()

        serializer = ParserCommentSerializer(comments, many=True)

        return Response({'data': serializer.data})

    def post(self, request):

        comment = ParserCommentSerializer(data=request.data)

        if comment.is_valid():
            comment.save(auth_comment = request.user)
            return Response({'statuse': 'Add'})
        else:
            return Response({'statuse': 'Error'})

class VideoIdAPIView(APIView):

    def get(self, request):
        all_data = ParserVideoId.objects.all()
        serializers = VideoIdSerializer(all_data, many=True)
        return Response({'data': serializers.data})

    def post(self, request):

        url = VideoUrlSerializer(data = request.data)
        result = {}
        if url.is_valid():
            url_ = url.data['video_id']
            ml_helper.get_video_id(url=url_)
            list_comments = ml_helper.get_comments()

            for i, j in enumerate(list_comments):
                X = vect.transform([j])
                result[i] = {'comment': j,'essessment':clf.predict(X)[0]}
            return Response(result)
        else:
            return Response(result)


