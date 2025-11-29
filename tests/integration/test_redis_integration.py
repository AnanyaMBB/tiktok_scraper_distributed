"""
Integration tests that require a running Redis instance.

These tests are marked with @pytest.mark.integration and can be skipped
in environments without Redis by running: pytest -m "not integration"
"""

import pytest
import os

# Skip all tests in this module if Redis is not available
pytestmark = pytest.mark.integration


def redis_available():
    """Check if Redis is available"""
    try:
        import redis
        client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            socket_connect_timeout=1
        )
        client.ping()
        return True
    except Exception:
        return False


@pytest.fixture
def redis_client():
    """Create a real Redis client for integration tests"""
    if not redis_available():
        pytest.skip("Redis not available")
    
    import redis
    client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=15,  # Use DB 15 for tests to avoid conflicts
        decode_responses=True
    )
    
    # Clean up before test
    client.flushdb()
    
    yield client
    
    # Clean up after test
    client.flushdb()


class TestRedisOperations:
    """Integration tests for Redis operations"""
    
    def test_username_tracking(self, redis_client):
        """Test tracking scraped usernames in Redis"""
        # Add usernames
        redis_client.sadd("scraped_usernames", "user1")
        redis_client.sadd("scraped_usernames", "user2")
        
        # Check membership (sismember returns 1/0, not True/False)
        assert redis_client.sismember("scraped_usernames", "user1")
        assert redis_client.sismember("scraped_usernames", "user2")
        assert not redis_client.sismember("scraped_usernames", "user3")
        
        # Check count
        assert redis_client.scard("scraped_usernames") == 2
    
    def test_download_queue(self, redis_client):
        """Test video download queue operations"""
        # Add to queue
        redis_client.sadd("download_queue", "video1")
        redis_client.sadd("download_queue", "video2")
        
        # Check queue (sismember returns 1/0, not True/False)
        assert redis_client.sismember("download_queue", "video1")
        
        # Remove from queue
        redis_client.srem("download_queue", "video1")
        assert not redis_client.sismember("download_queue", "video1")
    
    def test_scraping_lock(self, redis_client):
        """Test scraping lock mechanism"""
        # Set lock
        lock_key = "scraping:testuser"
        result = redis_client.set(lock_key, "task-123", nx=True, ex=3600)
        assert result is True
        
        # Try to set again (should fail)
        result2 = redis_client.set(lock_key, "task-456", nx=True, ex=3600)
        assert result2 is None
        
        # Release lock
        redis_client.delete(lock_key)
        
        # Now should succeed
        result3 = redis_client.set(lock_key, "task-789", nx=True, ex=3600)
        assert result3 is True
