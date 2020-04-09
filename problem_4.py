class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    output = False
    for u in group.get_users():
        if u == user:
            return True
    for g in group.get_groups():
        output |= is_user_in_group(user, g)
    return output

parent = Group("parent")

child = Group("child")
child_user = "child_user"
child.add_user(child_user)

sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_child1 = Group("subchild1")
sub_child_user1 = "sub_child_user1"
sub_child.add_user(sub_child_user1)

child.add_group(sub_child)
parent.add_group(child)

# child in Parent
print ("Pass" if (is_user_in_group(child_user, parent) == True) else "Fail")
# sub_child in Parent
print ("Pass" if (is_user_in_group(sub_child_user, parent) == True) else "Fail")
# sub_child 2 in Parent
print ("Pass" if (is_user_in_group(sub_child_user1, parent) == True) else "Fail")

