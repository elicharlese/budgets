def set_bucket_limits:
    small_bucket_limit = 0
    medium_bucket_limit = 0
    large_bucket_limit = 0
    if self.bucket == 0:
        return 0
    elif self.bucket > median_small:
        small_bucket_limit = self.bucket * median_small