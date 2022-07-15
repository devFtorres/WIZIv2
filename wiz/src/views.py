
from hashlib import new
from django.shortcuts import render, redirect
from .forms import CompanyForm, SeparatorForm, EmployerForm, ProductForm, PlanForm, WhyUsForm, NewForm, MainNewForm, ServiceForm
from django.contrib.auth.decorators import login_required
from src.models import Company, Separator, Employer, Plan, Product, New, WhyUs, MainNew, Service
from django.core.mail import send_mail



#INFORMATION PAGES
def home(request):
    return render (request, "home.html")

def about(request):
    return render (request, "about.html")

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        toemail = 'wizi.easy2022@gmail.com'
        message = message +  ' \ '  + email + ' \ ' + name
        send_mail(
            'WIZI - Easy to build webpage', #subject
            message, #message
            email, #from
            [toemail], #to email

        )
        return render (request, "contact.html", {'name': name})
    else:
        return render (request, "contact.html")
    

def conditions(request):
    return render (request, "conditions.html")

#COMPANIES

def list_all_companies(request):
    companies = Company.objects.all()
    context = {
        "companies": companies,
    }
    return render (request, "list_all_companies.html", context)


@login_required
def listing_companies(request):
    companies = Company.objects.filter(user=request.user)
    context = {
        "companies": companies,

    }
    return render (request, "list_companies.html", context)

@login_required
def retrieve_company(request, pk):
    company = Company.objects.get(id=pk)
    context={
        "company": company,
    }

    return render(request, "company.html", context)

@login_required
def company_create(request):
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("/companies")
        
    context = {
        "form": form
    }
    return render (request, "company_create.html", context)

