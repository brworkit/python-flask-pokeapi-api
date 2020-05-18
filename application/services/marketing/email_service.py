from application.utils import log, time
from application.database.db import mongo

class EmailService(object):
    def __init__(self):
        pass
 
    def save_new_email(self, body):
        log.i("find_coupons")
        item = mongo.db.emails.find_one({"email": body["email"]})
        if item:
            item["datetime"] = time.now_iso()
            item["active"] = True
            return mongo.db.emails.save(item)
        else:
            body["datetime"] = time.now_iso()
            body["active"] = True
            print(f"body: {body}")
            return mongo.db.emails.insert_one(body)

    def find_emails(self, active):
        log.i("find_emails")
        cursor = mongo.db.emails.find({"active": active}, {"_id": 0, "email": 1, "active": 1})
        result = []
        for email in cursor:
            result.append(email)       
        return result

    def unsubscribe_email(self, email):
        log.i("find_coupons")
        item = mongo.db.emails.find_one({"email": email})
        item["active"] = False
        print(f"item: {item}")
        return mongo.db.emails.save(item)
