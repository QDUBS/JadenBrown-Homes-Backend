from django.contrib import admin

from account.models import Account, AccountProfile, Contact, Address

admin.site.register(Account)
admin.site.register(AccountProfile)
admin.site.register(Contact)
admin.site.register(Address)
