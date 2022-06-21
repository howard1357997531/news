from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  #設定ckeeditor編輯器url，來找到實際檔案位置

    path('passwordreset/',PasswordResetView.as_view(template_name='accounts/passwordreset.html'),
    name='passwordreset'),
    path('passwordresetdone/',PasswordResetDoneView.as_view(template_name='accounts/passwordresetdone.html'),
    name='password_reset_done'),
    path('passwordresetconfirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='accounts/passwordresetconfirm.html'),
    name='password_reset_confirm'),
    path('passwordresetcomplete/',PasswordResetCompleteView.as_view(template_name='accounts/passwordresetcomplete.html'),
    name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)