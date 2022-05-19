from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, Review,\
    BookContributor


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title','isbn13')
    list_filter = ('publisher','publication_date')
    search_fields = ('title','isbn','publisher__name')
    def isbn13(self,obj):
        return f"{obj.isbn[0:3]}-{obj.isbn[3:4]}-\
            {obj.isbn[4:6]}-{obj.isbn[6:12]}-{obj.isbn[12:13]}"
  

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)
    # fields = ('content', 'rating', 'creator', 'book')
    fieldsets = ((None, {'fields': ('creator', 'book')})\
                ,('Review content', {'fields': ('content', 'rating')}))

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names','first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')

    def initialled_name(self,obj):
        """ self.first_names='Jerome David', self.last_names='Salinger => \
            'alinger, JD """
        initials = ''.join([name[0] for name
                            in obj.first_names.split(' ')])
        return "{}, {}".format(obj.last_names, initials)


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review,ReviewAdmin)

# Register your models here.

