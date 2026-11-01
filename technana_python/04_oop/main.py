import user
from post import Post
app_user_one = user.User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps engineer")
app_user_one.get_user_info()

app_user_two = user.User("43@44.com", "Adam Duma", "pwd3", "software engineer")
app_user_two.get_user_info()

new_post = Post("On a secret mission today", app_user_two.name)
new_post.get_post_info()