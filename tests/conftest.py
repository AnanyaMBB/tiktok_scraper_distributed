"""
Shared test fixtures and configuration for all tests.
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import MagicMock

# Add project paths for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))  # Add project root for package imports
sys.path.insert(0, str(project_root / 'shared'))
sys.path.insert(0, str(project_root / 'profile_scraper'))


# ============================================================================
# Redis Fixtures
# ============================================================================

@pytest.fixture
def mock_redis_client():
    """Create a mock Redis client"""
    mock = MagicMock()
    mock.sismember.return_value = False
    mock.sadd.return_value = 1
    mock.srem.return_value = 1
    mock.set.return_value = True
    mock.get.return_value = None
    mock.delete.return_value = 1
    mock.scard.return_value = 0
    mock.keys.return_value = []
    return mock


@pytest.fixture
def mock_redis_with_data():
    """Create a mock Redis client with some pre-existing data"""
    mock = MagicMock()
    
    # Simulate some usernames already scraped
    scraped_usernames = {"user1", "user2", "user3"}
    downloaded_videos = {"video1", "video2"}
    download_queue = {"video3", "video4"}
    
    def sismember_side_effect(key, value):
        if key == "scraped_usernames":
            return value in scraped_usernames
        elif key == "downloaded_videos":
            return value in downloaded_videos
        elif key == "download_queue":
            return value in download_queue
        return False
    
    mock.sismember.side_effect = sismember_side_effect
    mock.scard.return_value = len(scraped_usernames)
    mock.sadd.return_value = 1
    mock.srem.return_value = 1
    
    return mock


# ============================================================================
# S3/Spaces Client Fixtures
# ============================================================================

@pytest.fixture
def mock_s3_client():
    """Create a mock S3/Spaces client"""
    mock = MagicMock()
    mock.upload_file.return_value = None
    mock.head_object.return_value = {'ContentLength': 1000}
    mock.delete_object.return_value = {}
    
    # Mock paginator for list operations
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
    mock.get_paginator.return_value = mock_paginator
    
    return mock


# ============================================================================
# Sample Data Fixtures
# ============================================================================

@pytest.fixture
def sample_video_metadata():
    """Sample TikTok video metadata"""
    return {
        "id": "7500419371345431851",
        "desc": "Test video description #fyp #viral",
        "createTime": 1699900000,
        "author": {
            "id": "123456789",
            "uniqueId": "testuser",
            "nickname": "Test User",
            "verified": False,
            "secUid": "MS4wLjABAAAAtest"
        },
        "stats": {
            "playCount": 100000,
            "diggCount": 5000,
            "shareCount": 500,
            "commentCount": 200
        },
        "video": {
            "id": "7500419371345431851",
            "duration": 30,
            "ratio": "720p",
            "playAddr": "https://example.com/video.mp4",
            "downloadAddr": "https://example.com/video_download.mp4"
        },
        "music": {
            "id": "987654321",
            "title": "Original Sound",
            "authorName": "testuser"
        }
    }


@pytest.fixture
def sample_fyp_response():
    """Sample FYP API response"""
    return {
        "itemList": [
            {
                "id": "video1",
                "author": {"uniqueId": "user1", "id": "111"},
                "desc": "Video 1"
            },
            {
                "id": "video2",
                "author": {"uniqueId": "user2", "id": "222"},
                "desc": "Video 2"
            },
        ],
        "hasMore": True,
        "cursor": "123456789"
    }


# ============================================================================
# Mock Browser/Playwright Fixtures
# ============================================================================

@pytest.fixture
def mock_playwright_page():
    """Create a mock Playwright page"""
    mock_page = MagicMock()
    mock_page.goto.return_value = None
    mock_page.evaluate.return_value = None
    mock_page.query_selector.return_value = None
    mock_page.viewport_size = {'width': 1920, 'height': 1080}
    mock_page.mouse = MagicMock()
    return mock_page


# ============================================================================
# Temporary File Fixtures
# ============================================================================

@pytest.fixture
def temp_json_file(tmp_path):
    """Create a temporary JSON file for testing uploads"""
    import json
    file_path = tmp_path / "test_video.json"
    file_path.write_text(json.dumps({"id": "test123", "desc": "test"}))
    return str(file_path)


@pytest.fixture
def temp_video_file(tmp_path):
    """Create a temporary video file for testing"""
    file_path = tmp_path / "test_video.mp4"
    file_path.write_bytes(b'\x00' * 1024)  # 1KB dummy file
    return str(file_path)
