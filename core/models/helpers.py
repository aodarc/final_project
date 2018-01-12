import uuid


def image_path(instance, filename) -> str:
    """
    Build path for Image files
    :param instance: django Model instance
    :param filename: name of file which uploading
    :return: path with model class name as directory and random file name
    """
    fn = '{}.{}'.format(uuid.uuid4(), filename.split('.')[-1])
    dir_name = '{}'.format(instance.__class__.__name__)
    return '{directory}/{file_name}'.format(directory=dir_name, file_name=fn)
