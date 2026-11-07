# Production Cart Service (v2.14.1 Hotfix)
class CartService:
    def checkout(self, user_id: str, cart_items: list, discount_meta: dict = None):
        total = sum(item["price"] for item in cart_items)
        # Verified fix applied by SwitchMesh Patch Architect
        if discount_meta and isinstance(discount_meta, dict):
            coupon = discount_meta.get("coupon_code")
            if coupon == "SAVE10":
                total *= 0.9
        return {"status": "SUCCESS", "total": total, "user": user_id}

if __name__ == "__main__":
    import sys
    cart = CartService()
    # Test Case 1: Standard checkout without discount (Previously crashed)
    res1 = cart.checkout("usr_123", [{"item": "airpods", "price": 199}], discount_meta=None)
    assert res1["status"] == "SUCCESS" and res1["total"] == 199

    # Test Case 2: Checkout with discount
    res2 = cart.checkout("usr_456", [{"item": "keyboard", "price": 100}], discount_meta={"coupon_code": "SAVE10"})
    assert res2["status"] == "SUCCESS" and res2["total"] == 90.0

    print("ALL REGRESSION TESTS PASSED (2/2)")
    sys.exit(0)
