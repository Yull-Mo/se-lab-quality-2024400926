# test_app.py（单元测试）
import pytest
from app import app
def test_index():
    res = app.test_client().get('/')
    assert res.status_code == 200
