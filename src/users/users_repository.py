from users.users_model import User


async def get_users():
    users = await User.find_all().to_list()
    return users


""" def get_user(user_id):
    user = users_collection.find_one({"_id": user_id})
    if user:
        return User(**user)"""


async def create_user(user: User):
    await user.insert()
    return user


""" def update_user(user_id, user_data: User):
    result = users_collection.update_one(
        {"_id": user_id}, {"$set": user_data.dict()}
    )
    return result.modified_count


def delete_user(user_id):
    result = users_collection.delete_one({"_id": user_id})
    return result.deleted_count
 """