@login_required
def company_update(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect("/companies/")
        
    context = {
        "form": form
    }
    return render (request, "company_update.html", context)

@login_required
def company_delete(request, pk):
    company = Company.objects.get(id=pk)
    company.delete()
    return redirect("/companies/")

#SEPARATOR

@login_required
def listing_separator(request):
    
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None

    separators = Separator.objects.filter(company=company)

    context = {
        "separators": separators,
        "company": company,

    }
    return render (request, "list_separator.html", context)

@login_required
def retrieve_separator(request, pk):
    separator = Separator.objects.get(id=pk)
    context={
        "separator": separator,
    }

    return render(request, "separator.html", context)

@login_required
def separator_create(request):
    form = SeparatorForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = SeparatorForm(request.POST,  request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/separators/")
        
    context = {
        "form": form
    }
    return render (request, "separator_create.html", context)

@login_required
def separator_update(request, pk):
    separator = Separator.objects.get(id=pk)
    form = SeparatorForm(instance=separator)
    if request.method == "POST":
        form = SeparatorForm(request.POST, request.FILES, instance=separator)
        if form.is_valid():
            form.save()
            return redirect("/separators/")
        
    context = {
        "form": form
    }
    return render (request, "separator_update.html", context)

@login_required
def separator_delete(request, pk):
    separator = Separator.objects.get(id=pk)
    separator.delete()
    return redirect("/separators/")

#EMPLOYERS

@login_required
def listing_employer(request):

    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None
    
    employers = Employer.objects.filter(company=company)
    context = {
        "employers": employers,
        "company": company,

    }
    return render (request, "list_employer.html", context)

@login_required
def retrieve_employer(request, pk):
    employer = Employer.objects.get(id=pk)
    context={
        "employer": employer,
    }

    return render(request, "employer.html", context)

@login_required
def add_employer(request):
    form = EmployerForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = EmployerForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/employers/")
        
    context = {
        "form": form
    }
    return render (request, "add_employer.html", context)

@login_required
def employer_update(request, pk):
    employer = Employer.objects.get(id=pk)
    form = EmployerForm(instance=employer)
    if request.method == "POST":
        form = EmployerForm(request.POST, request.FILES, instance=employer)
        if form.is_valid():
            form.save()
            return redirect("/employers/")
        
    context = {
        "form": form
    }
    return render (request, "employer_update.html", context)

@login_required
def employer_delete(request, pk):
    employer = Employer.objects.get(id=pk)
    employer.delete()
    return redirect("/employers/")

#PRODUCTS

@login_required
def listing_product(request):

    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None

    products = Product.objects.filter(company=company)
    context = {
        "products": products,
        "company": company,

    }
    return render (request, "list_product.html", context)

@login_required
def retrieve_product(request, pk):
    product = Product.objects.get(id=pk)
    context={
        "product": product,
    }

    return render(request, "product.html", context)

@login_required
def add_product(request):
    form = ProductForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/products/")
        
    context = {
        "form": form
    }
    return render (request, "add_product.html", context)

@login_required
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("/products/")
        
    context = {
        "form": form
    }
    return render (request, "product_update.html", context)

@login_required
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("/products/")

#PLAN

@login_required
def listing_plan(request):

    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None

    plans = Plan.objects.filter(company=company)
    context = {
        "plans": plans,
        "company": company,

    }
    return render (request, "list_plan.html", context)

@login_required
def retrieve_plan(request, pk):
    plan = Plan.objects.get(id=pk)
    context={
        "plan": plan,
    }

    return render(request, "plan.html", context)

@login_required
def add_plan(request):
    form = PlanForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/plans/")
        
    context = {
        "form": form
    }
    return render (request, "add_plan.html", context)

@login_required
def plan_update(request, pk):
    plan = Plan.objects.get(id=pk)
    form = PlanForm(instance=plan)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect("/plans/")
        
    context = {
        "form": form
    }
    return render (request, "plan_update.html", context)

@login_required
def plan_delete(request, pk):
    plan = Plan.objects.get(id=pk)
    plan.delete()
    return redirect("/plans/")






#WHYUS

@login_required
def listing_why(request):
    
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None


    try:
        why = WhyUs.objects.get(company=company)
    except WhyUs.DoesNotExist:
        why = ''

    context = {
        "why": why,
        "company": company,

    }
    return render (request, "list_why.html", context)

@login_required
def retrieve_why(request):
    company = Company.objects.get(user=request.user)
    why = WhyUs.objects.get(company=company)
    context={
        "why": why,
    }

    return render(request, "why.html", context)

@login_required
def why_create(request):
    form = WhyUsForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = WhyUsForm(request.POST,  request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/why/")
        
    context = {
        "form": form
    }
    return render (request, "why_create.html", context)

@login_required
def why_update(request):
    company = Company.objects.get(user=request.user)
    why = WhyUs.objects.get(company=company)
    form = WhyUsForm(instance=why)
    if request.method == "POST":
        form = WhyUsForm(request.POST, instance=why)
        if form.is_valid():
            form.save()
            return redirect("/why/")
        
    context = {
        "form": form
    }
    return render (request, "why_update.html", context)

@login_required
def why_delete(request):
    company = Company.objects.get(user=request.user)
    why = WhyUs.objects.get(company=company)
    why.delete()
    return redirect("/why/")



#New

@login_required
def listing_new(request):
    
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None
    
    try:
        mainnew = MainNew.objects.get(company=company)
    except MainNew.DoesNotExist:
        mainnew = ''

    try:
        news = New.objects.filter(company=company).order_by('-id')
    except New.DoesNotExist:
        news = None


    
    

    context = {
        "news": news,
        "mainnew": mainnew,
        "company": company,

    }
    return render (request, "list_new.html", context)

@login_required
def retrieve_new(request, pk):
    new = New.objects.get(id=pk)
    context={
        "new": new,
    }

    return render(request, "new.html", context)

@login_required
def new_create(request):
    form = NewForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = NewForm(request.POST,  request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/new/")
        
    context = {
        "form": form
    }
    return render (request, "new_create.html", context)

@login_required
def new_update(request, pk):
    new = New.objects.get(id=pk)
    form = NewForm(instance=new)
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
            return redirect("/new/")
        
    context = {
        "form": form
    }
    return render (request, "new_update.html", context)

@login_required
def new_delete(request, pk):
    new = New.objects.get(id=pk)
    new.delete()
    return redirect("/new/")
    


#MainNew

@login_required
def listing_mainnew(request):
    
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None

    mainnew = MainNew.objects.filter(company=company)

    context = {
        "mainnew": mainnew,
        "company": company,

    }
    return render (request, "list_mainnew.html", context)

@login_required
def retrieve_mainnew(request, pk):
    mainnew = MainNew.objects.get(id=pk)
    context={
        "mainnew": mainnew,
    }

    return render(request, "mainnew.html", context)

@login_required
def mainnew_create(request):
    form = MainNewForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = MainNewForm(request.POST,  request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/new/")
        
    context = {
        "form": form
    }
    return render (request, "mainnew_create.html", context)

@login_required
def mainnew_update(request):
    company = Company.objects.get(user=request.user)
    mainnew = MainNew.objects.get(company=company)
    form = NewForm(instance=mainnew)
    if request.method == "POST":
        form = MainNewForm(request.POST, request.FILES, instance=mainnew)
        if form.is_valid():
            form.save()
            return redirect("/new/")
        
    context = {
        "form": form
    }
    return render (request, "mainnew_update.html", context)

@login_required
def mainnew_delete(request, pk):
    mainnew = MainNew.objects.get(id=pk)
    mainnew.delete()
    return redirect("/mainnew/")



#Service

@login_required
def listing_service(request):
    
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None

    services = Service.objects.filter(company=company)

    context = {
        "services": services,
        "company": company,

    }
    return render (request, "list_service.html", context)

@login_required
def retrieve_service(request, pk):
    service = Service.objects.get(id=pk)
    context={
        "service": service,
    }

    return render(request, "service.html", context)

@login_required
def service_create(request):
    form = ServiceForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = ServiceForm(request.POST,  request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/service/")
        
    context = {
        "form": form
    }
    return render (request, "service_create.html", context)

@login_required
def service_update(request, pk):
    service = Service.objects.get(id=pk)
    form = NewForm(instance=service)
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect("/service/")
        
    context = {
        "form": form
    }
    return render (request, "service_update.html", context)

@login_required
def service_delete(request, pk):
    service = Service.objects.get(id=pk)
    service.delete()
    return redirect("/service/")



#WEBPAGE

def my_wiz_view(request, slug):
    company = Company.objects.get(slug=slug)
    separators = Separator.objects.filter(company=company)
    employers = Employer.objects.filter(company=company)
    plans = Plan.objects.filter(company=company)
    products = Product.objects.filter(company=company)
    try:
        why = WhyUs.objects.get(company=company)
    except WhyUs.DoesNotExist:
        why = ''

    news = New.objects.filter(company=company).order_by('-id')[:3]

    try:
        mainnew = MainNew.objects.get(company=company)
    except MainNew.DoesNotExist:
        mainnew = ''
    
    services = Service.objects.filter(company=company)

    context = {
        "company": company,
        "separators": separators,
        "employers": employers,
        "products": products,
        "plans": plans,
        "why": why,
        "news": news,
        "mainnew": mainnew,
        "services": services,
    }



    if request.method == "POST":
        sub = request.POST.get('subject')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mailf = request.POST.get('mailcompany')

        send_mail(
        sub, #subject
        message+name, #message
        mailf, #from
        [email], #to email

    )
        return render(request, "my_wiz_view.html", context)
    else:
        return render(request, "my_wiz_view.html", context)

