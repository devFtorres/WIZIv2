from tkinter import Widget
from django.forms import ModelForm
from .models import Company, Employer, Separator, WhyUs, Plan, Product, New, MainNew, Service


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            "company",
            "about",
            "phone",
            "address",
            "email",
            "slug",
            "wallpapper",
            "welcome",
        ]

class SeparatorForm(ModelForm):
    class Meta:
        model = Separator
        fields = [
            "title",
            "desc",
            "image",
        ]


class WhyUsForm(ModelForm):
    class Meta:
        model = WhyUs
        fields = [
            "title1",
            "reason1",
            "title2",
            "reason2",
            "title3",
            "reason3",
        ]


class NewForm(ModelForm):
    class Meta:
        model = New
        fields = [
            "title",
            "image",
            "text",
        ]

class MainNewForm(ModelForm):
    class Meta:
        model = MainNew
        fields = [
            "title",
            "image",
            "text",
        ]

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = [
            "title",
            "desc",
        ]


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = [
                "name",
                "funcion",
                "image",
            ]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
                "image",
                "price",
                "name",
            ]


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = [
                "title",
                "price",
                "desc",
            ]



