"""
Tests for shared/proxy.py - Proxy management system.
"""

import pytest
import sys
import os
from unittest.mock import patch

# Setup path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))


class TestProxyManager:
    """Tests for ProxyManager class"""
    
    @patch.dict(os.environ, {
        'DATACENTER_PROXY_HOST': 'proxy.example.com',
        'DATACENTER_PROXY_PORT': '8080',
        'DATACENTER_PROXY_USERNAME': 'proxyuser',
        'DATACENTER_PROXY_PASSWORD': 'proxypass',
        'ROTATING_PROXY_HOST': '127.0.0.1',
        'ROTATING_PROXY_PORT': '3128',
    })
    def test_proxy_manager_initialization(self):
        """Test ProxyManager initializes with environment variables"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        
        assert manager.datacenter_host == "proxy.example.com"
        assert manager.datacenter_port == "8080"
        assert manager.datacenter_username == "proxyuser"
        assert manager.datacenter_password == "proxypass"
    
    @patch.dict(os.environ, {
        'DATACENTER_PROXY_HOST': 'proxy.example.com',
        'DATACENTER_PROXY_PORT': '8080',
    }, clear=False)
    def test_get_proxy_config_none(self):
        """Test get_proxy_config returns None for PROXY_TYPE_NONE"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        config = manager.get_proxy_config(ProxyManager.PROXY_TYPE_NONE)
        
        assert config is None
    
    @patch.dict(os.environ, {
        'DATACENTER_PROXY_HOST': 'proxy.example.com',
        'DATACENTER_PROXY_PORT': '8080',
        'DATACENTER_PROXY_USERNAME': 'proxyuser',
        'DATACENTER_PROXY_PASSWORD': 'proxypass',
    })
    def test_get_proxy_config_datacenter(self):
        """Test get_proxy_config returns correct format for datacenter proxy"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        config = manager.get_proxy_config(ProxyManager.PROXY_TYPE_DATACENTER)
        
        assert config is not None
        assert "http" in config
        assert "https" in config
        assert "proxyuser:proxypass@proxy.example.com:8080" in config["http"]
    
    def test_get_proxy_config_datacenter_without_auth(self):
        """Test datacenter proxy without authentication"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        # Override the loaded values directly
        manager.datacenter_host = "proxy.noauth.com"
        manager.datacenter_port = "3128"
        manager.datacenter_username = None
        manager.datacenter_password = None
        
        config = manager._get_datacenter_proxy()
        
        assert config is not None
        assert "http://proxy.noauth.com:3128" == config["http"]
        assert "@" not in config["http"]
    
    def test_get_proxy_config_datacenter_not_configured(self):
        """Test datacenter proxy returns None when not configured"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        # Override to simulate no config
        manager.datacenter_host = None
        manager.datacenter_port = None
        
        config = manager._get_datacenter_proxy()
        
        assert config is None
    
    @patch.dict(os.environ, {
        'ROTATING_PROXY_HOST': '127.0.0.1',
        'ROTATING_PROXY_PORT': '3128',
    })
    def test_get_proxy_config_rotating(self):
        """Test get_proxy_config for rotating proxy (Tor)"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        config = manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)
        
        assert config is not None
        assert "http" in config
        assert "127.0.0.1:3128" in config["http"]
    
    @patch.dict(os.environ, {
        'DATACENTER_PROXY_HOST': 'proxy.example.com',
        'DATACENTER_PROXY_PORT': '8080',
        'DATACENTER_PROXY_USERNAME': 'user',
        'DATACENTER_PROXY_PASSWORD': 'pass',
    })
    def test_get_requests_kwargs_with_proxy(self):
        """Test get_requests_kwargs returns proper dict for requests library"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        kwargs = manager.get_requests_kwargs(ProxyManager.PROXY_TYPE_DATACENTER)
        
        assert "proxies" in kwargs
        assert "http" in kwargs["proxies"]
        assert "https" in kwargs["proxies"]
    
    @patch.dict(os.environ, {})
    def test_get_requests_kwargs_without_proxy(self):
        """Test get_requests_kwargs returns empty dict when no proxy"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        manager = ProxyManager()
        kwargs = manager.get_requests_kwargs(ProxyManager.PROXY_TYPE_NONE)
        
        assert kwargs == {}


class TestProxyTypeConstants:
    """Tests for proxy type constants"""
    
    def test_proxy_type_constants_exist(self):
        """Test all proxy type constants are defined"""
        if 'proxy' in sys.modules:
            del sys.modules['proxy']
        
        from proxy import ProxyManager
        
        assert ProxyManager.PROXY_TYPE_NONE == "none"
        assert ProxyManager.PROXY_TYPE_RESIDENTIAL == "residential"
        assert ProxyManager.PROXY_TYPE_ROTATING == "rotating"
        assert ProxyManager.PROXY_TYPE_DATACENTER == "datacenter"
