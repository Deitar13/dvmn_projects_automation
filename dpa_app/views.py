from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from .forms import ChooseTimeForm
from .models import Student


def show_time_slots(request, user_id):
    if request.method == 'POST':
        form = ChooseTimeForm(request.POST)
        if form.is_valid():
            # Полученные из таблицы данные
            print(form.cleaned_data.get('best_time_slots')) # удобные временные слоты
            print(form.cleaned_data.get('ok_time_slots'))  # возможные слоты
            print(form.data.getlist('best_time_slots'))  # id удобных слотов
            print(form.data.getlist('ok_time_slots'))  # id возможных слотов
            print(form.data.get('user_id'))  # user_id из адреса

            return HttpResponseRedirect('/thanks/')
    try:
        student = Student.objects.get(tg_id=user_id)
    except Student.DoesNotExist:
        raise Http404('Page Not Found')
    else:
        form = ChooseTimeForm()
        return render(request, 'choose_time.html',
                      context={
                          'user_id': user_id,
                          'form': form,
                          'name': student.name
                      })


def show_thanks(request):
    return HttpResponse('Мы постараемся учесть твои пожелания =)')