from .models import Domain, Phylum, Class, Order, Family, Genus, Species
from rest_framework import viewsets, permissions, status
from .serializer import DomainSerializer, PhylumSerializer, ClassSerializer, OrderSerializer, FamilySerializer, GenusSerializer, SpeciesSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser


# Create your views here.

class DomainViewSet(viewsets.ModelViewSet):
    
    queryset = Domain.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = DomainSerializer

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]

class PhylumViewSet(viewsets.ModelViewSet):
    
    queryset = Phylum.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = PhylumSerializer

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # print(serializer.data)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        parent_serializer = DomainSerializer(instance.parent)

        data = serializer.data
        data['parent'] = parent_serializer.data

        return Response(data)

class ClassViewSet(viewsets.ModelViewSet):
    
    queryset = Class.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = ClassSerializer

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        parent_serializer = PhylumSerializer(instance.parent)

        data = serializer.data
        data['parent'] = parent_serializer.data

        return Response(data)

class OrderViewSet(viewsets.ModelViewSet):
    
    queryset = Order.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = OrderSerializer

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        parent_serializer = ClassSerializer(instance.parent)

        data = serializer.data
        data['parent'] = parent_serializer.data

        return Response(data)

class FamilyViewSet(viewsets.ModelViewSet):
    
    queryset = Family.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = FamilySerializer

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        parent_serializer = OrderSerializer(instance.parent)

        data = serializer.data
        data['parent'] = parent_serializer.data

        return Response(data)

class GenusViewSet(viewsets.ModelViewSet):
    
    queryset = Genus.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = GenusSerializer

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        parent_serializer = FamilySerializer(instance.parent)

        data = serializer.data
        data['parent'] = parent_serializer.data

        return Response(data)

class SpeciesViewSet(viewsets.ModelViewSet):
    
    queryset = Species.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = SpeciesSerializer

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        parent_serializer = GenusSerializer(instance.parent)

        data = serializer.data
        data['parent'] = parent_serializer.data

        return Response(data)
