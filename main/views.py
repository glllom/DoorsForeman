from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from main.forms import *
from main.models import *
from main.calculator import *


def index(request):
    """temp"""
    return render(request, 'index.html')


def success(request):
    """temp"""
    return HttpResponse('success')


""" Door Types """


def door_types(request):
    doors = DoorType.objects.all()
    form_error = None
    form = DoorTypeForm()
    if request.method == 'POST':
        form = DoorTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_error = True
    return render(request, 'doors.html', {'form': form, 'doors': doors, 'form_error': form_error})


class DoorUpdate(UpdateView):
    model = DoorType
    form_class = DoorTypeForm
    template_name = 'update_door.html'
    success_url = reverse_lazy('doors')


def remove_door(request, door_id):
    DoorType.objects.filter(id=door_id).delete()
    return redirect('doors')


"""Locks"""


def locks(request):
    all_locks = Lock.objects.all()
    form = LockForm()
    form_error = None
    if request.method == 'POST':
        form = LockForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form_error = True
    return render(request, 'locks.html', {'form': form,
                                          'locks': all_locks,
                                          'form_error': form_error})


class LockUpdate(UpdateView):
    model = Lock
    form_class = LockForm
    template_name = 'update_lock.html'
    success_url = reverse_lazy('locks')


def remove_lock(request, lock_id):
    Lock.objects.filter(id=lock_id).delete()
    return redirect('locks')


"""Hinges"""


def hinges(request):
    form = HingesForm()
    form_error = None
    all_hinges = Hinge.objects.all()
    if request.method == 'POST':
        form = HingesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form_error = True
    return render(request, 'hinges.html', {'form': form,
                                           'hinges': all_hinges,
                                           'form_error': form_error})


class HingesUpdate(UpdateView):
    model = Hinge
    form_class = HingesForm
    template_name = 'update_hinge.html'
    success_url = reverse_lazy('hinges')


def remove_hinge(request, hinge_id):
    Hinge.objects.filter(id=hinge_id).delete()
    return redirect('hinges')


"""Engravings"""


def engravings(request):
    form = EngravingForm()
    form_error = None
    all_engravings = EngravingType.objects.all()
    if request.method == 'POST':
        form = EngravingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_error = True
    return render(request, 'engraving.html', {'form': form,
                                              'engravings': all_engravings,
                                              'form_error': form_error})


class EngravingUpdate(UpdateView):
    model = EngravingType
    form_class = EngravingForm
    template_name = 'update_engraving.html'
    success_url = reverse_lazy('engravings')


def remove_engraving(request, engraving_id):
    EngravingType.objects.filter(id=engraving_id).delete()
    return redirect('engravings')


"""Structure"""


def structure(request):
    form = StructureForm()
    form_error = None
    all_structures = Structure.objects.all()
    if request.method == 'POST':
        form = StructureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_error = True
    return render(request, 'structure.html', {'form': form,
                                              'structures': all_structures,
                                              'form_error': form_error})


class StructureUpdate(UpdateView):
    model = Structure
    form_class = StructureForm
    template_name = 'update_structure.html'
    success_url = reverse_lazy('structure')


def remove_structure(request, structure_id):
    Structure.objects.filter(id=structure_id).delete()
    return redirect('structure')


'''Orders'''


def new_order(request):
    form = OrderForm()
    form_error = None
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            order = Order.objects.filter(id=request.POST['id'])[0]
            doors_group = DoorsGroupInstance(order=order, door_type=order.door_type, engraving=order.engraving,
                                             lock=order.lock, hinges=order.hinges)
            doors_group.save()
            return redirect(show_order, order_id=order.id)
        else:
            print(form.errors)
            form_error = True
    return render(request, 'new_order.html', {'form': form, 'form_error': form_error})


