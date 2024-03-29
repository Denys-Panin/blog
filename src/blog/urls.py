# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.decorators import cache
# from django.views.generic import RedirectView, TemplateView
from django.urls import include, path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about_us/', views.about_us, name='about_us'),
    path(
        'article/list/',
        views.ArticleListView.as_view(),
        name='article_list'
    ),
    path('article/list/<slug:slug>/', views.article_category,
         name='article_list_category'),
    path('article/create/', views.create_article, name='article_create'),
    path('article/<slug:slug>/', views.show_article, name='article_show'),
    path('article/update/<slug:slug>/', views.update_article,
         name='article_update'),
    path('article/delete/<slug:slug>/', views.delete_article,
         name='article_delete'),
    path('article/<slug:slug>/comment/', views.add_comment_to_article,
         name='add_comment'),

    # path('subscribers/', views.get_subscribers, name='subscribers'),
    # path('subscriber/add/', views.add_subscriber, name='subscriber_add'),
    # path(
    #     'authors/all/',
    #     cache.cache_page(60 * 2)(views.authors_all),
    #     name='authors_all'
    # ),

    path('authors/all/', views.get_authors, name='authors_all'),
    path('author/<slug:slug>/', views.get_author, name='author_get'),
    path(
        'author/delete/<slug:slug>/',
        views.delete_author,
        name='author_delete'
    ),
    path('book/list/', views.BooksListView.as_view(), name='book_list'),
    path('contact/', views.ContactUsView.as_view(), name='contact_us'),

    path('api/v1/', include('api.urls')),
]
