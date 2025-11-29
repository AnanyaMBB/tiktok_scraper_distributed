"""
Tests for shared/storage.py - Digital Ocean Spaces storage operations.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Setup path before any imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))


class TestUploadFile:
    """Tests for upload_file function"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_upload_file_success(self, mock_session, temp_json_file):
        """Test successful file upload"""
        mock_client = MagicMock()
        mock_session.return_value.client.return_value = mock_client
        
        # Force reimport with mocked session
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import upload_file
        
        result = upload_file(temp_json_file, "test/path.json")
        
        assert result is True
        mock_client.upload_file.assert_called_once()
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_upload_file_with_skip_existing_skips_when_exists(self, mock_session, temp_json_file):
        """Test upload skipped when file exists and skip_existing=True"""
        mock_client = MagicMock()
        mock_client.head_object.return_value = {'ContentLength': 100}  # File exists
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import upload_file
        
        result = upload_file(temp_json_file, "test/path.json", skip_existing=True)
        
        assert result is False  # Skipped
        mock_client.upload_file.assert_not_called()
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_upload_file_handles_exception(self, mock_session, temp_json_file):
        """Test upload handles exceptions gracefully"""
        mock_client = MagicMock()
        mock_client.upload_file.side_effect = Exception("Upload error")
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import upload_file
        
        result = upload_file(temp_json_file, "test/path.json")
        
        assert result is False


class TestFileExists:
    """Tests for file_exists function"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_file_exists_returns_true(self, mock_session):
        """Test file_exists returns True when file exists"""
        mock_client = MagicMock()
        mock_client.head_object.return_value = {'ContentLength': 100}
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import file_exists
        
        result = file_exists("test/path.json")
        
        assert result is True
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_file_exists_returns_false(self, mock_session):
        """Test file_exists returns False when file doesn't exist"""
        from botocore.exceptions import ClientError
        
        mock_client = MagicMock()
        mock_client.head_object.side_effect = ClientError(
            {'Error': {'Code': '404'}}, 'HeadObject'
        )
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import file_exists
        
        result = file_exists("nonexistent/path.json")
        
        assert result is False


class TestListFileIds:
    """Tests for list_file_ids function"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_list_file_ids_extracts_ids(self, mock_session):
        """Test list_file_ids extracts IDs from filenames"""
        mock_client = MagicMock()
        mock_paginator = MagicMock()
        mock_paginator.paginate.return_value = [
            {
                'Contents': [
                    {'Key': 'tiktok_video_metadata/testuser/123.json'},
                    {'Key': 'tiktok_video_metadata/testuser/456.json'},
                    {'Key': 'tiktok_video_metadata/testuser/789.json'},
                ]
            }
        ]
        mock_client.get_paginator.return_value = mock_paginator
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import list_file_ids
        
        result = list_file_ids("tiktok_video_metadata/testuser/", extension=".json")
        
        assert isinstance(result, set)
        assert len(result) == 3
        assert "123" in result
        assert "456" in result
        assert "789" in result
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_list_file_ids_empty_result(self, mock_session):
        """Test list_file_ids returns empty set when no files"""
        mock_client = MagicMock()
        mock_paginator = MagicMock()
        mock_paginator.paginate.return_value = [{'Contents': []}]
        mock_client.get_paginator.return_value = mock_paginator
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import list_file_ids
        
        result = list_file_ids("empty/prefix/")
        
        assert result == set()


class TestDeleteFile:
    """Tests for delete_file function"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_delete_file_success(self, mock_session):
        """Test successful file deletion"""
        mock_client = MagicMock()
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import delete_file
        
        result = delete_file("test/path.json")
        
        assert result is True
        mock_client.delete_object.assert_called_once()
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret'
    })
    @patch('boto3.session.Session')
    def test_delete_file_handles_exception(self, mock_session):
        """Test delete_file handles exceptions gracefully"""
        mock_client = MagicMock()
        mock_client.delete_object.side_effect = Exception("Delete error")
        mock_session.return_value.client.return_value = mock_client
        
        if 'storage' in sys.modules:
            del sys.modules['storage']
        
        from storage import delete_file
        
        result = delete_file("test/path.json")
        
        assert result is False
