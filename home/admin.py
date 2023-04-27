from django.contrib import admin
from home.models import registermodel,test,package,adminmodel,User,appointment
from home.models import Patient_List,feedback,Booking,doctor,Payment

admin.site.register(registermodel)
admin.site.register(test)
admin.site.register(package)
admin.site.register(adminmodel)
admin.site.register(Patient_List)
admin.site.register(feedback)
admin.site.register(Booking)
admin.site.register(doctor)
admin.site.register(appointment)
admin.site.register(Payment)






