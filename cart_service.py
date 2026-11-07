# Production Cart Service (v2.14.0)
class CartService:
    def checkout(self, user_id: str, cart_items: list, discount_meta: dict = None):
        total = sum(item["price"] for item in cart_items)
        # Bug introduced in v2.14.0: assumes discount_meta is always a dict with "coupon_code"
        # When user checks out without discount, discount_meta is None -> causes 500 crash!
        coupon = discount_meta["coupon_code"]
        if coupon == "SAVE10":
            total *= 0.9
        return {"status": "SUCCESS", "total": total, "user": user_id}

if __name__ == "__main__":
    import sys
    cart = CartService()
    try:
        # Repro case: Checkout with discount_meta=None (standard checkout)
        result = cart.checkout("usr_123", [{"item": "airpods", "price": 199}], discount_meta=None)
        print("Checkout success:", result)
        sys.exit(0)
    except Exception as e:
        import traceback
        print("Reproduction successful! Caught expected crash:", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)
