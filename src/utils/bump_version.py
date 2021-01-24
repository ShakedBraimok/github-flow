from src.utils.config_file import read_config


def bump_version(version,part):
    splited_version = version.split(".")
    version_len = len(splited_version)
    if version_len == 2:
        splited_version.append("0")
    if version_len == 1:
        splited_version = [splited_version[0],"0","0"]
    if part == "patch":
        part_value = int(splited_version[2])
        new_part_value = str(part_value + 1)
        version = splited_version[0] + "." + splited_version[1] + "." + new_part_value
    if part == "minor":
        part_value = int(splited_version[1])
        new_part_value = str(part_value + 1)
        splited_version[2] = "0"
        version = splited_version[0] + "." + new_part_value + "." + splited_version[2]
    if part == "major":
        part_value = int(splited_version[0])
        new_part_value = str(part_value + 1)
        splited_version[1] = "0"
        version = new_part_value + "." + splited_version[1] + "." + splited_version[2]
    return version
