from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection


 if total_requests > 0 else 0

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)
    return properties 


def get_redis_cache_metrics():
    redis_conn = get_redis_connection('default')
    info = redis_conn.info()
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else None
    metrics = {
        'hits': hits,
        'misses': misses,
        'hit_ratio': hit_ratio,
    }
    logging.info(f"Redis cache metrics: {metrics}")
    return metrics 
