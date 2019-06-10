# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Site
from .serializers import SiteSerializer


class SiteViewSet(viewsets.ModelViewSet):

    serializer_class = SiteSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Site.objects.all().prefetch_related('site_holdings')  # reduces number of database queries

    def list(self, request):
        all_sites = self.get_queryset()
        page = self.paginate_queryset(all_sites)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_sites, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        site = self.get_object()
        serializer = self.get_serializer(site)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        site_instance = self.get_object()
        serializer = self.get_serializer(site_instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(site_instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the site_instance.
            site_instance._prefetched_objects_cache = {}

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        site = self.get_object()
        self.perform_destroy(site)
        return Response({"message": "Site deleted successfully"})

    def sum(self, request):
        all_sites = self.get_queryset()
        page = self.paginate_queryset(all_sites)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_sites, many=True)
        return Response(serializer.data)

    def average(self, request):
        all_sites = self.get_queryset()
        page = self.paginate_queryset(all_sites)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_sites, many=True)
        return Response(serializer.data)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({"message": "Logout successfull"}, status=status.HTTP_200_OK)
