from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path("", views.dashboard, name = "Dashboard"),
   path("Lend Space", views.addandmgspace, name="land Your Space"),
   path("payment", views.Payment, name="payment"),
   path("Details", views.parking_Details, name="Details"),
   path("sign", views.sign_up_in, name="sign"),
   path("adminlog", views.adminlog,name="adminlog"),
   path("booked", views.booked_slots,name="booked"),
   path("ForgetPass",views.forgetPass,name='ForgetPass'),
   re_path(r"^updateclicked/$", views.updateclicked,name="updateclicked"),
   re_path(r"^cancelclicked/$", views.cancelclicked, name="cancelclicked")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)