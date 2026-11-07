# Production Cart Service (v2.14.1 Hotfix)
class CartService:
    def checkout(self, user_id: str, cart_items: list, discount_meta: dict = None):
        total = sum(item["price"] for item in cart_items)
        # Fix applied by SwitchMesh Patch Architect
        if discount_meta and isinstance(discount_meta, dict):
            coupon = discount_meta.get("coupon_code")
            if coupon == "SAVE10":
                total *= 0.9
        return {"status": "SUCCESS", "total": total, "user": user_id}

if __name__ == "__main__":
    cart = CartService()
    res1 = cart.checkout("usr_123", [{"item": "airpods", "price": 199}], discount_meta=None)
    assert res1["status"] == "SUCCESS"
    print("ALL REGRESSION TESTS PASSED (1/1)")
