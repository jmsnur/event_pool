from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    def get(self):

        r = self.request
        data = {
            "status": "success",
            "data": r
        }
        return Response(data=data, status=status.HTTP_200_OK)
