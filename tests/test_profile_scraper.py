"""
Tests for profile_scraper/profile_scraper_v5.py - TikTok Profile Scraper.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Setup paths
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(project_root, 'shared'))
sys.path.insert(0, os.path.join(project_root, 'profile_scraper'))


def cleanup_modules():
    """Remove cached modules to allow fresh imports with mocks"""
    modules_to_remove = [k for k in sys.modules.keys() 
                         if k.startswith(('profile_scraper', 'storage', 'proxy', 'celery'))]
    for mod in modules_to_remove:
        del sys.modules[mod]


class TestBotDetectionError:
    """Tests for BotDetectionError exception"""
    
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
    def test_bot_detection_error_can_be_raised(self, mock_redis, mock_boto):
        """Test BotDetectionError can be raised and caught"""
        cleanup_modules()
        
        from profile_scraper_v5 import BotDetectionError
        
        with pytest.raises(BotDetectionError) as exc_info:
            raise BotDetectionError("No API responses intercepted")
        
        assert "No API responses" in str(exc_info.value)
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_bot_detection_error_is_exception(self, mock_boto):
        """Test BotDetectionError is an Exception subclass"""
        cleanup_modules()
        
        from profile_scraper_v5 import BotDetectionError
        
        assert issubclass(BotDetectionError, Exception)


class TestTikTokProfileScraperInit:
    """Tests for TikTokProfileScraper initialization"""
    
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
    def test_scraper_init_defaults(self, mock_redis, mock_boto):
        """Test scraper initializes with default values"""
        cleanup_modules()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper()
        
        assert scraper.output_dir == "tiktok_videos"
        assert scraper.headless is False
        assert scraper.proxy_config is None
        assert scraper.redis_client is None
        assert scraper.queue_downloads is True
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_scraper_init_custom_values(self, mock_boto):
        """Test scraper initializes with custom values"""
        cleanup_modules()
        
        mock_redis_client = MagicMock()
        proxy_config = {"server": "http://proxy:8080"}
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper(
            output_dir="custom_output",
            headless=True,
            proxy_config=proxy_config,
            redis_client=mock_redis_client,
            queue_downloads=False
        )
        
        assert scraper.output_dir == "custom_output"
        assert scraper.headless is True
        assert scraper.proxy_config == proxy_config
        assert scraper.redis_client == mock_redis_client
        assert scraper.queue_downloads is False


class TestGetSpacesKey:
    """Tests for _get_spaces_key method"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_get_spaces_key_format(self, mock_boto):
        """Test _get_spaces_key returns correct format"""
        cleanup_modules()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper()
        key = scraper._get_spaces_key("nike", "12345")
        
        assert key == "tiktok_video_metadata/nike/12345.json"
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_get_spaces_key_with_special_username(self, mock_boto):
        """Test _get_spaces_key with special characters in username"""
        cleanup_modules()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper()
        key = scraper._get_spaces_key("user_name.test", "7500419371345431851")
        
        assert key == "tiktok_video_metadata/user_name.test/7500419371345431851.json"


class TestQueueVideoForDownload:
    """Tests for queue_video_for_download method"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_queue_video_no_redis(self, mock_boto, sample_video_metadata):
        """Test queue_video_for_download returns False without redis client"""
        cleanup_modules()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper(redis_client=None, queue_downloads=True)
        result = scraper.queue_video_for_download(sample_video_metadata, "testuser")
        
        assert result is False
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_queue_video_downloads_disabled(self, mock_boto, sample_video_metadata):
        """Test queue_video_for_download returns False when downloads disabled"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper(redis_client=mock_redis, queue_downloads=False)
        result = scraper.queue_video_for_download(sample_video_metadata, "testuser")
        
        assert result is False
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_queue_video_no_id(self, mock_boto):
        """Test queue_video_for_download returns False when video has no ID"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper(redis_client=mock_redis, queue_downloads=True)
        result = scraper.queue_video_for_download({"desc": "No ID"}, "testuser")
        
        assert result is False
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_queue_video_already_downloaded(self, mock_boto, sample_video_metadata):
        """Test queue_video_for_download skips already downloaded videos"""
        cleanup_modules()
        
        mock_redis = MagicMock()
        mock_redis.sismember.return_value = True  # Already downloaded
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper(redis_client=mock_redis, queue_downloads=True)
        result = scraper.queue_video_for_download(sample_video_metadata, "testuser")
        
        assert result is False


class TestHumanBehavior:
    """Tests for HumanBehavior class"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    @patch('time.sleep')
    def test_random_delay_executes(self, mock_sleep, mock_boto):
        """Test random_delay executes without error"""
        cleanup_modules()
        
        from profile_scraper_v5 import HumanBehavior
        
        HumanBehavior.random_delay(1, 2)
        mock_sleep.assert_called_once()
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_smooth_scroll_calls_evaluate(self, mock_boto, mock_playwright_page):
        """Test smooth_scroll calls page.evaluate"""
        cleanup_modules()
        
        from profile_scraper_v5 import HumanBehavior
        
        HumanBehavior.smooth_scroll(mock_playwright_page, 500)
        
        mock_playwright_page.evaluate.assert_called_once()


class TestBrowserArgs:
    """Tests for _get_browser_args method"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_browser_args_headed_mode(self, mock_boto):
        """Test browser args for headed mode"""
        cleanup_modules()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper(headless=False)
        args = scraper._get_browser_args()
        
        assert "--disable-blink-features=AutomationControlled" in args
        assert "--headless=new" not in args
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
    })
    @patch('boto3.session.Session')
    def test_browser_args_headless_mode(self, mock_boto):
        """Test browser args for headless mode"""
        cleanup_modules()
        
        from profile_scraper_v5 import TikTokProfileScraper
        
        scraper = TikTokProfileScraper(headless=True)
        args = scraper._get_browser_args()
        
        assert "--headless=new" in args
        assert "--disable-gpu" in args
        assert "--mute-audio" in args
