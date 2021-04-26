import os
import definitions


def load_rel_path(
        directory,
        filename,
        suffix
        # generate path string while directory, filename and suffix has to be handed manually // for now
):
    file_path = os.path.relpath(
        f'./{directory}/{filename}.{suffix}',
        start=definitions.root_dir())  # file path variable is generated via relpath and f string
    # .active directory is necessary to reach ~/extract_format/files

    return file_path
