from rest_framework import serializers
from core.models import Faq, Member, Block


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('title', 'description')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('user_id', 'warn')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('user_id', 'full_name', 'first_name', 'username', 'role')