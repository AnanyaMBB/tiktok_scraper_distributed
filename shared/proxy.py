"""
Flexible proxy management system
Supports:
- Residential proxies (Decodo or other residential providers)
- Rotating proxies (Tor or other rotating proxy services)
- Datacenter proxies (for high-speed needs)
- No proxy option
"""
import os
from typing import Optional, Dict
from dotenv import load_dotenv

load_dotenv()


class ProxyManager:
    """Manages different proxy configurations for different scrapers"""
    
    # Proxy types
    PROXY_TYPE_NONE = "none"
    PROXY_TYPE_RESIDENTIAL = "residential"
    PROXY_TYPE_ROTATING = "rotating"
    PROXY_TYPE_DATACENTER = "datacenter"
    
    def __init__(self):
        # Residential proxy (Decodo or similar)
        self.residential_host = os.getenv("RESIDENTIAL_PROXY_HOST")
        self.residential_port = os.getenv("RESIDENTIAL_PROXY_PORT")
        self.residential_username = os.getenv("RESIDENTIAL_PROXY_USERNAME")
        self.residential_password = os.getenv("RESIDENTIAL_PROXY_PASSWORD")
        
        # Rotating proxy (Tor via zhaowde/rotating-tor-http-proxy)
        self.rotating_host = os.getenv("ROTATING_PROXY_HOST", "127.0.0.1")
        self.rotating_port = os.getenv("ROTATING_PROXY_PORT", "3128")
        
        # Datacenter proxy (optional)
        self.datacenter_host = os.getenv("DATACENTER_PROXY_HOST")
        self.datacenter_port = os.getenv("DATACENTER_PROXY_PORT")
        self.datacenter_username = os.getenv("DATACENTER_PROXY_USERNAME")
        self.datacenter_password = os.getenv("DATACENTER_PROXY_PASSWORD")
    
    def get_proxy_config(self, proxy_type: str = PROXY_TYPE_NONE) -> Optional[Dict[str, str]]:
        """
        Get proxy configuration for requests library
        
        Args:
            proxy_type: Type of proxy (none, residential, rotating, datacenter)
            
        Returns:
            Dict with http/https proxy URLs, or None if no proxy
        """
        if proxy_type == self.PROXY_TYPE_RESIDENTIAL:
            return self._get_residential_proxy()
        elif proxy_type == self.PROXY_TYPE_ROTATING:
            return self._get_rotating_proxy()
        elif proxy_type == self.PROXY_TYPE_DATACENTER:
            return self._get_datacenter_proxy()
        else:
            return None
    
    def _get_residential_proxy(self) -> Optional[Dict[str, str]]:
        """Get residential proxy configuration (e.g., Decodo)"""
        if not all([self.residential_host, self.residential_port]):
            print("Warning: Residential proxy not configured")
            return None
        
        # Build proxy URL with or without auth
        if self.residential_username and self.residential_password:
            proxy_url = f"http://{self.residential_username}:{self.residential_password}@{self.residential_host}:{self.residential_port}"
        else:
            proxy_url = f"http://{self.residential_host}:{self.residential_port}"
        
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    
    def _get_rotating_proxy(self) -> Dict[str, str]:
        """Get rotating proxy configuration (Tor via zhaowde/rotating-tor-http-proxy)"""
        proxy_url = f"http://{self.rotating_host}:{self.rotating_port}"
        
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    
    def _get_datacenter_proxy(self) -> Optional[Dict[str, str]]:
        """Get datacenter proxy configuration"""
        if not all([self.datacenter_host, self.datacenter_port]):
            print("Warning: Datacenter proxy not configured")
            return None
        
        # Build proxy URL with or without auth
        if self.datacenter_username and self.datacenter_password:
            proxy_url = f"http://{self.datacenter_username}:{self.datacenter_password}@{self.datacenter_host}:{self.datacenter_port}"
        else:
            proxy_url = f"http://{self.datacenter_host}:{self.datacenter_port}"
        
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    
    def get_requests_kwargs(self, proxy_type: str = PROXY_TYPE_NONE) -> Dict:
        """
        Get kwargs dict for requests.get() with proxy configuration
        
        Usage:
            proxy_manager = ProxyManager()
            kwargs = proxy_manager.get_requests_kwargs(ProxyManager.PROXY_TYPE_ROTATING)
            response = requests.get(url, **kwargs)
        
        Args:
            proxy_type: Type of proxy to use
            
        Returns:
            Dict with proxies key if proxy is configured
        """
        proxies = self.get_proxy_config(proxy_type)
        
        if proxies:
            return {"proxies": proxies}
        else:
            return {}


# Convenience functions for common use cases
def get_residential_proxy() -> Optional[Dict[str, str]]:
    """Get residential proxy configuration (for anti-bot protection)"""
    manager = ProxyManager()
    return manager.get_proxy_config(ProxyManager.PROXY_TYPE_RESIDENTIAL)


def get_rotating_proxy() -> Optional[Dict[str, str]]:
    """Get rotating proxy configuration (for IP rotation)"""
    manager = ProxyManager()
    return manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)


def get_datacenter_proxy() -> Optional[Dict[str, str]]:
    """Get datacenter proxy configuration (for high-speed needs)"""
    manager = ProxyManager()
    return manager.get_proxy_config(ProxyManager.PROXY_TYPE_DATACENTER)


def get_no_proxy() -> None:
    """No proxy configuration"""
    return None


# Example usage and testing
if __name__ == "__main__":
    import requests
    import time
    
    manager = ProxyManager()
    
    print("=" * 60)
    print("Proxy Configuration Test")
    print("=" * 60)
    
    # Test without proxy
    print("\n1. Testing without proxy...")
    proxies = manager.get_proxy_config(ProxyManager.PROXY_TYPE_NONE)
    print(f"   No proxy: {proxies}")
    
    # Test with residential proxy
    print("\n2. Testing residential proxy (Decodo)...")
    proxies = manager.get_proxy_config(ProxyManager.PROXY_TYPE_RESIDENTIAL)
    if proxies:
        print(f"   Residential proxy configured: {proxies['http']}")
    else:
        print("   Residential proxy not configured")
    
    # Test with rotating proxy
    print("\n3. Testing rotating proxy (Tor)...")
    proxies = manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)
    if proxies:
        print(f"   Rotating proxy configured: {proxies['http']}")
        
        # Test actual requests with IP rotation
        print("\n   Testing IP rotation (5 requests):")
        for i in range(5):
            try:
                kwargs = manager.get_requests_kwargs(ProxyManager.PROXY_TYPE_ROTATING)
                response = requests.get("http://httpbin.org/ip", timeout=30, **kwargs)
                ip = response.json()['origin']
                print(f"   Request {i+1}: IP = {ip}")
                time.sleep(2)
            except Exception as e:
                print(f"   Request {i+1}: Error = {e}")
                time.sleep(2)
    else:
        print("   Rotating proxy not configured")
    
    # Test with datacenter proxy
    print("\n4. Testing datacenter proxy...")
    proxies = manager.get_proxy_config(ProxyManager.PROXY_TYPE_DATACENTER)
    if proxies:
        print(f"   Datacenter proxy configured: {proxies['http']}")
    else:
        print("   Datacenter proxy not configured")
    
    print("\n" + "=" * 60)
    print("✓ Proxy configuration test complete!")
    print("=" * 60)