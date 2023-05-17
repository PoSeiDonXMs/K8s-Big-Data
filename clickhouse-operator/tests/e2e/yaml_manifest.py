import yaml


def get_chi_name(chi_manifest_filename):
    return yaml.safe_load(open(chi_manifest_filename, "r"))["metadata"]["name"]


def get_manifest_data(manifest_filename):
    return yaml.safe_load(open(manifest_filename, "r"))


def get_multidoc_manifest_data(manifest_filename):
    return yaml.safe_load_all(open(manifest_filename, "r"))
