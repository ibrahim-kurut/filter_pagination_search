from .models import Path, Student

from faker import Faker


def run():
    fake = Faker(['tr-TR'])

    paths = (
        'FullStack developer',
        'Frontend developer',
        'Backend developer',
        'Mobile developer',
    )
    for path in paths:
        new_path = Path.objects.create(path_name=path)

        for _ in range(50):
             Student.objects.create(
                f_name=fake.first_name(),
                l_name=fake.last_name(),
                email=fake.email(),
                number=fake.pyint(),
                path=new_path
                )
            
        print("Bitti ............")
