import json
import pytest


class TestImage:
    @pytest.mark.run('first')
    def test_get_empty(self, client):
        response = client.get("/api/image/")
        data = json.loads(response.data)

        assert isinstance(data, list)
        assert len(data) == 0

    def test_post_no_data(self, client):
        response = client.post("/api/image/")
        assert response.status_code == 400

    def test_post_images(self, client):
        pass

    def test_post_images_invalid(self, client):
        pass


class TestImageId:
    def test_get_invalid_id(self, client):
        response = client.get("/api/image/1000")
        assert response.status_code == 400

    def test_delete_invalid_id(self, client):
        response = client.delete("/api/image/1000")
        assert response.status_code == 400


class TestImageCoco:
    def test_get_invalid_id(self, client):
        response = client.get("/api/image/1000/coco")
        assert response.status_code == 400


class TestImageThumbnail:
    def test_invalid_id(self, client):
        response = client.get("/api/image/1000/thumbnail")
        assert response.status_code == 400


