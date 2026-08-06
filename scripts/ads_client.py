#!/usr/bin/env python3
"""Helper chuẩn cho mọi script gọi Google Ads API — đóng gói các bẫy đã vấp 2026-08-06.

Dùng:
    import sys; sys.path.insert(0, 'scripts')
    from ads_client import client, retry, vnd, ACCOUNT
    c = client()
    rows = retry(lambda: list(c.get_service("GoogleAdsService").search(customer_id=ACCOUNT, query="...")))

Chạy bằng .venv-ads/bin/python (google-ads==31.0.0, API v24). Chi tiết bẫy: SETUP.md §1.
"""
import time

ACCOUNT = "6918288556"          # SMR- Sun Galaxy — luôn set login_customer_id
YAML = "/home/docdang/google-ads-smartland.yaml"
VERSION = "v24"
M = 1_000_000                   # 1 VND = 1.000.000 micros — quên nhân M là đặt giá nhỏ hơn 1.000 lần


def client(account: str = ACCOUNT):
    from google.ads.googleads.client import GoogleAdsClient
    c = GoogleAdsClient.load_from_storage(YAML, version=VERSION)
    c.login_customer_id = account   # BẮT BUỘC — thiếu là "không thấy account con"
    return c


def vnd(amount_vnd: int) -> int:
    """VND -> micros. budget.amount_micros = vnd(1_000_000)  # 1tr đ/ngày"""
    return amount_vnd * M


def retry(fn, n=4, base=3):
    """Mạng máy này thi thoảng rớt IPv6 (UNAVAILABLE) — retry với backoff là đủ."""
    for i in range(n):
        try:
            return fn()
        except Exception as e:
            if "UNAVAILABLE" in str(e) and i < n - 1:
                time.sleep(base * (i + 1))
                continue
            raise


if __name__ == "__main__":
    # self-check: đọc được tên account là mọi thứ thông
    c = client()
    r = retry(lambda: list(c.get_service("GoogleAdsService").search(
        customer_id=ACCOUNT, query="SELECT customer.descriptive_name FROM customer")))
    assert r, "không đọc được customer"
    print("OK:", r[0].customer.descriptive_name)
