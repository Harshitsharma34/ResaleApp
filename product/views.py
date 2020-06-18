from django.shortcuts import render
from .models import Product, ProductImages, Category
# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from account.forms import AdForm


def index(request):
    category = Category.objects.all()
    products = Product.objects.filter(category=category)
    context = {
        "category": category,
        "product": products
    }
    return render(request, 'index.html', context)


def productlist(request, category_slug=None):
    productlist = Product.objects.all()
    category = None
    categorylist = Category.objects.annotate(total_products=Count('product'))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        productlist = productlist.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query) |
            Q(category__category_name__icontains=search_query)
        )
    paginator = Paginator(productlist, 4)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {'product_list': productlist,
               "category_list": categorylist, "category": category}
    template = 'product/product_list.html'

    return render(request, template, context)


def productdetail(request, product_slug):
    productdetail = get_object_or_404(Product, slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'product/product_detail.html'
    context = {'product_detail': productdetail,
               'product_images': productimages}
    return render(request, template, context)


def post_ad(request):
    if request.method == 'POST':  # save
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
    else:
        form = AdForm()

    return render(request, 'product/post_ad.html', {'form': form})
