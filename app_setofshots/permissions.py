def admin_permissions_for_bar(class_to_decorate):
    class AdminPermissons(class_to_decorate):
        def has_change_permission(self, request, obj=None):
            if obj is not None and obj.title:
                if request.user.first_name == obj.title:
                    return True

        def has_delete_permission(self, request, obj=None):
            if obj is not None and obj.title:
                if request.user.first_name == obj.title:
                    return True
    return AdminPermissons


def admin_permissions_for_dish(class_to_decorate):
    class AdminPermissons(class_to_decorate):
        def has_change_permission(self, request, obj=None):
            if obj is not None:
                if request.user.first_name == str(obj.bar):
                    return True

        def has_delete_permission(self, request, obj=None):
            if obj is not None:
                if request.user.first_name == str(obj.bar):
                    return True
    return AdminPermissons
