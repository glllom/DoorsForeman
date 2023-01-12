from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name='home'),
    path('hinges', main.views.hinges, name='hinges'),
    path('engravings', main.views.engravings, name='engravings'),
    path('doors', main.views.door_types, name='doors'),
    re_path(r'^doors/(?P<pk>\d+)/', main.views.DoorUpdate.as_view(), name='door_type_update'),
    re_path(r'^locks/(?P<pk>\d+)/', main.views.LockUpdate.as_view(), name='lock_update'),
    re_path(r'^hinges/(?P<pk>\d+)/', main.views.HingesUpdate.as_view(), name='hinges_update'),
    re_path(r'^engravings/(?P<pk>\d+)/', main.views.EngravingUpdate.as_view(), name='engraving_update'),
    re_path(r'^structure/(?P<pk>\d+)/', main.views.StructureUpdate.as_view(), name='structure_update'),
    path('doors/remove/<door_id>', main.views.remove_door, name='door_type_remove'),
    path('lock/remove/<lock_id>', main.views.remove_lock, name='lock_remove'),
    path('hinge/remove/<hinge_id>', main.views.remove_hinge, name='hinge_remove'),
    path('engraving/remove/<engraving_id>', main.views.remove_engraving, name='engraving_remove'),
    path('structure/remove/<structure_id>', main.views.remove_structure, name='structure_remove'),
    path('success', main.views.success, name='success'),
    path('locks', main.views.locks, name='locks'),
    path('structure', main.views.structure, name='structure'),
    path('new_order', main.views.new_order, name='new_order'),
    re_path(r'^order/(?P<order_id>\d+)/', main.views.add_doors, name='add_doors'),
    re_path(r'^show_order/(?P<order_id>\d+)/', main.views.show_order, name='show_order'),
    re_path(r'^report/(?P<order_id>\d+)/', main.views.report, name='report'),
    re_path(r'^search_order', main.views.search_order, name='search_order'),
    re_path(r'^add_door_group/(?P<order_id>\d+)/', main.views.add_door_group, name='add_door_group'),

    path('ajax/load-locks', main.views.load_locks, name='ajax_load_locks'),
    path('ajax/load-hinges', main.views.load_hinges, name='ajax_load_hinges'),
    path('ajax/load-engravings', main.views.load_engraving, name='ajax_load_engraving'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
