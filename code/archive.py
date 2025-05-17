# This file contains code which is not used in the current version of the project but can be used for verification and checking of implementations.

import datetime

# This code verifies whether B.Q.3 worked - just insert into the lab class to make it work.
def quick_verify_q3(self):
    """Concise verification that Q3 updates were successful."""
    # Make sure we're connected
    if self.db is None:
        self.connect_to_mongo()

    print(f"\n{30 * '='} Q3 Update Verification {30 * '='}")

    # Model 1 verification
    print("\n# Model 1 Verification")
    count_before_1988 = self.db["m1_people"].count_documents(
        {"dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}}
    )
    count_updated = self.db["m1_people"].count_documents(
        {"dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}, "age": "30"}
    )
    print(f"People born before 1988: {count_before_1988}")
    print(f"People with age='30': {count_updated}")
    print(f"Update success rate: {count_updated / count_before_1988 * 100:.2f}%")
    sample = self.db["m1_people"].find_one(
        {"dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}},
        {"_id": 0, "fullName": 1, "dateOfBirth": 1, "age": 1},
    )
    print(f"Sample document: {sample}")

    # Model 2 verification
    print("\n# Model 2 Verification")
    count_before_1988 = self.db.m2_people.count_documents(
        {"dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}}
    )
    count_updated = self.db.m2_people.count_documents(
        {"dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}, "age": "30"}
    )
    print(f"People born before 1988: {count_before_1988}")
    print(f"People with age='30': {count_updated}")
    print(f"Update success rate: {count_updated / count_before_1988 * 100:.2f}%")
    sample = self.db.m2_people.find_one(
        {"dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}},
        {"_id": 0, "fullName": 1, "dateOfBirth": 1, "age": 1},
    )
    print(f"Sample document: {sample}")

    # Model 3 verification (more complex with embedded documents)
    print("\n# Model 3 Verification")
    pipeline = [
        {"$unwind": "$staff"},
        {"$match": {"staff.dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}}},
        {"$count": "total"},
    ]
    count_result = list(self.db.m3_companies.aggregate(pipeline))
    count_before_1988 = count_result[0]["total"] if count_result else 0

    pipeline = [
        {"$unwind": "$staff"},
        {
            "$match": {
                "staff.dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)},
                "staff.age": "30",
            }
        },
        {"$count": "total"},
    ]
    count_result = list(self.db.m3_companies.aggregate(pipeline))
    count_updated = count_result[0]["total"] if count_result else 0

    print(f"Staff born before 1988: {count_before_1988}")
    print(f"Staff with age='30': {count_updated}")
    print(f"Update success rate: {count_updated / count_before_1988 * 100:.2f}%")

    # Get a sample document
    pipeline = [
        {"$unwind": "$staff"},
        {"$match": {"staff.dateOfBirth": {"$lt": datetime.datetime(1988, 1, 1)}}},
        {"$project": {"_id": 0, "company": "$name", "staff": 1}},
        {"$limit": 1},
    ]
    sample = list(self.db.m3_companies.aggregate(pipeline))
    print(f"Sample staff: {sample[0] if sample else 'None found'}")
