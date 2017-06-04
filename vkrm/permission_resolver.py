# coding=utf-8
from vkrm.models import Action, Object, Permission


def get_object_permissions_for_user(user, entity):
    roles = user.role_set.all()
    if not roles:
        return {}
    role = roles[0]  # TODO: подумать

    object_type = entity.__class__.__name__
    try:
        obj = Object.objects.get(object_type=object_type, object_id=entity.id)
    except Object.DoesNotExist:
        return {}

    actions = Action.objects.all()

    permissions = {}
    for action in actions:
        if Permission.objects.filter(role=role, object=obj, action=action).exists():
            permissions[action.action_name] = True

    return permissions