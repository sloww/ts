from django.contrib import admin
from .models import Company, Deal, Contact,Address
from v1.admin import admin_site

from searchadmin.admin import SelectModelAdmin


# class DataMasterAdmin(SelectModelAdmin):
 ##25     search_fields = ('title','remark','distributor',)
 #26     list_display = ('master_code','title','remark', 'distributor', )
 #27     fields = ('master_code','title_show','title','img_show',
 #28         'img_url', 'scan_show','describe','describe_show', 'tel','company','master_uuid',
 #29         'remark', 'distributor', 'redirect_url','redirect_on',
 #30         'feedback_show',
 #31         )


class DealMasterAdmin(SelectModelAdmin):
    search_fields = ('num','p1name','p1spec','buyer__company__name','owner__company__name', )
    list_display = ('num','buyer_company','p1name','p1count','p1price', 'total','has_fapiao','has_pay','has_delivery','format_url', )
    readonly_fields = ('url','format_url','num',)
admin_site.register(Company)
admin_site.register(Address)
admin_site.register(Deal, DealMasterAdmin)
admin_site.register(Contact)

 

# Register your models here.
