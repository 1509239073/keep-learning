from django.contrib import admin
from blog.models import User,Employee,Test
# class TagInline(admin.TabularInline):
	# model = Tag
class UserAdmin(admin.ModelAdmin):
	# fields =('name','sex')
	list_display = ('name',)
	# # inlines = [TagInline]
	# fieldsets =(
	# 	['Main',{
	# 	    'fields':('name','sex')
	# 	}]

	# )


admin.site.register(User,UserAdmin)
admin.site.register([Employee,Test])




# Register your models here.
