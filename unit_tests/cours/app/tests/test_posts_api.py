from typing import Callable

from starlette.testclient import TestClient

import schemas
from models import Post


def test_get_posts(client: TestClient, db, post_factory: Callable[..., Post]):
    first_post = post_factory()
    response = client.get("/posts/")

    actual = db.query(Post).all()

    assert response.status_code == 200
    assert len(actual) == 1

    actual_post = actual[0]

    assert first_post.id == actual_post.id
    assert first_post.title == actual_post.title
    assert first_post.description == actual_post.description

def test_create_posts(client: TestClient, db):
    first_post = schemas.Post(
        title="title",
        description="description"
    )
    response = client.post("/posts/", json=first_post.dict())

    actual = db.query(Post).all()

    assert response.status_code == 200
    assert len(actual) == 1

    actual_post = actual[0]

    assert actual_post.id
    assert first_post.title == actual_post.title
    assert first_post.description == actual_post.description

    db.delete(actual_post)

def test_update_posts(client: TestClient, db, post_factory: Callable[..., Post]):
    first_post = post_factory()
    change_title_payload = schemas.Post(
        title="new title"
    )

    response = client.patch("/posts/", json=change_title_payload.dict())

    actual = db.query(Post).all()

    assert response.status_code == 200
    assert len(actual) == 1

    actual_post = actual[0]

    assert actual_post.id
    assert first_post.title == actual_post.title
    assert first_post.description == actual_post.description

    db.delete(actual_post)
