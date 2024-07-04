from django.shortcuts import render # type: ignore
from app1.models import contact_information

def main(request):

    #Создание
    #new_user=contact_information(username='maksim', email='dfjwuiqwe@mail.ru', number='83283481238')
    #new_user.save()

    #Чтение
    users = contact_information.objects.all()
    #email_information = contact_information.objects.filter()
    #for i in users:
       # print(f'Пользователь: {i.username}, Почта: {i.email}, Номер: {i.number}')

    #Изменение
    #change_link = contact_information.objects.get(email='dfjwuiqwe@mail.ru')
    #change_link.username='dima'
    #change_link.save()

    #Удаление
    #contact_information.objects.get(username="dima").delete()

    return render(request, 'main.html', {"data":users})
