from users.users_model import User
import users.users_repository as users_repository


async def get_users():
    users = await users_repository.get_users()
    return users


""" def get_user(user_id):
    # TODO: Implement logic to retrieve a specific user from the database based on the provided user_id
    pass """


async def create_user(user: User):
    await users_repository.create_user(user)
    return user


""" def update_user(user_id, user_data):
    # TODO: Implement logic to update a specific user in the database based on the provided user_id and user_data
    pass


def delete_user(user_id):
    # TODO: Implement logic to delete a specific user from the database based on the provided user_id
    pass """
