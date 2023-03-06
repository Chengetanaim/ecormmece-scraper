from django.shortcuts import render, redirect
from .models import Product, Category, Website
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# from .adding import process
#
# process()


def index(request):
    categories = Category.objects.all()
    category_list = Category.objects.order_by('-id')
    product_list = Product.objects.order_by('-id')
    paginator = Paginator(product_list, 12)
    paginator2 = Paginator(product_list, 6)
    category_paginator = Paginator(category_list, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
        products2 = paginator2.page(page)
        categories2 = category_paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
        products2 = paginator2.page(1)
        categories2 = category_paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
        products2 = paginator2.page(paginator2.num_pages)
        categories2 = category_paginator.page(category_paginator.num_pages)
    context = {'categories': categories,
               'products': products,
               'products2': products2,
               'categories2': categories2}
    return render(request, 'store/index.html', context)


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    product_list = category.products.order_by('-id')
    paginator = Paginator(product_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)

    context = {'category': category,
               'products': products,
               }
    return render(request, 'store/category.html', context)


def website(request, website_id):
    website = Website.objects.get(id=website_id)
    categories = Category.objects.all()
    product_list = website.products.order_by('-id')
    product_list_random = website.products.order_by('?')
    product_list_random2 = website.products.order_by('?')
    paginator = Paginator(product_list, 3)
    paginator_random = Paginator(product_list_random, 3)
    paginator_random2 = Paginator(product_list_random2, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
        products_random = paginator_random.page(page)
        products_random2 = paginator_random2.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
        products_random = paginator_random.page(1)
        products_random2 = paginator_random2.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
        products_random = paginator_random.page(paginator.num_pages)
        products_random2 = paginator_random2.page(paginator.num_pages)

    context = {'category': category,
               'products': products,
               'categories': categories,
               'products_random': products_random,
               'products_random2': products_random2,
               'website': website,
               }
    return render(request, 'store/website.html', context)


def about_us(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'store/about_us.html', context)


class SearchResultsView(ListView):
    model = Product
    template_name = 'store/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
        Q(name__icontains=query) | Q(category__name__icontains=query) | Q(website__name__icontains=query) | Q(price__icontains=query)
        )
        return object_list


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    product_list = Product.objects.filter(category=product.category)
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    context = {'product': product, 'products': products}
    return render(request, 'store/detail.html', context)


def store(request):
    product_list = Product.objects.order_by('-id')
    paginator = Paginator(product_list, 12)  # 12 categories in each page
    page = request.GET.get('page')
    try:

        products = paginator.page(page)
    except PageNotAnInteger:

        products = paginator.page(1)
    except EmptyPage:

        products = paginator.page(paginator.num_pages)

    categories = Category.objects.all()

    context = {'products': products, 'categories': categories}
    return render(request, 'store/store.html', context)


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect('store:mybookmarks')
    else:
    # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


@login_required()
def mybookmarks(request):
    images = Image.objects.filter(user=request.user)
    products = Product.objects.filter(users_like=request.user)
    context = {'images': images, 'products': products}
    return render(request, 'images/image/mybookmarks.html', context)


@login_required()
def mybookmark(request, bookmark_id):
    image = Image.objects.get(id=bookmark_id)
    context = {'image': image}
    return render(request, 'images/image/mybookmark.html', context)


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Product.objects.get(id=image_id)
            if action == 'bookmark':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


def mobile_search(request):
    return render(request, 'store/mobile_search.html')