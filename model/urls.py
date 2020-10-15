from django.conf.urls import url
from .views import FileUploadView, ModelVersionView, SendModelView

urlpatterns = [
    url(r'upload/', FileUploadView.as_view()),
    url(r'version/', ModelVersionView.as_view()),
    url(r'download/', SendModelView.as_view()),
]