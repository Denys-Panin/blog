from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.decorators import cache
from django.views.generic import RedirectView, TemplateView

from . import views

app_name = 'blog'
urlpatterns = [
    # path('myview/', views.my_view, name='my_view'),
    # path('', TemplateView.as_view(template_name='blog/home_page.html'), name='home_page'),  # TODO rework
    # path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),  # TODO rework

    path('', views.home_page, name='home_page'),
    path('about_us/', views.about_us, name='about_us'),
    # path('end/registration/',
    #     TemplateView.as_view(template_name='blog/thanks_for_activation.html'),  #TODO rework
    #     name='end_registration'
    #     ),
    path('article/list/', views.ArticleListView.as_view(), name='article_list'),
    # path('posts/list/csv/', views.PostXLSX.as_view(), name='posts_list_csv'),  #TODO rework
    path('article/create/', views.create_article, name='article_create'),
    path('article/<slug:slug>/', views.show_article, name='article_show'),
    path('article/update/<slug:slug>/', views.update_article, name='article_update'),
    path('article/delete/<slug:slug>/', views.delete_article, name='article_delete'),

    # path('subscribers/', views.get_subscribers, name='subscribers'),
    # path('subscriber/add/', views.add_subscriber, name='subscriber_add'),
    # path('authors/all/', cache.cache_page(60 * 2)(views.authors_all), name='authors_all'),

    path('authors/all/', views.get_authors, name='authors_all'),
    path('author/delete/<slug:slug>/', views.delete_author, name='author_delete'),
    path('book/list/', views.BooksListView.as_view(), name='book_list'),

    # path('categories/all/', views.get_categories, name='categories_all'),

    path('contact/', views.ContactUsView.as_view(), name='contact_us'),
    # path('contact/us/list/', views.ContactUsListView.as_view(), name='contact-us-list'),
    path('api/v1/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
