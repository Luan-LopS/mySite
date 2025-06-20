import factory
from faker import Factory as FakerFactory
from blog.models import Post
from django.contrib.auth.models import User
from django.utils.timezone import now

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('safe_email')
    username = factory.LazyAttribute(lambda x: faker.user_name())

    @classmethod
    def __prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls).__prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()

        return user


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda obj: faker.sentence())
    created_on = factory.LazyFunction(now)
    author = factory.SubFactory(UserFactory)
    status = 0

    class Meta:
        model = Post
