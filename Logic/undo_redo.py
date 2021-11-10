def list_versions(versions_list, current_version, lista):
    while len(versions_list) > current_version:
        del versions_list[len(versions_list) - 1]
    versions_list.append(lista)
    current_version += 1
    return versions_list, current_version


def undo(current_version):
    if current_version > 1:
        current_version -= 1
    return current_version


def redo(versions_list, current_version):
    if current_version != len(versions_list):
        current_version = current_version + 1
    return current_version
