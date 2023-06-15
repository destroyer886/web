from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index, name='home'),
   path("about",views.about, name='about'),
   path("gtav",views.gtav, name='gta v'),
   path("contact",views.contact, name='contact'),
   path('saveenquiry',views.saveEnquiry,name="saveenquiry"),
   path('signup',views.handlesignup, name="handlesignup"),
   path('login',views.handlelogin, name="handlelogin"),
   path('logout',views.handlelogout, name="handlelogout"),
   path("godofwar",views.gow, name='gow'),
   path("spiderman",views.spider, name='spider'),
   path("Pubg",views.pubg, name='pubg'),
   path("forza",views.forza, name='forza'),
   path("minecraft",views.minecraft, name='minecraft'),

]