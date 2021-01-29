from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from .serializers import BranchesSerialize
from django.views.generic import TemplateView, ListView
from .models import Branches
from django.db.models import Q


class PostListView(ListAPIView):
    serializer_class = BranchesSerialize
    filter_backends = [SearchFilter]
    search_fields = ['ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state']

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Branches
    template_name = 'search_results.html'
    

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Branches.objects.filter(
            Q(city__icontains=query) | Q(state__icontains=query) | 
            Q(ifsc__icontains=query) | Q(branch__icontains=query) |
            Q(district__icontains=query) | Q(address__icontains=query) 
        )
        return object_list
