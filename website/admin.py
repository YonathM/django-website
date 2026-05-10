from django.contrib import admin
from .models import News, Department, Statistic, Testimonial, Vacancy, TuitionFee, HeroImage, DigitalLibrary, ProductionUnit, Tender, DeanMessage
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date')
    list_filter = ('status', 'created', 'published_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('status', 'published_date')
    readonly_fields = ('author',)  # readonly in form
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Assign logged-in user only when creating new news
            obj.author = request.user
        super().save_model(request, obj, form, change)
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    list_filter = ("status",)
    readonly_fields = ('created_by',)  # readonly in form
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Assign logged-in user only when creating new department
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("title", "value")
    list_filter = ("status",)
    readonly_fields = ('created_by',)  # readonly in form
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Assign logged-in user only when creating new static
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'status', 'created_by', 'created_at')
    list_filter = ('status', 'created_by')
    search_fields = ('name', 'message')
    
    readonly_fields = ('created_by',)  # readonly in form

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Assign logged-in user only when creating new testimonial
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'application_deadline', 'status')
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'description', 'requirements')
    ordering = ('-published_date',)
    date_hierarchy = 'published_date'
    readonly_fields = ('created_by',)  # readonly in form
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Assign logged-in user only when creating new department
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
@admin.register(TuitionFee)
class TuitionFeeAdmin(admin.ModelAdmin):
    list_display = ("sector", "occupation", "fee", "created_at")  # columns in admin list view
    search_fields = ("sector", "occupation")  # adds search box
    list_filter = ("sector", "created_at")  # adds sidebar filters
    ordering = ("-created_at",)  # newest first
@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'image')
    ordering = ('order',)


@admin.register(DigitalLibrary)
class DigitalLibraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'status', 'published_date')
    list_filter = ('status', 'department')
    search_fields = ('title', 'description')
    readonly_fields = ('created_by',)  # readonly in form

@admin.register(ProductionUnit)
class ProductionUnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_type', 'status', 'published_date')
    list_filter = ('status', 'product_type')
    search_fields = ('title', 'description')
    readonly_fields = ('created_by',)  # readonly in form

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'closing_date', 'status')
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'description', 'requirements')
    ordering = ('-published_date',)
    date_hierarchy = 'published_date'
    readonly_fields = ('created_by',)  # readonly in form
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Assign logged-in user only when creating new department
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(DeanMessage)
class DeanMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_by')
    search_fields = ('name', 'message')
    readonly_fields = ('created_by',)  # readonly in form