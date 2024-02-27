def approve(modeladmin, request, queryset):
    queryset.update(is_approved=True)
    
def reprove(modeladmin, request, queryset):
    queryset.update(is_approved=False)