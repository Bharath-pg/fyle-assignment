from bankapi.viewsets import BranchesApi
from rest_framework import routers
from bankapi.views import PostListView

router = routers.DefaultRouter()
router.register(r'branches', BranchesApi)



