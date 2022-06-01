from rest_framework import serializers
from core.models import Faq, Member, Block


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('title', 'description')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('user', 'permanent')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('user_id', 'username', 'name', 'role')