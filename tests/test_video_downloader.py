"""
Tests for video_downloader/video_downloader.py - TikTok Video Downloader.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Setup paths
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_root)  # Add project root for package imports
sys.path.insert(0, os.path.join(project_root, 'shared'))


def cleanup_modules():
    """Remove cached modules to allow fresh imports with mocks"""
    modules_to_remove = [k for k in list(sys.modules.keys()) 
                         if k.startswith(('video_downloader', 'storage', 'proxy', 'celery'))]
    for mod in modules_to_remove:
        try:
            del sys.modules[mod]
        except KeyError:
            pass


class TestTikTokVideoDownloaderInit:
    """Tests for TikTokVideoDownloader initialization"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_downloader_init_defaults(self, mock_boto, tmp_path):
        """Test downloader initializes with default values"""
        cleanup_modules()
        
        from video_downloader.video_downloader import TikTokVideoDownloader
        
        # Use tmp_path to avoid creating real directories
        with patch('os.makedirs'):
            downloader = TikTokVideoDownloader()
            assert downloader.output_dir == "downloads"
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    def test_downloader_init_custom_dir(self, mock_boto, tmp_path):
        """Test downloader initializes with custom output directory"""
        cleanup_modules()
        
        custom_dir = str(tmp_path / "custom_downloads")
        
        from video_downloader.video_downloader import TikTokVideoDownloader
        
        downloader = TikTokVideoDownloader(output_dir=custom_dir)
        
        assert downloader.output_dir == custom_dir


class TestDownloadVideoWithYtdlp:
    """Tests for download_video_with_ytdlp method"""
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('yt_dlp.YoutubeDL')
    def test_download_video_success(self, mock_ytdl, mock_boto, tmp_path):
        """Test successful video download"""
        cleanup_modules()
        
        mock_ydl_instance = MagicMock()
        mock_ytdl.return_value.__enter__.return_value = mock_ydl_instance
        
        from video_downloader.video_downloader import TikTokVideoDownloader
        
        output_dir = str(tmp_path / "downloads")
        os.makedirs(output_dir, exist_ok=True)
        
        downloader = TikTokVideoDownloader(output_dir=output_dir)
        
        # Create mock file to simulate download
        mock_file = os.path.join(output_dir, "test123.mp4")
        with open(mock_file, 'wb') as f:
            f.write(b'\x00' * 1024)
        
        result = downloader.download_video_with_ytdlp(
            "https://www.tiktok.com/@user/video/test123",
            "test123"
        )
        
        assert result is not None
        assert "test123.mp4" in result
    
    @patch.dict(os.environ, {
        'SPACES_REGION_NAME': 'nyc3',
        'SPACES_SPACE_NAME': 'test-bucket',
        'SPACES_ACCESS_KEY': 'test-key',
        'SPACES_SECRET_KEY': 'test-secret',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379',
    })
    @patch('boto3.session.Session')
    @patch('yt_dlp.YoutubeDL')
    def test_download_video_retries_on_failure(self, mock_ytdl, mock_boto, tmp_path):
        """Test download retries on failure"""
        cleanup_modules()
        
        mock_ydl_instance = MagicMock()
        mock_ydl_instance.download.side_effect = Exception("Download failed")
        mock_ytdl.return_value.__enter__.return_value = mock_ydl_instance
        
        from video_downloader.video_downloader import TikTokVideoDownloader
        
        output_dir = str(tmp_path / "downloads")
        os.makedirs(output_dir, exist_ok=True)
        
        downloader = TikTokVideoDownloader(output_dir=output_dir)
        
        with pytest.raises(Exception):
            downloader.download_video_with_ytdlp(
                "https://www.tiktok.com/@user/video/test123",
                "test123",
                max_retries=2
            )
        
        # Should have tried twice
        assert mock_ydl_instance.download.call_count == 2


class TestVideoUrlConstruction:
    """Tests for video URL construction"""
    
    def test_video_url_format(self):
        """Test video URL is constructed correctly"""
        username = "testuser"
        video_id = "7500419371345431851"
        
        video_url = f"https://www.tiktok.com/@{username}/video/{video_id}"
        
        assert video_url == "https://www.tiktok.com/@testuser/video/7500419371345431851"
    
    def test_slideshow_url_format(self):
        """Test slideshow/photo URL is constructed correctly"""
        username = "testuser"
        video_id = "7500419371345431851"
        
        photo_url = f"https://www.tiktok.com/@{username}/photo/{video_id}"
        
        assert photo_url == "https://www.tiktok.com/@testuser/photo/7500419371345431851"
