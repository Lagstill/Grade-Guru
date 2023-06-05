from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import pytest

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Welcome to Grade Guru</h1>' in response.data
