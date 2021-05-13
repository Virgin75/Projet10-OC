from django.contrib import admin
from issuetracker.models import Project, Issue, Comment, Contributor

admin.site.register(Contributor)


class ContributorInline(admin.TabularInline):
    model = Project.contributors.through


@admin.register(Project)
class OfferAdmin(admin.ModelAdmin):
    inlines = (ContributorInline,)
    exclude = ('contributors',)  # Excluding field to hide unnecessary field, as mentioned in the docs


admin.site.register(Issue)
admin.site.register(Comment)
