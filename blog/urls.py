from django.urls import path

from .views import home, namangan, andijon, fargona, buxoro, toshkent, jizzax, sirdaryo, surxandaryo, xorazm, navoiy, qoraqolpogiston

urlpatterns = [
    path("", home),
    path("andijon/", andijon),
    path("namangan/", namangan),
    path("fargona/", fargona),
    path("buxoro/", buxoro),
    path("toshkent/", toshkent),
    path("jizzax/", jizzax),
    path("sirdaryo/", sirdaryo),
    path("surxandaryo/", surxandaryo),
    path("xorazm/", xorazm),
    path("qoraqolpogiston/", qoraqolpogiston),
    path("navoiy/", navoiy),
]