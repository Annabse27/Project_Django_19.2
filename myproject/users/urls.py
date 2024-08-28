from django.urls import path
from users.views import SignupView, CustomLoginView, CustomLogoutView, EmailVerificationView, PasswordResetView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('verify-email/<int:user_id>/', EmailVerificationView.as_view(), name='email_verification'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
```

Обновите основной `urls.py` (в `config/urls.py`), чтобы включить маршруты из нового приложения:

**`config/urls.py`**

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('catalog.urls')),  # Остальные маршруты остаются в каталоге
]
