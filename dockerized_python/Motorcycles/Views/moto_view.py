from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Motorcycles.models import Moto
from Motorcycles.serializers import MotoModelSerializer


class MotoGetView(APIView):

    def get(self, request):
        moto_list = Moto.objects.all()

        serializer = MotoModelSerializer(moto_list, many=True)

        return Response(serializer.data)


class MotoPostView(APIView):

    def post(self, request):

        serializer = MotoModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MotoDetailView(APIView):

    def get(self, request, moto_id):
        moto = Moto.objects.filter(id=moto_id).first()

        if not moto:
            return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MotoModelSerializer(moto)

        return Response(serializer.data)

    def delete(self, request, moto_id):
        moto = Moto.objects.filter(id=moto_id).first()

        if not moto:
            return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)

        moto.delete()

        return Response(status.HTTP_204_NO_CONTENT)

