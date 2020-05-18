from application.utils import log


class CouponPopulator(object):
    def __init__(self):
        pass

    def populate_all_response(self, page, total, coupons):
        log.i("populate_all_response")

        size = len(coupons)
        total_pages = int(total / size) if size > 0 else 0

        return {
            "pagination": {
                "page": page,
                "size": size,
                "total": total,
                "totalPage": total_pages
            },
            "data": coupons
        }

    def populate_preview_response(self, request, coupons):
        log.i("populate_preview_response")
        # log.i(f"coupons: {coupons}")

        result = []
        if request.args.get('preview') is not None:
            if request.args.get('preview') == "true":
                return self.create_preview(coupons=coupons)
        return coupons

    def create_preview(self, coupons):
        log.i("create_preview")
        result = []
        for coupon in coupons:
            result.append({
                "id": coupon["id"],
                "description": coupon["description"],
                "code": coupon["code"],
                "store": {
                    "name": coupon["store"]["name"],
                    "image": coupon["store"]["image"]
                },
                "category": {
                    "name": coupon["category"]["name"]
                },
                "link": coupon["link"],
                "expirationInfo": coupon["expirationInfo"]})
        return result

    def populate_minimum_response(self, items):
        log.i("populate_minimum_response")
        result = []
        for item in items:
            try:
                result.append({
                    "id": item["id"],
                    "description": item["description"],
                    "code": item["code"],
                    "store": {
                        "name": item["store"]["name"],
                        "image": item["store"]["image"]
                    },
                    "category": {
                        "name": item["category"]["name"]
                    },
                    "link": item["link"],
                    "expirationInfo": item["expirationInfo"]})
            except Exception as e:
                print(f"Exception: {e}")
                print(f"item: {item}")

        return result
