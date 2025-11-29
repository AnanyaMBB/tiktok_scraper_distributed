"""
Tests for fyp_scraper/fyp_scraper.py - TikTok For You Page Scraper.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from collections import OrderedDict

# Setup paths
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_root)  # Add project root for package imports
sys.path.insert(0, os.path.join(project_root, 'shared'))


def cleanup_modules():
    """Remove cached modules to allow fresh imports with mocks"""
    modules_to_remove = [k for k in list(sys.modules.keys()) 
                         if k.startswith(('fyp_scraper', 'storage', 'proxy', 'celery'))]
    for mod in modules_to_remove:
        try:
            del sys.modules[mod]
        except KeyError:
            pass


class TestTikTokFYPScraperInit:
    """Tests for TikTokFYPScraper initialization"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_scraper_init(self, mock_boto):
        """Test FYP scraper initializes correctly"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper
        
        scraper = TikTokFYPScraper(redis_client=mock_redis)
        
        assert scraper.redis_client == mock_redis
        assert scraper.output_dir == "tiktok_video_metadata"
        assert scraper.cookies is None
        assert scraper.headers is None
        assert scraper.api_params == {}
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_scraper_init_custom_output(self, mock_boto):
        """Test FYP scraper with custom output directory"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper
        
        scraper = TikTokFYPScraper(redis_client=mock_redis, output_dir="custom_dir")
        
        assert scraper.output_dir == "custom_dir"


class TestGetCookiesAndHeaders:
    """Tests for get_cookies and get_headers methods"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_get_cookies_not_initialized(self, mock_boto):
        """Test get_cookies raises exception when not initialized"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper
        
        scraper = TikTokFYPScraper(redis_client=mock_redis)
        
        with pytest.raises(Exception) as exc_info:
            scraper.get_cookies()
        
        assert "not initialized" in str(exc_info.value)
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_get_headers_not_initialized(self, mock_boto):
        """Test get_headers raises exception when not initialized"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper
        
        scraper = TikTokFYPScraper(redis_client=mock_redis)
        
        with pytest.raises(Exception) as exc_info:
            scraper.get_headers()
        
        assert "not initialized" in str(exc_info.value)
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_get_cookies_after_init(self, mock_boto):
        """Test get_cookies returns cookies after initialization"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper
        
        scraper = TikTokFYPScraper(redis_client=mock_redis)
        scraper.cookies = {"tt_webid_v2": "test_value"}
        
        cookies = scraper.get_cookies()
        
        assert cookies == {"tt_webid_v2": "test_value"}


class TestBuildApiUrl:
    """Tests for build_api_url method"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_build_api_url_not_initialized(self, mock_boto):
        """Test build_api_url raises exception when params not initialized"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper
        
        scraper = TikTokFYPScraper(redis_client=mock_redis)
        
        with pytest.raises(Exception) as exc_info:
            scraper.build_api_url()
        
        assert "not initialized" in str(exc_info.value)
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_build_api_url_contains_base_url(self, mock_boto):
        """Test build_api_url returns correct base URL"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper
        
        scraper = TikTokFYPScraper(redis_client=mock_redis)
        scraper.api_params_items = [
            ("count", "6"),
            ("device_id", "123456"),
            ("msToken", "test_token"),
        ]
        
        url = scraper.build_api_url()
        
        assert url.startswith("https://www.tiktok.com/api/recommend/item_list/")


class TestProcessAccounts:
    """Tests for process_accounts method"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_process_accounts_queues_new_users(self, mock_boto):
        """Test process_accounts queues new users for scraping"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.sismember.return_value = False
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper, celery_app
        
        with patch.object(celery_app, 'send_task') as mock_send_task:
            scraper = TikTokFYPScraper(redis_client=mock_redis)
            
            items = [
                {"author": {"uniqueId": "newuser1"}},
                {"author": {"uniqueId": "newuser2"}},
            ]
            
            scraper.process_accounts(items)
            
            assert mock_send_task.call_count == 2
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_process_accounts_skips_scraped_users(self, mock_boto):
        """Test process_accounts skips already scraped users"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.sismember.return_value = True  # Already scraped
        
        from fyp_scraper.fyp_scraper import TikTokFYPScraper, celery_app
        
        with patch.object(celery_app, 'send_task') as mock_send_task:
            scraper = TikTokFYPScraper(redis_client=mock_redis)
            
            items = [
                {"author": {"uniqueId": "user1"}},
            ]
            
            scraper.process_accounts(items)
            
            mock_send_task.assert_not_called()
