import unittest
import sys
import os

# Add src to path so we can import app
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import app, PROJECTS, DOC_TYPES

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home(self):
        """Test the home page."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dark Work, LLC', response.data)

    def test_static_logo(self):
        """Test that the static logo image is accessible."""
        response = self.client.get('/static/images/dark_work_logo.svg')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<svg', response.data)
        response.close()

    def test_project_pages(self):
        """Test each project page."""
        for project in PROJECTS:
            with self.subTest(project=project):
                response = self.client.get(f'/{project}')
                self.assertEqual(response.status_code, 200, f"Project page {project} failed")
                self.assertIn(project.encode(), response.data.lower() if project != 'zombieTim' else b'zombie')

    def test_document_pages(self):
        """Test each document page for each project."""
        for project in PROJECTS:
            for doc_type in DOC_TYPES:
                with self.subTest(project=project, doc_type=doc_type):
                    response = self.client.get(f'/{project}/{doc_type}')
                    self.assertEqual(response.status_code, 200, f"Document {doc_type} for project {project} failed")

    def test_404_pages(self):
        """Test 404 for non-existent projects/docs."""
        response = self.client.get('/invalid_project')
        self.assertEqual(response.status_code, 404)
        
        response = self.client.get('/dumb_phone/invalid_doc')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