def show_order(request, order_id):
    form_group = DoorsGroupInstanceForm()
    groups = DoorsGroupInstance.objects.filter(order=order_id)
    # print(*groups)
    doors = []
    for group in groups:
        for door in DoorInstance.objects.filter(group=group):
            doors.append(door)
    if doors:
        form = DoorInstanceForm(initial={
            'width': (doors[len(doors) - 1]).width,
            'height': (doors[len(doors) - 1]).height,
        })
    else:
        form = DoorInstanceForm()
    if request.method == 'POST':
        form = DoorInstanceForm(request.POST)
        if form.is_valid():
            new_door = form.save(commit=False)
            new_door.group = groups.last()
            new_door.number = len(doors) + 1
            new_door.save()
        else:
            print(form.errors)
        return redirect('show_order', order_id=order_id)
    else:
        return render(request, 'order.html', {'form': form, 'form_group': form_group,
                                              'groups': groups, 'doors': doors})


def add_door_group(request, order_id):
    form = DoorsGroupInstanceForm(request.POST)
    if form.is_valid():
        new_group = form.save(commit=False)
        new_group.order = Order.objects.filter(id=order_id)[0]
        print('valid')
        form.save()
    else:
        print('invalid')
        print(form.errors)
    return redirect('show_order', order_id=order_id)


def add_doors(request, order_id):
    form_error = None
    doors = DoorInstance.objects.get(order=order_id)
    form = DoorInstanceForm(request.POST)
    if request.method == 'POST':
        form = DoorInstanceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_doors', order_id=order_id)
    else:
        return render(request, 'order.html', {'engravings': EngravingType.objects.all(),
                                              'door_types': DoorType.objects.all(),
                                              'locks': Lock.objects.all(), 'hinges': Hinge.objects.all(),
                                              'doors': doors, 'form': form, 'form_error': form_error})


def search_order(request):
    if request.method == 'POST':
        return redirect('show_order', order_id=request.POST['search-field'])
    else:
        return redirect('index', request)


'''Reports'''


def report(request, order_id):
    order = Order.objects.get(id=order_id)
    doors = DoorInstance.objects.filter(order=order)
    doors_list = []
    panels_list = []
    structure2 = Structure.objects.filter(compatible_doors=order.door_type, compatible_engraving=order.engraving)[0]

    for door in doors:
        new_door = {'frame': door.frame.normalize(),
                    'width': door.width.normalize(),
                    'height': door.height.normalize(),
                    'amount_R': 1 if door.direction == 'R' else 0,
                    'amount_L': 1 if door.direction == 'L' else 0,
                    'door_type': door.door_type,
                    }
        for exist_door in doors_list:
            if kit_dimensions_compare(new_door, exist_door):
                if door.direction == 'R':
                    exist_door['amount_R'] += 1
                else:
                    exist_door['amount_L'] += 1
                break
        else:
            doors_list.append(new_door)
    for door in doors:
        new_door = {'width': (door.width + door.door_type.width_calculation).normalize(),
                    'height': (door.height + door.door_type.height_calculation).normalize(),
                    'amount_R': 1 if door.direction == 'R' else 0,
                    'amount_L': 1 if door.direction == 'L' else 0,
                    'door_type': door.door_type,
                    }
        for exist_door in panels_list:
            if kit_dimensions_compare(new_door, exist_door):
                if door.direction == 'R':
                    exist_door['amount_R'] += 1
                else:
                    exist_door['amount_L'] += 1
                break
        else:
            panels_list.append(new_door)
    return render(request, 'report.html', {'order': order,
                                           'doors': doors_list,
                                           'panels': panels_list,
                                           'structure2': structure2})


"""AJAX"""


def load_locks(request):
    door_type = request.GET.get('door_type')
    door_type = DoorType.objects.filter(id=door_type)[0]
    locks_list = Lock.objects.filter(compatible_doors=door_type)
    return render(request, 'locks_dropdown_list_options.html', {'locks': locks_list})


def load_hinges(request):
    door_type = request.GET.get('door_type')
    door_type = DoorType.objects.filter(id=door_type)[0]
    hinges_list = Hinge.objects.filter(compatible_doors=door_type)
    return render(request, 'hinges_dropdown_list_options.html', {'hinges': hinges_list})


def load_engraving(request):
    door_type = request.GET.get('door_type')
    door_type = DoorType.objects.filter(id=door_type)[0]
    engravings_list = EngravingType.objects.filter(compatible_doors=door_type)
    return render(request, 'engraving_dropdown_list_options.html', {'engravings': engravings_list})
