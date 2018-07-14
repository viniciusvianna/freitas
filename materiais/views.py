from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Material
from .forms import MaterialForm

@login_required
def materials_list(request):
	materials = Material.objects.all()
	return render(request, 'materials.html', {'materials' : materials})

@login_required
def new_material(request):
	form = MaterialForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		form.save()
		result = redirect('materials_list')
	else:
		result = render(request, 'material_form.html', {'form': form})

	return result

@login_required
def update_material(request, id):
	material = get_object_or_404(Material, pk=id)
	form = MaterialForm(request.POST or None, request.FILES or None, instance=material)

	if form.is_valid():
		form.save()
		result = redirect('materials_list')
	else:
		result = render(request, 'material_form.html', {'form': form})

	return result

@login_required
def delete_material(request, id):
	material = get_object_or_404(Material, pk=id)
	
	if request.method == 'POST':
		material.delete()
		result = redirect('materials_list')
	else:
		result = render(request, 'material_delete_confirm.html', {'material': material})

	return result

