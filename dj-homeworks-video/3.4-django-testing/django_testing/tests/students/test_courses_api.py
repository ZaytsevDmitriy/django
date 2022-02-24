import pytest
from django.urls import reverse
from students.models import Course


# Получение списка курсов
@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)

    url = reverse('courses-list')
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


# Получение одного курса
@pytest.mark.django_db
def test_get_one_course(client, course_factory):
    courses = course_factory(_quantity=10)
    first_course = courses[0]

    url = reverse('courses-detail', args=[first_course.id])
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == first_course.name


# Фильтрация курсов по ID
@pytest.mark.django_db
def test_get_id_filter_course(client, course_factory):
    courses = course_factory(_quantity=10)
    first_course = courses[0]

    url = reverse('courses-list')
    response = client.get(url, {'id': first_course.id})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == first_course.id


# Фильтрация курсов по name
@pytest.mark.django_db
def test_get_filter_course(client, course_factory):
    courses = course_factory(_quantity=10)
    first_course = courses[0]

    url = reverse('courses-list')
    response = client.get(url, {'name': first_course.name})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == first_course.name


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    url = reverse('courses-list')
    data = {'name': 'some course', 'students': []}
    response = client.post(url, data)

    assert response.status_code == 201
    data = response.json()
    assert Course.objects.get(id=data['id']).name == 'some course'


# Тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    update_course = Course.objects.first()

    url = reverse('courses-detail', args=[update_course.id])
    data = {'name': 'some course'}
    response = client.patch(url, data)

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'some course'


# Тест успешного удаления  курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_factory(_quantity=5)
    update_course = Course.objects.first()

    url = reverse("courses-detail", args=(update_course.id,))
    response = client.delete(url)

    assert response.status_code == 204
