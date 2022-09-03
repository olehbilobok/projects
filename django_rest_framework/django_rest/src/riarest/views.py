from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from riarest.models import Appartments, Cities, Owners
from riarest.serializers import AppartmentsSerializer, CitiesSerializer, OwnerSerializer
from rest_framework.pagination import LimitOffsetPagination


class AppartmentsList(APIView, LimitOffsetPagination):

    """List all appartments, or create a new appartment"""

    permission_classes = [IsAuthenticated]

    def get(self, request):

        request_query = request.GET
        appartments = Appartments.objects.all()

        if request_query:
            city = request_query.get('city')
            if city:
                appartments = appartments.filter(city=city)

            operation_type = request_query.get('operation_type')
            if operation_type:
                appartments = appartments.filter(operation_type=operation_type)

            min_price = request_query.get('min_price')
            max_price = request_query.get('max_price')
            if min_price or max_price:
                min_price = 0 if not min_price else min_price
                max_price = 100000000000 if not max_price else max_price
                appartments = appartments.filter(total_price__gte=min_price, total_price__lte=max_price)

            min_rooms = request_query.get('min_rooms')
            max_rooms = request_query.get('max_rooms')
            if min_rooms or max_rooms:
                min_rooms = 1 if not min_rooms else min_rooms
                max_rooms = 10 if not max_rooms else max_rooms
                appartments = appartments.filter(rooms_count__gte=min_rooms, rooms_count__lte=max_rooms)

        paginator = self.paginate_queryset(appartments, request)

        serializer = AppartmentsSerializer(paginator, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = AppartmentsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppartmentsDetail(APIView):

    """Retrieve, update or delete a appartment instance"""

    def get_object(self, pk):
        try:
            return Appartments.objects.get(pk=pk)
        except Appartments.DoesNotExist:
            return None

    def head(self, request, pk):
        if self.get_object(pk):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        appartments = self.get_object(pk)
        serializer = AppartmentsSerializer(appartments)
        return Response(serializer.data)

    def put(self, request, pk):
        appartments = self.get_object(pk)
        serializer = AppartmentsSerializer(appartments, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appartments = self.get_object(pk)
        appartments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CitiesList(APIView, LimitOffsetPagination):

    def get(self, request):
        cities = Cities.objects.all()
        paginator = self.paginate_queryset(cities, request)
        serializer = CitiesSerializer(paginator, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CitiesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CitiesDetail(APIView):

    def get_object(self, pk):
        try:
            return Cities.objects.get(pk=pk)
        except Cities.DoesNotExist:
            return None

    def head(self, request, pk):
        if self.get_object(pk):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        cities = self.get_object(pk)
        serializer = CitiesSerializer(cities)
        return Response(serializer.data)

    def put(self, request, pk):
        cities = self.get_object(pk)
        serializer = CitiesSerializer(cities, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cities = self.get_object(pk)
        cities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OwnersList(APIView, LimitOffsetPagination):

    def get(self, request):
        owners = Owners.objects.all()
        paginator = self.paginate_queryset(owners, request)
        serializer = OwnerSerializer(paginator, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OwnersDetail(APIView):

    def get_object(self, pk):
        try:
            return Owners.objects.get(pk=pk)
        except Owners.DoesNotExist:
            return None

    def head(self, request, pk):

        if self.get_object(pk):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        owners = self.get_object(pk)
        serializer = OwnerSerializer(owners)
        return Response(serializer.data)

    def put(self, request, pk):
        owners = self.get_object(pk)
        if owners:
            serializer = OwnerSerializer(owners, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        owners = self.get_object(pk)
        owners.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class Logout(APIView):
    def post(self, request):
        # simply delete the token
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
