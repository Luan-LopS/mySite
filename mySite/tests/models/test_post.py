import pytest
from blog.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_crate_published_post(post_published):
    assert post_published.title == 'pytest with factory'
