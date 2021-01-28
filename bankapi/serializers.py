from rest_framework import serializers
from .models import Branches




class BranchesSerialize(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['ifsc', 'branch', 'address', 'city', 'district', 'state']