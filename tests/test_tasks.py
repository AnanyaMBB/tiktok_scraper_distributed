"""
Tests for profile_scraper/tasks.py - Celery Tasks for Profile Scraping.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from datetime import datetime

# Setup paths
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(project_root, 'shared'))
sys.path.insert(0, os.path.join(project_root, 'profile_scraper'))


def cleanup_modules():
    """Remove cached modules to allow fresh imports with mocks"""
    modules_to_remove = [k for k in sys.modules.keys() 
                         if k.startswith(('tasks', 'profile_scraper', 'storage', 'proxy', 'celery'))]
    for mod in modules_to_remove:
        del sys.modules[mod]


class TestGetScrapeStats:
    """Tests for get_scrape_stats task - simple test that doesn't require complex mocking"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('redis.Redis')
    def test_get_scrape_stats(self, mock_redis_class, mock_boto):
        """Test get_scrape_stats returns correct stats"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.scard.return_value = 100
        mock_redis.keys.return_value = ["scraping:user1", "scraping:user2"]
        mock_redis_class.return_value = mock_redis
        
        from tasks import get_scrape_stats, redis_client
        
        # Patch the module-level redis_client
        with patch('tasks.redis_client', mock_redis):
            result = get_scrape_stats()
            
            assert result["total_usernames_scraped"] == 100
            assert result["currently_scraping"] == 2


class TestClearUserHistory:
    """Tests for clear_user_history task"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('redis.Redis')
    def test_clear_user_history(self, mock_redis_class, mock_boto):
        """Test clear_user_history removes user from scraped set"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis_class.return_value = mock_redis
        
        from tasks import clear_user_history
        
        with patch('tasks.redis_client', mock_redis):
            result = clear_user_history("testuser")
            
            assert result["cleared"] == "testuser"
            mock_redis.srem.assert_called_once_with("scraped_usernames", "testuser")


class TestScrapeProfileTaskBasics:
    """Basic tests for scrape_profile task structure"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('redis.Redis')
    def test_scrape_profile_skips_already_scraped(self, mock_redis_class, mock_boto):
        """Test task skips already scraped usernames"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.sismember.return_value = True  # Already scraped
        mock_redis_class.return_value = mock_redis
        
        from tasks import scrape_profile
        
        # Create mock task
        task = MagicMock()
        task.request.id = "test-task-id"
        
        with patch('tasks.redis_client', mock_redis):
            result = scrape_profile(task, "already_scraped_user")
            
            assert result["skipped"] is True
            assert result["success"] is True
            assert result["reason"] == "Already scraped"
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('redis.Redis')
    def test_scrape_profile_skips_in_progress(self, mock_redis_class, mock_boto):
        """Test task skips username being scraped by another worker"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.sismember.return_value = False
        mock_redis.set.return_value = False  # Lock already held
        mock_redis_class.return_value = mock_redis
        
        from tasks import scrape_profile
        
        task = MagicMock()
        task.request.id = "test-task-id"
        
        with patch('tasks.redis_client', mock_redis):
            result = scrape_profile(task, "in_progress_user")
            
            assert result["skipped"] is True
            assert result["success"] is True
            assert result["reason"] == "Already in progress"


class TestTaskResultFormat:
    """Tests for task result format"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('redis.Redis')
    def test_result_contains_required_fields(self, mock_redis_class, mock_boto):
        """Test task result contains all required fields"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.sismember.return_value = True  # Skip for simplicity
        mock_redis_class.return_value = mock_redis
        
        from tasks import scrape_profile
        
        task = MagicMock()
        task.request.id = "test-task-id"
        
        with patch('tasks.redis_client', mock_redis):
            result = scrape_profile(task, "testuser")
            
            # Check required fields exist
            assert "username" in result
            assert "task_id" in result
            assert "success" in result
            assert "videos_saved" in result
            assert "skipped" in result
            assert "error" in result
            assert "started_at" in result
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('redis.Redis')
    def test_result_timestamps_are_iso_format(self, mock_redis_class, mock_boto):
        """Test task result timestamps are in ISO format"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.sismember.return_value = True  # Skip for simplicity
        mock_redis_class.return_value = mock_redis
        
        from tasks import scrape_profile
        
        task = MagicMock()
        task.request.id = "test-task-id"
        
        with patch('tasks.redis_client', mock_redis):
            result = scrape_profile(task, "testuser")
            
            # Should be able to parse as ISO datetime
            datetime.fromisoformat(result["started_at"])
