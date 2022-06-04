from django.contrib import admin
from django import forms
from .models import *


class BlockingInLine(admin.StackedInline):
    model = Block
    extra = 1
    exclude = ('stop_time', )


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'violation')
    list_filter = ('violation',)
    exclude = ('violation', )


class BlockForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Member.objects.all(), label='Мембер', widget=forms.Select)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'stop_time')
    list_filter = ('permanent',)
    exclude = ('stop_time', )
    form = BlockForm
