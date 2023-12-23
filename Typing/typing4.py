from typing import NewType

UserId = NewType("UserId", int)
some_id = UserId(524313)

def get_user_name(user_id: UserId) -> str:
  return str(user_id)

user_a = get_user_name(UserId(324233))
user_b = get_user_name(23)  # error from mypy

print(user_a, user_b)

output = UserId(32342) + UserId(12345)
print(output)