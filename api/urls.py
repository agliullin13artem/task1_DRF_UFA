from api.spectacular.urls import urlpatterns as doc_urls
from groups.urls import urlpatterns as groups_urls
app_name = "api"

urlpatterns = []


urlpatterns += doc_urls
urlpatterns += groups_urls
